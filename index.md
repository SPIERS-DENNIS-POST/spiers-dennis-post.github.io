---
title: Main
description: Visit or contact Spiers-Dennis American Legion Post No. 24 in Olathe, Colorado. Learn about our officers, history, and membership.
permalink: /
---
<section class="hero">
<p class="eyebrow">American Legion Post 24 · Olathe, Colorado</p>
<h1>Spiers-Dennis Post No. 24</h1>
<p><strong>Post hall:</strong> {{ site.data.post.address.street | escape }}, {{ site.data.post.address.city | escape }}, {{ site.data.post.address.region | escape }} {{ site.data.post.address.postal_code | escape }}</p>
<p>Spiers-Dennis gathers local Olathe veterans, and orients them to serve their community, in order to sustain the project of our nation in one small corner.</p>
<section class="prose" aria-labelledby="purposes">
<div class="section-head"><h2 id="purposes">Purposes</h2></div>
<p>To uphold and defend the Constitution of the United States;<br>
To promote peace and good will among the peoples of the United States and all the nations of the Earth;<br>
To preserve the memories and incidents of the 2 World Wars and the other great hostilities fought to uphold democracy;<br>
To cement the ties and comradeship born of service;<br>
And to consecrate the efforts of its members to mutual helpfulness and service to their country.</p>
<p class="verified"><em>Source: <a href="https://www.govinfo.gov/content/pkg/PLAW-105publ225/html/PLAW-105publ225.htm">36 U.S.C. § 21702 — Purposes</a>.</em></p>
<p>FOR GOD AND COUNTRY WE ASSOCIATE OURSELVES TOGETHER FOR THE FOLLOWING PURPOSES:<br>
To uphold and defend the Constitution of the United States of America;<br>
To maintain law and order;<br>
To foster and perpetuate a one hundred percent Americanism;<br>
To preserve the memories and incidents of our associations in all wars;<br>
To inculcate a sense of individual obligation to the community, state and nation;<br>
To combat the autocracy of both the classes and the masses;<br>
To make right the master of might;<br>
To promote peace and goodwill on earth;<br>
To safeguard and transmit to posterity the principles of justice, freedom and democracy;<br>
To consecrate and sanctify our comradeship by our devotion to mutual helpfulness.</p>
<p class="verified"><em>Source: <a href="https://www.legion.org/about/organization/preamble">The American Legion — Preamble</a>.</em></p>
</section>
<p><a href="{{ '/contact/' | relative_url }}">Contact the Post</a></p>
<p><a href="{{ '/donate/' | relative_url }}">Learn how to support Post 24</a></p>
</section>
{% include next-meeting.html %}
<section aria-labelledby="post-information">
<div class="section-head"><h2 id="post-information">Explore the Post</h2></div>
<div class="grid">
<div class="card"><h3><a href="{{ '/history/' | relative_url }}">Our history</a></h3><p>Our roots in Olathe date back to at least 1920, including a clubhouse dedicated in 1923.</p></div>
<div class="card"><h3><a href="{{ '/governance/' | relative_url }}">Governance</a></h3><p>Current officers and information about the Post's governing documents.</p></div>
<div class="card"><h3><a href="{{ '/meetings/' | relative_url }}">Meetings</a></h3><p>Fourth Tuesday at 5:30 p.m., with dinner at 5:00 p.m. {% assign home_year = site.time | date: "%Y" | plus: 0 %}{% if site.data.meeting_calendar.december_meeting_years contains home_year %}The December {{ home_year }} meeting will be held.{% else %}December meetings are usually canceled.{% endif %}</p></div>
<div class="card"><h3><a href="{{ '/building/' | relative_url }}">Post Home</a></h3><p>Where to find us in Olathe.</p></div>
<div class="card"><h3><a href="{{ '/membership/' | relative_url }}">Membership</a></h3><p>Joining the Post and American Legion membership information.</p></div>
<div class="card"><h3><a href="{{ '/contact/' | relative_url }}">Contact us</a></h3><p>Our public phone number, email address, and location.</p></div>
</div>
</section>
<section aria-labelledby="american-legion">
<div class="section-head"><h2 id="american-legion">The American Legion</h2></div>
<p>For national membership requirements and programs, visit our <a href="{{ '/legion/' | relative_url }}">American Legion resource links</a>.</p>
</section>
