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