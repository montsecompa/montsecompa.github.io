#!/usr/bin/env python3
"""Builds the site's HTML pages in English (root), Spanish (/es/) and Catalan (/ca/).

Edit the text below, then run:  python3 build.py
Lists (publications, projects, talks...) live in data.js and need no rebuild.
"""
import os, html

HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en", "es", "ca"]
LANG_NAME = {"en": "English", "es": "Español", "ca": "Català"}
PREFIX = {"en": "", "es": "es/", "ca": "ca/"}
EMAIL = "montserrat.compa@uib.es"
ORCID = "https://orcid.org/0000-0002-0661-8712"
SCOPUS = "https://www.scopus.com/authid/detail.uri?authorId=57197743866"

# file, depth label
PAGES = [("index", "0 m"), ("about", "10 m"), ("research", "40 m"), ("publications", "120 m"),
         ("funding", "200 m"), ("career", "400 m"), ("talks", "600 m"), ("outreach", "700 m"), ("contact", "800 m")]

T = {
"en": {
 "nav": {"index":"Home","about":"About","research":"Research","publications":"Publications","funding":"Funding","career":"Career","talks":"Talks","outreach":"Outreach","contact":"Contact"},
 "gauge": {"index":"Surface","contact":"Seafloor"},
 "title": {"about":"About","research":"Research","publications":"Publications","funding":"Projects and funding","career":"Career","talks":"Conferences and talks","outreach":"Service and outreach","contact":"Contact"},
 "blurb": {"about":"Background, education and research interests.",
           "research":"Four lines of work on plastic pollution and human pressures in the Mediterranean.",
           "publications":"All peer-reviewed articles, book chapters and technical reports, searchable and filterable by theme.",
           "funding":"Research projects, budgets, fellowships, stays abroad and time at sea.",
           "career":"Positions held, teaching, and the students I have co-supervised.",
           "talks":"Oral and poster presentations at international and national meetings since 2016.",
           "outreach":"Peer review, events organised, and science communication.",
           "contact":"How to reach me for collaborations and student enquiries."},
 "meta_desc":"Montserrat Compa Ferrer, PhD: marine ecologist and Assistant Professor at the University of the Balearic Islands working on marine litter, microplastics, invasive species and cumulative pressures in the Mediterranean.",
 "skip":"Skip to content", "menu":"Menu", "next":"Next", "back":"Back to the surface", "theme":"Switch theme", "langs":"Language",
 "footer":"University of the Balearic Islands", "email":"Email",
 "role":"PhD, Marine Ecology",
 "lede":"I study how plastic pollution and other human pressures move through the Mediterranean, from floating litter at the sea surface down to the seafloor, and into the fish, sponges and crabs that live there.",
 "cta1":"Read the publications", "cta2":"Email me",
 "aff":"Assistant Professor, University of the Balearic Islands, Palma",
 "fig_title":"Cross-section of the sea showing where the research takes place: surface waters, water column, seafloor and the animals in between",
 "fig":["Floating litter and microplastics","Ingestion by fish","Water column","Seafloor: litter, sponges, invasive blue crab"],
 "figcap":"Where my work happens: litter is surveyed at the surface, in the water column and on the seafloor, and traced into marine fauna.",
 "explore":"Explore",
 "about_p":[
  "I am an Assistant Professor (Profesora Ayudante Doctora) in the Department of Biology and Geology at the University of the Balearic Islands. I completed my PhD in Marine Ecology at the same university in 2021, with a thesis on the quantification, ingestion and threat of plastic pollution on marine diversity, graded cum laude.",
  "My research follows marine litter through the ecosystem. I have mapped its distribution in aquaculture zones and Marine Protected Areas such as Cabrera National Park, and built risk assessments of plastic pollution for the Mediterranean at regional and national scales. My work on commercially important fish showed that long-term microplastic exposure in species like gilthead sea bream can trigger oxidative stress, inflammation and behavioural change, and that microplastics can carry pollutants such as organochlorine pesticides.",
  "More recently I have widened the lens to cumulative pressures on coastal benthic ecosystems: invasive species like the blue crab <i>Callinectes sapidus</i> and the alga <i>Batophora occidentalis</i>, marine heatwaves, pathogenic <i>Vibrio</i>, and sponges and sea urchins as bioindicators. I am also interested in modelling species diversity under multiple pressures.",
  "I teach in the BSc in Biology at UIB, sit on the academic committee of the Master in Marine Ecology, and co-supervise undergraduate and master's students. I care about statistical rigour and have organised training courses on zero-inflated, Bayesian and spatial models in R."],
 "edu":"Education",
 "edu_list":[("PhD, Marine Ecology","University of the Balearic Islands, 2021. Cum laude."),
             ("MSc, Marine Ecology","University of the Balearic Islands, 2018"),
             ("MSc, Terrestrial Ecology and Biodiversity Management","Autonomous University of Barcelona (CREAF), 2014"),
             ("BSc, Environmental Sciences","Humboldt State University, California, 2012"),
             ("Associate's Degree, Natural Sciences","Lake Tahoe Community College, California, 2010. With honours.")],
 "kw":"Keywords",
 "kw_list":["Marine litter","Microplastics","Marine Protected Areas","Biodiversity","Invasive species","Marine heatwaves","Biomarkers","Risk assessment","Spatial statistics"],
 "tools":"Tools", "tools_list":["R (Bayesian and non-parametric statistics)","ArcGIS and geostatistics"],
 "langs_h":"Languages", "langs_list":["Spanish","English (C2)","Catalan (B2)"],
 "res_head":"Research themes", "res_p":"Four lines of work, each linked to its papers.",
 "pub_p":"Peer-reviewed SCI journal articles and reviews, most in first-quartile journals. Titles are shown as published; my name is in bold.",
 "search":"Search titles, journals, species, co-authors", "firstonly":"First or last author only",
 "chapters":"Book chapters", "reports":"Selected technical reports", "reports_note":"14 scientific-technical reports in total, 3 as Principal Investigator.",
 "chapters_list":[
  ("2021","Residuos en el mar Balear","Alomar, C., Compa, M., Deudero, S. In <i>Informe Mar Balear 2021</i>. Conselleria de Medi Ambient, Govern de les Illes Balears."),
  ("2019","Beach systems of Balearic Islands: nature, distribution, and processes","Gómez-Pujol, L., Orfila, A., Morales, V., Compa, M., Pereda, L., Fornós, J.J., Tintoré, J. In <i>The Spanish Coastal Systems</i>, Springer Nature, pp. 269–287. <a href=\"https://doi.org/10.1007/978-3-319-93169-2_12\">doi</a>"),
  ("2017","Las playas de Menorca: naturaleza y distribución","Gómez-Pujol, L., Compa, M., Orfila, A., et al. In <i>Geomorfología litoral de Menorca</i>. Mon. Soc. Hist. Nat. Balears 25, pp. 67–86.")],
 "reports_list":[
  ("2023","5th meeting of the Network of Experts for ReDeveloping Models of the European Marine Environment","European Commission Joint Research Centre, JRC133204. <a href=\"https://doi.org/10.2760/114580\">doi:10.2760/114580</a>"),
  ("2022","Validated marine litter forecasting models","Interreg Med Plastic Busters MPAs, D.4.4.1"),
  ("2021","Piloted monitoring approaches to establish marine litter impact on biota","Interreg Med Plastic Busters MPAs, D.4.3.1"),
  ("2021","Experimental and architecture design document","MIREIA project (ESA), D.2.1"),
  ("2019","Forecasting marine litter pollution in Mediterranean MPAs","Interreg Med Plastic Busters MPAs, D.3.5.1"),
  ("2019","Diagnostic report on knowledge gaps and needs for marine litter monitoring in Mediterranean MPAs","Interreg Med Plastic Busters MPAs, Athens"),
  ("2019","Knowledge wave on marine litter from aquaculture sources","AQUA-LIT project (EU EMFF), D2.1–D2.2, plus data management plan D1.3")],
 "fund_p":"Competitively funded projects I have led or taken part in: international, national and regional. Over 200,000 € secured as Principal Investigator and co-applicant.",
 "th":["Years","Project","Budget"],
 "grants":"Fellowships and grants", "stays":"Research stays abroad",
 "stays_list":[
  ("2024","University of Bari Aldo Moro, Italy","Postdoctoral stay, 3 months. Host: Dr Caterina Longo. Funded by a José Castillejo mobility grant."),
  ("2018","CSIRO Oceans and Atmosphere, Tasmania, Australia","Predoctoral stay, 3 months. Balearic Islands risk assessment. Host: Dr Chris Wilcox"),
  ("2016","CSIRO Oceans and Atmosphere, Tasmania, Australia","Predoctoral stay, 6 weeks. Mediterranean risk assessment. Host: Dr Chris Wilcox"),
  ("2016","Imperial College London, United Kingdom","Predoctoral stay, 15 days. Mediterranean risk assessment. Host: Prof. Erik van Sebille"),
  ("2015","Technical University of Denmark (DTU)","Invited stay, 1 month. EUROFLEETS programme")],
 "sea":"At sea",
 "sea_list":[
  ("2019–20","Plastic Busters campaigns, Cabrera National Park","Two 10-day surveys of seafloor, surface water and biota"),
  ("2018–19","ACUIPLASTIC monthly surveys, Port d'Andratx","Surface microplastic sampling around aquaculture facilities"),
  ("2016","MEDIAS16 oceanographic survey","Spanish Mediterranean shelf"),
  ("2015","EUROFLEETS2 training cruise","Applied oceanography, Norwegian Sea")],
 "career_list":[
  ("Now","Assistant Professor (Profesora Ayudante Doctora)","Department of Biology and Geology, University of the Balearic Islands"),
  ("2025","Vicenç Mut postdoctoral researcher","University of the Balearic Islands, from October 2025"),
  ("2025","Postdoctoral researcher","University of the Balearic Islands, January to October 2025"),
  ("2023 – 2024","Juan de la Cierva-Formación postdoctoral researcher","University of the Balearic Islands. Spanish Ministry of Science, NextGenerationEU / PRTR (FJC2021-047606-I)"),
  ("2022","Margalida Comas postdoctoral researcher","Oceanographic Centre of the Balearic Islands (IEO-CSIC). Balearic Government and European Social Fund"),
  ("2020 – 2022","Senior research technician","Interreg Med Plastic Busters MPAs project, IEO-CSIC"),
  ("2016 – 2019","Predoctoral researcher (FPI)","IEO-CSIC, Balearic Government FPI programme"),
  ("2015","Beach monitoring and database maintenance","SOCIB and the University of the Balearic Islands"),
  ("2010 – 2012","Field and laboratory technician; geospatial analyst","California Sea Grant and the California Center for Rural Policy, USA"),
  ("2010 – 2011","Wilderness ranger and restoration crew","USDA Forest Service, USA")],
 "teach":"Teaching and mentoring",
 "teach_p":"Lecturer in the BSc in Biology at UIB and member of the academic committee of the Master in Marine Ecology. Member of a teaching innovation project on interdisciplinary biodiversity teaching (2025–27). Co-supervisor of 10 undergraduate and master's students from Spanish and French universities.",
 "talks_p":"Oral and poster presentations at international and national meetings, including the International Marine Debris Conference, MICRO, ICES, CIESM, SETAC and ECSA, and an invited talk in Prishtina (2025). Titles are shown in the language they were presented in.",
 "out_p":"Reviewing, editing, organising training, and sharing research beyond academia.",
 "service":"Service",
 "service_p":"Peer reviewer for about ten journals, including <i>Marine Pollution Bulletin</i>, <i>Science of the Total Environment</i> and <i>Environmental Pollution</i>. Guest editor of a special issue in <i>Biology</i>. Invited modelling expert at the European Commission Joint Research Centre (2023). Member of the Plastic Busters committee, University of Siena (2017).",
 "events":"Events organised",
 "events_list":[("2022–23","EC-InterDis Summer School","Early Career Summer School for Interdisciplinary Ocean Transformation, EuroMarine"),
                ("2019","Statistics courses at IEO-CSIC","Zero-inflated models, Bayesian analysis and statistical modelling in R")],
 "outreach":"Outreach",
 "outreach_list":[("2019","IB3 \"Méteo, temps i natura\"","Two television interviews on microplastics and synthetic fibres"),
   ("2019","Press interviews","<a href=\"https://www.ultimahora.es/noticias/sociedad/2019/03/28/1068441/plastico-enemigo-deriva.html\">Última Hora</a> round table, Lycée Français; <a href=\"http://saveu.cat/article.php?ent=1998\">Sa Veu de Sóller</a>"),
   ("2018","\"La sopa de plásticos\"","Public talk at No Plástico Festival, Inca"),
   ("2017","\"El efecto de los microplásticos en el Mar Mediterráneo\"","Public talk, Sóller"),
   ("Ongoing","11F and STEM outreach","School visits for the International Day of Women and Girls in Science")],
 "contact_h":"Get in touch",
 "contact_p":"I welcome collaborations on marine litter, microplastics, invasive species and Mediterranean conservation, and enquiries from prospective students.",
 "addr_h":"Address", "addr":"Department of Biology and Geology<br>Faculty of Sciences, University of the Balearic Islands<br>Ctra. de Valldemossa km 7.5, 07122 Palma, Spain",
 "profiles":"Researcher profiles",
},
"es": {
 "nav": {"index":"Inicio","about":"Sobre mí","research":"Investigación","publications":"Publicaciones","funding":"Financiación","career":"Trayectoria","talks":"Congresos","outreach":"Divulgación","contact":"Contacto"},
 "gauge": {"index":"Superficie","contact":"Fondo marino"},
 "title": {"about":"Sobre mí","research":"Investigación","publications":"Publicaciones","funding":"Proyectos y financiación","career":"Trayectoria","talks":"Congresos y ponencias","outreach":"Servicio y divulgación","contact":"Contacto"},
 "blurb": {"about":"Formación, trayectoria e intereses de investigación.",
           "research":"Cuatro líneas de trabajo sobre la contaminación por plásticos y las presiones humanas en el Mediterráneo.",
           "publications":"Todos los artículos revisados por pares, capítulos de libro e informes técnicos, con búsqueda y filtro por tema.",
           "funding":"Proyectos de investigación, presupuestos, becas, estancias en el extranjero y campañas en el mar.",
           "career":"Puestos ocupados, docencia y los estudiantes que he codirigido.",
           "talks":"Comunicaciones orales y pósteres en congresos internacionales y nacionales desde 2016.",
           "outreach":"Revisión por pares, actividades organizadas y comunicación científica.",
           "contact":"Cómo contactar conmigo para colaboraciones y consultas de estudiantes."},
 "meta_desc":"Montserrat Compa Ferrer, doctora en Ecología Marina y profesora ayudante doctora en la Universitat de les Illes Balears. Investiga la basura marina, los microplásticos, las especies invasoras y las presiones acumuladas en el Mediterráneo.",
 "skip":"Ir al contenido", "menu":"Menú", "next":"Siguiente", "back":"Volver a la superficie", "theme":"Cambiar tema", "langs":"Idioma",
 "footer":"Universitat de les Illes Balears", "email":"Correo",
 "role":"Doctora en Ecología Marina",
 "lede":"Estudio cómo la contaminación por plásticos y otras presiones humanas se mueven por el Mediterráneo, desde la basura que flota en superficie hasta el fondo marino, y cómo llegan a los peces, esponjas y cangrejos que viven allí.",
 "cta1":"Ver las publicaciones", "cta2":"Escríbeme",
 "aff":"Profesora ayudante doctora, Universitat de les Illes Balears, Palma",
 "fig_title":"Sección del mar que muestra dónde se desarrolla la investigación: aguas superficiales, columna de agua, fondo marino y los animales que viven en ellos",
 "fig":["Basura flotante y microplásticos","Ingestión por peces","Columna de agua","Fondo: basura, esponjas, cangrejo azul invasor"],
 "figcap":"Dónde se desarrolla mi trabajo: la basura se estudia en superficie, en la columna de agua y en el fondo, y se sigue hasta la fauna marina.",
 "explore":"Explorar",
 "about_p":[
  "Soy profesora ayudante doctora en el Departamento de Biología y Geología de la Universitat de les Illes Balears. Me doctoré en Ecología Marina en la misma universidad en 2021, con una tesis sobre la cuantificación, la ingestión y la amenaza de la contaminación por plásticos para la diversidad marina, con calificación cum laude.",
  "Mi investigación sigue la basura marina a través del ecosistema. He cartografiado su distribución en zonas de acuicultura y en Áreas Marinas Protegidas como el Parque Nacional de Cabrera, y he desarrollado evaluaciones de riesgo de la contaminación por plásticos para el Mediterráneo a escala regional y nacional. Mi trabajo con peces de interés comercial ha mostrado que la exposición prolongada a microplásticos en especies como la dorada puede provocar estrés oxidativo, inflamación y cambios de comportamiento, y que los microplásticos pueden transportar contaminantes como pesticidas organoclorados.",
  "Más recientemente he ampliado el enfoque a las presiones acumuladas sobre los ecosistemas bentónicos costeros: especies invasoras como el cangrejo azul <i>Callinectes sapidus</i> y el alga <i>Batophora occidentalis</i>, las olas de calor marinas, los <i>Vibrio</i> patógenos, y las esponjas y erizos de mar como bioindicadores. También me interesa modelizar la diversidad de especies bajo múltiples presiones.",
  "Doy clase en el Grado en Biología de la UIB, formo parte de la comisión académica del Máster en Ecología Marina y codirijo estudiantes de grado y máster. Me importa el rigor estadístico y he organizado cursos sobre modelos con exceso de ceros, bayesianos y espaciales en R."],
 "edu":"Formación",
 "edu_list":[("Doctorado en Ecología Marina","Universitat de les Illes Balears, 2021. Cum laude."),
             ("Máster en Ecología Marina","Universitat de les Illes Balears, 2018"),
             ("Máster en Ecología Terrestre y Gestión de la Biodiversidad","Universitat Autònoma de Barcelona (CREAF), 2014"),
             ("Grado (BSc) en Ciencias Ambientales","Humboldt State University, California, 2012"),
             ("Associate's Degree en Ciencias Naturales","Lake Tahoe Community College, California, 2010. Matrícula de honor.")],
 "kw":"Palabras clave",
 "kw_list":["Basura marina","Microplásticos","Áreas Marinas Protegidas","Biodiversidad","Especies invasoras","Olas de calor marinas","Biomarcadores","Evaluación de riesgos","Estadística espacial"],
 "tools":"Herramientas", "tools_list":["R (estadística bayesiana y no paramétrica)","ArcGIS y geoestadística"],
 "langs_h":"Idiomas", "langs_list":["Español","Inglés (C2)","Catalán (B2)"],
 "res_head":"Líneas de investigación", "res_p":"Cuatro líneas de trabajo, cada una enlazada con sus artículos.",
 "pub_p":"Artículos y revisiones en revistas SCI con revisión por pares, la mayoría en revistas del primer cuartil. Los títulos aparecen como se publicaron; mi nombre está en negrita.",
 "search":"Buscar títulos, revistas, especies, coautores", "firstonly":"Solo como primera o última autora",
 "chapters":"Capítulos de libro", "reports":"Informes técnicos seleccionados", "reports_note":"14 informes científico-técnicos en total, 3 como investigadora principal.",
 "fund_p":"Proyectos con financiación competitiva que he dirigido o en los que he participado: internacionales, nacionales y regionales. Más de 200.000 € obtenidos como investigadora principal y cosolicitante.",
 "th":["Años","Proyecto","Presupuesto"],
 "grants":"Becas y ayudas", "stays":"Estancias de investigación en el extranjero",
 "stays_list":[
  ("2024","Università degli Studi di Bari Aldo Moro, Italia","Estancia posdoctoral, 3 meses. Anfitriona: Dra. Caterina Longo. Financiada con una ayuda de movilidad José Castillejo."),
  ("2018","CSIRO Oceans and Atmosphere, Tasmania, Australia","Estancia predoctoral, 3 meses. Evaluación de riesgos en las Baleares. Anfitrión: Dr. Chris Wilcox"),
  ("2016","CSIRO Oceans and Atmosphere, Tasmania, Australia","Estancia predoctoral, 6 semanas. Evaluación de riesgos en el Mediterráneo. Anfitrión: Dr. Chris Wilcox"),
  ("2016","Imperial College London, Reino Unido","Estancia predoctoral, 15 días. Evaluación de riesgos en el Mediterráneo. Anfitrión: Prof. Erik van Sebille"),
  ("2015","Universidad Técnica de Dinamarca (DTU)","Estancia como invitada, 1 mes. Programa EUROFLEETS")],
 "sea":"Campañas en el mar",
 "sea_list":[
  ("2019–20","Campañas Plastic Busters, Parque Nacional de Cabrera","Dos campañas de 10 días en fondo, aguas superficiales y biota"),
  ("2018–19","Muestreos mensuales ACUIPLASTIC, Port d'Andratx","Muestreo de microplásticos en superficie alrededor de instalaciones de acuicultura"),
  ("2016","Campaña oceanográfica MEDIAS16","Plataforma mediterránea española"),
  ("2015","Campaña de formación EUROFLEETS2","Oceanografía aplicada, mar de Noruega")],
 "career_list":[
  ("Actualidad","Profesora ayudante doctora","Departamento de Biología y Geología, Universitat de les Illes Balears"),
  ("2025","Investigadora posdoctoral Vicenç Mut","Universitat de les Illes Balears, desde octubre de 2025"),
  ("2025","Investigadora posdoctoral","Universitat de les Illes Balears, de enero a octubre de 2025"),
  ("2023 – 2024","Investigadora posdoctoral Juan de la Cierva-Formación","Universitat de les Illes Balears. Ministerio de Ciencia, NextGenerationEU / PRTR (FJC2021-047606-I)"),
  ("2022","Investigadora posdoctoral Margalida Comas","Centro Oceanográfico de Baleares (IEO-CSIC). Govern de les Illes Balears y Fondo Social Europeo"),
  ("2020 – 2022","Técnica superior de investigación","Proyecto Interreg Med Plastic Busters MPAs, IEO-CSIC"),
  ("2016 – 2019","Investigadora predoctoral (FPI)","IEO-CSIC, programa FPI del Govern de les Illes Balears"),
  ("2015","Seguimiento de playas y mantenimiento de bases de datos","SOCIB y Universitat de les Illes Balears"),
  ("2010 – 2012","Técnica de campo y laboratorio; analista geoespacial","California Sea Grant y California Center for Rural Policy, EE. UU."),
  ("2010 – 2011","Guarda forestal y restauración de espacios naturales","USDA Forest Service, EE. UU.")],
 "teach":"Docencia y dirección",
 "teach_p":"Profesora en el Grado en Biología de la UIB y miembro de la comisión académica del Máster en Ecología Marina. Participante en un proyecto de innovación docente sobre la enseñanza interdisciplinar de la biodiversidad (2025–27). Codirectora de 10 estudiantes de grado y máster de universidades españolas y francesas.",
 "talks_p":"Comunicaciones orales y pósteres en congresos internacionales y nacionales, como la International Marine Debris Conference, MICRO, ICES, CIESM, SETAC y ECSA, y una conferencia invitada en Prishtina (2025). Los títulos aparecen en el idioma en que se presentaron.",
 "out_p":"Revisión de artículos, edición, organización de formación y difusión de la investigación fuera del ámbito académico.",
 "service":"Servicio",
 "service_p":"Revisora de unas diez revistas, entre ellas <i>Marine Pollution Bulletin</i>, <i>Science of the Total Environment</i> y <i>Environmental Pollution</i>. Editora invitada de un número especial de <i>Biology</i>. Experta invitada en modelización en el Joint Research Centre de la Comisión Europea (2023). Miembro del comité Plastic Busters, Universidad de Siena (2017).",
 "events":"Actividades organizadas",
 "events_list":[("2022–23","Escuela de verano EC-InterDis","Escuela de verano para investigadores jóvenes sobre transformación oceánica interdisciplinar, EuroMarine"),
                ("2019","Cursos de estadística en el IEO-CSIC","Modelos con exceso de ceros, análisis bayesiano y modelización estadística en R")],
 "outreach":"Divulgación",
 "outreach_list":[("2019","IB3 \"Méteo, temps i natura\"","Dos entrevistas en televisión sobre microplásticos y fibras sintéticas"),
   ("2019","Entrevistas en prensa","Mesa redonda de <a href=\"https://www.ultimahora.es/noticias/sociedad/2019/03/28/1068441/plastico-enemigo-deriva.html\">Última Hora</a>, Lycée Français; <a href=\"http://saveu.cat/article.php?ent=1998\">Sa Veu de Sóller</a>"),
   ("2018","\"La sopa de plásticos\"","Charla en el Festival No Plástico, Inca"),
   ("2017","\"El efecto de los microplásticos en el Mar Mediterráneo\"","Charla divulgativa, Sóller"),
   ("En curso","11F y divulgación STEM","Visitas a centros escolares por el Día Internacional de la Mujer y la Niña en la Ciencia")],
 "contact_h":"Contacto",
 "contact_p":"Estoy abierta a colaboraciones sobre basura marina, microplásticos, especies invasoras y conservación del Mediterráneo, y a consultas de futuros estudiantes.",
 "addr_h":"Dirección", "addr":"Departamento de Biología y Geología<br>Facultad de Ciencias, Universitat de les Illes Balears<br>Ctra. de Valldemossa km 7,5, 07122 Palma",
 "profiles":"Perfiles de investigadora",
},
"ca": {
 "nav": {"index":"Inici","about":"Sobre mi","research":"Recerca","publications":"Publicacions","funding":"Finançament","career":"Trajectòria","talks":"Congressos","outreach":"Divulgació","contact":"Contacte"},
 "gauge": {"index":"Superfície","contact":"Fons marí"},
 "title": {"about":"Sobre mi","research":"Recerca","publications":"Publicacions","funding":"Projectes i finançament","career":"Trajectòria","talks":"Congressos i ponències","outreach":"Servei i divulgació","contact":"Contacte"},
 "blurb": {"about":"Formació, trajectòria i interessos de recerca.",
           "research":"Quatre línies de feina sobre la contaminació per plàstics i les pressions humanes a la Mediterrània.",
           "publications":"Tots els articles revisats per parells, capítols de llibre i informes tècnics, amb cerca i filtre per tema.",
           "funding":"Projectes de recerca, pressuposts, beques, estades a l'estranger i campanyes a la mar.",
           "career":"Llocs ocupats, docència i els estudiants que he codirigit.",
           "talks":"Comunicacions orals i pòsters en congressos internacionals i nacionals des del 2016.",
           "outreach":"Revisió per parells, activitats organitzades i comunicació científica.",
           "contact":"Com contactar amb mi per a col·laboracions i consultes d'estudiants."},
 "meta_desc":"Montserrat Compa Ferrer, doctora en Ecologia Marina i professora ajudant doctora a la Universitat de les Illes Balears. Investiga els fems marins, els microplàstics, les espècies invasores i les pressions acumulades a la Mediterrània.",
 "skip":"Vés al contingut", "menu":"Menú", "next":"Següent", "back":"Torna a la superfície", "theme":"Canvia el tema", "langs":"Llengua",
 "footer":"Universitat de les Illes Balears", "email":"Correu",
 "role":"Doctora en Ecologia Marina",
 "lede":"Estudio com la contaminació per plàstics i altres pressions humanes es mouen per la Mediterrània, des dels fems que suren a la superfície fins al fons marí, i com arriben als peixos, les esponges i els crancs que hi viuen.",
 "cta1":"Consulta les publicacions", "cta2":"Escriu-me",
 "aff":"Professora ajudant doctora, Universitat de les Illes Balears, Palma",
 "fig_title":"Secció de la mar que mostra on es desenvolupa la recerca: aigües superficials, columna d'aigua, fons marí i els animals que hi viuen",
 "fig":["Fems flotants i microplàstics","Ingestió per peixos","Columna d'aigua","Fons: fems, esponges, cranc blau invasor"],
 "figcap":"On es desenvolupa la meva feina: els fems s'estudien a la superfície, a la columna d'aigua i al fons, i se'n segueix el rastre fins a la fauna marina.",
 "explore":"Explora",
 "about_p":[
  "Som professora ajudant doctora al Departament de Biologia i Geologia de la Universitat de les Illes Balears. Em vaig doctorar en Ecologia Marina a la mateixa universitat el 2021, amb una tesi sobre la quantificació, la ingestió i l'amenaça de la contaminació per plàstics per a la diversitat marina, amb qualificació cum laude.",
  "La meva recerca segueix els fems marins a través de l'ecosistema. N'he cartografiat la distribució en zones d'aqüicultura i en Àrees Marines Protegides com el Parc Nacional de Cabrera, i he desenvolupat avaluacions de risc de la contaminació per plàstics per a la Mediterrània a escala regional i estatal. La meva feina amb peixos d'interès comercial ha mostrat que l'exposició prolongada a microplàstics en espècies com l'orada pot provocar estrès oxidatiu, inflamació i canvis de comportament, i que els microplàstics poden transportar contaminants com pesticides organoclorats.",
  "Més recentment he ampliat l'enfocament a les pressions acumulades sobre els ecosistemes bentònics costaners: espècies invasores com el cranc blau <i>Callinectes sapidus</i> i l'alga <i>Batophora occidentalis</i>, les onades de calor marines, els <i>Vibrio</i> patògens, i les esponges i els eriçons de mar com a bioindicadors. També m'interessa modelitzar la diversitat d'espècies sota múltiples pressions.",
  "Faig classe al Grau en Biologia de la UIB, form part de la comissió acadèmica del Màster en Ecologia Marina i codirigeixo estudiants de grau i màster. M'importa el rigor estadístic i he organitzat cursos sobre models amb excés de zeros, bayesians i espacials en R."],
 "edu":"Formació",
 "edu_list":[("Doctorat en Ecologia Marina","Universitat de les Illes Balears, 2021. Cum laude."),
             ("Màster en Ecologia Marina","Universitat de les Illes Balears, 2018"),
             ("Màster en Ecologia Terrestre i Gestió de la Biodiversitat","Universitat Autònoma de Barcelona (CREAF), 2014"),
             ("Grau (BSc) en Ciències Ambientals","Humboldt State University, Califòrnia, 2012"),
             ("Associate's Degree en Ciències Naturals","Lake Tahoe Community College, Califòrnia, 2010. Matrícula d'honor.")],
 "kw":"Paraules clau",
 "kw_list":["Fems marins","Microplàstics","Àrees Marines Protegides","Biodiversitat","Espècies invasores","Onades de calor marines","Biomarcadors","Avaluació de riscos","Estadística espacial"],
 "tools":"Eines", "tools_list":["R (estadística bayesiana i no paramètrica)","ArcGIS i geoestadística"],
 "langs_h":"Llengües", "langs_list":["Castellà","Anglès (C2)","Català (B2)"],
 "res_head":"Línies de recerca", "res_p":"Quatre línies de feina, cadascuna enllaçada amb els seus articles.",
 "pub_p":"Articles i revisions en revistes SCI amb revisió per parells, la majoria en revistes del primer quartil. Els títols apareixen tal com es van publicar; el meu nom és en negreta.",
 "search":"Cerca títols, revistes, espècies, coautors", "firstonly":"Només com a primera o darrera autora",
 "chapters":"Capítols de llibre", "reports":"Informes tècnics seleccionats", "reports_note":"14 informes cientificotècnics en total, 3 com a investigadora principal.",
 "fund_p":"Projectes amb finançament competitiu que he dirigit o en què he participat: internacionals, estatals i regionals. Més de 200.000 € obtinguts com a investigadora principal i cosol·licitant.",
 "th":["Anys","Projecte","Pressupost"],
 "grants":"Beques i ajuts", "stays":"Estades de recerca a l'estranger",
 "stays_list":[
  ("2024","Università degli Studi di Bari Aldo Moro, Itàlia","Estada postdoctoral, 3 mesos. Amfitriona: Dra. Caterina Longo. Finançada amb un ajut de mobilitat José Castillejo."),
  ("2018","CSIRO Oceans and Atmosphere, Tasmània, Austràlia","Estada predoctoral, 3 mesos. Avaluació de riscos a les Balears. Amfitrió: Dr. Chris Wilcox"),
  ("2016","CSIRO Oceans and Atmosphere, Tasmània, Austràlia","Estada predoctoral, 6 setmanes. Avaluació de riscos a la Mediterrània. Amfitrió: Dr. Chris Wilcox"),
  ("2016","Imperial College London, Regne Unit","Estada predoctoral, 15 dies. Avaluació de riscos a la Mediterrània. Amfitrió: Prof. Erik van Sebille"),
  ("2015","Universitat Tècnica de Dinamarca (DTU)","Estada com a convidada, 1 mes. Programa EUROFLEETS")],
 "sea":"Campanyes a la mar",
 "sea_list":[
  ("2019–20","Campanyes Plastic Busters, Parc Nacional de Cabrera","Dues campanyes de 10 dies al fons, a les aigües superficials i en biota"),
  ("2018–19","Mostrejos mensuals ACUIPLASTIC, Port d'Andratx","Mostreig de microplàstics en superfície a l'entorn d'instal·lacions d'aqüicultura"),
  ("2016","Campanya oceanogràfica MEDIAS16","Plataforma mediterrània espanyola"),
  ("2015","Campanya de formació EUROFLEETS2","Oceanografia aplicada, mar de Noruega")],
 "career_list":[
  ("Actualitat","Professora ajudant doctora","Departament de Biologia i Geologia, Universitat de les Illes Balears"),
  ("2025","Investigadora postdoctoral Vicenç Mut","Universitat de les Illes Balears, des d'octubre de 2025"),
  ("2025","Investigadora postdoctoral","Universitat de les Illes Balears, de gener a octubre de 2025"),
  ("2023 – 2024","Investigadora postdoctoral Juan de la Cierva-Formación","Universitat de les Illes Balears. Ministeri de Ciència, NextGenerationEU / PRTR (FJC2021-047606-I)"),
  ("2022","Investigadora postdoctoral Margalida Comas","Centre Oceanogràfic de Balears (IEO-CSIC). Govern de les Illes Balears i Fons Social Europeu"),
  ("2020 – 2022","Tècnica superior de recerca","Projecte Interreg Med Plastic Busters MPAs, IEO-CSIC"),
  ("2016 – 2019","Investigadora predoctoral (FPI)","IEO-CSIC, programa FPI del Govern de les Illes Balears"),
  ("2015","Seguiment de platges i manteniment de bases de dades","SOCIB i Universitat de les Illes Balears"),
  ("2010 – 2012","Tècnica de camp i laboratori; analista geoespacial","California Sea Grant i California Center for Rural Policy, EUA"),
  ("2010 – 2011","Guarda forestal i restauració d'espais naturals","USDA Forest Service, EUA")],
 "teach":"Docència i direcció",
 "teach_p":"Professora al Grau en Biologia de la UIB i membre de la comissió acadèmica del Màster en Ecologia Marina. Participant en un projecte d'innovació docent sobre l'ensenyament interdisciplinari de la biodiversitat (2025–27). Codirectora de 10 estudiants de grau i màster d'universitats espanyoles i franceses.",
 "talks_p":"Comunicacions orals i pòsters en congressos internacionals i nacionals, com la International Marine Debris Conference, MICRO, ICES, CIESM, SETAC i ECSA, i una conferència convidada a Prishtina (2025). Els títols apareixen en la llengua en què es van presentar.",
 "out_p":"Revisió d'articles, edició, organització de formació i difusió de la recerca fora de l'àmbit acadèmic.",
 "service":"Servei",
 "service_p":"Revisora d'unes deu revistes, entre les quals <i>Marine Pollution Bulletin</i>, <i>Science of the Total Environment</i> i <i>Environmental Pollution</i>. Editora convidada d'un número especial de <i>Biology</i>. Experta convidada en modelització al Joint Research Centre de la Comissió Europea (2023). Membre del comitè Plastic Busters, Universitat de Siena (2017).",
 "events":"Activitats organitzades",
 "events_list":[("2022–23","Escola d'estiu EC-InterDis","Escola d'estiu per a investigadors joves sobre transformació oceànica interdisciplinària, EuroMarine"),
                ("2019","Cursos d'estadística a l'IEO-CSIC","Models amb excés de zeros, anàlisi bayesiana i modelització estadística en R")],
 "outreach":"Divulgació",
 "outreach_list":[("2019","IB3 \"Méteo, temps i natura\"","Dues entrevistes a la televisió sobre microplàstics i fibres sintètiques"),
   ("2019","Entrevistes a la premsa","Taula rodona d'<a href=\"https://www.ultimahora.es/noticias/sociedad/2019/03/28/1068441/plastico-enemigo-deriva.html\">Última Hora</a>, Lycée Français; <a href=\"http://saveu.cat/article.php?ent=1998\">Sa Veu de Sóller</a>"),
   ("2018","\"La sopa de plásticos\"","Xerrada al Festival No Plástico, Inca"),
   ("2017","\"El efecto de los microplásticos en el Mar Mediterráneo\"","Xerrada divulgativa, Sóller"),
   ("En curs","11F i divulgació STEM","Visites a centres escolars pel Dia Internacional de la Dona i la Nena en la Ciència")],
 "contact_h":"Contacte",
 "contact_p":"Estic oberta a col·laboracions sobre fems marins, microplàstics, espècies invasores i conservació de la Mediterrània, i a consultes de futurs estudiants.",
 "addr_h":"Adreça", "addr":"Departament de Biologia i Geologia<br>Facultat de Ciències, Universitat de les Illes Balears<br>Ctra. de Valldemossa km 7,5, 07122 Palma",
 "profiles":"Perfils d'investigadora",
},
}
# Chapter and report titles stay in their original language
for l in ("es", "ca"):
    T[l]["chapters_list"] = T["en"]["chapters_list"]
    T[l]["reports_list"] = T["en"]["reports_list"]

import hashlib
def ver(name):
    """Short content hash so browsers fetch a file again whenever it changes."""
    with open(os.path.join(HERE, name), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]

SVG = open(os.path.join(HERE, "assets", "sea.svg"), encoding="utf-8").read()


def li_list(items):
    return "".join(f'<li><span class="y">{y}</span><span><b>{b}</b><small>{s}</small></span></li>' for y, b, s in items)


def head_block(key, l, t):
    return f'<span class="depth">{dict(PAGES)[key]}</span>\n    <div class="head"><h2>{t}</h2>'


def content(key, l):
    t = T[l]
    if key == "index":
        svg = SVG.format(title=html.escape(t["fig_title"]), *[html.escape(x) for x in t["fig"]])
        tiles = "".join(f'<a href="{k}.html"><b>{t["title"][k]}</b><span>{t["blurb"][k]}</span></a>' for k, _ in PAGES[1:])
        return f'''<section class="hero">
  <div class="wrap">
    <div>
      <h1>Montserrat Compa Ferrer<em>{t["role"]}</em></h1>
      <p class="lede">{t["lede"]}</p>
      <div class="actions">
        <a class="btn solid" href="publications.html">{t["cta1"]}</a>
        <a class="btn" href="mailto:{EMAIL}">{t["cta2"]}</a>
      </div>
      <div class="ids">
        <span>{t["aff"]}</span>
        <a href="{ORCID}" rel="noopener">ORCID 0000-0002-0661-8712</a>
        <a href="{SCOPUS}" rel="noopener">Scopus</a>
      </div>
    </div>
    <figure class="profile" style="margin:0">
      {svg}
      <figcaption>{t["figcap"]}</figcaption>
    </figure>
    <div class="facts" id="facts"></div>
  </div>
</section>
<section class="block"><div class="wrap"><div class="head"><h2>{t["explore"]}</h2></div><div class="explore">{tiles}</div></div></section>'''
    if key == "about":
        edu = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in t["edu_list"])
        kw = "".join(f"<span>{k}</span>" for k in t["kw_list"])
        tools = "".join(f"<span>{k}</span>" for k in t["tools_list"])
        langs = "".join(f"<span>{k}</span>" for k in t["langs_list"])
        paras = "\n".join(f"<p>{p}</p>" for p in t["about_p"])
        return f'''<section class="block" id="about">
  <div class="wrap">
    {head_block(key,l,t["title"][key])}</div>
    <div class="about">
      <div class="prose">
{paras}
      </div>
      <div class="side">
        <h3>{t["edu"]}</h3>
        <dl>{edu}</dl>
        <h3>{t["kw"]}</h3>
        <div class="tags">{kw}</div>
        <h3 style="margin-top:22px">{t["tools"]}</h3>
        <div class="tags">{tools}</div>
        <h3 style="margin-top:22px">{t["langs_h"]}</h3>
        <div class="tags">{langs}</div>
      </div>
    </div>
  </div>
</section>'''
    if key == "research":
        return f'''<section class="block" id="research">
  <div class="wrap">
    {head_block(key,l,t["res_head"])}<p>{t["res_p"]}</p></div>
    <div class="themes" id="themes"></div>
  </div>
</section>'''
    if key == "publications":
        return f'''<section class="block" id="publications">
  <div class="wrap">
    {head_block(key,l,t["title"][key])}<p>{t["pub_p"]}</p></div>
    <div class="pubtools" id="pubtools">
      <input class="search" id="q" type="search" placeholder="{t["search"]}" aria-label="{t["search"]}">
      <label class="toggle"><input type="checkbox" id="firstonly"> {t["firstonly"]}</label>
    </div>
    <p class="pubcount" id="pubcount" aria-live="polite"></p>
    <div id="publist"></div>
    <div class="cols2">
      <div>
        <h3 style="margin-bottom:14px">{t["chapters"]}</h3>
        <ul class="list">{li_list(t["chapters_list"])}</ul>
      </div>
      <div>
        <h3 style="margin-bottom:14px">{t["reports"]}</h3>
        <ul class="list">{li_list(t["reports_list"])}</ul>
        <p style="font-size:.88rem;color:var(--ink-2);margin-top:12px">{t["reports_note"]}</p>
      </div>
    </div>
  </div>
</section>'''
    if key == "funding":
        th = t["th"]
        return f'''<section class="block" id="funding">
  <div class="wrap">
    {head_block(key,l,t["title"][key])}<p>{t["fund_p"]}</p></div>
    <table class="fund">
      <thead><tr><th>{th[0]}</th><th>{th[1]}</th><th style="text-align:right">{th[2]}</th></tr></thead>
      <tbody id="fundrows"></tbody>
    </table>
    <div class="cols2">
      <div>
        <h3 style="margin-bottom:14px">{t["grants"]}</h3>
        <ul class="list" id="grants"></ul>
      </div>
      <div>
        <h3 style="margin-bottom:14px">{t["stays"]}</h3>
        <ul class="list">{li_list(t["stays_list"])}</ul>
        <h3 style="margin:34px 0 14px">{t["sea"]}</h3>
        <ul class="list">{li_list(t["sea_list"])}</ul>
      </div>
    </div>
  </div>
</section>'''
    if key == "career":
        tl = "".join(f'<li{" class=\"now\"" if i == 0 else ""}><span class="y">{y}</span><b>{b}</b><small>{s}</small></li>'
                     for i, (y, b, s) in enumerate(t["career_list"]))
        return f'''<section class="block" id="career">
  <div class="wrap">
    {head_block(key,l,t["title"][key])}</div>
    <div class="cols2" style="margin-top:0">
      <ol class="tl">{tl}</ol>
      <div>
        <h3 style="margin-bottom:14px">{t["teach"]}</h3>
        <p style="color:var(--ink-2);font-size:.95rem">{t["teach_p"]}</p>
        <ul class="list" id="students"></ul>
      </div>
    </div>
  </div>
</section>'''
    if key == "talks":
        return f'''<section class="block" id="talks">
  <div class="wrap">
    {head_block(key,l,t["title"][key])}<p>{t["talks_p"]}</p></div>
    <div id="talklist"></div>
  </div>
</section>'''
    if key == "outreach":
        return f'''<section class="block" id="outreach">
  <div class="wrap">
    {head_block(key,l,t["title"][key])}<p>{t["out_p"]}</p></div>
    <div class="cards3">
      <div>
        <h3>{t["service"]}</h3>
        <p style="color:var(--ink-2);font-size:.95rem">{t["service_p"]}</p>
      </div>
      <div>
        <h3>{t["events"]}</h3>
        <ul class="list">{li_list(t["events_list"])}</ul>
      </div>
      <div>
        <h3>{t["outreach"]}</h3>
        <ul class="list">{li_list(t["outreach_list"])}</ul>
      </div>
    </div>
  </div>
</section>'''
    if key == "contact":
        return f'''<section class="block" id="contact">
  <div class="wrap">
    {head_block(key,l,t["contact_h"])}<p>{t["contact_p"]}</p></div>
    <div class="contact-grid">
      <div><h3>{t["email"]}</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
      <div><h3>{t["addr_h"]}</h3><p>{t["addr"]}</p></div>
      <div><h3>{t["profiles"]}</h3><p><a href="{ORCID}">ORCID 0000-0002-0661-8712</a><br><a href="{SCOPUS}">Scopus 57197743866</a><br><a href="https://github.com/montsecompa">GitHub</a></p></div>
    </div>
  </div>
</section>'''


def page(key, l):
    t = T[l]
    up = "../" if PREFIX[l] else ""
    fname = f"{key}.html"
    title = "Montserrat Compa Ferrer" if key == "index" else f'{t["title"][key]} | Montserrat Compa Ferrer'
    desc = t["meta_desc"] if key == "index" else t["blurb"][key]
    base_url = "https://montsecompa.github.io/"
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{base_url}{PREFIX[x]}{"" if key=="index" else fname}">\n' for x in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{base_url}{"" if key=="index" else fname}">\n'
    nav = "".join(f'<a href="{k}.html"{" class=\"on\" aria-current=\"page\"" if k == key else ""}>{t["nav"][k]}</a>' for k, _ in PAGES[1:])
    gauge = "".join(f'<li><a href="{k}.html"{" class=\"on\"" if k == key else ""}>{t["gauge"].get(k, t["nav"][k])}<span>{d}</span></a></li>' for k, d in PAGES)
    langs = "".join(f'<a href="{up}{PREFIX[x]}{fname}" hreflang="{x}" lang="{x}" title="{LANG_NAME[x]}"{" aria-current=\"true\" class=\"on\"" if x == l else ""}>{x.upper()}</a>' for x in LANGS)
    idx = [p[0] for p in PAGES].index(key)
    nxt = ""
    if key != "index":
        nxt = (f'<section class="next"><div class="wrap"><a href="{PAGES[idx+1][0]}.html">{t["next"]}: {t["title"][PAGES[idx+1][0]]}</a></div></section>'
               if idx + 1 < len(PAGES) else f'<section class="next"><div class="wrap"><a href="index.html">{t["back"]}</a></div></section>')
    needs_data = key in ("index", "research", "publications", "funding", "career", "talks")
    data = f'<script src="{up}data.js?v={ver('data.js')}"></script>\n' if needs_data else '<script>const THEMES={},OTHER={},PUBS=[],FACTS=[];</script>\n'
    # On the English home page, send returning visitors to the language they chose before
    redirect = ""
    if key == "index" and l == "en":
        redirect = '<script>try{var g=localStorage.getItem("mc-lang");if(g==="es"||g==="ca")location.replace(g+"/")}catch(e){}</script>\n'
    return f'''<!doctype html>
<html lang="{l}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
{alts}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}style.css?v={ver('style.css')}">
{redirect}<script>try{{var t=localStorage.getItem("mc-theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html">Montserrat Compa</a>
    <div class="right">
      <nav class="main" id="nav">{nav}</nav>
      <nav class="langs" aria-label="{t["langs"]}">{langs}</nav>
      <button class="menu-btn" aria-expanded="false" aria-controls="nav">{t["menu"]}</button>
    </div>
  </div>
</header>
<nav class="gauge" aria-hidden="true"><ol><span class="bob"></span>{gauge}</ol></nav>
<main id="main">
{content(key, l)}
{nxt}
</main>
<footer class="slim">
  <div class="wrap">
    <span>© <span id="yr"></span> Montserrat Compa Ferrer, {t["footer"]}</span>
    <span class="fl"><a href="mailto:{EMAIL}">{t["email"]}</a><a href="{ORCID}">ORCID</a><button class="theme-btn" id="themebtn">{t["theme"]}</button></span>
  </div>
</footer>
{data}<script src="{up}site.js?v={ver('site.js')}"></script>
</body>
</html>
'''


if __name__ == "__main__":
    for l in LANGS:
        out = os.path.join(HERE, PREFIX[l])
        os.makedirs(out, exist_ok=True)
        for key, _ in PAGES:
            with open(os.path.join(out, f"{key}.html"), "w", encoding="utf-8") as f:
                f.write(page(key, l))
    print("Built", len(LANGS) * len(PAGES), "pages")
