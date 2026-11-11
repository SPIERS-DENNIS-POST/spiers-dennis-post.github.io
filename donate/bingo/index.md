---
layout: bingo
title: Bingo in Olathe
description: Public Bingo on Friday, Saturday, and Sunday at the American Legion hall in Olathe, Colorado. Find times, prices, visitor directions, and contacts.
permalink: /donate/bingo/
provenance_ids: [post-bingo-session-listing-2026-11-10, post-bingo-posted-notices-2026-11-10, post-visitor-parking-2026-11-10, post-visitor-entrance-2026-11-10, post-wheelchair-entrance-2026-11-10]
source_ids: [colorado-bingo-underage-purchase-law]
---
<section class="bingo-hero" aria-labelledby="bingo-title">
<div class="bingo-hero-copy">
<p class="bingo-eyebrow">FRIDAY · SATURDAY · SUNDAY / OLATHE, COLORADO</p>
<h1 id="bingo-title">BINGO<span aria-hidden="true">!</span></h1>
<p class="bingo-hero-title">Your seat at the table.</p>
<p class="bingo-hero-description">Good company, a little suspense, and a reason to get together. Join us for public Bingo at the American Legion hall in Olathe.</p>
<div class="bingo-hero-tags"><span>OPEN TO THE PUBLIC</span><span>THREE DAYS A WEEK</span></div>
</div>
<div class="bingo-ticket" aria-hidden="true">
<div class="bingo-ticket-top"><span>YOUR LUCKY NIGHT</span><span>NO. 024</span></div>
<div class="bingo-ticket-letters"><span>B</span><span>I</span><span>N</span><span>G</span><span>O</span></div>
<div class="bingo-ticket-grid"><span>7</span><span>18</span><span>32</span><span>53</span><span>66</span><span>11</span><span>24</span><span>41</span><span>59</span><span>71</span><span>3</span><span>27</span><span class="bingo-ticket-free">★</span><span>48</span><span>63</span><span>15</span><span>29</span><span>39</span><span>56</span><span>72</span><span>1</span><span>20</span><span>45</span><span>50</span><span>69</span></div>
<div class="bingo-ticket-bottom"><span>SPIERS-DENNIS POST 24</span><span>OLATHE, CO</span></div>
</div>
</section>
<section class="bingo-section bingo-schedule" id="schedule" aria-labelledby="bingo-schedule-title">
<div class="bingo-section-heading"><p class="bingo-eyebrow">01 / WEEKLY SESSIONS</p><h2 id="bingo-schedule-title">Find your night.</h2><p>American Legion Post 65 and {{ site.data.post.name | escape }} run the sessions below. Each day shows the host Post.</p></div>
<div class="bingo-days">
{% for session in site.data.bingo.sessions %}
<article id="{{ session.id | escape }}" class="bingo-day{% if session.id == 'friday' %} bingo-day-friday{% elsif session.id == 'sunday' %} bingo-day-sunday{% endif %}"><div class="bingo-day-top"><span class="bingo-day-label">{{ session.abbreviation | escape }}</span><span class="bingo-day-post">{% if session.organizer == 'post65' %}POST 65{% else %}POST {{ site.data.post.post_number }}{% endif %}</span></div><h3>{{ session.day | escape }}</h3><p class="bingo-day-time"><time datetime="{{ session.start_time }}">{% include bingo-time.html value=session.start_time %}</time></p><p class="bingo-day-note">Doors open at <time datetime="{{ session.doors_time }}">{% if session.doors_time == '12:00' %}noon{% else %}{% include bingo-time.html value=session.doors_time compact=true %}{% endif %}</time></p></article>
{% endfor %}
</div>
</section>
<section class="bingo-prices" aria-labelledby="bingo-price-title">
<div class="bingo-section-heading"><div><p class="bingo-eyebrow">02 / WHAT IT COSTS</p><h2 id="bingo-price-title">Prices &amp; play</h2></div><p>Machine packages, paper packs, and extras for every Bingo session.</p></div>
<h3 class="bingo-prices-subhead">Machine packages <span>All sessions</span></h3>
<div class="bingo-price-tiers">
{% for package in site.data.bingo.machine_packages %}
<article id="machine-{{ package.id | escape }}" class="bingo-price-tier bingo-tier-{{ package.id | escape }}"><div class="bingo-tier-top"><h4>{{ package.name | escape }}</h4><strong><data value="{{ package.price }}" data-currency="{{ site.data.bingo.currency }}">${{ package.price }}</data></strong></div><p class="bingo-tier-spec">TAB-E {{ package.machine_number }} · {{ package.faces }} faces</p><p>{{ package.yellow_da }} yellow D/A, {{ package.blue_da }} blue D/A, {{ package.progressives }} progressive, {{ package.included_packs }} pack included</p></article>
{% endfor %}
</div>
<div class="bingo-paper-wrap">
<section class="bingo-paper-panel" aria-labelledby="bingo-paper-title"><h3 id="bingo-paper-title">Paper packs</h3><table class="bingo-paper-table"><thead><tr><th scope="col">Packs</th><th scope="col">Price</th></tr></thead><tbody>
{% for paper in site.data.bingo.paper_packs %}
<tr id="paper-{{ paper.count }}"><th scope="row">{{ paper.count }} {% if paper.count == 1 %}pack{% else %}packs{% endif %}</th><td><data value="{{ paper.price }}" data-currency="{{ site.data.bingo.currency }}">${{ paper.price }}</data></td></tr>
{% endfor %}
</tbody></table></section>
<section class="bingo-paper-panel" aria-labelledby="bingo-extras-title"><h3 id="bingo-extras-title">Extras</h3><table class="bingo-paper-table bingo-extras-table"><thead><tr><th scope="col">Item</th><th scope="col">Price</th></tr></thead><tbody>
{% for extra in site.data.bingo.extras %}
<tr id="extra-{{ extra.id | escape }}"><th scope="row">{{ extra.name | escape }}</th><td><data value="{{ extra.price }}" data-currency="{{ site.data.bingo.currency }}">${{ extra.price }}</data>{% if extra.unit != empty %} {{ extra.unit | escape }}{% endif %}</td></tr>
{% endfor %}
</tbody></table></section>
</div>
<details class="bingo-terms"><summary>New to Bingo? Game terms explained</summary><dl>
{% for item in site.data.bingo.terms %}
<div><dt>{{ item.term | escape }}</dt><dd>{{ item.meaning | escape }}</dd></div>
{% endfor %}
</dl></details>
<p class="bingo-price-note">Prices are subject to change.</p>
<p class="bingo-age-note"><strong>Age requirement:</strong> You must be at least {{ site.data.bingo.minimum_purchase_age }} years old to purchase Bingo cards or other chances to play, in accordance with Colorado law.</p>
<section class="bingo-payment" aria-labelledby="bingo-payment-title">
<h3 id="bingo-payment-title">Payment methods</h3>
<p>We currently accept <strong>{{ site.data.bingo.payment_methods.accepted | join: ' and ' | escape }}</strong> for Bingo purchases. <strong>{{ site.data.bingo.payment_methods.not_accepted | escape }}</strong> are not accepted.</p>
<p>{{ site.data.bingo.payment_methods.check_instruction | escape }}</p>
</section>
</section>
<section id="venue" class="bingo-detail bingo-arrival bingo-visit" aria-labelledby="bingo-arrival-title">
<p class="bingo-eyebrow">03 / HOW TO GET HERE</p><h2 id="bingo-arrival-title">Come on in.</h2>
<address><strong>American Legion Post Home</strong><span>315 South 5th Street</span><span>Olathe, Colorado 81425</span></address>
<p>Street parking is available along <strong>South 5th Street</strong> and <strong>Hersum Avenue</strong>. Use the streetside double doors in the <strong>cinderblock west section</strong> to enter the main hall.</p>
<p>The west entrance is wheelchair-accessible. The brick east entrance leads to a stairwell and is not wheelchair-accessible.</p>
<p class="bingo-map-links"><a href="https://www.openstreetmap.org/way/1411993746">OpenStreetMap</a><a href="https://www.google.com/maps/search/?api=1&amp;query=315%20S%205th%20St%2C%20Olathe%2C%20CO%2081425">Google Maps</a></p>
</section>
<section class="bingo-contact" aria-labelledby="bingo-contact-title">
<div><p class="bingo-eyebrow">04 / QUESTIONS?</p><h2 id="bingo-contact-title">Talk to the Posts.</h2><p>For questions about hours, pricing, or your first visit, contact the Post running your session.</p><p>For questions about games, pricing, or participation, you can also speak with a games manager during any Bingo session.</p></div>
<div class="bingo-contact-cards"><div class="bingo-contact-card"><span class="bingo-contact-type">SATURDAY &amp; SUNDAY</span><h3>Spiers-Dennis Post 24</h3><a href="tel:+1{{ site.data.post.contact.phone | remove: '-' }}">{{ site.data.post.contact.phone | escape }}</a><a href="mailto:{{ site.data.post.contact.email | escape }}">{{ site.data.post.contact.email | escape }}</a><p>The Post's shared desk phone accepts texts and voicemail.</p></div><div id="post65" class="bingo-contact-card"><span class="bingo-contact-type">FRIDAY</span><h3>{{ site.data.bingo.post65.name | escape }}</h3><a href="{{ site.data.bingo.post65.website | escape }}">Post 65 website</a><p>Contact Post 65 through its website for Friday Bingo questions.</p></div></div>
</section>