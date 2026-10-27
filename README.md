# Spiers-Dennis Post No. 24
Source for https://spiers-dennis-post.github.io/, the Jekyll-powered GitHub Pages site of American Legion Post 24 in Olathe, Colorado.
## Editing
All pages are edited as source files in this repository. The site needs no CMS, database, tracking scripts, or JavaScript to display its content. Preview locally with Ruby and Bundler by running `bundle install` and `bundle exec jekyll serve`.
- `_data/post.yml`: canonical Post name, address, public desk telephone, and official Post email.
- `_data/officers.yml`: officer assignments and reporting date; the roster appears in `governance/index.md`.
- `_data/sources.yml`: reference records for historical and organizational claims.
- `_data/facts.yml`: reserved structured facts for later publication.
- `_news/` and `_letters/`: dated Markdown content for news and Commander's letters. Their index pages remain unindexed and unlinked from the main navigation until content exists.
- `_includes/`: citations and Schema.org metadata; `_layouts/`: shared HTML.
- `robots.txt` and `sitemap.xml`: crawler discovery.
## Editorial standards
Write as the Post addressing a visitor. Prefer useful facts, plain language, and direct links. Treat familiar local landmarks and Post activities as part of our own story, not as discoveries made by third-party researchers. Cite historical and formal claims without explaining the research process at length. Do not place source-evaluation notes, confidence scores, alternative property leads, or editing instructions on public pages. Keep those in the repository's research documentation.
If important details such as a meeting time or public opening hours are not confirmed, don't guess. Direct visitors to the Post's shared contact channels rather than displaying rows of empty fields. Preserve old page URLs and remove `noindex: true` when a page has substantive material ready for indexing.
National American Legion eligibility and programs belong on the national website; link instead of copying those rules. The Post's original Constitution and Bylaws have not yet been supplied and must not be replaced with national templates.
## Research notes
The original charter date is not established from the Centennial source. An earlier Post website stated "Founded in 2014", but did not explain the date. A corporate-formation date in a secondary state-registry mirror and property information for a differently written street address are not verified as historical charter or hall facts. Previously listed contact numbers, personal email addresses, and secondary-directory officer claims do not supersede the information directly supplied by the Post. Keep these uncertainties out of everyday visitor copy.
The January 30, 2026 Colorado Department membership report records 5 new, 4 PUFL, 53 renewals and 1 headquarters transfer, total 63 and goal 63. This is a dated reporting snapshot, not a live membership roll.
## Contact privacy
Only the shared Post telephone (970-644-0731) and official Post email (americanlegion24.olathe@gmail.com) may be published as contact information. Never include personal telephone numbers, private email addresses, home addresses, or personal contact details for members or officers, including information in scans, images, source documents, and metadata.
## Meeting schedule
The Post Commander confirmed meetings on the fourth Tuesday monthly, dinner at 5:00 p.m., and usually canceling the December meeting due to holidays. The original message spelled the meeting start time `%:30`; it remains unpublished until clarified. When confirmed, update the meeting page and `_data/facts.yml` together. Avoid claiming December is canceled every year without a dated announcement.
## Publishing
GitHub Pages builds from `main`. The `jekyll-redirect-from` plugin preserves the former `/officers/` URL and redirects it to `/governance/`. The footer links to privacy, copyright, website information, and accessibility pages. Changes to the site's legal policies require review by authorized Post leadership.
