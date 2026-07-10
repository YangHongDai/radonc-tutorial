(function(){
  const SK='radonc_lang';
  const NAV_SCROLL_EDGE=8;
  let lang=localStorage.getItem(SK)||'en';

  function syncTopNavHeight(){
    const nav=document.querySelector('.top-nav');
    if(nav){
      document.documentElement.style.setProperty('--top-nav-height',`${nav.offsetHeight}px`);
    }
  }

  function apply(l){
    lang=l; localStorage.setItem(SK,l);
    document.documentElement.lang=l==='zh'?'zh-Hant':'en';
    document.querySelectorAll('[data-lang]').forEach(el=>{
      el.style.display=el.dataset.lang===l?'':'none';
    });
    document.querySelectorAll('[data-zh][data-en]').forEach(el=>{
      el.textContent=el.dataset[l];
    });
    const btn=document.getElementById('langToggle');
    if(btn) btn.textContent=l==='zh'?'EN':'\u4e2d\u6587';
    syncTopNavHeight();
    document.dispatchEvent(new CustomEvent('langchange',{detail:{lang:l}}));
  }

  function toggle(){ apply(lang==='zh'?'en':'zh'); }
  function get(){ return lang; }

  function markActiveNavLink(){
    const currentUrl=new URL(window.location.href);
    document.querySelectorAll('.top-nav-links a[href]').forEach(link=>{
      let isActive=false;
      try{
        const targetUrl=new URL(link.getAttribute('href'),currentUrl.href);
        isActive=decodeURIComponent(targetUrl.pathname)===decodeURIComponent(currentUrl.pathname);
      }catch(err){}
      link.classList.toggle('active',isActive);
      if(isActive) link.setAttribute('aria-current','page');
      else link.removeAttribute('aria-current');
    });
  }

  function updateTopNavScrollState(rail,links,prev,next){
    const maxScroll=Math.max(links.scrollWidth-links.clientWidth,0);
    const canScrollLeft=links.scrollLeft>NAV_SCROLL_EDGE;
    const canScrollRight=links.scrollLeft<maxScroll-NAV_SCROLL_EDGE;
    rail.classList.toggle('can-scroll-left',canScrollLeft);
    rail.classList.toggle('can-scroll-right',canScrollRight);
    prev.disabled=!canScrollLeft;
    next.disabled=!canScrollRight;
  }

  function enhanceTopNav(){
    const links=document.querySelector('.top-nav-links');
    if(!links||links.dataset.enhanced==='true') return;

    const rail=document.createElement('div');
    rail.className='top-nav-rail';

    const prev=document.createElement('button');
    prev.type='button';
    prev.className='top-nav-scroll-btn';
    prev.setAttribute('aria-label','Scroll left');
    prev.title='Scroll left';
    prev.innerHTML='&#x2039;';

    const next=document.createElement('button');
    next.type='button';
    next.className='top-nav-scroll-btn';
    next.setAttribute('aria-label','Scroll right');
    next.title='Scroll right';
    next.innerHTML='&#x203A;';

    const leftFade=document.createElement('div');
    leftFade.className='top-nav-fade left';
    const rightFade=document.createElement('div');
    rightFade.className='top-nav-fade right';

    links.dataset.enhanced='true';
    links.parentNode.insertBefore(rail,links);
    rail.append(prev,leftFade,links,rightFade,next);

    const scrollByStep=direction=>{
      links.scrollBy({
        left:direction*Math.max(links.clientWidth*.55,180),
        behavior:'smooth'
      });
    };
    const update=()=>{
      updateTopNavScrollState(rail,links,prev,next);
      syncTopNavHeight();
    };

    prev.addEventListener('click',()=>scrollByStep(-1));
    next.addEventListener('click',()=>scrollByStep(1));
    links.addEventListener('scroll',update,{passive:true});
    window.addEventListener('resize',update);
    window.addEventListener('load',update,{once:true});
    if(document.fonts&&document.fonts.ready){
      document.fonts.ready.then(update);
    }

    markActiveNavLink();
    requestAnimationFrame(()=>{
      const activeLink=links.querySelector('a.active');
      if(activeLink){
        activeLink.scrollIntoView({block:'nearest',inline:'center'});
      }
      update();
    });
  }

  document.addEventListener('DOMContentLoaded',()=>{
    const nav=document.querySelector('.top-nav-inner');
    if(nav && !document.getElementById('langToggle')){
      const btn=document.createElement('button');
      btn.id='langToggle';
      btn.className='lang-toggle';
      btn.type='button';
      btn.textContent=lang==='zh'?'EN':'\u4e2d\u6587';
      btn.onclick=toggle;
      nav.appendChild(btn);
    }
    enhanceTopNav();
    apply(lang);
    syncTopNavHeight();
  });

  window.I18n={apply,toggle,get};
})();
