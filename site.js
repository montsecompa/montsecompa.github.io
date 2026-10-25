const $ = s => document.querySelector(s);
const esc = s => s.replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const themeOf = k => THEMES[k] || OTHER;
const count = k => PUBS.filter(p=>p[1]===k).length;

// headline numbers
if ($("#facts")) {
  $("#facts").innerHTML = [
    [PUBS.length,"peer-reviewed articles"],
    ["2,400+","citations (Google Scholar)"],
    ["26","h-index (Google Scholar)"],
    ["12","funded projects, 3 as PI"],
    ["10","students co-supervised"]
  ].map(([b,s])=>`<div><b>${b}</b><span>${s}</span></div>`).join("");
}

// research themes
if ($("#themes")) {
  $("#themes").innerHTML = Object.entries(THEMES).map(([k,t])=>
    `<div class="theme"><h3><span class="sw" style="background:${t.color}"></span>${t.name}</h3><p>${t.text}</p><a href="publications.html?theme=${k}">See ${count(k)} papers</a></div>`).join("");
}

// publications
if ($("#publist")) {
  let filter = new URLSearchParams(location.search).get("theme") || "all";
  if (filter!=="all" && !THEMES[filter] && filter!=="other") filter="all";
  const chips = [["all","All",null],
    ["litter","Marine litter",THEMES.litter.color],
    ["ingest","Microplastic ingestion",THEMES.ingest.color],
    ["risk","Risk assessment",THEMES.risk.color],
    ["invasive","Invasive species",THEMES.invasive.color],
    ["other","Other",OTHER.color]];
  const tools = $("#pubtools");
  chips.forEach(([k,label,c])=>{
    const b=document.createElement("button"); b.className="chip"; b.dataset.k=k;
    b.innerHTML=(c?`<span class="sw" style="background:${c}"></span>`:"")+label;
    b.addEventListener("click",()=>setFilter(k));
    tools.insertBefore(b,$("#q"));
  });
  const setFilter = k => {
    filter=k;
    document.querySelectorAll(".chip").forEach(c=>c.setAttribute("aria-pressed",c.dataset.k===k));
    const u=new URL(location); if(k==="all") u.searchParams.delete("theme"); else u.searchParams.set("theme",k);
    history.replaceState(null,"",u);
    renderPubs();
  };
  const boldMe = a => esc(a).replace(/Compa, M\./g,"<b>Compa, M.</b>");
  function renderPubs(){
    const q=$("#q").value.trim().toLowerCase(), fo=$("#firstonly").checked;
    const rows=PUBS.filter(p=>(filter==="all"||p[1]===filter)&&(!fo||p[6])&&(!q||(p[2]+" "+p[3]+" "+p[4]).toLowerCase().includes(q)));
    $("#pubcount").textContent = `Showing ${rows.length} of ${PUBS.length} articles`;
    if(!rows.length){$("#publist").innerHTML=`<p class="empty">No articles match. Clear the search or choose another theme.</p>`;return;}
    const years=[...new Set(rows.map(r=>r[0]))];
    $("#publist").innerHTML=years.map(y=>`<div class="yr"><h3>${y}</h3><div>${rows.filter(r=>r[0]===y).map(p=>{
      const t=themeOf(p[1]); const role=p[6]==="f"?"First author":p[6]==="l"?"Last author":"";
      const title=p[5]?`<a class="t" href="https://doi.org/${p[5]}" rel="noopener">${esc(p[2])}</a>`:`<span class="t">${esc(p[2])}</span>`;
      return `<article class="pub" style="--c:${t.color}">${title}<span class="a">${boldMe(p[3])}</span><span class="j"><i>${esc(p[4])}</i>${role?`<span class="role">${role}</span>`:""}</span></article>`;
    }).join("")}</div></div>`).join("");
  }
  $("#q").addEventListener("input",renderPubs);
  $("#firstonly").addEventListener("change",renderPubs);
  setFilter(filter);
}

// funding
if ($("#fundrows")) {
  $("#fundrows").innerHTML=FUND.map(f=>`<tr><td>${f[0]}</td><td><span class="pn">${esc(f[1])}${f[3]?'<span class="pi">PI</span>':""}</span><span class="meta">${esc(f[2])}</span></td><td class="amt">${f[4]}</td></tr>`).join("");
}
if ($("#grants")) {
  $("#grants").innerHTML=GRANTS.map(g=>`<li><span class="y">${g[0]}</span><span><b>${esc(g[1])}</b>${g[2]?`<small>${esc(g[2])}</small>`:""}</span></li>`).join("");
}
if ($("#students")) {
  $("#students").innerHTML=STUDENTS.map(s=>`<li><span class="y">${s[0]}</span><span><b>${esc(s[1])}</b><small>${esc(s[2])}</small></span></li>`).join("");
}

// talks
if ($("#talklist")) {
  const tyears=[...new Set(TALKS.map(t=>t[0]))];
  $("#talklist").innerHTML=tyears.map((y,i)=>{
    const ts=TALKS.filter(t=>t[0]===y);
    return `<details class="talks"${i<2?" open":""}><summary>${y} <span style="color:var(--ink-2);font-weight:400;margin-left:auto;margin-right:16px">${ts.length} presentation${ts.length>1?"s":""}</span></summary>${ts.map(t=>`<div class="talk"><span style="color:var(--ink-2)">${t[4]==="i"?"Intl.":"Natl."}</span><span>${esc(t[1])}<span class="v">${esc(t[2])}</span></span><span class="f">${t[3]}</span></div>`).join("")}</details>`;
  }).join("");
}

// mobile menu
const btn=$(".menu-btn"), nav=$("#nav");
btn.addEventListener("click",()=>{const o=nav.classList.toggle("open");btn.setAttribute("aria-expanded",o);});

// depth gauge marker on the current page
const cur=document.querySelector(".gauge a.on"), bob=$(".gauge .bob");
if(cur && bob){ const li=cur.parentElement; bob.style.top=(li.offsetTop+li.offsetHeight/2-4)+"px"; }

// theme toggle
$("#yr").textContent=new Date().getFullYear();
$("#themebtn").addEventListener("click",()=>{
  const r=document.documentElement, dark=r.dataset.theme?r.dataset.theme==="dark":matchMedia("(prefers-color-scheme: dark)").matches;
  r.dataset.theme=dark?"light":"dark"; try{localStorage.setItem("mc-theme",r.dataset.theme)}catch(e){}
});
