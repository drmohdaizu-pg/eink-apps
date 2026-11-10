# E-ink App Hub

A small web app for e-ink screens running the [EPD-nRF5](https://github.com/tsl0922/EPD-nRF5) firmware. It connects over Bluetooth straight from the browser and sends pictures to the screen.

**Open it:** https://drmohdaizu-pg.github.io/eink-apps/ in Chrome or Edge, click **Connect screen**, pick your device.

## Apps

- **Dashboard**: date, month calendar, weather and air quality for your city
- **Note**: big auto-sized text, first line in red
- **Quote**: funny, inspiring or scientists' quotes
- **To-do**: checklist with red priorities and a progress bar (dark or light)
- **Draw**: brush, fill, undo
- **Image**: photos with dithering, crop/zoom/rotate, auto-optimise, text and drawing on top, and **Save optimised PNG**
- **Gallery**: pictures from this repository's `gallery/` folder, one tap to load and send

Every app can show a small battery icon (enter the voltage from **Check battery**).

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
