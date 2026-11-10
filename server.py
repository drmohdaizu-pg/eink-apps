"""Local server for the E-ink App Hub.

Serves the app's files and relays two read-only requests to Malaysia's
Department of Environment (DOE) air-quality service. The DOE server only lets
its own website read that data from a browser, so the page asks this server,
which fetches it and passes it back.

Run:  python server.py [port]      (default port 8765)
"""
import http.server
import socketserver
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOE_BASE = "https://eqms.doe.gov.my/api3/publicportalapims/"
# Only these DOE endpoints may be relayed (nearest station, current reading)
DOE_ALLOWED = {"getstationidbylonglat", "currentapicurrentlocation"}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        url = urllib.parse.urlsplit(self.path)
        if url.path.startswith("/doe/"):
            return self.relay_doe(url)
        return super().do_GET()

    def relay_doe(self, url):
        endpoint = url.path[len("/doe/"):]
        if endpoint not in DOE_ALLOWED:
            return self.send_error(404, "Unknown DOE endpoint")
        target = DOE_BASE + endpoint + ("?" + url.query if url.query else "")
        try:
            req = urllib.request.Request(target, headers={"User-Agent": "eink-app-hub/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                body = resp.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
        except (urllib.error.URLError, TimeoutError) as e:
            self.send_error(502, f"DOE service unavailable: {e}")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", port), Handler) as httpd:
        print(f"E-ink App Hub on http://localhost:{port}")
        httpd.serve_forever()
