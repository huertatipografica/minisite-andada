# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static showcase website for the **Andada** typeface by HT Fonts. Hosted on GitHub Pages at andada.htfonts.com. No build system or framework — pure HTML/CSS/JS served as-is.

## Development

**No build step required.** Open `index.html` in a browser to preview.

### Python Image Utilities

Setup (one-time):
```bash
./setup_venv.sh
source venv/bin/activate
```

Resample JPGs (resize to max width, default 1920px, quality 80):
```bash
python python/resample_jpgs.py [folder_path] [width] [quality]
```

Convert images to GIF:
```bash
python python/convert_to_gif.py [folder_path]
```

Python dependency: Pillow>=10.0.0 (installed via `requirements.txt`).

## Architecture

- **index.html** — Single-page site (~1,430 lines). All content lives here, organized as `<section>` elements with anchor IDs for navigation (`#Overview`, `#Aboutfont`, `#especimen`, `#Awards`, `#characterset`, `#OpenType`, `#orthotypography`, `#fontinuse`, `#Guarani`, `#foot`).
- **style.css** — Monolithic stylesheet. Single responsive breakpoint at 700px. Max content width 1000px.
- **js/jquery.slides.js** — Hero image carousel plugin (loaded alongside jQuery from CDN).
- **python/** — Batch image processing scripts (resample, convert format). These operate on the `img/` directory.
- **img/** — All site images, predominantly GIF format (converted from JPG/PNG for consistency). Includes `img/uso/` for font-in-use examples.

## Key Conventions

- Site content is in **English**. Code comments (HTML/CSS/JS) are in **Spanish**.
- All specimen/showcase images use **GIF format** — new images should be converted to GIF using the Python utility.
- CSS class names use lowercase/hyphen-case. Layouts use a mix of floats and flexbox.
- No test framework, linter, or CI pipeline exists.
- Deployment is via push to `master` (GitHub Pages).
