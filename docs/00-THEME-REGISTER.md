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
