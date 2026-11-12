# E-ink App Hub

A small web app for e-ink screens running the [EPD-nRF5](https://github.com/tsl0922/EPD-nRF5) firmware. It connects over Bluetooth straight from the browser and sends pictures to the screen.

**Open it:** https://drmohdaizu-pg.github.io/eink-apps/ in Chrome or Edge, click **Connect screen**, pick your device.

## Apps

- **Dashboard**: date, clock, month calendar, weather and air quality for your city. The clock can update itself every 5 min to 1 hour while the laptop stays connected.
- **Note**: big auto-sized text, first line in red
- **Away**: out-of-office card with status, "back at" time or date, message and contact line
- **Quote**: 50 funny, 50 inspiring and 50 scientists' quotes, plus **My quotes** (your own, saved in your browser). Shuffled with no repeats, with Previous / Next
- **To-do**: checklist with red priorities and a progress bar (dark or light)
- **Draw**: brush, fill, undo
- **Image** (private, nothing is uploaded): photos or the **camera** (live e-ink viewfinder, then Snap), with dithering, crop/zoom/rotate, auto-optimise, text and drawing on top, and **Save optimised PNG**
- **Gallery** (public): pictures from this repository's `gallery/` folder, one tap to load and send. It keeps its own picture, so it never replaces the photo open in Image.

Every app can show a small battery icon (enter the voltage from **Check battery**).

**Built-in clock** switches the screen to the firmware's own clock, which runs on the screen's battery with no laptop. It fully redraws every minute, so it uses more battery; the firmware's author advises against leaving it on long-term.

## Air quality

- On GitHub Pages: US AQI from [Open-Meteo](https://open-meteo.com/).
- Run locally with `python server.py` and open http://localhost:8765 to get Malaysia's official Air Pollutant Index (DOE) for Malaysian cities. The server relays two read-only DOE requests that browsers can't make directly.

## Gallery

Add pictures by opening the [`gallery`](gallery) folder on GitHub → **Add file → Upload files** → **Commit**. They appear in the Gallery tab within a minute.

- Pictures already at the screen's size and colours (for example from **Save optimised PNG**) are sent pixel-for-pixel.
- Any other photo is auto-optimised when you pick it.
- **The gallery is public**, like the rest of this repository. Don't put personal photos here.

The starter pictures (`red-sun-mountains`, `bunga-raya`, `bauhaus`, `contours`) are 400×300 black/white/red.

## Notes

- Your to-do list, city and settings are saved only in your own browser.
- `fontlab.html` compares fonts as they look on the 1-bit screen.
- Literata font: SIL Open Font License 1.1 (see `fonts/`).
