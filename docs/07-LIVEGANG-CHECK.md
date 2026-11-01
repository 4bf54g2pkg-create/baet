# Livegang H1-kopie · controle 1 nov 2026

Thema: "Hyper kopie 5 okt (H1-test)" 194824929546. Live nu: "Hyper" 188874326282.

## Blokkade
- **Product Samples-app is aan één thema gekoppeld.** Openbare app-instelling: `visibility: {type: custom, themes: ["188874326282"]}`.
  Het script (main.min.js) start alleen als `Shopify.theme.id` in die lijst staat. Na publicatie van de H1-kopie
  (id 194824929546) doet de app niets en kan niemand stalen afrekenen.
  Oplossing (in de app, door de eigenaar): Product Samples → instellingen → themazichtbaarheid: H1-kopie aanvinken (of "alle thema's").
  Daarna in de voorbeeldweergave opnieuw testen, dan pas publiceren.

## Getest en in orde
- Stalen kiezen: collectie, homepage, inspiratiepagina en productpagina komen samen in één lijst (localStorage pd-edit, max 5).
- /pages/sample toont de gekozen stalen; met de app-instelling gesimuleerd: conceptorder #D1597 (2 stalen à € 0, verzending € 6,95,
  totaal € 6,95, tag product-samples-app) en doorsturen naar de betaalpagina. Vanaf de productpagina (samplelade): #D1598.
- Winkelmand: paneel toevoegen, lade opent, gratis-verzendingmelding, afrekenknop. (Afrekenpagina zelf niet bereikbaar vanuit de testomgeving.)
- 31 pagina's: status 200, één H1, geen Liquid-fouten, geen horizontaal scrollen op mobiel.
- Alle templates van live bestaan in de H1-kopie; geen producten met eigen template.
- Apps gelijk aan live: BookX, Inbox-chat, Judge.me, Samita (zakelijk), Rez (pre-order), Instafeed. XO Insert Code is leeg op live.
- Tracking gelijk: G-N9ZMX91VEZ, GT-WPTCFVT8, AW-16753512576, Pinterest.
- URL's veranderen niet (thema wisselt geen handles).

## Opruimen (met akkoord)
- 110 tijdelijke afbeeldingen `assets/pdtmp-*` (≈ 100 MB, nergens gebruikt) en `templates/collection.doorladen-test.json`.
- Oude snelle weergave (overlaygroep, sectie quick-view): niet zichtbaar, maar bevat een oude calculator-script
  (JS-fout "addEventListener of null" op o.a. 689, montagekit, eindprofielen) en de tekst "3 jaar garantie".
- Testconcepten #D1597 en #D1598 (product-samples-app).

## Na livegang
- Eén echte stalenbestelling vanaf een telefoon plaatsen en de afrekenpagina controleren.
- Gidsen als artikelen aanmaken (nu ?view=gids-…, noindex).

## 813 Natural Oak (1 nov 2026)
- Product stond op actief maar niet in het kanaal Online Store: nu gepubliceerd in Online Store (alleen dat kanaal).
- Eigen Google-titel/-omschrijving leeggemaakt (zoals de andere decors); het thema maakt nu "Houten wandpaneel 813 Natural Oak | 8 mm naadloos | PureDeco".
  De oude omschrijving noemde ten onrechte 5 mm en 260 cm.
- Alt-teksten in de vaste opbouw (PureDeco Wandpaneel Hout 813 …, sfeerbeeld (visualisatie), detailaanzicht).
- Staal pd-staal-813.jpg (600×600) uit de productfoto.
- custom.sibling_products van alle houtdecors (602, 607, 615, 810, 811, 812, 813 en 'hout') bevat nu dezelfde 7 decors.
- H1-kopie: houtvolgorde (pd_decor_order) 607 · 813 · 602 · 615 · 811 · 812 · 810; houttekst "zeven decors" + tabelrij 813;
  813 in de lijst naadloze houtdecors; kiezer meldt nu ook decors die alleen als Signature (8 mm) bestaan.

## Stalen na aanpassing app (1 nov 2026, echte test, geen simulatie)
- App-zichtbaarheid nu: themes 188874326282 (Hyper) en 194824929546 (H1-kopie).
- /pages/sample na kiezen op collectie (813), homepage (670) en inspiratiepagina (812): #D1603 en #D1604, beide 3 stalen à € 0, verzending € 6,95.
- Productpagina 689 → samplelade: #D1601 (1 staal, € 6,95).
- #D1600 bevatte maar 1 van 3 stalen: gemaakt op het moment dat de app-instellingen net waren gewijzigd. De app wist zijn eigen lijst
  als zijn instellingen veranderen (main.min.js: isAppSettingsChanged → clear). Daarna 3× herhaald zonder fout.
- Testconcepten van deze sessie: #D1597, #D1598, #D1600–#D1604. #D1599 (824 Taupe, 20:41) is niet van deze test.

## Zoeken: verzamelproducten verborgen (H1-kopie)

- Oude verzamelproducten (meerdere decors in één product) staan niet meer in de zoekresultaten en zoeksuggesties: `hout`, `wandpaneel-art`, `metaal`, `leer`, `doorlopend-marmer`.
- Lijst aanpasbaar: Thema-instellingen › Puredeco · decors › Niet tonen in zoeken (één handle per regel).
- De productpagina's zelf blijven bestaan en gepubliceerd (Google Shopping landt erop: /products/hout 222 sessies in 90 dagen).
- Getest: zoeken op 811, 812 en 842 geeft 1 resultaat (het losse decorproduct); de zoeksuggesties idem.
- `solide-kleuren` blijft zichtbaar: de losse producten 656–659 staan op concept, dus dit is de enige plek voor die kleuren.
- Gedaan (winkeldata): 843 Stucco Shadow formaat 280x122 → 260x122; decorkiezer (custom.sibling_products) van 842 en 843 = 840, 841, 842, 843. Gecontroleerd: alle vier tonen 'Art · 4 decors' en 260 × 122 cm; calculator 843 bij 4,20 × 2,70 m = 8 panelen.
- Nog open (winkeldata, wacht op akkoord): prijzen verzamelproducten vs. losse producten, 260-varianten 811/812 uit `hout`.
