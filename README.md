# E-ink App Hub

A small web app for e-ink screens running the [EPD-nRF5](https://github.com/tsl0922/EPD-nRF5) firmware. It connects over Bluetooth straight from the browser and sends pictures to the screen.

**Open it:** https://drmohdaizu-pg.github.io/eink-apps/ in Chrome or Edge, click **Connect screen**, pick your device.

## Apps

- **Dashboard**: date, month calendar, weather and air quality for your city
- **Note**: big auto-sized text, first line in red
- **Quote**: funny or inspiring quotes
- **To-do**: checklist with red priorities and a progress bar (dark or light)
- **Draw**: brush, fill, undo
- **Image**: photos with dithering, crop/zoom/rotate, auto-optimise, text and drawing on top

Every app can show a small battery icon (enter the voltage from **Check battery**).

## Air quality

- On GitHub Pages: US AQI from [Open-Meteo](https://open-meteo.com/).
- Run locally with `python server.py` and open http://localhost:8765 to get Malaysia's official Air Pollutant Index (DOE) for Malaysian cities. The server relays two read-only DOE requests that browsers can't make directly.

## Notes

- Your to-do list, city and settings are saved only in your own browser.
- `fontlab.html` compares fonts as they look on the 1-bit screen.
- Literata font: SIL Open Font License 1.1 (see `fonts/`).
