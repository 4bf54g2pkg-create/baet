# PUREDECO — THEME REGISTER (SAFETY RECORD)
Datum: 2026-09-22
Shop: PureDeco — puredeco.nl (Shopify plan, EUR, NL, tz CEST)

## LIVE THEME — READ ONLY
LIVE THEME:        Hyper
LIVE THEME ID:     188874326282
LIVE THEME GID:    gid://shopify/OnlineStoreTheme/188874326282
LIVE STATUS:       PUBLISHED (role: MAIN)
Theme Store ID:    3247 (Hyper — Shopify Theme Store)
Preview prefix:    /t/2
Created:           2026-03-04T08:41:01Z
Last updated:      2026-09-22T09:13:33Z  <-- let op: vandaag nog gewijzigd

## OVERIGE BESTAANDE THEMES (unpublished, NIET aanraken)
188848374026  Horizon                       UNPUBLISHED  (ander theme, store id 2481)
189441605898  Copy of theme (Save purpose)  UNPUBLISHED  (backup 2026-03-25)
190879269130  Copy of Hyper                 UNPUBLISHED  (2026-05-21)
194018902282  Faruk FAQ pagina wijziging    UNPUBLISHED  (2026-09-12)
194090926346  Kopie van Hyper               UNPUBLISHED  (2026-09-14)

## DEVELOPMENT THEME — hier wordt gewerkt
DEVELOPMENT THEME:     PUREDECO — LUXURY B2B — DEVELOPMENT
DEVELOPMENT THEME ID:  194359853322
DEVELOPMENT THEME GID: gid://shopify/OnlineStoreTheme/194359853322
DEVELOPMENT STATUS:    UNPUBLISHED (role: UNPUBLISHED)
Preview prefix:        /t/7
Aangemaakt:            2026-09-22T14:22:53Z
Processing:            voltooid (processingFailed: false)
Bron:                  volledige duplicate van live theme Hyper (188874326282)

## INTEGRITEITSCONTROLE (MD5, live vs development) — ALLE IDENTIEK
config/settings_data.json    bc9202efeafe5de71c2520a01b0e4a87  = OK
config/settings_schema.json  d4fb5af16eeffc621c53db4d0ada3008  = OK
layout/theme.liquid          327b40b2517ecaaa37bff2f595649a74  = OK
templates/index.json         c95cd40c7aa5f999a54f62abfb4b1aab  = OK
templates/product.json       4d2b64800a7a5996a8c2cce4bb4a89e2  = OK
templates/collection.json    b50fd8e70bc60d887789828e4d9f472e  = OK
templates/robots.txt.liquid  79fe39ff3f6c96eb3ef97395ad254787  = OK

## AFSPRAKEN
- Live theme 188874326282 = READ ONLY. Geen enkele schrijfactie.
- Alle ontwikkeling uitsluitend in 194359853322.
- Publiceren alleen na expliciete toestemming van de opdrachtgever.
- Geen automatische deployment naar production geconfigureerd.
- Shopify MCP blokkeert bovendien technisch: theme publishing, theme deletion,
  en theme file writes naar het MAIN theme.

## WIJZIGINGEN LIVE THEME (door opdrachtgever)
- 2026-10-05 13:33 UTC — templates/product.json: WhatsApp-link contactblok
  van wa.me/31850870490 naar wa.me/31316700214 (handmatig in theme-editor,
  door opdrachtgever; door Claude gecontroleerd). Nieuw controlepunt live
  updatedAt: 2026-10-05T13:33:36Z.

## 6 okt 2026 · winkelbrede objecten aangemaakt voor H1-test
- Menu `pd-hoofdmenu` (Wandpanelen · Akupanelen · Accessoires · Inspiratie · Studio Herwen) en `pd-mobiel` (idem + Samples · Zakelijk · Veelgestelde vragen · Contact).
- Alleen gekoppeld in H1-test (`sections/header-group.json`). Het live theme gebruikt nog `main-menu-1` / `mobile-menu`; die zijn niet gewijzigd.

## 6 okt 2026 · montage-animatie
- Bestand (Shopify Files): `puredeco-montage-v2.mp4`, Video `gid://shopify/Video/51238636093706` (36 s, 5 stappen incl. op maat maken, 1080p, illustratie). Vorige versie `puredeco-montage.mp4` (51238562988298) niet meer gekoppeld.
- Winkel-metafield `puredeco.montage_video` (file_reference) verwijst ernaar; alleen H1-test leest dit (secties pd-product-hero en pd-product-details). Een sectie-instelling "Montagefilm" of een productvideo gaat voor.
- Bron: `media/film.html` (beeld-voor-beeld gerenderd met Playwright, gecodeerd met ffmpeg).

## Ronde 7 (6 okt 2026) · alleen H1-test
- Footer: nieuwe sectie `pd-footer` in `footer-group.json` (oude nieuwsbrief met 5%-welkomstkorting en oude footer uitgeschakeld, niet verwijderd). Menu's `pd-footer-collecties`, `pd-footer-service`, `pd-footer-zakelijk`.
- Productpagina: samples-paneel "The Puredeco Edit" (rechts op desktop, onderblad op mobiel) met het Product Samples-appblok als knop; collectiekaarten "Meer uit de …collectie"; vragenblok "Goed om te weten"; Studio Herwen met foto (instelling `studio_image`, anders laatste productfoto) en Route-knop; achtergrondritme papier/zand.
- Montagefilm laadt pas als het blok in beeld komt. Mobiel: staande film 4:5 (`shop.metafields.puredeco.montage_video_mobile` → Video 51239725170954, bron `media/puredeco-montage-staand.mp4`) en hoofdstukken als swipe-rij.
- Let op: de bestaande pagina `/pages/sample` voegt volledige panelen toe aan de winkelmand (sectie `product-samples-selector` met gewone producten). Nog niet aangepast.
- Productbeeld "In de praktijk" (alleen H1-test): toont `product.metafields.puredeco.project_video` als eerste weergave, met stappen uit `puredeco.project_steps` ("Naam@seconde|…") en bijschrift `puredeco.project_caption`. Eerste invulling: 670 Pandora Slate, Video 51239827702026 (`media/670-montage-4x5.mp4`), stappen Op maat zagen@0 · Plaatsen@2 · Klaar@6.2, "in een toilet". Nieuwe projectvideo per decor = deze drie velden vullen bij het product.
- Homepage (alleen H1-test): `sections/pd-home.liquid` + `pd-home-cta.liquid` in `templates/index.json`; oude secties uitgeschakeld, Instafeed behouden ("Bij klanten en in projecten"). Hero gebruikt de bestaande heldenbeelden (ChatGPT_Image_8_sep_2026_11_25_14 / 11_22_33); stappenbeelden montage = Files `pd-montage-stap-1..5.jpg` (uit de montagefilm).
- Puredeco Projects (alleen H1-test): `sections/pd-projects.liquid` bovenaan `templates/page.btbcta.json` (= /pages/form); oude slideshow en stappen uit, aanmelding zakelijke klant (Sami Wholesale) blijft eronder. Aanvraagformulier = Shopify-contactformulier (geen bijlagen mogelijk). Documentatie, adviseur, reactietijd en foto's verschijnen pas als ze in de editor zijn ingevuld.
- Header (alleen H1-test): `sections/header.liquid` met eigen menu-regel `pd-hnav` (links van het logo, vanaf 1024 px; tweede menuregel verborgen), CTA's Professionals (tekst) + Samples (omlijnd), inklappen bij scrollen uit. Menu `pd-hoofdmenu` = Collecties (met submenu) · Inspiratie · Projecten · Studio; `pd-mobiel` idem + Samples, Veelgestelde vragen, Contact.

## Beeldbank en beeldset (ronde 8)
- `media/beeldbank/`: 107 originele catalogusbeelden (packshots, details, sfeerrenders, oude heldenbeelden), opgehaald via tijdelijke kopieën `assets/pdtmp-*` in H1-test. Die kopieën kunnen via de koppeling niet verwijderd worden: verwijder ze in Shopify (Thema → H1-test → Code bewerken → assets, alles met `pdtmp-`) vóór publicatie.
- `media/banners/`: nieuwe beeldset (hero desktop/mobiel, 6 collectiebanners + kaarten, Projects-hero + 4 sectoren, Edit-samplebox, praktijk-670, social posts/story). Generator: `tools/banners/gen.py`; artboard `docs/ontwerp-puredeco-finish/Beeldset.dc.html`.
- Let op: de huidige heldenfoto's (ChatGPT_Image_8_sep_2026_*) hebben tekst in het beeld.
- Samplepagina (alleen H1-test): `sections/pd-samples.liquid` bovenaan `templates/page.sample.json` (/pages/sample), oude secties uit. Alle decors uit collectie Wandpanelen per soort, "+ Sample · € 0", max. 3, vaste balk; toevoegen via /cart/add.js met eigenschap "Voorbeeld van" (zoals de Product Samples-app). Te testen: €0-prijs in de kassa.

## Homepage-hero optie B gekozen (811 · Materiaal) — H1-test
- Beelden in Shopify Files: `pd-home-hero-811.jpg` (desktop 2:1, links echt 811-oppervlak, rechts interieur-visualisatie) en `pd-home-hero-811-mobiel.jpg` (alleen het oppervlak).
- `pd-home`: nieuwe instelling `hero_caption_photo` (bijschrift links). Staat die ingevuld, dan krijgt `hero_caption` de klasse `ph-hero__cap--d`: op desktop een licht label rechtsonder, op mobiel verborgen (daar staat alleen het echte oppervlak in beeld).
- `index.json`: hero_caption "811 Walnut Classic · interieur: visualisatie", hero_caption_photo "811 Walnut Classic · Signature · echte productfoto".
- Checksums: pd-home 367414288dbb07169c27681b7ef45006 · index.json 38e247336322f297c7544ddd2926446a · puredeco-premium.css f815561d99a8db0dca77e7eb48e3e387.

## Beton ciré en travertin naar voren + merkverhaal 812 — H1-test
- `pd-home`: nieuw blok 1b "Beton ciré en travertin" direct onder de hero (donker, id `#beton-travertin`, instelling `show_stone`). 691 Concrete Smoke (badkamer = media[1], staal = media[2]) en 851 Travertine Ivory (badkamer = media[1], staal = media[3]); interieurs gemarkeerd als visualisatie; tekst alleen uit de productbeschrijvingen (5 mm buigbaar / 8 mm kliksysteem, waterbestendig).
- Collecties: kaart "Beton ciré en travertin" op plek 2 (link naar het blok, beeld 851 woonkamer). "In het interieur": 851 vervangen door 812 (media[2]) om dubbel beeld te voorkomen.
- Merkverhaal: `pd-merkverhaal-812.jpg` (812 Walnut Deep, slaapkamer, visualisatie).
- Samplepagina: groep "Beton ciré en travertin" op plek 2.
- Menu's pd-hoofdmenu, pd-mobiel en pd-footer-collecties (alleen H1-test): "Beton ciré" en "Travertin" na Hout, met link naar de productpagina's (er is geen collectie voor).
- Checksums: pd-home db3c9cd7… · index.json 502dd7df… · css 76622467… · pd-samples 458b1401….

## Sectorbeeld hotel: 810 Noir Oak met LED — H1-test
- Bron: Unsplash, https://unsplash.com/photos/modern-hotel-room-with-a-large-bed-and-city-view-EPuN25MPwAU (Unsplash-licentie: gratis commercieel gebruik en bewerken; geen naamsvermelding verplicht). Origineel: `media/sector/hotel-bron.jpg`. Door de klant gekozen voor Hotels (6 okt).
- LED-profielen komen nog online; daarna link vanaf het hotelbeeld en noemen in het bijschrift.
- Bewerking (`tools/sector/hotel.py 810led`, `tools/sector/vloer.py`): wand achter het bed = 2 panelen 810 Noir Oak (244 cm, symmetrisch achter het hoofdbord), LED aan beide uiteinden, kunstwerk weggelaten, blauw tapijt → warm greige.
- Shopify Files: `pd-sector-hotels-810-led.jpg` (1200×1200). Gebruikt als sector_image_1 op de homepage (index.json) en Projecten (page.btbcta.json; daar ook sector 2–4 gezet). pd-projects toont nu ook het label "Visualisatie" bij ingestelde sectorbeelden.
- Checksums: pd-projects 44bfbb18… · page.btbcta.json 76b65ee5… · index.json 2ffbfea1….

## Collectiepagina in de huisstijl + SEO — H1-test
- Nieuw: `sections/pd-collection.liquid`, `snippets/pd-clean-html.liquid`. `templates/collection.json`: breadcrumbs → pd_collection → apps; oude H1-rich-text en product-grid uitgezet (staan nog in het template). Groene winkelwagenknop (custom CSS #55884d in product-grid) is daarmee weg.
- Hero met H1 = metafield custom.seo_h1 (anders collectietitel), intro = eerste alinea van de opgeschoonde beschrijving, USP's (samples, 3 jaar garantie, 3–6 werkdagen), collectiebeeld (gemarkeerd als visualisatie).
- Collectienavigatie met ankerteksten (instelbaar: handle|tekst per regel). Filters (list-filters) en sorteren met rel="nofollow". 24 per pagina met echte paginalinks (geen oneindig scrollen).
- Kaarten: sfeerbeeld (visualisatie) met paneel bij hover, code + naam (h3), maat en uitvoering uit de opties, prijs per paneel, "Bekijk en bereken" + "+ Sample" (zelfde lijst als /pages/sample, max 5).
- Onder de grid: "Over …" met opgeschoonde collectietekst (div/section/form en data-attributen uit opgeplakte ChatGPT-opmaak vallen weg), FAQ-blokken (optioneel per collectie-handle), afsluiter met samples/studio.
- Structured data: CollectionPage + ItemList (producten op de pagina), FAQPage (alleen zichtbare vragen); BreadcrumbList kwam al uit sections/breadcrumbs.liquid.
- Geen URL's gewijzigd; geen redirects nodig.
- Horeca-sectorbeeld: `pd-sector-horeca-691-led.jpg` als sector_image_2 op homepage en Projecten. Bron nog aanleveren.
- Checksums: pd-collection 16735971… · pd-clean-html f4926a0b… · collection.json e5d08e55… · css 57714e6b… · index.json ec197b6a… · page.btbcta.json d1fadbef….

### SEO-advies dat winkeldata raakt (nog niet gedaan, toestemming nodig)
1. Collectiebeschrijvingen opschonen in de admin (bamboepanelen-samples, akupanelen-samples, actie, nieuwe-collectie bevatten opgeplakte chat-opmaak incl. leeg formulier; de theme-weergave schoont het al op, maar de admin-tekst blijft vuil).
2. custom.seo_h1 invullen voor japandi en akupanelen.
3. Tegenstrijdige retourbelofte: SEO-beschrijving Hout zegt "90 dagen retour", elders "30 dagen bedenktijd".
4. "4,9 van 5 op Google Reviews" in de beschrijving van Wandpanelen controleren of onderbouwen.
5. Productafbeeldingen met alt-tekst "Renderique Photo 1" herschrijven.
6. Dubbele collecties (akupanelen / akupanelen-samples, wandpanelen / bamboepanelen-samples) concurreren op dezelfde zoekwoorden: eentje noindex of de beschrijvingen duidelijk anders maken. URL's blijven staan.

## SEO-winkeldata doorgevoerd (7 okt, met toestemming) — geen URL's/handles gewijzigd
- Collectiebeschrijvingen opgeschoond (zelfde tekst, zonder opgeplakte chat-opmaak; interne links met ankertekst "houten wandpanelen" / "naadloze wandpanelen"): bamboepanelen-samples, akupanelen-samples, actie, nieuwe-collectie, sale, kunst, onze-bestsellers, 8mm-naadloos.
- SEO-titel/-beschrijving toegevoegd: akupanelen-samples, sale. Hout: "90 dagen retour" → "30 dagen bedenktijd".
- custom.seo_h1: japandi "Japandi wandpanelen", akupanelen "Akupanelen voor wand en plafond".
- 51 alt-teksten van productfoto's van actieve producten (o.a. "Renderique Photo 1" → "Houten wandpaneel 811 Walnut Classic, sfeerbeeld (visualisatie)").
- Niet gedaan, bewust: noindex op dubbele collecties. Het live hoofdmenu linkt "Wandpanelen" naar /collections/bamboepanelen-samples; zonder Search Console-data kan noindex een rankende pagina kosten. Eerst in Search Console kijken welke URL rankt.
- Open: Algemene voorwaarden bevatten nog "90 DAGEN TEVREDENHEIDSGARANTIE" (juridisch document, niet aangepast). Product 620 Light Brown toont als eerste foto het 619 Jade-beeld.

## Samples A + B (7 okt) — H1-test
- Stalen: 24 uitsneden `pd-staal-<code>.jpg` in Bestanden (bron: media/stalen, tools/banners/stalen.py) + `pd-edit-samplebox.jpg`. Snippet `pd-swatch` kiest het staal uit Bestanden, anders de productfoto (dan ingezoomd). Nieuw decor? Upload `pd-staal-<code>.jpg`.
- A · `pd-samples` herbouwd als stalenkaart: hero met samplebox-foto, filters met aantallen, groepen (Hout, Beton en travertin, Japandi, Leer, Art, Marmer), stalen met interieur bij hover (visualisatie), genummerde keuze 1–5, samplebox met 5 vakken rechts (desktop) / balk onderin (mobiel). Aanvragen zoals voorheen (cart/add met "Voorbeeld van").
- B · productpagina: knop "Eerst voelen? Gratis staal" met staal onder "In winkelmand"; voegt toe en opent het paneel "Toegevoegd aan je samplebox" met 5 vakken, "Past hierbij" (3 decors: metafield custom.sample_pairs, anders custom.sibling_products, anders de collectie) en "Samples aanvragen" → /pages/sample#box. Collectiekaarten gebruiken hetzelfde staal.
- Eén gedeelde keuze (localStorage pd-edit, max 5) op samplepagina, productpagina en collectiekaarten.
- Checksums: pd-swatch 3b7ab0f2… · pd-samples b56985e7… · pd-product-hero 36379f12… · pd-collection 2219cee2… · css c8b5fa32….

## 2026-10-07 — Stalen via de Product Samples-app (fix: volle paneelprijs bij afrekenen)
- Oorzaak: stalenkaart en productlade deden `/cart/add.js`; de app werkt met een eigen conceptorder (stalen € 0 + € 6,95). Gewone winkelmand = paneelprijs.
- Nieuw `snippets/pd-sample-app.liquid`: per gekozen decor wordt de productpagina onzichtbaar geladen en de echte app-knop `[product-samples-button]` ingedrukt; daarna herlaadt de pagina en opent de app-lijst (`.product-samples-widget__trigger`).
- `pd-samples` (knop "Samples aanvragen") en `pd-product-hero` (lade, knop "Samples aanvragen") gebruiken dit. App-blok weer gerenderd in de lade (verborgen, nodig voor de koppeling).
- Checksums: snippet 31cb9b91…, pd-samples f38a6b02…, pd-product-hero 8f4d92f5…, css 74f1c4f8…
- Te testen in voorbeeld H1-test: 2–3 stalen kiezen → app-lijst moet die stalen tonen → afrekenen € 0 + € 6,95.
- Update: iframe-methode bleef hangen (Shopify blokkeert inladen in frame). Nu: rij in sessionStorage, browser gaat per decor naar de productpagina, drukt de app-knop, en opent na het laatste decor de app-lijst. Voortgangsscherm "Stalen klaarzetten · x van n". Snippet md5 88b88095….
- Update 2: wachtrij + overlay weg. Nu net als live: echte app-knop indrukken (op productpagina direct; vanaf samplepagina naar eerste decor #pd-sample). md5 snippet 14f9d5e7…, pd-samples 85c5eb90…, pd-product-hero 00f47f4d…. Volledige koppeling volgt zodra puredeco.nl/cdn.shopify.com bereikbaar zijn voor analyse van de app.
