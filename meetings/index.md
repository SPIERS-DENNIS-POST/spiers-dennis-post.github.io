---
title: Meetings
description: Spiers-Dennis Post 24 meetings and weekly gatherings in Olathe, including Monday coffee, Thursday PTSD Group, and fourth-Tuesday Post meetings.
permalink: /meetings/
source_ids: [post-meetings-2026-10-27, post-weekly-gatherings-2026-10-27, post-facilities-traditions-2026-10-27]
---
# Post meetings
Our regular meeting schedule and location are listed below.
{% include facts.html section="meetings" exclude="December meeting" %}
{% assign december_meeting = site.data.facts.meetings | where: "label", "December meeting" | first %}
{% if december_meeting and december_meeting.value %}<p class="notice">Our December meeting is {{ december_meeting.value | downcase | escape }}.</p>{% endif %}
## {{ site.time | date: "%Y" }} meeting dates
These are the fourth Tuesdays from January through November. December is excluded because the meeting is usually canceled.
{% include meeting-year-dates.html %}
Select a date to download its event as an iCalendar (.ics) file for your preferred calendar app. <a href="{{ '/meetings/calendar.ics' | relative_url }}">Download all {{ site.time | date: "%Y" }} meeting dates (.ics)</a> instead if you want the full year.
Calendar entries use an editable one-hour placeholder; the meeting end time is not confirmed.
Please [contact the Post]({{ '/contact/' | relative_url }}) to confirm any schedule changes, especially around the holidays.
## Weekly gatherings
For veterans. You do not need to be a member of the American Legion.
### Monday coffee
We get together for coffee at the Post hall every Monday morning.
{% include facts.html section="monday_coffee" %}
<p>Coffee was started by James Smith, USMC.</p>
### PTSD Group
Our PTSD Group meets at the Post hall on Thursdays and is conducted by a Vet Center counselor.
{% include facts.html section="ptsd_group" %}
<p>For participation details or schedule changes, please <a href="{{ '/contact/' | relative_url }}">contact the Post</a>.</p>
## Annual observances and traditions
These are our customary activities; arrangements for a particular year may vary.<sup class="reference"><a href="#reference-post-facilities-traditions-2026-10-27" aria-label="Reference 3">[3]</a></sup>
### Memorial Day
Post members place flags at Olathe, Pea Green, and Ash Mesa cemeteries.
### Veterans Day
The Post attends the OMHS Veterans Day Assembly, held in the middle school gym.
### Thanksgiving
Members and their families traditionally hold Thanksgiving dinner at the Post, using its large gathering areas and kitchen.
