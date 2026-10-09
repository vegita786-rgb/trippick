(function(){
  if(document.querySelector(".trip-social-growth")) return;
  const footer=document.querySelector("footer");
  if(!footer) return;
  const sec=document.createElement("section");
  sec.className="section trip-social-growth";
  sec.innerHTML='<div class="card"><div class="k">Stay trip-ready</div><h2>Follow TripPick for short booking checks</h2><p class="muted">Hotel fee traps, airport-transfer comparisons, attraction access and practical booking reminders.</p><a class="btn" href="https://www.facebook.com/people/TripPick/61595201849887/" target="_blank" rel="noopener">Follow on Facebook</a> <a class="btn" href="https://www.pinterest.com/vegita786/travel-planning-booking-tips/" target="_blank" rel="noopener">See travel pins</a> <button class="btn" id="trip-share-guide" type="button">Share this guide</button></div>';
  footer.parentNode.insertBefore(sec,footer);
  const b=document.getElementById("trip-share-guide");
  b.onclick=async()=>{const data={title:document.title,text:"Useful TripPick travel guide",url:location.href};try{if(navigator.share)await navigator.share(data);else{await navigator.clipboard.writeText(location.href);b.textContent="Link copied";}}catch(e){}};
})();
(function(){
  const c=window.TRIPPICK_AFFILIATE||{};
  const p=location.pathname.split('/').pop();
  const map={
    "rome-colosseum-tours.html":["viator","colosseum","Check current Colosseum options"],
    "colosseum-arena-vs-underground.html":["viator","colosseum","Compare Colosseum experiences"],
    "colosseum-underground-tickets-sold-out.html":["viator","colosseum","Check current Colosseum availability"],
    "colosseum-ticket-release-date-calculator.html":["viator","colosseum","See Colosseum experiences"],
    "rome-vatican-tours.html":["viator","vatican","Check current Vatican tours"],
    "paris-louvre-tours.html":["viator","louvre","Check current Louvre options"],
    "statue-liberty-tour-guide.html":["viator","statueLiberty","Check current Statue of Liberty options"],
    "statue-liberty-crown-vs-pedestal.html":["viator","statueLiberty","See Statue of Liberty experiences"],
    "vegas-grand-canyon-tours.html":["viator","grandCanyon","Check current Grand Canyon tours"],
    "grand-canyon-west-vs-south-rim-vegas.html":["viator","grandCanyon","Compare Grand Canyon tours"],
    "best-hotels-times-square.html":["travelpayouts","timesSquareHotels","Compare Times Square hotel options"],
    "times-square-family-hotels.html":["travelpayouts","timesSquareHotels","Compare family-friendly hotel options"],
    "times-square-hotel-fees-checklist.html":["travelpayouts","timesSquareHotels","Check current Times Square stays"],
    "las-vegas-strip-hotels.html":["travelpayouts","vegasHotels","Compare Las Vegas Strip hotels"],
    "airport-transfer-jfk-manhattan.html":["travelpayouts","jfkTransfer","Compare JFK transfer options"],
    "jfk-manhattan-with-luggage.html":["travelpayouts","jfkTransfer","Check current JFK transfer options"],
    "jfk-group-transfer-cost-calculator.html":["travelpayouts","jfkTransfer","Compare live JFK transfer options"],
    "rome-fco-airport-transfer-guide.html":["travelpayouts","fcoTransfer","Compare Rome FCO transfer options"]
  };
  const m=map[p]; if(!m) return;
  const url=c[m[0]]&&c[m[0]][m[1]];
  if(!c.enabled || !url) return;
  const pending=[...document.querySelectorAll('.btn.disabled, span.btn.disabled')];
  pending.forEach(el=>{
    const a=document.createElement('a');
    a.className='btn affiliate-live';
    a.href=url; a.target='_blank'; a.rel='sponsored nofollow noopener';
    a.textContent=m[2];
    el.replaceWith(a);
  });
  const muted=[...document.querySelectorAll('.muted')];
  const target=muted.find(x=>/partner link|tracked partner|affiliate approval/i.test(x.textContent));
  if(target) target.textContent=c.disclosure;
})();