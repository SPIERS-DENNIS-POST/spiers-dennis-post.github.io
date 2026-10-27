---
title: Sources & corrections
description: Primary source registry and corrections contact for Spiers-Dennis American Legion Post No. 24.
permalink: /sources/
---
# Sources & corrections
This website distinguishes Post-published information, American Legion national and Department records, and unresolved research leads. Published statements should cite the underlying source instead of treating an unsourced summary as primary evidence.
## Source registry
<ul class="external-list">
{% for source in site.data.sources %}
<li id="source-{{ source.id | slugify }}"><strong><a href="{{ source.url | escape }}">{{ source.title | escape }}</a></strong>{% if source.details %}<p>{{ source.details | escape }}</p>{% endif %}{% if source.published_on %}<p>Report date: {{ source.published_on | date: "%Y-%m-%d" }}</p>{% endif %}</li>
{% endfor %}
</ul>
## Corrections
Report apparent factual errors through the Post's <a href="mailto:{{ site.data.post.contact.email | escape }}">public email</a> or <a href="tel:+1{{ site.data.post.contact.phone | remove: '-' }}">desk telephone</a>. Do not use repository issues to disclose member information, private contact details, or confidential records.
The Post's shared desk phone and organizational email are the only contact channels approved for publication. No member's or officer's personal contact information may be published.
