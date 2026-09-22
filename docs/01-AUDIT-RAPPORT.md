# PUREDECO.NL — GEÏNTEGREERD AUDIT- & REDESIGNVOORSTEL
**Datum:** 22 september 2026
**Scope:** Luxury / B2B / Shopify transformatie
**Status:** Fase 1 (analyse) afgerond — **geen enkele wijziging doorgevoerd**

---

## 0. VEILIGHEIDSVERANTWOORDING (STAP 1 T/M 5)

| | |
|---|---|
| **LIVE THEME** | Hyper |
| **LIVE THEME ID** | `188874326282` |
| **LIVE STATUS** | **PUBLISHED** (role: MAIN) |
| **Theme Store ID** | 3247 (Hyper) |
| **Laatst gewijzigd** | 2026-09-22 09:13 UTC |
| **DEVELOPMENT THEME** | PUREDECO — LUXURY B2B — DEVELOPMENT |
| **DEVELOPMENT THEME ID** | `194359853322` |
| **DEVELOPMENT STATUS** | **UNPUBLISHED** |
| **Preview-prefix** | `/t/7` |

**Integriteitscontrole (MD5, live vs. development) — alle bestanden identiek:**

| Bestand | MD5 | Status |
|---|---|---|
| `config/settings_data.json` | `bc9202efeafe5de71c2520a01b0e4a87` | ✅ |
| `config/settings_schema.json` | `d4fb5af16eeffc621c53db4d0ada3008` | ✅ |
| `layout/theme.liquid` | `327b40b2517ecaaa37bff2f595649a74` | ✅ |
| `templates/index.json` | `c95cd40c7aa5f999a54f62abfb4b1aab` | ✅ |
| `templates/product.json` | `4d2b64800a7a5996a8c2cce4bb4a89e2` | ✅ |
| `templates/collection.json` | `b50fd8e70bc60d887789828e4d9f472e` | ✅ |
| `templates/robots.txt.liquid` | `79fe39ff3f6c96eb3ef97395ad254787` | ✅ |

**Bevestiging:** het live theme is vanaf nu **READ ONLY**. Er is geen automatische deployment naar productie geconfigureerd. Publicatie gebeurt uitsluitend na expliciete toestemming. Aanvullend blokkeert de gebruikte Shopify-koppeling technisch zowel theme-publicatie, theme-verwijdering als schrijfacties naar het MAIN theme.

**Overige aanwezige themes (niet aangeraakt):** Horizon (188848374026), Copy of theme (Save purpose) (189441605898), Copy of Hyper (190879269130), Faruk FAQ pagina wijziging (194018902282), Kopie van Hyper (194090926346).

### Beperking van deze audit — belangrijk
Uitgaand netwerkverkeer naar `puredeco.nl` is in deze omgeving geblokkeerd door de netwerkpolicy. De audit is daarom uitgevoerd op de **bron**: de volledige theme-code, alle templates, theme-instellingen, en de catalogus/content via de Shopify Admin API. Dat is een sterker uitgangspunt dan een renderende pagina voor code-, SEO- en architectuurbevindingen.

**Wat hierdoor nog in de browser geverifieerd moet worden** (opgenomen als taak in de roadmap):
- werkelijk geleverde bytes en Core Web Vitals (LCP/CLS/INP) via PageSpeed Insights / CrUX;
- visuele QA en hover/focus-states;
- rendering van structured data via de Rich Results Test;
- exacte werking van app-geïnjecteerde code (Judge.me, Samita, BookEasy, Instafeed).

---

## A. CURRENT BRAND PERCEPTION

PureDeco presenteert zich digitaal vandaag als **een goed draaiende, prijsgedreven Nederlandse webshop in bamboe-wandpanelen** — niet als materialenmerk.

Dat is geen indruk maar een optelsom van concrete signalen in de code:

| Signaal | Vindplaats |
|---|---|
| Eerste item in het hoofdmenu is **"ACTIE"** | menu `main-menu-1` |
| Twee losse kortingscollecties: "ACTIE" (8) én "Sale" (9) | collections |
| Nieuwsbrief-CTA boven de footer: *"Meld je aan en ontvang 5% korting op je eerste bestelling."* | `footer-group.json` |
| Eerste USP direct onder de hero: *"Betaal flexibel met Klarna"* | `index.json` sectie 2 |
| Klarna-vermelding óók in de topbar én op de PDP | `header-group.json`, `product.json` |
| Sale-prijs in rood `#c4301c` + sale-badges op productkaarten | `settings_data.json` |
| `compareAtPrice` structureel gevuld (119,95 van 149,95 / 89,95 van 124,95 / 139,95 van 169,95) | catalogus |
| Cart-drawer: *"✌🏼 GRATIS VERZENDING BOVEN €600!"* (caps + emoji) | `overlay-group.json` |
| Marquee/lopende band met USP's op collectiepagina's | `collection.json` sectie 10 |
| Twinkelende ster-animatie op menu-item "wandpanelen" (`star_twinkle`) | `header-group.json` |
| Emoji als iconen in de footer (📞 ✉️ 📍) | `footer-group.json` |

**Conclusie:** het merk communiceert *prijs, snelheid en actie*. Een interieurarchitect of hotelier die deze site opent, ziet geen merk dat hij kan specificeren — hij ziet een consumentenwebshop met aanbiedingen.

---

## B. WAT MAAKT PUREDECO NU MINDER PREMIUM

### B1. De homepage heeft geen kop — de merkbelofte staat ín een plaatje
De hero-slide op de homepage heeft `title: ""`, `subheading: ""` en `description: ""`. De volledige boodschap zit gebakken in een afbeelding: `ChatGPT_Image_8_sep_2026_11_25_14.png`.

Gevolgen:
- **Geen `<h1>` op de homepage** (bevestigd in code: `sections/slideshow.liquid` regel 231 rendert `<h2>`, nooit `<h1>`);
- de belofte is **niet leesbaar voor screenreaders** en niet vertaalbaar;
- de LCP-afbeelding heeft **`alt=""`**;
- de tekst schaalt niet mee op mobiel.

### B2. De beeldtaal is AI-gegenereerd
Minimaal 20 sleutelbeelden zijn ChatGPT-afbeeldingen, herkenbaar aan de bestandsnaam. Desktop-hero 2,08 MB PNG (1983×793), mobiel-hero 2,10 MB PNG (941×1671). Andere voorbeelden: 5,88 MB, 5,28 MB, 3,33 MB. Nog op **22 september 2026** zijn drie nieuwe PNG's van 2,7–3,3 MB geüpload.

Voor een merk dat "architecturaal materialenmerk" wil zijn, is dit het zwaarwegendste probleem: **er is geen bewijs van echte materialen in echte ruimtes.** Een interieurarchitect herkent AI-beeld direct en leest het als "dit bedrijf heeft geen projecten".

### B3. Het thema is nog zichtbaar een demo-thema
Restanten van de originele demo ("Gara"/meubelwinkel) staan nog in de live templates:

- `collection.json`: collectieblokken **"Spoke Sofa", "Turn Chairs", "Curve Coat", "Bend Chairs", "Press Tables", "Lighting", "Cross Tables", "Bar Chairs"**; zoekknoppen "Living Room, Planters, Gravel Rug, Table Mirror, Ray Table Lamp"; kaart *"Saving $30 for Lighting"*.
- `overlay-group.json`: **"Save an extra 10%", promocode "GARA10", "Select lamp from $170", "Free Delivery on all major appliances $500+"**, teaser "Special Offers For You".
- `product.json`: sectie getiteld **"Online sportvoeding & supplementen winkel"** met kaarten *"De grootste in sportvoeding"* en *"Voor sporters, door sporters"*.
- `index.json`: dezelfde kaart *"Voor sporters, door sporters"*; badge-tekst **"garace - where design meet function -"** (met typefouten); badge **"Save 99$"**.
- `index.json`: twee `featured-collection`-secties met placeholder-instellingen `heading: "Collections"` en `button_label: "Button label"`.

Deze blokken staan grotendeels op `disabled`, maar ze staan wél in het live theme en tonen dat de site nooit is opgeschoond.

### B4. Typografie zonder hiërarchie
`type_header_font` en `type_body_font` zijn **beide `instrument_sans_n5`** — dezelfde letter voor koppen en broodtekst. Er is dus geen typografisch contrast. Daarbovenop:

- `buttons_font_weight: 700`, `navigation_font_weight: 700`, `subheading_font_weight: 700` — alles vet;
- losse secties overrulen het schaalsysteem met harde px-waarden en `heading_weight: 800` (`feature-cards-with-icons`, `contact-help-section`);
- `buttons_transform: capitalize` → Nederlandse knoppen worden *"Bekijk De Collectie"* in plaats van *"Bekijk de collectie"*;
- `heading_mobile_scale: 70` → koppen krimpen naar 70% op mobiel, wat de hero-impact op het belangrijkste kanaal wegneemt.

Luxe ontstaat uit ruimte, contrast en rust — niet uit gewicht. Nu is het omgekeerde ingesteld.

### B5. Twee botsende knopsystemen tegelijk live
| Systeem | Radius | Kleur | Waar gedefinieerd |
|---|---|---|---|
| Thema-knoppen | `square` → **0 px** | scheme-afhankelijk | `settings_data.json` + `css-variables.liquid` |
| `.pd-btn` | **999 px (pil)** | `#55884d` hardcoded | inline `{% style %}` in `layout/theme.liquid` |

Daarnaast vier verschillende radii door elkaar: `inputs_corner_radius: round`, `badges_corner_radius: round`, `blocks_corner_radius: slightly`, `pcard_corner_radius: slightly`. Er is geen radius-systeem.

### B6. Kleursysteem is een demo-palet
16 color schemes, waarvan het merendeel ongewijzigde demo-kleuren: roze `#f5e2e2`, lavendel `#dbe1ff`, mint `#e0efe4`, limoen `#f4f691`, rood `#c4301c`, geel `#ffe093`, crème `#f9f2df`, petrol `#072835`. In **elk** schema staat `primary_accent: #c4301c` — een demo-rood dat niets met PureDeco te maken heeft.

### B7. Tegenstrijdige beloftes
| Belofte | Waarde | Vindplaats |
|---|---|---|
| Gratis verzending | **€ 600** | topbar, cart-drawer, PDP, `free_shipping_minimum_amount` |
| Gratis verzending | **€ 500** | quick-view `icon-with-text` |
| Levertijd | 3–6 werkdagen | USP-balk, PDP, quick-view |
| Levertijd | "Voor 12:00 besteld, vandaag verzonden" | `delivery_text` in theme-instellingen |
| Beoordeling | **9,4 / 10** | topbar |
| Beoordeling | **4,9 / 5 (Google Reviews)** | collectiebeschrijving `wandpanelen` |

Voor B2C is dit verwarrend; voor B2B is het diskwalificerend.

---

## C. LUXURY DESIGN AUDIT

| Onderdeel | Bevinding | Prio |
|---|---|---|
| Hero | Geen tekst, geen H1, AI-beeld, `alt=""`, PNG-bron 2,08 MB | **P0** |
| Kleur | 16 demo-schema's, geen merkpalet, demo-accent `#c4301c` overal | **P1** |
| Kleur | `scheme-inverse` is **kapot**: `text #ffffff` op `background #f7f7f7` (**1,07:1**) | **P0** |
| Kleur | `scheme-9069f5b2…`: `text #000000` op `background #000000` | **P0** |
| Typografie | Eén font voor kop én tekst; overal weight 700/800 | **P1** |
| Knoppen | Twee systemen (0 px vs. 999 px), geen hiërarchie | **P1** |
| Motion | `star_twinkle` op nav-item; marquee-banden; parallax beschikbaar | **P2** |
| Ruimte | `page_width: 1520`; secties met harde px-padding per sectie | **P2** |
| Logo | `logo_width: 400` px desktop — zeer groot voor een premium merk | **P3** |
| Iconografie | Emoji in footer; losse SVG's zonder consistente stijl | **P2** |

**Belangrijkste vondst:** het kapotte `scheme-inverse` is vermoedelijk de **oorzaak** van de tekstloze hero. De hero gebruikt `color_scheme: "scheme-inverse"`; daarin is de tekstkleur wit en de achtergrond bijna wit. Elke ingevoerde kop zou onzichtbaar zijn geweest. De tekst is toen in het beeld gezet. Eén kapotte tokenwaarde heeft zo de belangrijkste SEO- en merkboodschap van de site uitgeschakeld.

---

## D. B2B GAP ANALYSIS

### Wat er al is (en meer waard is dan het nu oplevert)
- **Samita Wholesale** (app) met `samitaWS.MSRP`-metafield en volume-prijzen;
- theme-secties `wholse-seller.liquid`, `verkooppartner-section.liquid`, `quick-order-list.liquid`, `product-samples-selector.liquid`, `showroom-partner.liquid`, `multi-step-advice-form.liquid`;
- een **Product Samples**-app op PDP en collectiepagina;
- een showroom + afspraakmodule (BookEasy);
- productmetafields voor `materiaal_en_description`, `duurzaamheid_description`, `montage_hand_description`.

De bouwstenen bestaan dus al. Ze zijn alleen niet tot propositie gemaakt.

### De kloof

**1. B2B bestaat niet op desktop.**
Het desktop-hoofdmenu (`main-menu-1`) bevat: ACTIE · Wandpanelen · Akupanelen · Accessoires · FAQ. **Geen enkele B2B-ingang.** "Zakelijk" bestaat alleen in de footer en in het mobiele menu. Een interieurarchitect op desktop heeft geen pad.

**2. De B2B-landingspagina is een formulier.**
`/pages/form` — paginatitel letterlijk **"form"**. Template `page.btbcta.json` bevat: een slide "PureDeco Pro-partner", een 3-staps uitleg "Ik wil mijn bedrijf registreren, hoe werkt dat?", een rich-text "Meld je aan als zakelijke klant" en het Samita-registratieblok. Het contactformulier met KvK-veld staat op `disabled`.

Er staat **geen** propositie op: geen sectoren, geen projecten, geen technische documentatie, geen levertijden, geen projectbegeleiding, geen materiaalbibliotheek, geen contactpersoon.

**3. `main-page` is uitgeschakeld op deze template** → de B2B-pagina heeft **geen `<h1>`**.

**4. Er is geen projectlaag.** Er zijn **nul metaobject-definities** voor projecten of cases. Er is geen enkele projectpagina. Het bewijs dat B2B-kopers nodig hebben, bestaat niet.

**5. Geen sectorpagina's.** Hotels, horeca, interieurarchitecten, chaletbouw, standbouw, aannemers: nul pagina's.

**6. Geen specificatielaag.** Geen metafields voor brandklasse, toepassingsgebied, levertijd per project, downloads, technische tekeningen. `sku` is op vrijwel alle varianten **leeg** — een architect kan niets specificeren zonder artikelnummer.

**7. Een `myshopify.com`-link op de B2B-pagina.**
`page.btbcta.json` bevat `https://puredeco-3.myshopify.com/customer_authentication/redirect?locale=nl`. Op precies de pagina waar een professional inlogt, springt hij naar het interne Shopify-domein.

---

## E. UX AUDIT

### Navigatie — de zwaarste bevindingen

| # | Bevinding | Prio |
|---|---|---|
| E1 | **"Wandpanelen" in het hoofdmenu linkt naar `/collections/bamboepanelen-samples`** terwijl de collectie `/collections/wandpanelen` (31 producten) apart bestaat. De primaire categorie-ingang wijst naar de verkeerde pagina. | **P0** |
| E2 | Eerste menu-item is **"ACTIE"** | **P1** |
| E3 | Menu-items met **voorloopspatie**: `" Accessoires"`, `" FAQ"` | **P2** |
| E4 | **Typefout in een live URL**: `/pages/verkoopparters` (moet "verkooppartners" zijn) — óók de paginatitel "Verkoopparters" | **P1** |
| E5 | Typefout in mobiel menu: **"Zakelijik"** | **P2** |
| E6 | Desktop- (5 items) en mobiel menu (9 items) zijn **verschillend**; mobiel heeft méér | **P1** |
| E7 | Menu "Inspiratie": het item *"5 Creatieve toepassingen van bamboepanelen"* linkt naar **het onderhoudsartikel** (`…tips-voor-het-onderhouden…-1`) | **P1** |
| E8 | **Geen submenu's, geen mega-menu.** Materiaal/decor-navigatie bestaat niet. | **P1** |
| E9 | Footer bevat `<a>info@puredeco.nl</a>` — **anchor zonder `href`** | **P2** |
| E10 | Footer-blok "Inspiratie" staat op `disabled` | **P2** |
| E11 | Geen juridisch menu onderin (`footer_bottom_menu: ""`) | **P1** |
| E12 | Topbar toont social-iconen voor Twitter en TikTok terwijl `social_twitter_link` en `social_tiktok_link` **leeg** zijn | **P2** |

### Collectiepagina
- `breadcrumbs`: **disabled** → geen kruimelpad, geen BreadcrumbList;
- `main-collection-banner`: **disabled** → geen collectie-hero, geen sfeerbeeld, en (zie G) geen H1;
- de pagina opent met een rich-text-kop en gaat direct naar het productraster;
- onderaan een marquee met USP's, waarvan één tekstblok **leeg** is.

### Productpagina
- productbeschrijving staat in tab 1 ("Productbeschrijving", `{{ product.description }}`) — correct opgehaald, maar achter een klik;
- de tabs 2–4 tonen netjes de metafields (materiaal, duurzaamheid, montage);
- `collapsible_tab "Materiaal en onderhoud"` staat op `disabled` en dupliceert tab 2;
- vier `custom_liquid`-blokken met hardgecodeerde HTML/SVG/JS in de productinformatie;
- twee concurrerende sample-mechanismen: een uitgeschakelde eigen knop *"Gratis Sample (0€)"* en het Product Samples-appblok;
- **geen B2B-ingang**: geen projectofferte, geen technische downloads, geen toepassingsgebieden, geen levertijd-op-project.

---

## F. CRO AUDIT

| # | Bevinding | Impact | Prio |
|---|---|---|---|
| F1 | **Hoofdmenu-item "Wandpanelen" leidt naar de samples-collectie** — elke bezoeker die het assortiment wil zien, komt op de verkeerde pagina | Direct omzetverlies op de belangrijkste navigatieklik | **P0** |
| F2 | `alert('yes')` in productie (zie J1) — onderbreekt formulierverzending met een browser-popup | Formulier-conversie | **P0** |
| F3 | Levertijd-fallback zegt **"Op voorraad. Binnen 3-6 werkdagen in huis"** ongeacht werkelijke voorraad | Misleidend; retour- en klachtenrisico | **P0** |
| F4 | Product *Wandpaneel Japandi 619 Jade* heeft voorraad **−22** | Overselling | **P1** |
| F5 | *Wandpaneel Japandi 620 Light Brown* toont **de foto van 619 Jade**, inclusief de alt-tekst van 619 | Verkeerd product getoond; Merchant Center-risico | **P0** |
| F6 | Drie verschillende gratis-verzendgrenzen en twee verschillende reviewscores | Vertrouwen | **P1** |
| F7 | Knoplabels in `capitalize` → "Bekijk De Collectie" | Waargenomen kwaliteit | **P2** |
| F8 | Alle `a.pd-btn.pd-btn-primary` worden via JS gekaapt: `preventDefault()` + klik op de BookEasy-knop. Elke primaire PureDeco-knop opent dus de afsprakenmodule in plaats van te navigeren | Potentieel ernstig — verifiëren in browser | **P0** |
| F9 | Geen B2B-conversiepad (sample → technisch → offerte) | B2B-lead-conversie | **P1** |

---

## G. SEO RISK AUDIT

### G1. Systematisch ontbrekende H1's — bevestigd in code

| Paginatype | H1 aanwezig? | Bewijs |
|---|---|---|
| **Homepage** | ❌ **Nee** | `slideshow.liquid:231` rendert `<h2>`; geen enkele homepagesectie rendert `<h1>` |
| **Collectiepagina** | ❌ **Nee** | `main-collection-banner` (die wél een `heading_tag`-instelling met default `h1` heeft) staat **disabled**; de vervanger `rich-text.liquid` rendert hardcoded `<h2>` |
| **B2B-pagina `/pages/form`** | ❌ **Nee** | `main-page` (die `<h1>` rendert) staat disabled |
| **Productpagina** | ⚠️ **Dubbel** | `product-information-blocks.liquid` rendert het producttitel-blok zowel als `<h1>` **én** als `<h2>` in een link naar zichzelf |

Dit raakt exact de pagina's waar PureDeco op wil ranken: "wandpanelen", "naadloze wandpanelen", "japandi wandpanelen", "betonlook wandpanelen".

### G2. De materiaalcollecties krijgen geen interne links
De homepage-slider "Breed assortiment wandpanelen" linkt naar **filter-URL's**:
```
https://puredeco.nl/collections/all?filter.p.m.custom.tag_filter=Hout
https://puredeco.nl/collections/all?filter.p.m.custom.tag_filter=Japandi
https://puredeco.nl/collections/all?filter.p.m.custom.tag_filter=Leer
https://puredeco.nl/collections/all?filter.p.m.custom.tag_filter=Marmer
```
Terwijl de **echte, indexeerbare collecties bestaan**: `/collections/hout-1`, `/collections/japandi`, `/collections/leer`, `/collections/doorlopend-marmer`, `/collections/kunst`, `/collections/8mm-naadloos`.

Gefacetteerde URL's worden door Shopify gecanonicaliseerd naar de bovenliggende collectie. De interne linkwaarde van de homepage gaat dus naar pagina's die niet kunnen ranken, terwijl de pagina's die wél kunnen ranken geen enkele prominente interne link krijgen. **Dit is de grootste onbenutte SEO-kans op de site.**

### G3. Keyword-kannibalisatie op het kernwoord
| Collectie | Titel | Producten |
|---|---|---|
| `/collections/wandpanelen` | "Wandpanelen kopen \| Naadloos & Bamboekern \| Puredeco" | 31 |
| `/collections/bamboepanelen-samples` | "Bamboepanelen" | 46 |

Twee concurrerende hoofdcategoriepagina's. Het hoofdmenu linkt naar de tweede, de footer naar de eerste.

Daarnaast **"Akupanelen" twee keer**: `/collections/akupanelen` (2 producten, in het menu) en `/collections/akupanelen-samples` (6 producten, rijkere content, niet in het menu).

En twee kortingscollecties: `ACTIE` (8) en `Sale` (9).

### G4. Titels zijn meta-titels geworden
De **collectietitel** — die als on-page kop wordt gebruikt — is letterlijk `Wandpanelen kopen | Naadloos & Bamboekern | Puredeco`. Ook een producttitel: `Wandpaneel Concrete Smoke 691 | Betonlook | Puredeco`. Pipes en merknaam in een zichtbare kop is precies het signaal dat een premium merk niet uitstraalt — en het dupliceert het aparte SEO-titelveld.

### G5. Metadata grotendeels leeg
- **14 van de 16 collecties** hebben geen SEO-titel en geen meta-description;
- van de eerste ~50 producten hebben er **3** een ingevulde SEO-titel/description;
- `productType` is **leeg op alle producten**;
- `sku` is leeg op vrijwel alle varianten.

### G6. Geen breadcrumb-structured-data
`sections/breadcrumbs.liquid` bevat alleen `aria-label="breadcrumbs"` — **geen `BreadcrumbList`**. Plus: breadcrumbs staan uit op collectiepagina's.

### G7. Product-structured-data
`main-product.liquid` gebruikt `{{ product | structured_data }}`. Judge.me injecteert daarnaast eigen review-schema. **Te verifiëren in de Rich Results Test:** of er dubbele `Product`-entiteiten ontstaan en of `aggregateRating` correct koppelt.

### G8. Lege collectie live
`/collections/samples` bevat **0 producten**.

### G9. Wat beschermd moet blijven
- **30 redirects** (grotendeels van een WordPress/WooCommerce-migratie: `/product/*`, `/category/*`, `/product-tag/*`) — **niet verwijderen**;
- alle bestaande collection-, product- en page-handles;
- `templates/robots.txt.liquid` (voegt alleen Facebook-crawlers toe — ongevaarlijk, laten staan);
- canonical-tag in `layout/theme.liquid` (correct: `{{ canonical_url }}`);
- markt **België is actief** (zelfde domein, geen aparte webpresence) — geen hreflang-risico, wel meenemen in tests.

> **Uitgangspunt voor fase 2: geen enkele bestaande URL wordt gewijzigd zonder uw expliciete toestemming.** Dat geldt óók voor de typefout `/pages/verkoopparters`: die corrigeren we alléén mét redirect én mét uw akkoord.

---

## H. PERFORMANCE AUDIT

### Broncodegewicht (ongecomprimeerd)
| Asset | Grootte | Laadwijze |
|---|---|---|
| `theme.css` | **192 KB** | preload in `<head>` |
| `vendor.css` | 12 KB | preload in `<head>` |
| `vendor.js` | **230 KB** | `defer`, elke pagina |
| `theme.js` | **99 KB** | `defer`, elke pagina |
| `photoswipe.js` | 91 KB | conditioneel |
| `section-main-product.css` | 22 KB | PDP |

≈ **204 KB CSS render-blocking** en **329 KB JS op elke pagina**, vóór apps.

### Apps met eigen JS
Judge.me · Product Samples · Samita Wholesale · Instafeed · BookEasy (bookx) · Google & YouTube-kanaal · Facebook & Instagram-kanaal · Bol.com-koppeling.

### Beeldmateriaal
Bron-PNG's van 1,5–5,9 MB voor sfeer- en hero-beelden. Shopify's CDN transcodeert weliswaar naar WebP via `image_url`, maar een fotografische PNG-master transcodeert aanzienlijk minder efficiënt dan een correct voorbereide master. *Te meten in de browser.*

### Concrete performance-bug
`snippets/product-information-blocks.liquid`, blok `sibling_product`:
```liquid
<img style="width:30px;height:30px;" src="{{ sibling_ref.featured_image | img_url: 'master' }}">
```
Voor elke kleurvariant wordt de **volledige master-afbeelding** (tot 2048×2048, vaak 1–2 MB) geladen en met CSS naar **30×30 px** geschaald. Op een product met vijf siblings zijn dat vijf master-images voor vijf swatches. **P0 performance.**

### Overig
- negen losse inline `<script>`-blokken in `layout/theme.liquid` op elke pagina;
- drie `setTimeout`-hacks die de UI ná 2 s, 5 s en **15 s** aanpassen (zie J);
- `parallax` en `motion-element` door het hele thema.

---

## I. ACCESSIBILITY AUDIT

| # | Bevinding | WCAG | Prio |
|---|---|---|---|
| I1 | `scheme-inverse`: tekst `#ffffff` op achtergrond `#f7f7f7` = **1,07:1** | 1.4.3 (min. 4,5:1) | **P0** |
| I2 | `scheme-9069f5b2…`: `#000000` op `#000000` = **1,00:1** | 1.4.3 | **P0** |
| I3 | `scheme-11`: subtext `#516971` op `#000000` = **3,61:1** | 1.4.3 | **P1** |
| I4 | LCP-hero heeft **`alt=""`** en bevat de enige merkboodschap als tekst in het beeld | 1.1.1 | **P0** |
| I5 | **Geen H1** op home, collectie en B2B-pagina; dubbele titel (H1+H2) op PDP | 1.3.1, 2.4.6 | **P0** |
| I6 | Emoji als functionele iconen in de footer (screenreader leest "telephone receiver") | 1.1.1 | **P2** |
| I7 | `<a>info@puredeco.nl</a>` zonder `href` — niet focusbaar | 2.1.1 | **P2** |
| I8 | Primaire links worden via JS `preventDefault()` gekaapt en openen een widget | 2.1.1, 3.2 | **P1** |
| I9 | Alt-teksten `"Team member 1/2/3"` op de contactsectie | 1.1.1 | **P2** |
| I10 | `menu_trigger: hover` voor het hoofdmenu | 2.1.1 | **P2** |
| I11 | Alt-tekst van product 620 beschrijft product 619 | 1.1.1 | **P1** |

**Positief:** het thema heeft een correcte skip-link, `aria-label`s op modals, `role="status"` op prijs/voorraad en een `visually-hidden`-patroon. De basis is goed; de fouten zitten in de configuratie en de maatwerkcode.

---

## J. SHOPIFY CODE AUDIT

### J1. `alert('yes')` staat live in productie — **P0**
`layout/theme.liquid`:
```js
document.addEventListener('DOMContentLoaded', function() {
  var form = document.querySelector('form');
  form.addEventListener('submit', function() {
    alert('yes');
    document.querySelector('input[name="return_to"]').value = '/';
  });
});
```
Debugcode die op **elke pagina** het eerste formulier pakt en bij verzending een browser-popup `yes` toont. Daarna volgt een `querySelector` die op de meeste formulieren `null` is en een exception gooit. Dit moet direct weg.

### J2. Twee JS-fouten op elke pagina — **P0**
```js
document.querySelector("button.booking_cta").addEventListener("click", …)
document.querySelector(".booking_cta a").addEventListener("click", …)
```
Beide zonder null-check. Op elke pagina zonder die elementen — dus vrijwel alle — gooien deze twee scriptblokken een `TypeError`.

### J3. Drie `setTimeout`-UI-hacks — **P1**
| Vertraging | Effect |
|---|---|
| 2 000 ms | Pre-order-knoptekst wordt pas ná 2 s "Houd mij op de hoogte" |
| 5 000 ms | Formulierknop wordt pas ná 5 s "Verzenden" |
| **15 000 ms** | Volume-prijstabel op productkaarten wordt pas ná **15 seconden** verborgen |

De gebruiker ziet dus 15 seconden lang een element dat verborgen hoort te zijn. Dit hoort in CSS/Liquid, niet in een timer.

### J4. Hardcoded `myshopify.com`-URL's in live templates — **P0**
| Bestand | URL |
|---|---|
| `templates/page.btbcta.json` | `https://puredeco-3.myshopify.com/customer_authentication/redirect?locale=nl` |
| `templates/product.json` | `https://puredeco-3.myshopify.com/faqs` |

De tweede wijst bovendien naar `/faqs` in plaats van `/pages/faqs` → **dode link op elke productpagina**, naar een ander domein.

### J5. Klant-e-mailadres in de browserconsole — **P0 (AVG)**
`snippets/samita-custom.liquid`, regel 1:
```liquid
console.log({{ customer.email | json }});
```
Van elke ingelogde klant wordt het e-mailadres naar de console geschreven — leesbaar voor elk third-party script op de pagina. Dit is een privacylek en moet weg.

### J6. Altijd-ware conditie — **P1**
`snippets/product-information-blocks.liquid`:
```liquid
{% if inventory_quantity == 0 or inventory_quantity > 0 %}is-soldout{% endif %}
```
Dit is `>= 0` en dus waar voor praktisch elk product. De klasse `is-soldout` staat daardoor op vrijwel elke productpagina.

### J7. Dubbele producttitel — **P1**
```liquid
<h1 class="product__title …">{{ product.title | escape }}</h1>
<a href="{{ product.url }}" class="product__title">
  <h2 class="h1">{{ product.title | escape }}</h2>
</a>
```
De titel staat twee keer in de DOM, de tweede als link naar de pagina zelf.

### J8. Logica op vertaalde strings en harde collectietitels — **P1**
```liquid
{% if inventory_message == 'Niet op voorraad' %}      → breekt bij taalwissel
{% if product.collections.first.title == 'Akupanelen' %}  → 'Akupanelen' bestaat 2×; .first is niet-deterministisch
{% for c in product.collections %}{% if c.title == 'Akupanelen' %}
```

### J9. Businesscontent hardcoded in een generieke theme-sectie — **P1**
`sections/image-with-text.liquid` bevat een volledig meerstapsformulier met vaste Nederlandse koppen: *"Gratis interieuradvies op maat"*, *"Jouw gegevens"*, *"Vertel ons over je ruimte"*, *"Jouw stijl & voorkeuren"*, *"Bedankt!"*. Niet configureerbaar, niet vertaalbaar, en verdwijnt bij elke theme-update.

### J10. Niet-vertaalde en foutieve teksten
- `cart_empty_message`: *"Not sure where to start? Try these collections:"* (Engels op een NL-shop);
- `cart_recommendations_heading`: *"Pair Well With"* (Engels);
- knoplabel *"Gratis Sample (0€)"* — onjuiste Nederlandse valutanotatie;
- popup met **"Bouwvaksluiting – gesloten van 23 juli t/m 12 augustus"** staat nog in het theme (wel `disabled`).

### J11. Architectuur — positief
Het thema heeft een **volwaardig CSS-variabelen-tokensysteem** (`snippets/css-variables.liquid`): `--font-body-*`, `--font-heading-*`, `--font-button-*`, radius-tokens afgeleid uit theme-instellingen, en color schemes. **Dat is belangrijk goed nieuws:** een groot deel van het premium-redesign kan via tokens en instellingen, zonder de CSS te herschrijven. Dit verlaagt risico én doorlooptijd aanzienlijk.

### J12. Overige observaties
- `locales/nl.json` bestaat, maar de theme-default is `en.default.json`; `de` en `en` zijn **niet gepubliceerd** terwijl header én footer een taalkiezer tonen;
- `templates/page.customer-care.json` en `templates/page.find-a-store.json` zijn **wezen** — geen pagina gebruikt ze;
- pagina `/pages/ai-visualizer` (*"Visualiseer je wand"*, unpublished) verwijst naar template `page.ai-visualizer` die **niet in dit theme bestaat** — het werk staat kennelijk in een ander theme;
- `custom_css` wordt per sectie geïnjecteerd en stuurt elementen buiten die sectie aan (bv. `button.add-to-cart-btn {background:#55884d}` vanuit de header).

---

## K. PROPOSED DESIGN SYSTEM — "PUREDECO SURFACE SYSTEM"

### K1. Kleur

Uw voorstel is een warm monochroom palet. Onze aanbeveling wijkt op één punt bewust af — zie het advies onderaan.

```
/* FUNDAMENT */
--pd-charcoal        #1A1A18   Primaire tekst, primaire knop
--pd-charcoal-soft   #3A3A36   Secundaire tekst
--pd-warm-white      #F7F5F0   Paginaachtergrond
--pd-stone           #E8E3DA   Secties, kaarten
--pd-taupe           #A89F91   Metadata, captions, iconen
--pd-line            #DDD8CE   Randen, scheidingen

/* MERK-ACCENT */
--pd-green           #375832   Verdiepte PureDeco-groen (accent, focus)
--pd-green-soft      #EAEFE7   Achtergrond voor groen accent

/* FUNCTIONEEL */
--pd-success         #375832
--pd-error           #8C2F22   (vervangt demo-rood #c4301c)
--pd-focus           #1A1A18   met 2px offset
```

**Aangepast t.o.v. uw voorstel — en waarom:**

1. **Charcoal `#1A1A18` in plaats van `#171717`.** Een minimale warme verschuiving (licht groen-bruine ondertoon) laat charcoal samenklinken met travertijn, hout en taupe. Neutraal `#171717` leest koeler en gaat licht "digitaal" ogen naast warme materiaalfoto's.

2. **De PureDeco-groen blijft — verdiept naar `#375832`.** Dit is **tegengeluid** op de impliciete aanname dat alles monochroom wordt. `#55884d` is bestaande merkequity: het zit in het logo-accent, de knoppen, de menu-highlight en de herkenning bij terugkerende klanten. Groen volledig schrappen kost herkenning zonder dat het luxe oplevert. Verdiept naar `#375832` wordt het bosgroen in plaats van grasgroen: rustiger, natuurlijker, en het haalt **7,40:1** contrast op warm wit (AAA). Ter vergelijking: het huidige `#55884d` haalt slechts **3,84:1** en zakt daarmee onder AA voor normale tekst — het wordt nu wél voor tekstlinks gebruikt (`team_link_color`), wat een bestaande toegankelijkheidsfout is. Inzet: accent, focus-ring, actieve staat, duurzaamheidsclaims — **niet** als primaire knopkleur.

3. **`#c4301c` (demo-rood) wordt overal vervangen.** Dit is geen merkkleur.

**Contrastverificatie (op `--pd-warm-white #F7F5F0`):**

| Combinatie | Ratio | WCAG |
|---|---|---|
| `#1A1A18` op `#F7F5F0` | **16,00:1** | AAA |
| `#3A3A36` op `#F7F5F0` | **10,48:1** | AAA |
| `#A89F91` op `#F7F5F0` | **2,40:1** | ⚠️ **alleen voor niet-tekstuele elementen** |
| `#375832` op `#F7F5F0` | **7,40:1** | AAA |
| `#8C2F22` op `#F7F5F0` | **7,57:1** | AAA |
| `#6B6459` op `#F7F5F0` | **5,37:1** | AA |
| `#55884d` (huidig) op `#F7F5F0` | **3,84:1** | ❌ **faalt AA** |
| `#F7F5F0` op `#1A1A18` | **16,00:1** | AAA |

> **Let op — taupe.** `#A89F91` haalt geen 4,5:1 en mag dus **niet** voor captions of metadata worden gebruikt, hoe mooi het ook oogt. Voor secundaire tekst gebruiken we `#6B6459` (**5,37:1**, AA). Taupe blijft voor lijnen, iconen en decoratieve elementen. Dit is precies het soort keuze waarbij "luxe" en "toegankelijk" botsen — en waar toegankelijkheid wint.

### K2. Typografie

**Aanbeveling: twee letters, maximaal contrast, minimale gewichten.**

| Rol | Font | Weight | Tracking | Toepassing |
|---|---|---|---|---|
| Display / H1–H2 | **Serif** (voorstel: *Freight Display*, *Canela* of vrij alternatief *Instrument Serif*) | 400 | −0,02em | Hero, sectiekoppen |
| H3–H6 | Sans (*Instrument Sans*) | 500 | −0,01em | Subkoppen |
| Body | Sans (*Instrument Sans*) | 400 | 0 | Lopende tekst |
| Eyebrow / label | Sans | 500 | **+0,12em**, uppercase, 12px | Sectie-labels, categorieën |
| Technisch / specs | Sans tabular | 400 | 0 | Specificatietabellen |
| Knop | Sans | 500 | +0,02em | **`text-transform: none`** |

**Kritieke wijzigingen:**
- `buttons_transform: capitalize` → **`none`**. "Bekijk de collectie", niet "Bekijk De Collectie";
- alle weights 700/800 → **400/500**;
- `heading_mobile_scale: 70` → **85**;
- harde px-koppen in `feature-cards-with-icons` en `contact-help-section` → terug naar de typeschaal.

> **Waarschuwing vooraf:** een serif toevoegen betekent een extra webfont. Voorwaarden: alleen `latin` subset, `font-display: swap`, maximaal twee gewichten, en meten dat LCP niet verslechtert. Blijkt dat wel zo, dan gaan we naar één sans met sterker groottecontrast. Font gaat nooit vóór performance.

**Typeschaal (desktop / mobiel):**
```
hd1   72 / 44 px    line-height 1.05
h1    56 / 36 px    1.10
h2    40 / 28 px    1.15
h3    28 / 22 px    1.25
h4    22 / 19 px    1.35
body  17 / 16 px    1.65
small 14 / 14 px    1.55
label 12 / 12 px    1.40  +0.12em uppercase
```

### K3. Spacing & grid
```
--pd-space-3xs 4   --pd-space-2xs 8    --pd-space-xs 12
--pd-space-sm  16  --pd-space-md  24   --pd-space-lg  40
--pd-space-xl  64  --pd-space-2xl 96   --pd-space-3xl 140

Sectie-ritme desktop: 96–140 px  (nu: 40–60 px)
Sectie-ritme mobiel:  56–80 px
Container:            1440 px    (nu 1520 px)
Editorial container:  1100 px
Tekstkolom:           max 68 tekens
Grid:                 12 koloms, gutter 24 px
```
Ruimte is het goedkoopste luxe-instrument dat er is, en het meest onderbenut op de huidige site.

### K4. Buttons & CTA — één systeem

```
Gemeenschappelijk:  radius 2px · hoogte 52px (mobiel 48px) · padding 0 32px
                    font-weight 500 · letter-spacing .02em · text-transform none
                    transition 200ms cubic-bezier(.4,0,.2,1) · geen shadow · geen gradient

PRIMARY     bg #1A1A18   tekst #F7F5F0
            hover: bg #3A3A36
SECONDARY   transparant · 1px border #1A1A18 · tekst #1A1A18
            hover: bg #1A1A18, tekst #F7F5F0
TERTIARY    tekstlink · underline 1px offset 4px · optioneel pijl →
            hover: pijl 4px naar rechts, underline naar currentColor
GHOST       alleen tekst, geen rand (in donkere/beeldcontext)
DISABLED    opacity .38 · cursor not-allowed
LOADING     tekst behoudt breedte · spinner 16px
FOCUS       outline 2px #1A1A18 · offset 2px · ALTIJD zichtbaar
```

**Hiërarchie-regel:** maximaal **één** primaire knop per viewport. De huidige site zet zwarte/groene knoppen op elke actie; daardoor stuurt niets.

**Te verwijderen:** het `.pd-btn` pill-systeem uit `layout/theme.liquid` én de JS die alle `a.pd-btn.pd-btn-primary` kaapt.

### K5. Cards
```
Productkaart      radius 2px · geen border · geen shadow
                  beeld 4/5 portret (nu 1/1)
                  titel 17px/500 · prijs 17px/400 · geen rood
                  hover: beeld scale(1.03) over 600ms, verder niets
Materiaalkaart    beeld 3/4 · label uppercase 12px · titel 22px serif
Projectkaart      beeld 16/9 · locatie + sector als eyebrow · titel serif
```

### K6. Forms
```
Hoogte 52px · radius 2px · border 1px #DDD8CE · bg #FFFFFF
Label boven het veld, 14px/500 — nooit alleen placeholder
Focus: border #1A1A18 + outline 2px offset 1px
Error: border #8C2F22 + tekst 14px eronder (nooit alleen kleur)
Verplicht-markering expliciet in tekst, niet alleen met *
```

### K7. Motion
```
Standaard 200ms   cubic-bezier(.4,0,.2,1)
Beeld     600ms   cubic-bezier(.22,1,.36,1)
Fade-in   400ms   translateY(12px) → 0   één keer, niet herhalend
Max scale 1.03
@media (prefers-reduced-motion: reduce) → alles naar 0ms
```
**Te verwijderen:** `star_twinkle`, marquees, parallax op hero's.

### K8. Overige tokens
```
Radius      knop 2 · card 2 · input 2 · badge 2 · modal 4    (één systeem)
Borders     1px #DDD8CE
Shadows     geen — diepte via ruimte en toonverschil
Iconografie 1,25px stroke, 24px grid, één set (emoji verwijderen)
Beeld       hero 21/9 desktop · 4/5 mobiel
            product 4/5 · materiaal 3/4 · project 16/9 · detail 1/1
```

---

## L. PROPOSED HOMEPAGE STRUCTURE

Uw voorstel telde 11 blokken. Onze aanbeveling comprimeert naar **9** en verschuift commercie naar achteren. Reden: elke extra sectie kost scrolldiepte, en bij 12 secties (de huidige situatie) bereikt vrijwel niemand het onderste blok.

| # | Sectie | Inhoud | Waarom |
|---|---|---|---|
| **01** | **HERO** | Eén stilstaand architecturaal interieurbeeld (geen carrousel). **Echte `<h1>` in HTML.** H1: *"Architecturale wandoppervlakken"*. Sub: *"Premium wandpanelen voor exclusieve interieurs en professionele projecten."* Primair: **Ontdek de collectie** · Secundair: **Voor professionals** | Herstelt H1, LCP en merkbelofte in één keer. Carrousel eruit: slide 2–4 worden nauwelijks gezien en kosten LCP |
| **02** | **MATERIALEN** | 6 materiaalkaarten → **de echte collecties**: Hout · Japandi · Marmerlook · Leerlook · Betonlook · Kunst/Structuur. Groot editorial beeld per kaart | Lost G2 op: interne linkwaarde naar indexeerbare pagina's |
| **03** | **HET SYSTEEM** | 8 mm naadloos kliksysteem, materiaalopbouw met bamboekern, buigbaarheid, waterbestendigheid, brandklasse B1, E0. Eén technische tekening of macro-detail | Verschuift van "voordelen" naar "specificatie". Werkt voor beide doelgroepen |
| **04** | **SIGNATURE PROJECT** | Eén groot project, full-bleed, met locatie/sector/materiaal | Het bewijs dat nu volledig ontbreekt |
| **05** | **VOOR PROFESSIONALS** | Zes sectoren als rustig raster + de dienstenbelofte (samples, projectprijzen, technische documentatie, levertijden, vast aanspreekpunt). CTA: **Bekijk PureDeco Professionals** | Maakt B2B een pijler i.p.v. een footerkolom |
| **06** | **COLLECTIE / BESTSELLERS** | Productraster, 4 kolommen, rustige kaarten, geen sale-badges | Commercie — maar ná het merkverhaal |
| **07** | **MERKVERHAAL** | Waarom bamboekern, duurzaamheid, herkomst, showroom Herwen | Onderscheid |
| **08** | **ADVIES & SHOWROOM** | Persoonlijk advies + showroomafspraak, gecombineerd (nu twee losse secties) | Minder herhaling |
| **09** | **FOOTER** | Rustige, brede footer met juridisch menu onderin | E11 |

**Wat vervalt:** de Klarna-USP-balk direct onder de hero (verplaatst naar cart/checkout, waar hij hoort), de Instafeed-sectie, de dubbele `featured-collection` met placeholderinstellingen, en de tweede slideshow.

> **Tegengeluid over de B2B-slide.** De huidige homepage heeft een aparte B2B-slideshow ("Groei samen met PureDeco → Partner worden"). Wij adviseren die **niet** terug te brengen als slide, maar als sectie 05. Een slide wordt weggeklikt; een sectie wordt gelezen. Bovendien: "Partner worden" is een *transactie*-CTA, terwijl een interieurarchitect in de oriëntatiefase eerst wil zien *wat* u voor projecten doet.

---

## M. PROPOSED PROFESSIONALS STRUCTURE

**URL-advies:** nieuwe pagina op **`/pages/professionals`**. `/pages/form` blijft bestaan en blijft het registratieformulier — met een 301 naar de nieuwe hub zodra u akkoord geeft. Zo raakt geen enkele bestaande link of advertentie-landingspagina beschadigd.

```
01  HERO            "PureDeco voor professionals"
                    Sub: materialen, documentatie en projectbegeleiding
                    voor interieurarchitecten, hospitality en bouw
                    CTA: Samples aanvragen · Bespreek uw project
02  SECTOREN        6 kaarten → sectorpagina's
03  WAT WIJ LEVEREN Samples · projectprijzen · technische documentatie ·
                    levertijden · maatwerk toplagen · vast aanspreekpunt ·
                    showroom · montage-instructie
04  MATERIAALBIBLIOTHEEK  Alle decors met specs, filterbaar op
                    toepassing, brandklasse, afmeting
05  HET SYSTEEM     8 mm naadloos, opbouw, montage, onderhoud
06  PROJECTEN       3 recente cases
07  DOWNLOADS       Technische fiches · montagehandleiding ·
                    onderhoudsvoorschrift · brandcertificaat
08  PROCES          Sample → advies → offerte → levering → nazorg
09  ACCOUNT         Zakelijk account aanvragen (Samita-registratie)
10  CONTACT         Vast aanspreekpunt, met naam en foto
```

> **Belangrijke randvoorwaarde.** Blok 03 en 07 mogen **uitsluitend** claims en documenten bevatten die PureDeco daadwerkelijk kan leveren. Wij bouwen de structuur; u levert per item aan of het bestaat. Wat niet bestaat, gaat er niet in — een architect die een niet-bestaand technisch blad aanvraagt, is een verloren relatie. Dit is een expliciet openstaand punt vóór fase 2.

---

## N. PROPOSED B2B SECTOR STRUCTURE

Zes pagina's, **inhoudelijk verschillend**, niet zes keer dezelfde tekst met een ander woord:

| Sector | Kernvraag van de koper | Eigen inhoud |
|---|---|---|
| **Hotels & hospitality** | Brandveiligheid, slijtvastheid, herhaalbaarheid over 120 kamers | Brandklasse B1, reinigbaarheid, naleverbaarheid per batch, akoestiek |
| **Restaurants & horeca** | Vet, vocht, reiniging, sfeer bij kunstlicht | Waterbestendigheid, reinigingsprotocol, materiaal bij warm licht |
| **Interieurarchitecten** | Specificeerbaarheid | Artikelnummers, technische fiches, samplebox, RAL/NCS-referenties, montagedetails |
| **Chaletbouwers** | Vocht, temperatuurwisseling, snelle montage | Buigbaarheid, vochtgedrag, kliksysteem, montagetijd per m² |
| **Standbouwers** | Snelheid, demontabel, herbruikbaar | Gewicht, montage/demontage, transport, korte levertijd |
| **Aannemers & projectinrichters** | Planning, volume, marge | Levertijden, voorraadposities, projectprijzen, leveringen in fases |

Per pagina: hero · pijnpunten · relevante materialen · technische eisen · referentieproject · downloads · CTA (sample + projectofferte).

---

## O. PROPOSED PRODUCT PAGE

```
01  Breadcrumb (mét BreadcrumbList structured data)
02  Galerij 4/5 · materiaal-macro · roomscene · montagedetail
03  Titel (één <h1>) · decornummer · prijs (geen rood)
04  Materiaalkarakteristiek — 2 regels, geen USP-muur
05  Kleur/sibling-keuze (met correct geschaalde swatches, zie H)
06  Voorraad + levertijd — gekoppeld aan werkelijke voorraad
07  B2C: Aantal + In winkelwagen
    B2B: Sample aanvragen · Projectofferte · Bespreek uw project
08  SPECIFICATIES (open, niet dichtgeklapt)
    Afmeting · dikte · systeem · kern · toplaag · brandklasse ·
    emissieklasse · buigstraal · gewicht/m² · toepassing · artikelnummer
09  Montage & onderhoud (metafields — al aanwezig)
10  Duurzaamheid (metafield — al aanwezig)
11  Downloads
12  In dit project toegepast → gerelateerde projecten
13  Verwante materialen
14  FAQ (productspecifiek, niet generiek)
```

**Te verwijderen van de PDP:** de dubbele `<h2>`-titel, de dode `myshopify.com/faqs`-link, de uitgeschakelde dubbele sample-knop, de "sportvoeding"-sectie, de testimonial-placeholders, de Klarna-blok-dubbeling.

**Kritiek voor B2B:** `sku` moet gevuld worden. Zonder artikelnummer kan geen architect specificeren en geen aannemer bestellen. Dit is catalogusdata, geen designwerk — maar het blokkeert de B2B-propositie.

---

## P. PROPOSED COLLECTION PAGE

```
01  Breadcrumb (AANZETTEN — staat nu uit)
02  Collectie-hero MET beeld en een echte <h1>
    (main-collection-banner weer inschakelen; die heeft al een
     heading_tag-instelling met default h1)
03  Materiaalintroductie — 3–4 zinnen, redactioneel geschreven
04  Sfeerbeeld full-bleed
05  Filter + productraster (functionaliteit ongewijzigd behouden)
06  Toepassingen — waar werkt dit materiaal
07  Technische eigenschappen — compacte tabel
08  Projecten met dit materiaal
09  Verwante materialen
10  FAQ / verdiepende content (de huidige SEO-tekst, herschreven)
```

**SEO-bescherming:** handles blijven ongewijzigd. De bestaande SEO-tekst blijft behouden — herschreven voor leesbaarheid, niet verwijderd. De keyword-titel *"Wandpanelen kopen | Naadloos & Bamboekern | Puredeco"* verhuist naar het **SEO-titelveld**; de zichtbare collectietitel wordt *"Wandpanelen"*. De pipes verdwijnen uit de kop, de zoekwoorden blijven in de `<title>`.

---

## Q. PROPOSED PROJECT SYSTEM

Te bouwen als **Shopify metaobject** (`project`) — er bestaat nu nog geen enkele definitie:

```
Velden:
  titel · slug · locatie · sector (hotel/horeca/kantoor/retail/particulier/chalet/stand)
  opdrachtgever (optioneel) · architect/ontwerper (optioneel)
  jaar · oppervlakte m² · toegepaste materialen (product_reference[])
  korte omschrijving · uitgebreide omschrijving
  hero-beeld · galerij (file_reference[]) · detailbeelden
  quote + naam/functie (optioneel) · gerelateerde projecten
```

```
Templates:
  /pages/projecten        overzicht, filterbaar op sector en materiaal
  /projects/<slug>        detailpagina (architecturale case study)
```

Detailpagina: hero full-bleed · metadata-blok (locatie/sector/jaar/m²) · projectverhaal · galerij met ruime witruimte · "toegepaste materialen" met productlinks · CTA sample/offerte · verwante projecten.

**Waarde:** dit is tegelijk het B2B-bewijs, de belangrijkste contentmotor voor SEO (elk project = unieke content rond een materiaal + sector + locatie) en de sterkste luxe-signaalgever. Zonder projecten blijft PureDeco digitaal een webshop.

> **Randvoorwaarde:** dit valt of staat met **echte projectfotografie**. Drie echte projecten zijn meer waard dan twintig AI-beelden. Zie R.

---

## R. IMPLEMENTATION ROADMAP

### FASE 0 — VEILIGHEID ✅ AFGEROND
Live theme geïdentificeerd · development-kopie gemaakt en geverifieerd · integriteit gecontroleerd · register vastgelegd.

### FASE 1 — P0 HERSTEL (week 1) — *los van het redesign*
Dit zijn fouten in het **live** theme die nu schade doen. Ze worden in het development theme opgelost, getest, en pas ná uw akkoord gepubliceerd.

| # | Actie | Bron |
|---|---|---|
| 1 | `alert('yes')`-debugcode verwijderen | J1 |
| 2 | Null-checks op de twee `booking_cta`-scripts | J2 |
| 3 | `console.log(customer.email)` verwijderen (AVG) | J5 |
| 4 | Beide `myshopify.com`-URL's vervangen door relatieve links | J4 |
| 5 | Hoofdmenu "Wandpanelen" naar de juiste collectie | E1 |
| 6 | `scheme-inverse` en `scheme-9069f5b2…` repareren | C, I1–I2 |
| 7 | Foto + alt-tekst van *Japandi 620 Light Brown* corrigeren | F5 |
| 8 | `img_url: 'master'` → `image_url: width: 60` voor swatches | H |
| 9 | Voorraad −22 en de "Op voorraad"-fallback corrigeren | F3, F4 |
| 10 | Vrije-verzendgrens overal gelijktrekken (€ 600) | B7 |

### FASE 2 — FUNDAMENT (week 2–3)
Design tokens (kleur, typografie, spacing, radius) · knopsysteem · focus states · header/navigatie met mega-menu incl. Professionals · footer met juridisch menu · demo-content opruimen.

### FASE 3 — KERNTEMPLATES (week 4–6)
Homepage (L) · collectietemplate met H1 en breadcrumbs (P) · producttemplate (O).

### FASE 4 — B2B (week 7–9)
Professionals-hub (M) · één sectorpagina als blauwdruk (N) · projectmetaobject + overzicht + detail (Q) · sample- en offerteflow · B2B-events in GA4.

### FASE 5 — CONTENT & SEO (doorlopend, start direct)
Projectfotografie · materiaalfotografie · SEO-titels/descriptions voor 14 collecties en 68 producten · `sku` en `productType` vullen · collectieteksten herschrijven · materiaalcollecties intern linken.

### FASE 6 — QA & MEETPLAN
Desktop/tablet/mobiel · Chrome/Safari/Firefox/Edge · Core Web Vitals vóór/ná · Rich Results Test · Merchant Center-feeddiagnose · GA4-events · volledige checkout- en formuliertest · toegankelijkheidstest met toetsenbord en screenreader.

---

## PRIORITEITENOVERZICHT

### P0 — kritiek
| # | Probleem | Oplossing | Impact | Risico | Component |
|---|---|---|---|---|---|
| 1 | `alert('yes')` bij formulierverzending, live | Verwijderen | Conversie + merk | Geen | `layout/theme.liquid` |
| 2 | JS-fouten op elke pagina (`booking_cta`) | Null-checks | Stabiliteit, INP | Geen | `layout/theme.liquid` |
| 3 | Klant-e-mail in console (AVG) | Verwijderen | Compliance | Geen | `snippets/samita-custom.liquid` |
| 4 | `myshopify.com`-links op B2B- en productpagina | Relatieve URL's | Vertrouwen, dode link | Geen | `page.btbcta.json`, `product.json` |
| 5 | "Wandpanelen" → samples-collectie | Link corrigeren | Omzet | Laag | menu `main-menu-1` |
| 6 | Geen H1 op home/collectie/B2B | H1 herstellen | SEO + a11y | Laag | meerdere |
| 7 | `scheme-inverse` wit-op-wit | Kleuren repareren | A11y + oorzaak tekstloze hero | Laag | `settings_data.json` |
| 8 | Hero: AI-PNG 2,08 MB, `alt=""`, tekst in beeld | Echte fotografie + HTML-tekst | LCP + merk + SEO | Middel (beeld nodig) | `index.json` |
| 9 | Verkeerde productfoto Japandi 620 | Corrigeren | Vertrouwen, feed | Geen | catalogus |
| 10 | Swatches laden master-images | `image_url: width: 60` | Performance | Geen | `product-information-blocks.liquid` |
| 11 | "Op voorraad" ongeacht voorraad | Conditie op werkelijke voorraad | Compliance | Laag | `product.json` |
| 12 | `.pd-btn`-links gekaapt door JS | Verwijderen, echte links | Conversie + a11y | Middel — eerst verifiëren | `layout/theme.liquid` |

### P1 — zeer hoge impact
Materiaalcollecties intern linken i.p.v. filter-URL's (G2) · kannibalisatie wandpanelen/bamboepanelen en akupanelen oplossen (G3) · B2B in het hoofdmenu (D1) · Professionals-hub (M) · projectsysteem (Q) · typografiesysteem (K2) · knopsysteem (K4) · breadcrumbs aan + BreadcrumbList (G6) · SEO-metadata vullen (G5) · `sku` vullen (O) · dubbele producttitel (J7) · `setTimeout`-hacks (J3) · verzendgrens/reviewscore gelijktrekken (B7) · juridisch footermenu (E11) · demo-content verwijderen (B3).

### P2 — belangrijke verbetering
Spacing-ritme · `star_twinkle` en marquees verwijderen · emoji-iconen vervangen · menu-spaties en typefouten · Engelse strings vertalen · beeldratio's uniformeren · alt-teksten "Team member 1/2/3" · taalkiezer verbergen zolang alleen NL gepubliceerd is · weesjes `page.customer-care` / `page.find-a-store` opruimen · `custom_css` uit secties halen.

### P3 — verfijning
Logo-breedte terugbrengen · badge-kleuren harmoniseren · iconenset uniformeren · micro-interacties op kaarten · `templates/page.ai-visualizer` beoordelen.

---

## OPENSTAANDE VRAGEN — BESLISSINGEN DIE U MOET NEMEN

1. **Kortingspositionering.** ACTIE in het menu, Sale-collectie, structurele `compareAtPrice`, 5% nieuwsbriefkorting en Klarna-prominentie zijn samen de sterkste rem op premium-perceptie. Dit is een **commerciële** keuze, geen designkeuze. Wij adviseren: korting behouden waar die omzet oplevert, maar uit de merklagen halen (menu, hero, footer-CTA) en naar de commerciële lagen verplaatsen (collectiepagina, cart, e-mail). Graag uw richting.
2. **Groen behouden of volledig monochroom?** Onze aanbeveling: behouden, verdiept naar `#3E6238` (zie K1).
3. **Serif toevoegen?** Alleen als LCP het toelaat (zie K2).
4. **Welke B2B-diensten bestaan écht?** Nodig vóór M en N.
5. **Is er echte projectfotografie beschikbaar?** Bepalend voor Q en voor het hele luxe-traject.
6. **`/pages/verkoopparters`** — typefout in een live URL. Corrigeren mét 301, of laten staan?
7. **Wat is de rol van Bol.com?** Er loopt een actieve koppeling (`bol.*`-metafields, `bol-import`-tags). Marktplaatsaanwezigheid en premium-positionering kunnen botsen.

---

*Einde rapport. Er zijn geen wijzigingen aangebracht aan het live theme of aan het development theme. Fase 2 start uitsluitend na uw akkoord.*
