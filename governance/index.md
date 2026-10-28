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
<dl class="fact-list">
{% for office in site.data.officers.offices %}
{% assign person = site.data.officers.people | where: "id", office.person_id | first %}
<div class="fact-row" id="{{ office.name | slugify }}">
<dt>{{ office.name | escape }}</dt>
<dd>{% if office.filled_by_role %}<strong>Filled by {{ office.filled_by_role | escape }}</strong>{% else %}<strong>{{ person.name | escape }}</strong>{% if person.service_abbreviation or person.distinction or office.installed_year %}<small class="entry-meta">{% if person.service_abbreviation %}{{ person.service_abbreviation | escape }}{% endif %}{% if person.distinction %}{% if person.service_abbreviation %} · {% endif %}{{ person.distinction | escape }}{% endif %}{% if office.installed_year %}{% if person.service_abbreviation or person.distinction %} · {% endif %}Installed {{ office.installed_year }}{% endif %}</small>{% endif %}{% endif %}</dd>
</div>
{% endfor %}
</dl>
<h2>Constitution and Bylaws</h2>
<p>The Post's Constitution and Bylaws are not yet available on this website. For questions about these documents, please <a href="{{ '/contact/' | relative_url }}">contact the Post</a>. Other public records can be found in our <a href="{{ '/documents/' | relative_url }}">Public Documents directory</a>.</p>
<h2>National and Department governing documents</h2>
<ul>
<li><a href="https://www.govinfo.gov/content/pkg/USCODE-2024-title36/html/USCODE-2024-title36-subtitleII-partB-chap217.htm">Congressional charter of The American Legion</a> — 36 U.S.C. Chapter 217 (2024 U.S. Code edition).</li>
<li><a href="https://www.legion.org/getmedia/fba34c55-e1f8-4ac5-8db4-0866cf4b2d9a/20ia0926-constitution-and-by-laws.pdf">National Constitution and By-Laws</a> — official American Legion PDF.</li>
<li><a href="https://coloradolegion.org/uploads/1/4/6/7/146715414/department_of_colorado_constitution_bylaws_amended_june_20_2026.docx">Department of Colorado Constitution and By-Laws</a> — amended June 20, 2026 (Word document).</li>
</ul>
<p>Official websites: <a href="https://coloradolegion.org/">Department of Colorado</a> · <a href="https://www.legion.org/">The American Legion (National)</a>.</p>
