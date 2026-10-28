---
title: Sources & corrections
description: Sources for Post 24 history and records, and how to request a correction.
permalink: /sources/
---
# Sources and corrections
Our history and records pages link to original evidence where available. This directory retains source descriptions, research context, limitations, and unresolved questions for visitors, historians, and automated readers. The Post reports its own schedules, leadership, facilities, and traditions directly on the relevant pages; supporting provenance is retained here without circular footnotes.
<ul class="external-list">
{% for source in site.data.sources %}
<li id="source-{{ source.id | slugify }}"><strong>{% if source.url %}<a href="{{ source.url | escape }}">{{ source.title | escape }}</a>{% else %}{{ source.title | escape }}{% endif %}</strong>{% if source.details %}<p>{{ source.details | escape }}</p>{% endif %}{% if source.published_on %}<p>{{ source.published_on | date: "%B %-d, %Y" }}</p>{% endif %}</li>
{% endfor %}
</ul>
## Corrections
If you notice an error, email <a href="mailto:{{ site.data.post.contact.email | escape }}">{{ site.data.post.contact.email | escape }}</a> or call <a href="tel:+1{{ site.data.post.contact.phone | remove: '-' }}">{{ site.data.post.contact.phone | escape }}</a>.
