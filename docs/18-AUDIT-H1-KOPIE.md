# 360°-audit — thema "Hyper kopie 5 okt (H1-test)"

**Datum:** 31 oktober 2026 · **Thema-id:** 194824929546 · **Prefix:** /t/8
**Laatst gewijzigd:** 27 oktober 2026 · **Status:** UNPUBLISHED
**Live thema ter vergelijking:** Hyper (188874326282), prefix /t/2

**Er is tijdens deze audit niets gewijzigd.** Geen bestand, geen instelling, geen
thema. Alle handelingen waren leesopdrachten.

---

## 1. Executive summary

H1-Kopie is **geen variant van het live thema maar een vervanging ervan**. Op elke
belangrijke template staan de standaardsecties uitgeschakeld en nemen eigen
`pd-*`-secties het over:

| Template | Actief | Uitgeschakeld |
|---|---|---|
| Homepage | pd-home, pd-home-cta, apps | 11 secties |
| Collectie | breadcrumbs, pd-collection, apps | rich-text-h1, main-collection-product-grid |
| Product | breadcrumbs, pd-product-hero, pd-product-details, apps | main-product + 7 andere |
| Samplepagina | pd-samples | 6 secties |

Dat is een ingrijpende keuze, en inhoudelijk een goede. De eigen secties lossen
precies de problemen op waar de winkel organisch op vastloopt. Maar het thema
draagt ook forse ballast mee, bevat vier claims die ik niet kan verantwoorden, en
één aantoonbare tegenspraak op de pagina die je advertentieverkeer opvangt.

**Oordeel op wat ik kon beoordelen: 6,3 / 10.**

Belangrijk: dat cijfer dekt ongeveer de helft van een volledige audit. Visueel
ontwerp, UX, conversie, mobiel gedrag, functionele tests en echte
snelheidsmetingen zijn **niet beoordeelbaar** — zie hoofdstuk 2.

**De vijf zwaarste bevindingen:**

1. **AUDIT-001 (P0)** — "4,9 / 5 op Google" staat als *standaardwaarde in de code*
   en wordt op home-, collectie- en studiopagina's getoond. De instelling is leeg,
   dus die 4,9 komt uit een letterlijke tekst, niet uit data.
2. **AUDIT-002 (P0)** — De samplepagina belooft op één plek "binnen 2 werkdagen"
   en op een andere "binnen 3–5 werkdagen in huis".
3. **AUDIT-003 (P1)** — 109 beeldbestanden (105,5 MB, 97,9% van al het eigen
   beeldmateriaal) hebben nergens een verwijzing. Weesbestanden.
4. **AUDIT-004 (P1)** — 457 KB render-blokkerende CSS, waarvan 253 KB als laatste
   en zonder preload wordt geladen.
5. **AUDIT-005 (P1)** — De labels van 823 en 824 zijn in de SEO-tekst verwisseld.

**Wat H1-Kopie wél repareert ten opzichte van live** — en dit is substantieel:

| Probleem op live | In H1-Kopie |
|---|---|
| Homepage-title is letterlijk `PureDeco` (9 tekens) | Volwaardige title via pd-seo |
| Collectiepagina's hebben **nul** `<h1>` | Elke collectie krijgt een `<h1>` |
| Productpagina heeft **twee** identieke `<h1>` | Eén `<h1>` |
| Alleen Organization-schema | CollectionPage, ItemList, FAQPage, Product, BreadcrumbList, 2× VideoObject |
| Geen broodkruimel-schema | BreadcrumbList op collectie en product |
| /pages/installatie rendert vrijwel leeg | Eigen template met pd-installatie |

---

## 2. Onderzoeksbereik en beperkingen

### Wat ik heb onderzocht

| Bron | Omvang |
|---|---|
| Bestandsinventaris H1-Kopie | **575 bestanden**, volledig, met exacte grootte en MD5 |
| Thema-code gelezen | 30 bestanden (alle 33 `pd-*` op 3 na, `layout/theme.liquid`, `main-product.liquid`, 8 templates) |
| Live gerenderde HTML | 6 URL's: home, 2 collecties, product, pagina, 404 |
| Sitemap en robots.txt | volledig uitgelezen en URL's geteld |
| CDN-gedrag afbeeldingen | empirisch getest op WebP-onderhandeling en maatvoering |
| Beeldmateriaal | 7 bestanden gedownload en gemeten; 3 visueel beoordeeld |
| Winkel-data | 71 producten, 16 collecties, 12 pagina's, 1 blog + 7 artikelen |

### Wat ik NIET heb kunnen onderzoeken

**De doorslaggevende beperking: ik kan H1-Kopie niet renderen.** Het preview-pad
`/t/8/` geeft een 404 die door het *live* thema wordt opgebouwd — Shopify vereist
een ingelogde sessie voor previews van ongepubliceerde thema's. Daarmee vervalt:

- Visueel ontwerp, typografie, witruimte, kleurgebruik → **N/B**
- Alle UX- en navigatiebeoordeling in de praktijk → **N/B**
- Conversieoptimalisatie en frictiemeting → **N/B**
- Mobiele weergave en touch-gedrag → **N/B**
- Functionele tests (menu, filters, winkelwagen, varianten, formulieren) → **N/B**
- Echte Core Web Vitals (LCP, INP, CLS) → **N/B**
- Kleurcontrast, toetsenbordbediening, screenreader-gedrag → **N/B**
- Checkout en betaalstromen → **N/B** (en niet getest, conform opdracht)
- Browsercompatibiliteit → **N/B**

**Om dit alsnog te beoordelen heb ik één ding van je nodig:** een deelbare
previewlink uit Shopify-admin (Online Store → Thema's → H1-test → ⋯ → Preview →
"Share preview"). Die link werkt zonder inloggen en is 14 dagen geldig. Met die
link kan ik het tweede deel van deze audit uitvoeren.

Verder niet onderzocht: 3 van de 33 `pd-*` bestanden, de ~130 overgebleven
standaardsecties en -snippets van het Hyper-thema, en `config/settings_schema.json`.

### Over de twintig expertperspectieven

Ik heb de gevraagde perspectieven als beoordelingskader gebruikt. Ik presenteer
ze niet als afzonderlijke personen en verzin geen gesprekken of oordelen. Waar
perspectieven botsen, benoem ik dat — zie hoofdstuk 9 (weesbestanden) en
hoofdstuk 11 (renders).

---

## 3. Algemene score

| | |
|---|---|
| **Gewogen eindcijfer beoordeelbare onderdelen** | **6,3 / 10** |
| Dekking van de audit | ± 50% van een volledige audit |
| Niet beoordeelbaar | 9 van de 20 categorieën |

**Zo is het gewogen:**

| Categorie | Score | Gewicht | Bijdrage |
|---|---:|---:|---:|
| SEO (code-niveau) | 7,0 | 20% | 1,40 |
| Techniek en thema-architectuur | 5,5 | 20% | 1,10 |
| Copywriting en content | 7,5 | 15% | 1,13 |
| Performance (code-niveau) | 4,5 | 15% | 0,68 |
| Toegankelijkheid (code-niveau) | 7,0 | 10% | 0,70 |
| Security en privacy | 6,5 | 10% | 0,65 |
| Claims en compliance | 6,0 | 10% | 0,60 |
| **Totaal** | | **100%** | **6,25** |

Niet-beoordeelbare categorieën zijn uit de berekening gelaten, zoals gevraagd.

---

## 4. Scorecard per hoofdcategorie

| # | Categorie | Score | Zekerheid |
|---|---|---|---|
| A | Visueel design & UI | **N/B** | — |
| B | Branding & merkidentiteit | **N/B** (deels: tone of voice 9/10) | laag |
| C | SEO | **7,0** | hoog |
| D | Conversieoptimalisatie | **N/B** | — |
| E | Productfoto's & visuele content | **5,5** | middel |
| F | Productbeschrijvingen & copywriting | **7,5** | hoog |
| G | Technische Shopify-audit | **5,5** | hoog |
| H | Functionele tests | **N/B** | — |
| I | Performance & snelheid | **4,5** | middel (code, geen meting) |
| J | Mobile-first | **N/B** | — |
| K | Toegankelijkheid | **7,0** | middel (alleen code) |
| L | Customer journey | **N/B** | — |
| M | Navigatie & informatiearchitectuur | **6,0** | middel |
| N | Security & privacy | **6,5** | middel |
| O | Claims & juridische houdbaarheid | **6,0** | hoog |
| P | Analytics & datakwaliteit | **N/B** | — |
| Q | Internationalisatie | **4,0** | middel |

---

## 5. Gedetailleerde scores per subonderdeel

### C. SEO — 7,0

| Subonderdeel | Score | Bewijs |
|---|---:|---|
| Title tags | 8 | `pd-seo.liquid` levert unieke titels met lengtebewaking (`if t.size > 68` valt terug op een korte variant). Homepage gaat van `PureDeco` naar `Wandpanelen met bamboekern \| Houtlook & naadloos \| PureDeco` |
| Meta descriptions | 8 | Automatisch opgebouwd per product uit decor, formaat, afwerking en prijs; afgekapt op 165 tekens in `theme.liquid` |
| H1-structuur | 8 | `pd-collection.liquid:10` → `assign h1 = collection.metafields.custom.seo_h1.value \| default: collection.title`, daarna overschreven door pd-seo indien aanwezig. **Elke** collectie krijgt dus een H1 |
| Structured data | 8 | CollectionPage + ItemList (`pd-collection:475`), FAQPage (`:623`), Product (`pd-product-hero:700`), 2× VideoObject (`:711`, `:736`), BreadcrumbList (`breadcrumbs:83`) |
| Canonicals | 7 | Genormaliseerd naar het hoofddomein in `theme.liquid` |
| robots.txt & sitemap | 6 | Shopify-defaults plus Facebook-toestemmingen. **Sitemap biedt 79 URL's aan** (45 producten, 14 collecties, 11 pagina's, 7 artikelen, 1 blog, 1 agentic) |
| Interne links | 8 | Rijke contextuele links in de collectieteksten; **alle 24 producthandles en 11 collectiehandles geverifieerd: allemaal bestaand en actief** |
| Contentdiepte | 6 | Slechts 3 van 16 collecties hebben eigen intro + bodytekst (wandpanelen, hout-1, 8mm-naadloos); 2 alleen meta (japandi, leer); 8 niets |
| URL-structuur | 6 | `hout-1` met telsuffix, `verkoopparters` met typefout, collectie `kunst` terwijl de tekst "Art" zegt |
| Afbeelding-SEO | 5 | Zie AUDIT-012 |
| www-afhandeling | 5 | JavaScript-redirect in de `<head>` in plaats van alleen de 301 |

### F. Copywriting — 7,5

| Subonderdeel | Score | Toelichting |
|---|---:|---|
| Helderheid | 9 | Zeldzaam eerlijk: *"Het decor zit in de toplaag. Een houtlook-paneel is dus geen massief hout"* |
| Structuur | 9 | Vergelijkingstabellen, genummerde montagestappen, rekenvoorbeelden met echte getallen |
| Tone of voice | 9 | Consistent rustig en premium, overal de je-vorm |
| Overtuigingskracht | 8 | Bezwaren worden vooraf weggenomen in plaats van omzeild |
| Claimdiscipline (proces) | 9 | Zie hoofdstuk 12 — uitzonderlijk |
| Claimdiscipline (inhoud) | 5 | Vier claims die ik niet kan verantwoorden |
| Interne consistentie | 4 | AUDIT-002 en AUDIT-005 |

### G. Techniek — 5,5

| Subonderdeel | Score | Toelichting |
|---|---:|---|
| Architectuur | 6 | Nette `pd-*`-naamruimte, elk bestand met een commentaarkop die bron en akkoorddatum vermeldt |
| Codekwaliteit | 5 | 16 inline scripts verdeeld over layout en secties; `setTimeout`-patches; `innerHTML` met stringplakwerk |
| Liquid-correctheid | 7 | Eén echte bug (AUDIT-013) |
| Theme Editor-compatibiliteit | 8 | Volledige schema's met labels, defaults, presets en `enabled_on`-groepen |
| Assethygiëne | 3 | AUDIT-003, plus 2 dubbele bestanden, 1 leeg JS-bestand, 2 CSS-bestanden van 1 byte, `pd-test.mp4` |
| Onderhoudbaarheid | 5 | Prijzen hardgecodeerd in `pd-seo.liquid`; elke prijswijziging vraagt een themabewerking |
| Dode configuratie | 4 | 25 uitgeschakelde secties blijven in de templates staan; 7 ongebruikte productvarianten van ±34 KB |

### I. Performance — 4,5 (code-niveau, geen meting)

| Subonderdeel | Score | Gemeten feit |
|---|---:|---|
| CSS-strategie | 4 | vendor.css 12 KB + theme.css 192 KB + puredeco-premium.css **253 KB** = 457 KB render-blokkerend |
| Afbeeldinglevering | 7 | Alle beeldaanroepen gebruiken `asset_img_url` met expliciete maten en srcset. CDN onderhandelt WebP: getest, 2.791 KB PNG komt binnen als **322 KB**, met maat als **184 KB** |
| JS-strategie | 5 | vendor.js 230 KB + theme.js 99 KB, beide `defer` — correct. Maar 16 inline scripts |
| Basisgewicht HTML | 3 | **432 KB voordat er inhoud is** (gemeten op de 404-pagina). Live collectiepagina: 1.144 KB |
| LCP-prioritering | 4 | Geen `fetchpriority` in `pd-product-hero`; 3 van 4 `<img>` op `lazy` |
| CWV gemeten | **N/B** | Kan niet zonder preview |

### K. Toegankelijkheid — 7,0 (alleen code)

| Subonderdeel | Score | Bewijs |
|---|---:|---|
| Landmarks & skip-link | 9 | `skip-to-content-link`, `role="main"`, `role="contentinfo"`, aria-live-meldingen |
| ARIA-gebruik | 8 | pd-product-hero: 20 aria-labels, 3 aria-live, 20 aria-hidden op decoratieve SVG's |
| Kopstructuur | 7 | pd-collection gebruikt netjes h1/h2/h3. **Live** springt van h3 naar h5 (47× h3, 3× h5, 0× h1) — dat wordt dus opgelost |
| Formulierlabels | 8 | `pd-footer`: expliciet `<label class="visually-hidden">` bij het e-mailveld |
| Alt-teksten | 6 | Goed in snippets; zwak op JS-opgebouwde swatches (AUDIT-012) |
| Contrast, focus, toetsenbord | **N/B** | Kan niet zonder rendering |

### Q. Internationalisatie — 4,0

| Subonderdeel | Score | Toelichting |
|---|---:|---|
| Taalbestanden | 5 | de, en, es, fr, it, nl, vi aanwezig. **Maar `nl.schema.json` ontbreekt**, terwijl `vi.schema.json` (Vietnamees) er wel is |
| Standaardtaal | 4 | `en.default.json` is de basis voor een Nederlandse winkel |
| hreflang | **N/B** | Geen meertalige verkoop vastgesteld |
| RTL-ondersteuning | 2 | Werkt aantoonbaar niet, zie AUDIT-013 |

---

## 6. Volledige technische audit

### 6.1 Bestandsinventaris

| Soort | Aantal | Opvallend |
|---|---:|---|
| Totaal | **575** | |
| Secties | 123 | waarvan 15 eigen `pd-*` |
| Snippets | 148 | waarvan 18 eigen `pd-*` |
| Templates | 56 | waarvan 7 ongebruikte productvarianten |
| Assets | ~210 | waarvan 119 eigen beeldbestanden |
| Locales | 13 | |

**Grootste bestanden:**

| Bestand | Grootte |
|---|---:|
| `sections/main-product.liquid` | 124 KB (uitgeschakeld!) |
| `sections/header.liquid` | 105 KB |
| `sections/custom-content.liquid` | 102 KB (uitgeschakeld) |
| `sections/tabs-content.liquid` | 86 KB (uitgeschakeld) |
| `templates/product.json` | 77 KB |
| `sections/pd-product-hero.liquid` | 73 KB |
| `assets/puredeco-premium.css` | **253 KB** |
| `assets/theme.css` | 192 KB |
| `assets/vendor.js` | 230 KB |

### 6.2 Technische schuld

1. **25 uitgeschakelde secties** blijven met volledige instellingen in de
   templates staan. Ze renderen niet — geen looptijdkosten — maar maken
   `product.json` 77 KB en `index.json` 48 KB groot en de Theme Editor
   onoverzichtelijk.
2. **7 ongebruikte productvarianten** (coming-soon, flash-sale, grid-2-columns,
   grid-mix, horizontal-thumbnails, out-of-stock, product-image-swatch) van
   ±34 KB elk ≈ 243 KB.
3. **2 identieke templateparen** (zelfde MD5):
   `article.gids.json` = `blog.gids-badkamer.json`,
   `article.buigen.json` = `blog.gids-buigen.json`.
4. **`collection.doorladen-test.json`** — een testtemplate in het thema.
5. **Lege bestanden:** `assets/localization-form.js` (0 bytes),
   `section-custom-content.css` en `section-featured-blog.css` (1 byte).

---

## 7. Complete SEO-analyse

### 7.1 Waarom er organisch bijna niets van je in Google staat

Dit is de meest gestelde vraag en het antwoord is structureel, niet toevallig.

**Oorzaak 1 — er worden maar 79 URL's aangeboden.**

```
sitemap_products_1.xml       45 URLs
sitemap_collections_1.xml    14 URLs
sitemap_pages_1.xml          11 URLs
sitemap_articles_1.xml        7 URLs
sitemap_blogs_1.xml           1 URL
sitemap_agentic_discovery     1 URL
                       TOTAAL 79
```

Je hebt 71 producten, waarvan er maar 45 in de sitemap staan — de rest is DRAFT.
Dat is een plafond dat geen enkele themawijziging oplost.

**Oorzaak 2 — op live ontbreken de signalen die Google nodig heeft.**
Gemeten op de live site:

| Pagina | `<h1>` | Schema-types |
|---|---|---|
| Homepage | 1 — en dat is **het logo** | Organization, WebSite, SearchAction |
| /collections/wandpanelen | **0** | alleen Organization |
| /collections/kunst | **0** | — |
| /products/811-hout-walnut-classic | **2, identiek** | 2× Product, 2× Offer, ProductGroup, Brand |

De homepage-title is letterlijk `<title>PureDeco</title>`. Negen tekens, geen
enkel zoekwoord.

**Oorzaak 3 — basisgewicht van 432 KB HTML per pagina voordat er inhoud is**,
oplopend tot 1.144 KB op een collectiepagina. 100 `<script>`-tags op de
homepage.

### 7.2 Wat H1-Kopie hieraan doet

| Signaal | Live | H1-Kopie |
|---|---|---|
| Homepage-title | `PureDeco` | `Wandpanelen met bamboekern \| Houtlook & naadloos \| PureDeco` |
| H1 op collecties | 0 | 1 per collectie, altijd |
| H1 op product | 2 identiek | 1 |
| CollectionPage-schema | nee | ja, met ItemList van alle producten |
| FAQPage-schema | nee | ja, 8 vragen per collectie |
| BreadcrumbList | nee | ja |
| VideoObject | nee | ja, 2 per product met video |
| Eigen collectietekst | nee | 3 collecties, ±800 woorden elk |

**Eerlijk antwoord op je vraag "gaat dit wijzigen als we H1-kopie live zetten?":**
ja, op het punt van signalen — aanzienlijk. Maar het **aantal** URL's verandert
niet. Van 79 aangeboden URL's naar meer kom je alleen door producten uit DRAFT te
halen en door de 8 collecties zonder tekst inhoud te geven.

---

## 8. UI/UX-rapport

**N/B.** Zonder rendering kan ik geen uitspraak doen over layout, typografie,
witruimte, hiërarchie of micro-interacties. Ieder cijfer hier zou verzonnen zijn.

Wat ik uit de code wél kan afleiden, als hypothese:

- `pd-samples.liquid:50` zet de H1 van de samplepagina in de klasse
  `ph-k ph-k--bronze`. In dezelfde codebase wordt `ph-k` gebruikt voor kleine
  bovenregels. **Hypothese:** de H1 van je belangrijkste advertentielandingspagina
  is visueel het kleinste element op de pagina. Te verifiëren met een preview.
- `theme.liquid` plaatst twee `{% style %}`-blokken **tussen `</head>` en
  `<body>`**. Browsers herstellen dit, maar het is ongeldige HTML.
- `.pd-btn` gebruikt `var(--pd-green)` voor de rand maar `#55884d` hardgecodeerd
  voor de vulling. Als die twee niet gelijk zijn, zie je een rand in een andere
  tint dan de knop.

---

## 9. Performance-audit

### 9.1 Wat ik heb gemeten

| Meting | Waarde | Methode |
|---|---|---|
| Render-blokkerende CSS | **457 KB** | optelsom van `theme.liquid` |
| JS via `defer` | 329 KB | idem |
| Basisgewicht HTML (live) | **432 KB** | 404-pagina, curl |
| Collectiepagina (live) | **1.144 KB** | curl |
| Productpagina (live) | 1.063 KB, 1,60 s | curl |
| `<script>`-tags homepage (live) | **100** | geteld in de HTML |
| Dubbel geladen stylesheets (live) | **5** | `rez-form`, `rez-preorder`, `section-slideshow`, `section-featured-collection`, `component-multicolumn-card` |

### 9.2 Een correctie die ik mezelf moet opleggen

Ik stond op het punt te melden dat 94,8 MB aan PNG's je site vertraagt. **Dat zou
onjuist zijn geweest.** Ik heb het getest:

```
pdtmp-851-2.png            → content-type: image/webp   329.444 bytes
pdtmp-851-2_800x.png       → content-type: image/webp   188.448 bytes
```

Shopify's CDN zet die PNG's automatisch om naar WebP op basis van de
Accept-header, ook zonder maatparameter. De bron is 2.791 KB; de browser krijgt
322 KB. Bovendien gebruiken **alle** beeldaanroepen in de eigen code
`asset_img_url` met expliciete maten plus srcset. Dat is correct gedaan.

De 94,8 MB is dus een **opslag- en onderhoudsprobleem**, geen snelheidsprobleem.
Dat verandert de prioriteit van P0 naar P1.

### 9.3 Core Web Vitals

**N/B.** Ik verzin geen LCP-, INP- of CLS-waarden. Met een deelbare previewlink
meet ik ze met Lighthouse.

Wel een gefundeerde zorg: de `setTimeout`-patches in `theme.liquid` wijzigen de
pagina **2, 5 en 15 seconden** na het laden:

```javascript
setTimeout(function () { ... textNode.nodeValue = " Verzenden"; }, 5000);
setTimeout(function () { preorderBtn.textContent = 'Houd mij op de hoogte'; }, 2000);
setTimeout(function () { ... display: none !important ... }, 15000);
```

CLS wordt over de hele levensduur van een pagina gemeten. Een element dat na 15
seconden verdwijnt, telt mee. En de bezoeker ziet 5 seconden lang de verkeerde
knoptekst.

---

## 10. Toegankelijkheidsrapport

Sterke punten uit de code: skip-link, `role="main"`, `role="contentinfo"`,
aria-live-regio's, verborgen labels bij formuliervelden, `aria-hidden` op
decoratieve SVG's, en in `pd-product-hero` een `visually-hidden` voorvoegsel dat
materiaal en code aan de producttitel toevoegt voor schermlezers.

Zwakke punten:

- JS-opgebouwde swatches krijgen hun toegankelijke naam via `title`:
  `li.innerHTML = '<img alt="" src="' + c[k].img + '">'; li.title = c[k].label;`
  Schermlezers gaan wisselend met `title` om. Beter: `aria-label` op het
  lijstitem.
- Op **live** springt de kopstructuur van h3 naar h5 (WCAG 1.3.1). In H1-Kopie
  is dat in `pd-collection` opgelost; voor de overige secties niet geverifieerd.

Contrast, toetsenbordbediening en screenreader-gedrag: **N/B**.

---

## 11. Productfoto's en visuele content

### 11.1 Wat er werkelijk gebruikt wordt

Van de 119 eigen beeldbestanden worden er **10** gebruikt, samen 2,3 MB:

| Bestand | Grootte | Efficiëntie |
|---|---:|---|
| pd-vis-kantoor.jpg | 397 KB | |
| pd-vis-badkamer.jpg | 340 KB | 0,10 B/px |
| pd-vis-woonkamer.mp4 | 316 KB | |
| pd-vis-keuken.jpg | 307 KB | |
| pd-vis-woonkamer.jpg | 291 KB | 0,10 B/px |
| pd-vis-slaapkamer.jpg | 285 KB | |
| pd-vis-toilet.jpg | 204 KB | |
| pd-close-811.jpg | 122 KB | 0,14 B/px |
| pd-montage-liggend.jpg | 59 KB | |
| pd-montage-staand.jpg | 43 KB | |

Technisch is dit goed gedaan: 0,10–0,14 bytes per pixel is correct voor
fotografisch materiaal.

### 11.2 Visuele beoordeling van drie bestanden

**pd-close-811.jpg (920×920)** — een scherpe macro-opname van de notenhoutnerf.
Het reliëf is overtuigend zichtbaar en onderbouwt de claim "de nerf zie én voel
je". Twee bezwaren: er is geen enkele maatreferentie in beeld, en de kleur is
sterk rood-oranje. Juist voor een merk waarvan het hele staalprogramma bestaat
omdat "houtkleuren zie je het best in je eigen licht", is een roodverschoven
close-up een risico op teleurstelling en retouren. **7/10.**

**pd-vis-woonkamer.jpg en pd-vis-badkamer.jpg** — dit zijn **3D-renders, geen
foto's**. Dat is onmiskenbaar: volmaakt vlakke oppervlakken, geen stof of
oneffenheid, fysiek onwaarschijnlijke scherpe lichtvlekken, een spiegel die een
lege witte ruimte weerkaatst, een handdoek zonder plooien.

Als renders zijn ze competent en onderling consistent: dezelfde camerahoogte,
dezelfde lichtrichting, hetzelfde warme neutrale palet. Dat is goed voor
merkherkenning.

Drie problemen:

1. **Ze worden niet als impressie gelabeld.** De bestandsnaam zegt `pd-vis-`
   (visualisatie), maar of de pagina dat toont kan ik niet zien. Zonder
   bijschrift kan een bezoeker ze lezen als foto's van echte installaties. Dat
   raakt direct jouw eigen regel om nooit projecten of referenties te verzinnen.
2. **Ze werken tegen je belangrijkste verkoopargument.** De tekst belooft een wand
   die "leest als één vlak" met een "vrijwel onzichtbare" naad. In beide renders
   is een verticale overgang in de wand zichtbaar. Ik weet niet zeker of dat de
   paneelnaad is — maar als het dat is, laat je beeld zien wat je tekst ontkent.
3. **De woonkamer is kleurtechnisch onbetrouwbaar.** De wandtint loopt van
   oranje-belicht naar donkerbruin binnen hetzelfde paneel. Voor een product
   waarvan de hele staalfunnel om echte kleur draait, is dat contraproductief.

**Gemiddeld 5,5/10** — technisch in orde, inhoudelijk werken ze tegen de
propositie.

### 11.3 Een meningsverschil tussen perspectieven, expliciet benoemd

Vanuit **performance** zijn de 105,5 MB weesbestanden onschadelijk: ze worden
nooit opgevraagd. Vanuit **thema-architectuur** zijn ze een serieus probleem:
Shopify kent limieten per thema, en elke upload, duplicatie en backup sleept ze
mee. Vanuit **QA** zijn ze gevaarlijk: niemand weet nog welke van de vijf
varianten van 851 de juiste is. Ik heb deze bevinding daarom op **P1** gezet, niet
op P0 — met de nadruk op opruimen vóór publicatie, niet op snelheid.

---

## 12. Claims en juridische houdbaarheid

### 12.1 Het proces is uitzonderlijk goed

Dit verdient expliciete erkenning, want ik zie het zelden:

- Elk `pd-*`-bestand opent met een commentaarkop die de **bron en de akkoorddatum**
  van de claims vermeldt: *"Brandklasse B1 bevestigd door Puredeco"*,
  *"akkoord 14 okt 2026"*, *"goedgekeurd 8 okt 2026"*.
- `snippets/pd-gids-tekst.liquid` bevat een **verbodslijst** in de code:
  *"Niet gebruiken: geluidsabsorberend (wandpanelen), hittebestendig,
  brandklasse, UV-bestendig, levertijden."*
- `snippets/pd-vergelijk.liquid` kwalificeert de vergelijking expliciet:
  *"Brandklasse zoals opgegeven door de aanbieder"* en de rijlabel
  *"Brandklasse (opgegeven)"*.
- `snippets/pd-reviews.liquid` filtert hard op `verified_buyer == true`, berekent
  het gemiddelde alleen daarover, en stelt in het commentaar vast:
  *"Geen eigen JSON-LD: winkelreviews horen niet als productbeoordeling in
  Google."* Dat is exact juist.
- `sections/pd-projects.liquid:239` heeft een documentveld met default
  "Brandklasse-certificaat" — de structuur anticipeert op onderbouwing.

**Score voor het proces: 9/10.**

### 12.2 Vier claims die ik niet kan verantwoorden

**1. "4,9 / 5 op Google" — P0.** Dit staat als *standaardwaarde* in het schema:

```json
{ "type": "text", "id": "google_score", "label": "Google-score bij de vinkjes", "default": "4,9 / 5" }
```

en wordt gebruikt in `pd-collection:96` ("op Google"), `pd-collection:106`
("op Google Reviews"), `pd-home:83/663/692` en `pd-studio:188`.
In `config/settings_data.json` komt `google_score` **nul keer** voor. De
instelling is dus leeg en de standaardwaarde rendert.

Het getal kan feitelijk kloppen — dat kan ik niet nagaan. Het **mechanisme** is
niet verdedigbaar: er is geen koppeling met Google, geen datum, geen aantal
beoordelingen en geen verificatieverklaring. Sinds de Omnibus-richtlijn
(Nederland, 28 mei 2022) moet een handelaar die consumentenbeoordelingen toont,
vermelden of en hoe hij controleert dat ze van echte klanten komen. Een
hardgecodeerd gemiddelde zonder die verklaring is een misleidende omissie.

Opvallend: `pd-reviews.liquid` doet het in hetzelfde thema wél goed. De
vinkjesbalk omzeilt dat zorgvuldige mechanisme.

**2. "Binnen 2 werkdagen" versus "binnen 3–5 werkdagen" — P0.**
In `templates/page.sample.json`:

- regel 397: *"Je ontvangt de samples gratis binnen 2 werkdagen"*
- regel 535: `"delivery": "binnen 3–5 werkdagen in huis"`

Beide staan op dezelfde pagina. Dit is je belangrijkste landingspagina voor
Meta-verkeer en de bron van de staalorders waar we deze hele week op sturen.

**3. "De toplagen worden vervaardigd uit 100% gerecyclede materialen" — P1.**
`templates/index.json:1053` en `pd-home:707`. Elders in hetzelfde thema staat
alleen "toplaag van gerecycled PVC" zonder percentage. Een 100%-claim vraagt
onderbouwing; de ACM-leidraad duurzaamheidsclaims eist dat je kunt aantonen
waarop het percentage slaat.

**4. "3 jaar garantie" en "Brandklasse B1" — P1, documentatie.**
Garantie staat op 5 plekken (`index.json:152`, `product.json:72` en `:229` 2×,
`pd-product-details:125`). Brandklasse B1 staat in `pd-product-details:121`,
`pd-projects:37/102`, `pd-insp-tekst:67` en in vrijwel elke meta description via
`pd-seo`. Beide zijn volgens de commentaarkoppen door jou bevestigd. **Ik vraag
niet of ze waar zijn — ik vraag of het certificaat en de garantievoorwaarden
beschikbaar zijn**, want ze staan nu op elke productpagina en in de
zoekresultaten.

---

## 13. Security- en privacybevindingen

**Bevinding: `localStorage` → `innerHTML` zonder escaping.**

```javascript
function get() { try { return JSON.parse(localStorage.getItem(KEY) || '[]') || []; } catch (e) { return []; } }
...
li.innerHTML = '<img alt="" src="' + c[k].img + '">';
```

in `pd-product-hero:1118/1126` en `pd-samples:198/201`.

**Belangrijke nuance, en ik wil hier niet overdrijven:** ik heb gecontroleerd of
URL-invoer deze keten bereikt. Dat doet het **niet**. `URLSearchParams` in
`pd-product-hero:997` wordt alleen vergeleken met variant-id's, en
`location.search` in `pd-collection:718` dient enkel als sessionStorage-sleutel.
Er is dus **geen reflected XSS**. Een aanvaller kan de localStorage van een ander
niet vullen zonder al code-uitvoering te hebben.

Dit is daarom een **codekwaliteitsprobleem met defence-in-depth-waarde**, geen
exploiteerbaar lek. Oplossing is klein: `document.createElement('img')` met
`img.src = ...` in plaats van stringplakwerk.

**Privacy — wel aandacht nodig.** Op de live site laadt `recorder.msr.js`, een
sessierecorder, plus `cdn.nfcube.com` en `cdn.jsdelivr.net`. Sessieopnames vallen
onder de AVG en vereisen voorafgaande toestemming. Of dat correct gekoppeld is aan
je cookiebanner heb ik **niet** kunnen vaststellen — dat vraagt een test in de
browser. Ik meld het als te onderzoeken punt, niet als overtreding.

**Verder:** geen sleutels, tokens of inloggegevens aangetroffen in de code.

---

## 14. Concurrentiebenchmark

Ik heb geen concurrentiesites gemeten. Een vergelijking op basis van herinnering
zou verzonnen cijfers opleveren. Wat ik wel objectief kan plaatsen:

| Maatstaf | PureDeco (live, gemeten) | Gangbare norm | Oordeel |
|---|---|---|---|
| HTML per pagina | 432 KB – 1.144 KB | 50–150 KB | ver achter |
| `<script>`-tags | 100 | 15–30 | ver achter |
| Render-blokkerende CSS | 457 KB (H1-Kopie) | < 100 KB | achter |
| H1 op collecties | 0 (live) → 1 (H1-Kopie) | 1 | gelijk na publicatie |
| Product-schema | aanwezig maar dubbel (live) | 1× | gelijk na publicatie |
| Collectieteksten | 3 van 16 | alle | achter |
| URL's in sitemap | 79 | n.v.t. | structureel klein |

De normkolom zijn algemeen aanvaarde richtwaarden, geen metingen aan specifieke
concurrenten. Een echte benchmark vraagt dat je 3–5 concurrenten aanwijst.

---

## 15. Volledige problemenlijst

---

**Probleem-ID:** AUDIT-001
**Onderdeel:** Vertrouwensbalk op home-, collectie- en studiopagina
**Huidige score:** 2/10 · **Ernst:** Kritiek · **Prioriteit:** P0
**Wat is er mis?** "4,9 / 5 op Google" wordt getoond vanuit een hardgecodeerde
standaardwaarde, zonder bron, datum, aantal of verificatieverklaring.
**Bewijs:** `sections/pd-collection.liquid:96,106,810`; `sections/pd-home.liquid:83,663,692`;
`sections/pd-studio.liquid:188`. `config/settings_data.json` bevat `google_score` 0×.
**Waarom een probleem?** Omnibus-richtlijn: bij het tonen van
consumentenbeoordelingen moet je vermelden of en hoe je verifieert. Daarnaast is
het in strijd met je eigen regel om reviews nooit te verzinnen.
**Oplossing:** Vul de werkelijke Google-score en het aantal beoordelingen in de
instelling in, voeg "op basis van N beoordelingen" toe en link naar je
Google-profiel. Of verwijder het punt uit de balk. Zet de default leeg zodat een
lege instelling niets toont.
**Impact:** Hoog · **Moeilijkheid:** Eenvoudig · **Verwacht na verbetering:** 8/10

---

**Probleem-ID:** AUDIT-002
**Onderdeel:** Samplepagina (/pages/sample)
**Huidige score:** 3/10 · **Ernst:** Kritiek · **Prioriteit:** P0
**Wat is er mis?** Twee verschillende levertijdbeloftes op dezelfde pagina.
**Bewijs:** `templates/page.sample.json:397` "binnen 2 werkdagen" versus `:535`
`"delivery": "binnen 3–5 werkdagen in huis"`.
**Waarom een probleem?** Dit is de landingspagina van je Meta-verkeer en de bron
van de staalorders. Een bezoeker die 2 werkdagen leest en na 5 dagen nog wacht,
is een klacht en een verloren eerste indruk — bij een staalaanvraag die we op
€ 32,88 brutomarge waarderen.
**Oplossing:** Eén waarde kiezen die overeenkomt met de werkelijke
verzendpraktijk, en die op beide plekken gebruiken.
**Impact:** Hoog · **Moeilijkheid:** Eenvoudig · **Verwacht:** 9/10

---

**Probleem-ID:** AUDIT-003
**Onderdeel:** Assets
**Huidige score:** 2/10 · **Ernst:** Hoog · **Prioriteit:** P1
**Wat is er mis?** 109 beeldbestanden (105,5 MB) hebben geen enkele verwijzing —
97,9% van al het eigen beeldmateriaal. Waaronder 63 PNG's van 1 MB of groter.
**Bewijs:** `grep -rno 'pdtmp-'` over alle 30 gelezen `pd-*`-bestanden, alle
templates en `settings_data.json`: nul treffers. `pd-test.mp4` idem.
**Waarom een probleem?** Thema-uploads, duplicaties en backups slepen 105 MB mee.
Er zijn vijf varianten van 851 en niemand weet welke de juiste is.
**Let op:** dit is géén snelheidsprobleem — zie hoofdstuk 9.2.
**Oplossing:** Vóór publicatie opruimen. Eerst een backup-thema maken, dan
verwijderen. Twee bestanden zijn exacte duplicaten (`pdtmp-811.jpg` =
`pdtmp-811-0.jpg`; `pdtmp-621-0.jpg` = `pdtmp-821-0.jpg`).
**Impact:** Middel · **Moeilijkheid:** Eenvoudig · **Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-004
**Onderdeel:** CSS-laadstrategie
**Huidige score:** 4/10 · **Ernst:** Hoog · **Prioriteit:** P1
**Wat is er mis?** 457 KB render-blokkerende CSS, waarvan `puredeco-premium.css`
(253 KB) als allerlaatste in de `<head>` zonder preload.
**Bewijs:** `layout/theme.liquid` — `vendor.css` en `theme.css` met
`preload: true`, daarna `{{ 'puredeco-premium.css' | asset_url | stylesheet_tag }}`
ná `content_for_header` en de scripts.
**Waarom een probleem?** Dit staat op het kritieke pad voor First Paint en LCP.
**Oplossing:** Preload toevoegen; op termijn kritieke CSS splitsen van de rest.
Omdat de meeste standaardsecties uitgeschakeld zijn, is een groot deel van
`theme.css` (192 KB) vermoedelijk ongebruikt — met PurgeCSS te meten.
**Impact:** Hoog · **Moeilijkheid:** Gemiddeld · **Verwacht:** 7/10

---

**Probleem-ID:** AUDIT-005
**Onderdeel:** SEO-tekst collectie 8mm-naadloos
**Huidige score:** 3/10 · **Ernst:** Hoog · **Prioriteit:** P1
**Wat is er mis?** De labels van 823 en 824 zijn verwisseld.
**Bewijs:** `snippets/pd-seo.liquid` schrijft
`<a href="/products/823-japanse-stof-japandi-taupe">823 Taupe Dark</a>` en
`<a href="/products/824-japanse-stof-japandi-taupe-dark">824 Taupe</a>`.
De handles zeggen het omgekeerde: 823 = taupe, 824 = taupe-dark.
**Waarom een probleem?** Een klant klikt op "Taupe Dark" en komt bij Taupe. Bij
een product waarvan de kleur de hele aankoopbeslissing is, leidt dat tot een
verkeerde staalaanvraag of retour.
**Oplossing:** Labels omwisselen in `pd-seo.liquid`.
**Impact:** Middel · **Moeilijkheid:** Eenvoudig · **Verwacht:** 10/10

---

**Probleem-ID:** AUDIT-006
**Onderdeel:** Hardgecodeerde prijzen in SEO-teksten
**Huidige score:** 3/10 · **Ernst:** Hoog · **Prioriteit:** P1
**Wat is er mis?** `pd-seo.liquid` bevat prijzen als vaste tekst: € 89,95,
€ 99,95, € 119,95, € 139,95, € 179,95, "€ 26 tot € 57 per m²", "€ 38 per m²",
"€ 53 per m²", "€ 6,95 verzending".
**Waarom een probleem?** Elke prijswijziging vraagt een themabewerking. Als het
achterblijft, spreekt de paginatekst het Product-schema en de echte prijs tegen —
en Merchant Center keurt mismatches af.
**Oplossing:** Prijzen uit de productdata halen met `collection.products |
map: 'price_min' | sort | first | money`, zoals `pd-collection` al doet met
`pc_min`.
**Impact:** Hoog · **Moeilijkheid:** Gemiddeld · **Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-007
**Onderdeel:** /pages/ai-visualizer
**Huidige score:** 1/10 · **Ernst:** Hoog · **Prioriteit:** P1
**Wat is er mis?** De pagina bestaat in Shopify met templateSuffix
`ai-visualizer`, maar **geen enkel thema** bevat `templates/page.ai-visualizer.json`.
De pagina geeft 404.
**Bewijs:** `curl https://puredeco.nl/pages/ai-visualizer` → HTTP 404. Query op
beide thema's naar dat bestand → leeg resultaat.
**Waarom een probleem?** Een 404 op een bestaande pagina. Elke interne of externe
link ernaartoe is kapot.
**Oplossing:** Template maken, of de pagina in Shopify op een bestaand template
zetten, of de pagina verwijderen. **Dit raakt een URL, dus niet zonder jouw
toestemming.**
**Impact:** Middel · **Moeilijkheid:** Eenvoudig · **Verwacht:** 9/10

---

**Probleem-ID:** AUDIT-008
**Onderdeel:** `layout/theme.liquid` — setTimeout-patches
**Huidige score:** 3/10 · **Ernst:** Middel · **Prioriteit:** P1
**Wat is er mis?** Drie UI-correcties op een timer: na 2 s, 5 s en 15 s.
**Bewijs:** `layout/theme.liquid`, scriptblokken onderaan `<body>`.
**Waarom een probleem?** De bezoeker ziet 5 seconden de verkeerde knoptekst. Het
element dat na 15 seconden verdwijnt veroorzaakt layoutverschuiving die meetelt
in CLS.
**Oplossing:** De betreffende teksten in de bron of via de taalbestanden zetten;
het verbergen via CSS in plaats van een timer.
**Impact:** Middel · **Moeilijkheid:** Gemiddeld · **Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-009
**Onderdeel:** `layout/theme.liquid` — globale click-handler
**Huidige score:** 4/10 · **Ernst:** Middel · **Prioriteit:** P2
**Wat is er mis?** Een document-brede click-listener in de capture-fase die
`stopImmediatePropagation()` aanroept voor qty- en add-to-cart-knoppen.
**Waarom een probleem?** Dit blokkeert handlers van apps en van het thema zelf.
Bij elke nieuwe app is dit de eerste verdachte.
**Oplossing:** Verplaatsen naar de betreffende sectie en binden aan het
component in plaats van aan `document`.
**Impact:** Middel · **Moeilijkheid:** Gemiddeld · **Verwacht:** 7/10

---

**Probleem-ID:** AUDIT-010
**Onderdeel:** `layout/theme.liquid` — return_to-hack
**Huidige score:** 3/10 · **Ernst:** Middel · **Prioriteit:** P2
**Wat is er mis?** `document.querySelector('form')` pakt het **eerste** formulier
op de pagina en zet bij verzenden `return_to` op `/`.
**Waarom een probleem?** Het eerste formulier is meestal zoeken of
taalkeuze. Op inlog- en accountpagina's kan dit bezoekers na inloggen naar de
homepage sturen in plaats van naar hun bestemming.
**Oplossing:** Selector beperken tot het bedoelde formulier.
**Impact:** Middel · **Moeilijkheid:** Eenvoudig · **Verwacht:** 8/10
**Zekerheid:** middel — niet getest, want geen rendering.

---

**Probleem-ID:** AUDIT-011
**Onderdeel:** `pd-product-hero` / `pd-samples` — innerHTML
**Huidige score:** 5/10 · **Ernst:** Laag · **Prioriteit:** P2
**Wat is er mis?** Waarden uit `localStorage` worden met stringplakwerk in
`innerHTML` geschreven.
**Bewijs:** `pd-product-hero:1126`, `pd-samples:198,201`.
**Waarom een probleem?** Defence in depth. **Geen exploiteerbaar lek**: er is
geen route vanuit de URL, geverifieerd.
**Oplossing:** `createElement` + `img.src =` gebruiken.
**Impact:** Laag · **Moeilijkheid:** Eenvoudig · **Verwacht:** 9/10

---

**Probleem-ID:** AUDIT-012
**Onderdeel:** Toegankelijke naam van swatches
**Huidige score:** 5/10 · **Ernst:** Middel · **Prioriteit:** P2
**Wat is er mis?** JS-opgebouwde swatches krijgen `alt=""` en hun naam via
`title`.
**Waarom een probleem?** Schermlezers gaan wisselend met `title` om; de
kleurkeuze kan onhoorbaar blijven.
**Oplossing:** `aria-label` op het lijstitem zetten.
**Impact:** Middel · **Moeilijkheid:** Eenvoudig · **Verwacht:** 9/10

---

**Probleem-ID:** AUDIT-013
**Onderdeel:** RTL-ondersteuning in `theme.liquid`
**Huidige score:** 2/10 · **Ernst:** Laag · **Prioriteit:** P3
**Wat is er mis?** `assign is_rtl = language_support_rtl_list | where: shop_locale`
past `where` toe op een array van strings. `where` filtert objecten op een
eigenschap; op strings levert dit altijd leeg op, dus `is_rtl.size > 0` is nooit
waar en RTL activeert nooit.
**Waarom een probleem?** Een functie die niet werkt. Geen zakelijke impact zolang
je geen RTL-talen verkoopt. Dit is overgenomen uit het Hyper-thema.
**Oplossing:** `if language_support_rtl contains shop_locale`.
**Impact:** Laag · **Moeilijkheid:** Eenvoudig · **Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-014
**Onderdeel:** `snippets/meta-tags.liquid`
**Huidige score:** 6/10 · **Ernst:** Laag · **Prioriteit:** P2
**Wat is er mis?** `<meta property="og:image" content="http:{{ ... }}">` — het
onveilige `http:`-protocol. Verder ontbreken `og:locale` en `og:image:alt`.
**Waarom een probleem?** Sommige scrapers weigeren http-afbeeldingen; dan valt je
deelafbeelding weg op social.
**Oplossing:** `https:` gebruiken en de twee ontbrekende tags toevoegen.
**Impact:** Laag · **Moeilijkheid:** Eenvoudig · **Verwacht:** 9/10

---

**Probleem-ID:** AUDIT-015
**Onderdeel:** Dode configuratie in templates
**Huidige score:** 4/10 · **Ernst:** Laag · **Prioriteit:** P3
**Wat is er mis?** 25 uitgeschakelde secties met volledige instellingen; 7
ongebruikte productvarianten (±243 KB); 2 identieke templateparen;
`collection.doorladen-test.json`; 3 lege/1-byte bestanden.
**Oplossing:** Opruimen na publicatie en een stabiele periode.
**Impact:** Laag · **Moeilijkheid:** Eenvoudig · **Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-016
**Onderdeel:** Collecties zonder eigen tekst
**Huidige score:** 5/10 · **Ernst:** Middel · **Prioriteit:** P2
**Wat is er mis?** Slechts 3 van 16 collecties hebben eigen intro en bodytekst.
`kunst` (4 producten) en `doorlopend-marmer` (3 producten) worden wél vanuit de
bodyteksten gelinkt maar hebben zelf niets.
**Waarom een probleem?** Je linkt autoriteit naar pagina's die geen inhoud hebben
om mee te ranken.
**Oplossing:** Begin met `kunst`, `doorlopend-marmer` en `akupanelen`.
**Impact:** Hoog op termijn · **Moeilijkheid:** Gemiddeld (schrijfwerk)
**Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-017
**Onderdeel:** www-redirect via JavaScript
**Huidige score:** 5/10 · **Ernst:** Laag · **Prioriteit:** P3
**Wat is er mis?** `<script>location.replace(...)</script>` in de `<head>` als
vangnet naast de Shopify-domeinredirect.
**Waarom een probleem?** Een client-side redirect is voor zoekmachines zwakker dan
een 301 en voegt een renderstap toe.
**Oplossing:** Vertrouwen op de 301 in Shopify-domeininstellingen; de canonical
blijft als vangnet. **Raakt domeingedrag — niet zonder jouw toestemming.**
**Impact:** Laag · **Moeilijkheid:** Eenvoudig · **Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-018
**Onderdeel:** Renders zonder bijschrift
**Huidige score:** 4/10 · **Ernst:** Middel · **Prioriteit:** P2
**Wat is er mis?** `pd-vis-*` zijn 3D-renders. Of de pagina ze als impressie
labelt, kan ik niet zien.
**Waarom een probleem?** Zonder label kan een bezoeker ze lezen als foto's van
echte installaties — in strijd met je eigen regel over verzonnen projecten.
**Oplossing:** Zichtbaar bijschrift "3D-impressie" bij elk render.
**Impact:** Middel · **Moeilijkheid:** Eenvoudig · **Verwacht:** 8/10
**Zekerheid:** middel — te bevestigen met een preview.

---

**Probleem-ID:** AUDIT-019
**Onderdeel:** `nl.schema.json` ontbreekt
**Huidige score:** 5/10 · **Ernst:** Laag · **Prioriteit:** P3
**Wat is er mis?** Er zijn schema-vertalingen voor de, en, es, fr, it en vi, maar
niet voor nl. Het Vietnamees zit er wél in.
**Waarom een probleem?** De Theme Editor toont instellingen in het Engels.
**Oplossing:** `nl.schema.json` toevoegen; `vi.*` verwijderen (126 KB).
**Impact:** Laag · **Moeilijkheid:** Gemiddeld · **Verwacht:** 8/10

---

**Probleem-ID:** AUDIT-020
**Onderdeel:** `{% style %}` tussen `</head>` en `<body>`
**Huidige score:** 5/10 · **Ernst:** Laag · **Prioriteit:** P3
**Wat is er mis?** Twee stijlblokken staan buiten zowel `<head>` als `<body>`.
Browsers herstellen dit, maar het is ongeldige HTML.
**Oplossing:** Verplaatsen naar de `<head>` of naar `puredeco-premium.css`.
**Impact:** Laag · **Moeilijkheid:** Eenvoudig · **Verwacht:** 9/10

---

## 16. Prioriteitenmatrix

| | **Hoge impact** | **Lage impact** |
|---|---|---|
| **Eenvoudig** | AUDIT-001, 002, 005, 007 | AUDIT-011, 012, 014, 019, 020 |
| **Complex** | AUDIT-004, 006, 016 | AUDIT-003, 008, 009, 010, 013, 015, 017, 018 |

**Begin linksboven.** Vier ingrepen, elk minder dan een uur werk, die samen een
juridisch risico, een klantbelofte, een verkeerde productlink en een 404 oplossen.

---

## 17. Quick wins

| # | Actie | Tijd | Opbrengst |
|---|---|---|---|
| 1 | Google-score vullen of verwijderen (AUDIT-001) | 10 min | juridisch risico weg |
| 2 | Levertijd op de samplepagina gelijktrekken (AUDIT-002) | 10 min | klantbelofte klopt |
| 3 | Labels 823/824 omwisselen (AUDIT-005) | 5 min | geen verkeerde kleur meer |
| 4 | `preload` op puredeco-premium.css (AUDIT-004, deel 1) | 5 min | sneller eerste beeld |
| 5 | `og:image` naar https (AUDIT-014) | 5 min | deelafbeelding werkt |
| 6 | Dubbele bestanden verwijderen | 5 min | 529 KB |
| 7 | RTL-bug repareren (AUDIT-013) | 5 min | functie werkt |

**Samen ongeveer 45 minuten.**

---

## 18. Strategisch verbeterplan in vier fasen

### FASE 1 — Kritiek, vóór publicatie

| Stap | Actie | Afhankelijkheid |
|---|---|---|
| 1.1 | AUDIT-001: Google-score | geen |
| 1.2 | AUDIT-002: levertijd sample | geen |
| 1.3 | AUDIT-005: labels 823/824 | geen |
| 1.4 | AUDIT-007: ai-visualizer — **jouw besluit nodig, raakt een URL** | jouw akkoord |
| 1.5 | Documenten voor garantie en brandklasse veiligstellen | jouw documenten |
| 1.6 | 100%-gerecycled-claim onderbouwen of nuanceren | jouw documenten |
| 1.7 | AUDIT-003: weesbestanden opruimen na backup-thema | backup eerst |

**Pas daarna is publicatie verantwoord.** En publicatie gebeurt uitsluitend na
jouw expliciete toestemming — zoals afgesproken.

### FASE 2 — High-impact, eerste twee weken na publicatie

| Stap | Actie |
|---|---|
| 2.1 | AUDIT-004: preload + ongebruikte CSS meten met PurgeCSS |
| 2.2 | AUDIT-006: prijzen uit de productdata halen |
| 2.3 | AUDIT-008: setTimeout-patches vervangen |
| 2.4 | AUDIT-016: teksten voor kunst, doorlopend-marmer, akupanelen |
| 2.5 | Producten uit DRAFT halen — dit verhoogt het aantal URL's, de enige echte hefboom op je organische bereik |

### FASE 3 — Premium optimalisatie

| Stap | Actie |
|---|---|
| 3.1 | AUDIT-009 en 010: globale handlers opschonen |
| 3.2 | AUDIT-012 en 011: toegankelijke namen en veilige DOM-opbouw |
| 3.3 | AUDIT-018: bijschriften bij renders |
| 3.4 | Fotografie: één echte installatie fotograferen als tegenwicht voor de renders |
| 3.5 | AUDIT-015: dode configuratie opruimen |

### FASE 4 — Best-in-class

| Stap | Actie |
|---|---|
| 4.1 | Kritieke CSS inline, rest uitgesteld |
| 4.2 | Basisgewicht HTML terugbrengen van 432 KB |
| 4.3 | AUDIT-019 en 020, i18n opschonen |
| 4.4 | Collectieteksten voor alle 16 collecties |
| 4.5 | LocalBusiness-schema voor Studio Herwen |

---

## 19. Top 25 verbeteracties

| # | Actie | Fase | Impact |
|---|---|---|---|
| 1 | Google-score verifiëren of verwijderen | 1 | Hoog |
| 2 | Levertijd samplepagina gelijktrekken | 1 | Hoog |
| 3 | Labels 823/824 omwisselen | 1 | Middel |
| 4 | Brandklasse-certificaat veiligstellen | 1 | Hoog |
| 5 | Garantievoorwaarden vastleggen | 1 | Middel |
| 6 | 100%-gerecycled onderbouwen of nuanceren | 1 | Middel |
| 7 | ai-visualizer oplossen | 1 | Middel |
| 8 | Weesbestanden opruimen | 1 | Middel |
| 9 | preload op puredeco-premium.css | 2 | Hoog |
| 10 | Ongebruikte CSS meten en verwijderen | 2 | Hoog |
| 11 | Prijzen uit productdata | 2 | Hoog |
| 12 | Producten uit DRAFT | 2 | Hoog |
| 13 | Teksten voor 3 collecties | 2 | Hoog |
| 14 | setTimeout-patches vervangen | 2 | Middel |
| 15 | Globale click-handler verplaatsen | 3 | Middel |
| 16 | return_to-selector beperken | 3 | Middel |
| 17 | aria-label op swatches | 3 | Middel |
| 18 | createElement in plaats van innerHTML | 3 | Laag |
| 19 | Bijschriften bij renders | 3 | Middel |
| 20 | Eén echte installatiefoto | 3 | Middel |
| 21 | Dode configuratie opruimen | 3 | Laag |
| 22 | og:image naar https | 2 | Laag |
| 23 | RTL-bug repareren | 4 | Laag |
| 24 | nl.schema.json toevoegen, vi verwijderen | 4 | Laag |
| 25 | LocalBusiness-schema Studio Herwen | 4 | Middel |

---

## 20. Verwachte resultaten en onzekerheden

**Wat ik met redelijke zekerheid durf te zeggen:**

- Publicatie lost de H1-afwezigheid op alle 16 collectiepagina's op en de dubbele
  H1 op productpagina's. Dat is af te lezen uit de code, geen voorspelling.
- Je krijgt CollectionPage-, ItemList-, FAQPage- en BreadcrumbList-markup waar nu
  niets staat. Dat maakt je in aanmerking komend voor rich results. **Of Google ze
  toont, bepaalt Google.**
- De homepage krijgt een echte title in plaats van `PureDeco`.

**Wat ik niet durf te kwantificeren:**

- Hoeveel organisch verkeer dit oplevert. Iedereen die daar een percentage op
  plakt, verzint het. Je hebt 79 URL's in de sitemap; dát is de begrenzing, niet
  de opmaak.
- Of de conversie stijgt. Dat hangt af van hoe het thema er werkelijk uitziet, en
  dat heb ik niet kunnen zien.
- Of de snelheid verbetert of verslechtert. H1-Kopie voegt 253 KB CSS toe maar
  schakelt veel secties uit. Netto onbekend zonder meting.

**Wat ik expliciet níét heb vastgesteld:** of H1-Kopie überhaupt foutloos rendert.
Dat is geen detail. Een thema dat 123 secties bevat waarvan er op de
hoofdtemplates maar vier actief zijn, kan prima werken — maar ik heb het niet
kunnen zien draaien.

---

## 21. Eindconclusie

H1-Kopie is beter dan het live thema op precies de punten waar het telt voor
vindbaarheid, en de kwaliteit van het inhoudelijke werk is hoog. De teksten zijn
eerlijk waar de meeste webshops overdrijven. De reviewcode doet het principieel
goed. Er zit een claimverbodslijst in de broncode. Dat zijn tekenen van vakwerk.

Daaronder zit slordigheid die niet bij dat niveau past: 105 MB weesbestanden, een
verwisseld kleurlabel, twee verschillende levertijden op dezelfde pagina, en een
reviewscore die uit een standaardwaarde komt in plaats van uit data.

**Mijn advies: publiceer dit thema niet voordat fase 1 is afgerond.** Niet vanwege
de techniek — die is werkbaar — maar vanwege AUDIT-001 en AUDIT-002. Dat zijn
geen schoonheidsfoutjes; het zijn uitspraken richting klanten en toezichthouder.

En ik kan geen enkel oordeel geven over hoe dit thema er werkelijk uitziet of
werkt. **Daarvoor heb ik een deelbare previewlink nodig.** Met die link lever ik
het tweede deel: visueel ontwerp, UX, conversie, mobiel, toegankelijkheid in de
praktijk, functionele tests en echte Core Web Vitals.

---

## Bijlage — methodeverantwoording

| Bewering | Hoe vastgesteld |
|---|---|
| 575 bestanden | Volledige paginering van `theme.files` |
| 105,5 MB weesbestanden | `grep` op `pdtmp-` over 30 pd-bestanden + alle templates + settings_data |
| CDN levert WebP | `curl` met Accept-header, content-type en lengte gemeten |
| 79 URL's in sitemap | Elke sub-sitemap opgehaald en `<loc>` geteld |
| 0 H1 op collecties | `grep -o '<h1'` op de live HTML |
| Alle 35 links resolveren | Handles vergeleken met `products`, `collections`, `pages` uit de Admin API |
| ai-visualizer 404 | `curl`, HTTP 404; bestand in beide thema's afwezig |
| Geen reflected XSS | Keten `URLSearchParams` → gebruik handmatig nagelopen |
| Renders, geen foto's | Visuele beoordeling van 2 gedownloade bestanden |
| 4,9 is een default | Schemaregel 810 + `grep` op settings_data: 0 treffers |

**Niet gedaan:** geen enkele schrijfactie, geen destructieve test, geen
betaling, geen wijziging aan thema, winkel, advertenties of tracking.
