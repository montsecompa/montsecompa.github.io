# Montserrat Compa Ferrer: personal academic website

Live at **https://montsecompa.github.io**, in English (site root), Spanish (`/es/`) and Catalan (`/ca/`). The language switch in the header opens the same page in the other language, and the site remembers the visitor's choice.

It is a static site with no framework, hosted on GitHub Pages.

| File | What it holds |
|---|---|
| `data.js` | All lists: publications, projects, grants, students, talks, research themes and the headline numbers. Text written as `{en:…, es:…, ca:…}` is shown in the page's language. |
| `build.py` | All page text in the three languages (About, Career, Outreach…). Running it writes the 27 HTML pages. |
| `site.js` | Draws the lists and holds the short interface labels in each language. |
| `style.css` | Styling. |
| `assets/sea.svg` | The home-page illustration (labels are filled in per language). |

## Update it

**A new publication, project, talk, grant or student:** add a row to the matching array in `data.js`, run `python3 build.py`, and commit. Publication and talk titles stay in the language they were published in, so they are written once.

| What | Array |
|---|---|
| Publications | `PUBS` (year, theme, title, authors, journal, DOI, role `f`/`l`) |
| Projects and budgets | `FUND` (years, name, funder and PI, led by me true/false, budget) |
| Fellowships and grants | `GRANTS` |
| Students | `STUDENTS` |
| Conference presentations | `TALKS` (year, title, venue, format, `i` international / `n` national) |
| Home-page numbers | `FACTS` |

**Page text (biography, career timeline, education, contact…):** edit it in `build.py` for each language, then run `python3 build.py` and commit everything. Also rerun it after changing `data.js`, `site.js` or `style.css`, so visitors' browsers pick up the new files straight away.
