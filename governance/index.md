---
title: Governance
description: Post officers, constitutional and bylaws references, and governing authorities for Spiers-Dennis American Legion Post 24.
permalink: /governance/
redirect_from:
  - /officers/
source_ids: [post-officer-roster-2026-10-27, legion-officers-guide-2026]
---
# Governance
The Post's locally adopted Constitution and Bylaws have not yet been supplied for publication. National suggested model provisions or Department rules must not be presented as the Post's adopted text.
<h2 id="officers">Post officers</h2>
<p>The office assignments below were provided by the serving Post Commander and reflect the roster as reported on <time datetime="{{ site.data.officers.as_of | date: '%Y-%m-%d' }}">{{ site.data.officers.as_of | date: "%B %-d, %Y" }}</time>.<sup class="reference"><a href="#reference-post-officer-roster-2026-10-27" aria-label="Reference 1">[1]</a></sup></p>
<dl class="fact-list">
{% for office in site.data.officers.offices %}
{% assign person = site.data.officers.people | where: "id", office.person_id | first %}
<div class="fact-row" id="{{ office.name | slugify }}">
<dt>{{ office.name | escape }}</dt>
<dd>{% if office.filled_by_role %}<strong>Filled by {{ office.filled_by_role | escape }}</strong>{% else %}<strong>{{ person.name | escape }}</strong><small class="entry-meta">{{ person.service_branch | escape }} ({{ person.service_abbreviation | escape }}){% if office.installed_year %} · Installed {{ office.installed_year }}{% endif %}</small>{% endif %}</dd>
</div>
{% endfor %}
</dl>
<p><strong>Office terminology:</strong> The American Legion's 2026 Officer's Guide uses <em>Finance Officer</em>; its suggested post bylaws also use <em>Finance Officer/Treasurer</em>.<sup class="reference"><a href="#reference-legion-officers-guide-2026" aria-label="Reference 2">[2]</a></sup> The Post's own adopted bylaws have not yet been published here.</p>
<p>To contact the Post, use its <a href="{{ '/contact/' | relative_url }}">shared desk telephone or organizational email</a>. Individual officers' personal contact information is not published.</p>
## Constitution
[Post constitution reference page]({{ '/governance/constitution/' | relative_url }})
## Bylaws
[Post bylaws reference page]({{ '/governance/bylaws/' | relative_url }})
## Other governing authorities
[The American Legion Department of Colorado](https://coloradolegion.org/) and [The American Legion](https://www.legion.org/) publish their own governance materials. Those are external sources, not substitutes for locally adopted documents.
