---
title: Home
description: Visit or contact Spiers-Dennis American Legion Post No. 24 in Olathe, Colorado. Learn about our officers, history, and membership.
permalink: /
---
<section class="hero">
<p class="eyebrow">American Legion Post 24 · Olathe, Colorado</p>
<h1>Spiers-Dennis Post No. 24</h1>
<p class="lede">Spiers-Dennis Post is the American Legion Post in Olathe, Colorado. Learn about our history, find the Post hall, meet our officers, and get in touch.</p>
<p><strong>Post hall:</strong> {{ site.data.post.address.street | escape }}, {{ site.data.post.address.city | escape }}, {{ site.data.post.address.region | escape }} {{ site.data.post.address.postal_code | escape }}</p>
<p><strong>Phone:</strong> <a href="tel:+1{{ site.data.post.contact.phone | remove: '-' }}">{{ site.data.post.contact.phone | escape }}</a> <span aria-hidden="true">·</span> <strong>Email:</strong> <a href="mailto:{{ site.data.post.contact.email | escape }}">{{ site.data.post.contact.email | escape }}</a></p>
</section>
<section aria-labelledby="post-information">
<div class="section-head"><h2 id="post-information">Explore the Post</h2></div>
<div class="grid">
<div class="card"><h3><a href="{{ '/history/' | relative_url }}">Our history</a></h3><p>Our roots in Olathe date back to at least 1920, including a clubhouse dedicated in 1923.</p></div>
<div class="card"><h3><a href="{{ '/governance/' | relative_url }}">Governance</a></h3><p>Current officers and information about the Post's governing documents.</p></div>
<div class="card"><h3><a href="{{ '/meetings/' | relative_url }}">Meetings</a></h3><p>Fourth Tuesday at 5:30 p.m., with dinner at 5:00 p.m. December meetings are usually canceled.</p></div>
<div class="card"><h3><a href="{{ '/building/' | relative_url }}">Post hall</a></h3><p>Where to find us in Olathe.</p></div>
<div class="card"><h3><a href="{{ '/membership/' | relative_url }}">Membership</a></h3><p>Joining the Post and American Legion membership information.</p></div>
<div class="card"><h3><a href="{{ '/contact/' | relative_url }}">Contact us</a></h3><p>Our public phone number, email address, and location.</p></div>
</div>
</section>
<section aria-labelledby="american-legion">
<div class="section-head"><h2 id="american-legion">The American Legion</h2></div>
<p>For national membership requirements and programs, visit our <a href="{{ '/legion/' | relative_url }}">American Legion resource links</a>.</p>
</section>
