---
title: Meetings
description: Spiers-Dennis Post 24 meets at 5:30 p.m. on the fourth Tuesday of each month. Dinner is served at 5 p.m.; December meetings are usually canceled.
permalink: /meetings/
source_ids: [post-meetings-2026-10-27]
---
# Post meetings
Our regular meeting schedule and location are listed below.
{% include facts.html section="meetings" exclude="December meeting" %}
{% assign december_meeting = site.data.facts.meetings | where: "label", "December meeting" | first %}
{% if december_meeting and december_meeting.value %}<p class="notice">Our December meeting is {{ december_meeting.value | downcase | escape }}.</p>{% endif %}
Please [contact the Post]({{ '/contact/' | relative_url }}) to confirm any schedule changes, especially around the holidays.
