# Spiers-Dennis Post public website
Source for https://spiers-dennis-post.github.io/ — a minimal, static, HTML-first Jekyll website.
## Publishing
On GitHub, open Settings → Pages and choose Deploy from a branch → main → /(root). GitHub Pages builds Jekyll from source. The site is publicly readable without JavaScript.
For local preview, install Ruby and Bundler, then run `bundle install` and `bundle exec jekyll serve`.
## Content organization
- `_data/post.yml`: Post identity and canonical contact details for the shared Post desk telephone and Post email; unknown fields remain empty.
- `_data/facts.yml`: Local key-value records for meetings, building, membership, and mailing information; phone and email are maintained only in `_data/post.yml`.
- `_data/sources.yml`: Source registry for locally published claims.
- `_data/legion_links.yml`: Official American Legion destinations.
- `governance/`: Constitution, Bylaws, and relevant governing material.
- `history/`: Sourced historical information.
- `_news/`: News posts, one Markdown file per item.
- `_letters/`: Commander's letters, one Markdown file per letter.
- `_includes/facts.html` and `_includes/references.html`: Reusable readable facts and superscript references.
- `sitemap.xml` and `robots.txt`: Discovery endpoints.
## Adding a verified local fact
Update the relevant `value` in `_data/facts.yml`, using plain text. If a citation is appropriate, add a source record with `id`, `title`, `url` (if available), `details`, and `published_on` to `_data/sources.yml`. Add its ID to the fact's `source_ids` array and to the page's front matter `source_ids`, in the order the citations should be numbered. Remove `noindex: true` on that page only when it has meaningful, verified public content.
If address information is added, update `_data/post.yml` too; extend `_includes/schema.html` only when the structured address is complete and verified.
## Adding a news item
Create a Markdown file such as `_news/2026-11-01-post-update.md` with this content:
```markdown
---
title: Post update
date: 2026-11-01
author: Authorized author
summary: Short factual summary.
source_ids: []
---
The approved article text goes here.
```
Remove `noindex: true` from `news/index.html` once the index contains a published item. Publication source metadata can include `source_ids` when citations are relevant.
## Adding a commander's letter
Create a file in `_letters/` with `title`, `date`, `author`, and the approved letter text, following the news example. Remove `noindex: true` from `commanders-letters/index.html` when the archive is populated.
## Governance documents
Do not invent or summarize missing provisions. Publish the supplied Constitution or Bylaws with a documented document version and effective date, headings for each article, and stable section IDs for direct citations. If the original source may be published, put a copy under `assets/` and link it from the HTML transcription.
## Indexing and accuracy
The homepage and substantive national-resource pages may be indexed. Unpopulated local sections are tagged `noindex,follow` and omitted from the sitemap. Remove that tag per section when content has been approved and verified.
This site does not copy American Legion national rules; it links to the official information owner. Avoid personal, private, or unauthorized records.
## Requirements
No JavaScript runtime, no client-side data fetching, no database, no CMS, and no special AI-crawler-only content. HTML, CSS, canonical links, XML sitemap, and JSON-LD make the pages useful to ordinary browsers, assistive tools, search engines, and retrieval systems.
## Public contact policy
Only the Post's shared desk telephone and official Post email may be published as contact information. Never commit any member's or officer's personal phone number, private email, home address, or other personal contact details, including inside documents, scans, images, or metadata. Review all source material before publication. The Contact page, site footer, and JSON-LD schema draw from the single authorized record in `_data/post.yml`.
## Website policies
The footer links to `legal/privacy.md`, `legal/copyright.md`, `legal/site-information.md`, and `legal/accessibility.md`. These describe the current static website and should be reviewed by authorized Post leadership. Formal publishing authority is not yet confirmed. The shared public Post email and desk telephone are available as general contact channels; do not invent private or personal editorial contacts.
Revisit the privacy policy before adding forms, analytics, embedded services, or other means of collecting visitor data. Verify rights and permissions before uploading archival photographs, letters, logos, or documents. The accessibility statement identifies WCAG 2.2 AA as a target, not a certification.
