# Spiers-Dennis Post No. 24 public reference website
Source for https://spiers-dennis-post.github.io/ — a static HTML-first Jekyll website for Spiers-Dennis American Legion Post No. 24 in Olathe, Colorado.
## Publishing
GitHub Pages builds the default `main` branch using Jekyll. For local preview, run `bundle install` and `bundle exec jekyll serve` with Ruby and Bundler.
## Information model
- `_data/post.yml`: canonical identity, verified public physical location, and the Post's explicitly authorized desk telephone and email.
- `_data/facts.yml`: machine-readable fact fields for meetings, building, local membership, and outstanding mailing details.
- `_data/sources.yml`: stable, original-source citations with titles, URLs, and source-scope notes.
- `_data/legion_links.yml`: official links to national Legion topics that should not be copied locally.
- `history/`: Post-specific sourced history and dated official Department membership reports.
- `_data/officers.yml` and `officers/`: current Post officers with role assignments, military service branch, source date, and any specifically confirmed installation year; no personal contact information.
- `building/`: physical address and cautiously described limits of available property evidence.
- `governance/`: pending local Constitution and Bylaws; superior templates do not stand in for adopted local documents.
- `_news/` and `_letters/`: source-edited dated publications; no web editor or database.
- `_includes/`: citation, fact, and Schema.org templates.
## Source and uncertainty rules
Published assertions should link to the original document or authorized organizational publication whenever available. A research summary is a starting point, not a substitute for first-party documents. Records may conflict: never assert a founding date or current officeholder merely because a directory says so. Historical membership snapshots are not live counts. Leave fields blank when evidence is insufficient, and remove `noindex: true` only after a page has substantive source-supported content.
The American Legion Centennial entry documents charter members and namesakes but not the exact original charter date. A prior Post website contains a conflicting, unexplained 2014 founding statement. The 2004 corporate-formation lead, 2004 memorial chronology, current meeting schedule, earlier officer identifications, historic membership comparisons, and building ownership/construction details require additional primary verification or explicit Post confirmation before publication as current official facts.
## Personal information rule
The only public contact information authorized here is the shared Post desk telephone (970-644-0731) and Post email (americanlegion24.olathe@gmail.com). Do not publish personal telephone numbers, private email addresses, residential addresses, or private contact details of individual members or officers. This rule covers text, historical scans, documents, images, attachments, and metadata. Charter-member historical names do not constitute public contact channels.
## Maintenance
News items live in `_news/`; commander's letters live in `_letters/`. Create date-stamped Markdown files with `title`, `date`, `author`, and article text. Publish the local Constitution and Bylaws only from copies of the actual adopted instruments; give sections stable IDs and source links.
Do not add JavaScript-required content, tracking scripts, mandatory client-side rendering, or redundant national rules. Review the four `legal/` pages with authorized Post leadership before treating them as finally adopted legal policy.
## Officer roster updates
Edit `_data/officers.yml` when an authorized Post officer confirms a change. Maintain each person's name and service branch once under `people`, and link roles through the `offices` list, allowing one person to fill multiple offices. Record the `as_of` date and source in `_data/sources.yml`. Do not infer exact installation dates, additional terms, or office assignments from third-party directories. The public page uses Finance Officer, the title in the national Officer's Guide; any different legally operative title must be checked against the Post's adopted local documents.
