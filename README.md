# Montserrat Compa Ferrer: personal academic website

A multi-page static website with no build step, hosted on GitHub Pages. Each section has its own page (`about.html`, `research.html`, `publications.html`, `funding.html`, `career.html`, `talks.html`, `outreach.html`, `contact.html`); styling is in `style.css`, the lists are in `data.js`, and `site.js` renders them.

## Publish it

1. On GitHub, create a new public repository named **`<your-username>.github.io`**.
2. Upload every file in this folder (including `.nojekyll`) to the repository root (Add file → Upload files → Commit).
3. Go to **Settings → Pages**, set *Source* to "Deploy from a branch", branch `main`, folder `/ (root)`, and save.
4. After a minute the site is live at `https://<your-username>.github.io`.

## Update it

All lists are plain JavaScript arrays in `data.js`:

| What | Array |
|---|---|
| Publications | `PUBS` (year, theme, title, authors, journal, DOI, role `f`/`l`) |
| Projects and budgets | `FUND` (years, name, funder, PI true/false, budget) |
| Fellowships and grants | `GRANTS` |
| Students | `STUDENTS` |
| Conference presentations | `TALKS` |

Add a new row, commit, and GitHub Pages republishes automatically. The headline numbers on the home page (citations, h-index) are at the top of `site.js`.
