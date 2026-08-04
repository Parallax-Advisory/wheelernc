# wheelernc.com

Static resume site for David B. Wheeler. No framework, no build step.

## Files

- `index.html` - the resume page
- `styles.css` - screen, mobile, and print styles
- `files/David_B_Wheeler_Resume.pdf` - downloadable PDF resume

## Deploy

Render Static Site.

- Build command: (none)
- Publish directory: `.`

Custom domains: `wheelernc.com` and `www.wheelernc.com`.

## Updating the PDF

Replace `files/David_B_Wheeler_Resume.pdf` and push to `main`. Render redeploys automatically.

## Local preview

    python -m http.server 8000
