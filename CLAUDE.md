# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static showcase website for the **Andada** typeface by HT Fonts. Hosted on GitHub Pages at andada.htfonts.com. No build system or framework — pure HTML/CSS/JS served as-is.

## Development

**No build step required.** Open `index.html` in a browser to preview.

The Python image-processing utilities (resample, convert-to-GIF) previously kept here now live in the parent `minisites/` directory, shared across all font sites.

## Architecture

- **index.html** — Single-page site (~1,430 lines). All content lives here, organized as `<section>` elements with anchor IDs for navigation (`#Overview`, `#Aboutfont`, `#especimen`, `#Awards`, `#characterset`, `#OpenType`, `#orthotypography`, `#fontinuse`, `#Guarani`, `#foot`).
- **style.css** — Monolithic stylesheet. Single responsive breakpoint at 700px. Max content width 1000px.
- **js/jquery.slides.js** — Hero image carousel plugin (loaded alongside jQuery from CDN).
- **img/** — All site images, predominantly GIF format (converted from JPG/PNG for consistency). Includes `img/uso/` for font-in-use examples.

## Key Conventions

- Site content is in **English**. Code comments (HTML/CSS/JS) are in **Spanish**.
- All specimen/showcase images use **GIF format** — new images should be converted to GIF using the shared Python utility in `minisites/`.
- CSS class names use lowercase/hyphen-case. Layouts use a mix of floats and flexbox.
- No test framework, linter, or CI pipeline exists.
- Deployment is via push to `master` (GitHub Pages).
