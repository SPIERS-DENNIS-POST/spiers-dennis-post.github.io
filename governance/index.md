---
title: Governance
description: Current officers and governing documents of Spiers-Dennis American Legion Post No. 24.
permalink: /governance/
redirect_from:
  - /officers/
source_ids: [post-officer-roster-2026-10-27]
documents: []
---
# Governance
<h2 id="officers">Post officers</h2>
<p><small>As of <time datetime="{{ site.data.officers.as_of | date: '%Y-%m-%d' }}">{{ site.data.officers.as_of | date: "%B %-d, %Y" }}</time></small><sup class="reference"><a href="#reference-post-officer-roster-2026-10-27" aria-label="Reference 1">[1]</a></sup></p>
<dl class="fact-list">
{% for office in site.data.officers.offices %}
{% assign person = site.data.officers.people | where: "id", office.person_id | first %}
<div class="fact-row" id="{{ office.name | slugify }}">
<dt>{{ office.name | escape }}</dt>
<dd>{% if office.filled_by_role %}<strong>Filled by {{ office.filled_by_role | escape }}</strong>{% else %}<strong>{{ person.name | escape }}</strong><small class="entry-meta">{{ person.service_abbreviation | escape }}{% if office.installed_year %} · Installed {{ office.installed_year }}{% endif %}</small>{% endif %}</dd>
</div>
{% endfor %}
</dl>
<h2>Constitution and Bylaws</h2>
<p>The Post's Constitution and Bylaws are not yet available on this website. For questions about these documents, please <a href="{{ '/contact/' | relative_url }}">contact the Post</a>. Other public records can be found in our <a href="{{ '/documents/' | relative_url }}">Public Documents directory</a>.</p>
<h2>Other Legion governing documents</h2>
<p><a href="https://coloradolegion.org/">American Legion Department of Colorado</a> · <a href="https://www.legion.org/">The American Legion (National)</a></p>
