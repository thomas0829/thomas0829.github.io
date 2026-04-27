# thomas0829.com

Personal website and CV for Ying-Chun Lee, focused on VLA, robotics, and software systems. Built with Jekyll and hosted on GitHub Pages.

**Live site:** [https://thomas0829.com](https://thomas0829.com)

## Structure

```
_pages/          # English pages (home, cv, publications)
_pages/zh/       # Chinese (Traditional) pages
_layouts/        # Custom layouts (home, cv, publications)
_sass/layout/    # Page-specific SCSS (_home, _cv, _publications)
_data/           # Navigation configs, CV data
_includes/       # Masthead, head, footer partials
images/          # Profile photo, paper thumbnails, favicons
files/           # Downloadable files (resume)
assets/          # CSS, JS, fonts
```

## Local Development

```bash
docker-compose up
```

Site runs at `http://localhost:4000`.

## Deployment

Pushes to `master` auto-deploy via GitHub Actions to GitHub Pages.
