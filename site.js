const LANG = document.documentElement.lang || "en";
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const num = s => LANG==="en" ? s : String(s).replace(/,/g,".");
const tr = x => (x && typeof x === "object") ? (x[LANG] || x.en) : x;

const UI = {
  en:{papers:n=>`See ${n} papers`, all:"All", showing:(a,b)=>`Showing ${a} of ${b} articles`,
      none:"No articles match. Clear the search or choose another theme.", first:"First author", last:"Last author",
      pres:n=>`${n} presentation${n>1?"s":""}`, intl:"Intl.", natl:"Natl.", pi:"PI",
      fmt:{"Oral":"Oral","Poster":"Poster","Poster and flash talk":"Poster and flash talk","Invited talk":"Invited talk"}},
  es:{papers:n=>`Ver ${n} artículos`, all:"Todos", showing:(a,b)=>`Mostrando ${a} de ${b} artículos`,
      none:"Ningún artículo coincide. Borra la búsqueda o elige otro tema.", first:"Primera autora", last:"Última autora",
      pres:n=>`${n} presentaci${n>1?"ones":"ón"}`, intl:"Intl.", natl:"Nac.", pi:"IP",
      fmt:{"Oral":"Oral","Poster":"Póster","Poster and flash talk":"Póster y presentación flash","Invited talk":"Conferencia invitada"}},
  ca:{papers:n=>`Veure ${n} articles`, all:"Tots", showing:(a,b)=>`Es mostren ${a} de ${b} articles`,
      none:"Cap article coincideix. Esborra la cerca o tria un altre tema.", first:"Primera autora", last:"Darrera autora",
      pres:n=>`${n} presentaci${n>1?"ons":"ó"}`, intl:"Intl.", natl:"Nac.", pi:"IP",
      fmt:{"Oral":"Oral","Poster":"Pòster","Poster and flash talk":"Pòster i presentació flaix","Invited talk":"Conferència convidada"}}
}[LANG] || {};

const themeOf = k => THEMES[k] || OTHER;
const count = k => PUBS.filter(p=>p[1]===k).length;

if ($("#facts")) {
  $("#facts").innerHTML = FACTS.map(([b,s])=>`<div><b>${num(b)}</b><span>${esc(tr(s))}</span></div>`).join("");
}

if ($("#themes")) {
  $("#themes").innerHTML = Object.entries(THEMES).map(([k,t])=>
    `<div class="theme"><h3><span class="sw" style="background:${t.color}"></span>${esc(tr(t.name))}</h3><p>${esc(tr(t.text))}</p><a href="publications.html?theme=${k}">${UI.papers(count(k))}</a></div>`).join("");
}

if ($("#publist")) {
  let filter = new URLSearchParams(location.search).get("theme") || "all";
  if (filter!=="all" && !THEMES[filter] && filter!=="other") filter="all";
  const chips = [["all",UI.all,null], ...Object.entries(THEMES).map(([k,t])=>[k,tr(t.short),t.color]), ["other",tr(OTHER.short),OTHER.color]];
  const tools = $("#pubtools");
  chips.forEach(([k,label,c])=>{
    const b=document.createElement("button"); b.className="chip"; b.dataset.k=k;
    b.innerHTML=(c?`<span class="sw" style="background:${c}"></span>`:"")+esc(label);
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
    $("#pubcount").textContent = UI.showing(rows.length, PUBS.length);
    if(!rows.length){$("#publist").innerHTML=`<p class="empty">${UI.none}</p>`;return;}
    const years=[...new Set(rows.map(r=>r[0]))].sort((a,b)=>b-a);
    $("#publist").innerHTML=years.map(y=>`<div class="yr"><h3>${y}</h3><div>${rows.filter(r=>r[0]===y).map(p=>{
      const t=themeOf(p[1]); const role=p[6]==="f"?UI.first:p[6]==="l"?UI.last:"";
      const title=p[5]?`<a class="t" href="https://doi.org/${p[5]}" rel="noopener">${esc(p[2])}</a>`:`<span class="t">${esc(p[2])}</span>`;
      return `<article class="pub" style="--c:${t.color}">${title}<span class="a">${boldMe(p[3])}</span><span class="j"><i>${esc(p[4])}</i>${role?`<span class="role">${role}</span>`:""}</span></article>`;
    }).join("")}</div></div>`).join("");
  }
  $("#q").addEventListener("input",renderPubs);
  $("#firstonly").addEventListener("change",renderPubs);
  setFilter(filter);
}

if ($("#fundrows")) {
  $("#fundrows").innerHTML=FUND.map(f=>`<tr><td>${f[0]}</td><td><span class="pn">${esc(tr(f[1]))}${f[3]?`<span class="pi">${UI.pi}</span>`:""}</span><span class="meta">${esc(tr(f[2]))}</span></td><td class="amt">${f[4]?num(f[4]):"–"}</td></tr>`).join("");
}
if ($("#grants")) {
  $("#grants").innerHTML=GRANTS.map(g=>`<li><span class="y">${g[0]}</span><span><b>${esc(tr(g[1]))}</b>${g[2]?`<small>${esc(tr(g[2]))}</small>`:""}</span></li>`).join("");
}
if ($("#students")) {
  $("#students").innerHTML=STUDENTS.map(s=>`<li><span class="y">${s[0]}</span><span><b>${esc(s[1])}</b><small>${esc(tr(s[2]))}</small></span></li>`).join("");
}

if ($("#talklist")) {
  const tyears=[...new Set(TALKS.map(t=>t[0]))];
  $("#talklist").innerHTML=tyears.map((y,i)=>{
    const ts=TALKS.filter(t=>t[0]===y);
    return `<details class="talks"${i<2?" open":""}><summary>${y} <span style="color:var(--ink-2);font-weight:400;margin-left:auto;margin-right:16px">${UI.pres(ts.length)}</span></summary>${ts.map(t=>`<div class="talk"><span style="color:var(--ink-2)">${t[4]==="i"?UI.intl:UI.natl}</span><span>${esc(t[1])}<span class="v">${esc(t[2])}</span></span><span class="f">${UI.fmt[t[3]]||t[3]}</span></div>`).join("")}</details>`;
  }).join("");
}

// mobile menu
const btn=$(".menu-btn"), nav=$("#nav");
btn.addEventListener("click",()=>{const o=nav.classList.toggle("open");btn.setAttribute("aria-expanded",o);});

// depth gauge marker
const cur=document.querySelector(".gauge a.on"), bob=$(".gauge .bob");
if(cur && bob){ const li=cur.parentElement; bob.style.top=(li.offsetTop+li.offsetHeight/2-4)+"px"; }

// remember the chosen language
document.querySelectorAll(".langs a").forEach(a=>a.addEventListener("click",()=>{try{localStorage.setItem("mc-lang",a.hreflang)}catch(e){}}));

// theme toggle
$("#yr").textContent=new Date().getFullYear();
$("#themebtn").addEventListener("click",()=>{
  const r=document.documentElement, dark=r.dataset.theme?r.dataset.theme==="dark":matchMedia("(prefers-color-scheme: dark)").matches;
  r.dataset.theme=dark?"light":"dark"; try{localStorage.setItem("mc-theme",r.dataset.theme)}catch(e){}
});
