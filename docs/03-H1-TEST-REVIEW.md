# REVIEW — THEME "Hyper kopie 5 okt (H1-test)"
**Theme-ID:** `194824929546` · **Status:** UNPUBLISHED · **Aangemaakt:** 05-10-2026 09:51 UTC · **Laatst gewijzigd:** 12:20 UTC
**Bron:** kopie van het live theme *Hyper* (`188874326282`); `config/settings_data.json` is identiek aan live (MD5 `bc9202ef…`).
**Methode:** alle bestanden met een wijzigingsdatum na het kopiëren opgehaald en regel voor regel vergeleken met live. Alleen gelezen, niets aangepast.

---

## 1. Wat er in dit theme veranderd is (9 bestanden)

| Bestand | Wijziging | Oordeel |
|---|---|---|
| `layout/theme.liquid` | `alert('yes')` weg; null-checks op formulier en op beide `booking_cta`-scripts; laadt `puredeco-premium.css` | ✅ Lost twee P0's op (debugpopup, JS-fouten op elke pagina) |
| `sections/header.liquid` | Logo is niet langer de `<h1>`; in plaats daarvan een **visueel verborgen** `<h1>` met instelbare tekst (standaard *"Premium PureDeco wandpanelen voor wonen én projecten"*) | ⚠️ Beter dan het logo als H1, maar zie §2.2 |
| `sections/header-group.json` | **BookX-appblok uit de header verwijderd** | ⛔ Waarschijnlijk breekt dit de afspraakknoppen, zie §2.1 |
| `sections/rich-text-h1.liquid` (nieuw) | Kopie van `rich-text` die een `<h1>` rendert; gebruikt metafield `custom.seo_h1` als dat gevuld is | ✅ Netjes opgelost, met terugvaloptie |
| `templates/collection.json` | Kruimelpad **aan**; kopsectie gebruikt `rich-text-h1` | ✅ Collecties krijgen een H1 en een kruimelpad |
| `sections/breadcrumbs.liquid` | Tussenstap "Collecties" weg; **BreadcrumbList JSON-LD** toegevoegd voor collectie- en productpagina's, gelijk aan het zichtbare pad | ✅ Goed, met één kanttekening (§2.3) |
| `snippets/product-information-blocks.liquid` | In de quick-view wordt de titel een `<div>` in plaats van een extra `<h1>` | ✅ Voorkomt meerdere H1's op collectiepagina's |
| `assets/puredeco-premium.css` (nieuw, 177 regels) | Monochrome knoppen (zwart/wit i.p.v. groen), radius 0–2 px, `text-transform: none`, stille zwarte badges in plaats van rood | ✅ Zelfde richting als het designsysteem in het dev theme; makkelijk terug te draaien |
| `snippets/meta-tags.liquid` | Opnieuw opgeslagen, **inhoud identiek** aan live | — |

**Metafield-data (al live in de catalogus, niet in het theme):** `custom.seo_h1` is gevuld voor 13 van 16 collecties (leeg bij *akupanelen*, *samples* en *japandi*; daar wordt de collectietitel gebruikt).

---

## 2. Bevindingen

### 2.1 ⛔ BLOKKEREND — afspraakknoppen werken vermoedelijk niet meer
- De knoppen *"Plan je afspraak"* op de showroompagina (`puredeco-showroom-page.liquid`, regels 813, 894 en de locatiekaarten) hebben `href="javascript:void(0)"`. Ze werken alleen doordat een script een klik doorgeeft aan `.bookeasy-btn`.
- Dat element komt uit het **BookX-appblok**. Op de showroompagina zelf staat dat blok uit; het enige actieve blok stond in de header, en **dat is in dit theme verwijderd**. Het BookX-app-embed staat wel aan, maar alleen met de instelling `enable_cart_validation`.
- Daarnaast onderschept het script onderaan `theme.liquid` nog steeds **elke** `a.pd-btn.pd-btn-primary` (`preventDefault` + `stopPropagation`). Daardoor doen ook *"Interesse? Neem contact op"* (partner) en de sampleknop op de showroompagina niets als `.bookeasy-btn` ontbreekt. In live openen ze de agenda in plaats van te navigeren; hier wordt het waarschijnlijk een dode klik.
- **Testen in de preview vóór publicatie:** `/pages/showroom` → alle vier de knoppen aanklikken. Werkt het niet, dan het BookX-blok terugzetten, of het onderscheppen beperken tot knoppen met `enable_cta_app` en de overige knoppen gewoon laten navigeren.

### 2.2 ⚠️ Homepage-H1 is verborgen tekst
- Een `<h1>` met `visually-hidden` wordt door screenreaders gelezen, maar bezoekers zien hem niet. Google weegt verborgen tekst lager en kan het, met marketingwoorden als "Premium", als manipulatie zien. Het risico is klein, maar het levert ook weinig op.
- De sterkere oplossing is een **zichtbare** kop in de hero (zoals de `pd-hero`-sectie in het dev theme doet). Tot die hero er is, is dit een acceptabele tussenstap; de tekst is via de theme-editor aan te passen.
- Tekstsuggestie zonder superlatief: *"Naadloze wandpanelen voor wonen en projecten"*.

### 2.3 ⚠️ Kruimelpad op productpagina's kan via "Sale" of "Actie" lopen
- Zonder collectiecontext (bezoeker komt via Google of een directe link) gebruikt het kruimelpad `product.metafields.breadcrumb.primary_collection`. **Die metafield-definitie bestaat niet**, dus valt het pad terug op `product.collections | first`.
- Welke collectie "eerste" is, ligt niet vast; dat kan *Actie*, *Sale* of *Onze Bestsellers* zijn. Dat wordt dan zichtbaar en in de BreadcrumbList zoals Google hem toont, bijvoorbeeld *Home › Sale › Wandpaneel Hout 810*.
- **Oplossing (later):** metafield `breadcrumb.primary_collection` aanmaken en per product de materiaalcollectie invullen.

### 2.4 ⚠️ Wat in dit theme nog niet is opgelost (wel in het dev theme)
- `console.log` van het e-mailadres van ingelogde klanten in `snippets/samita-custom.liquid` (**AVG**).
- Dubbele producttitel op de PDP: na de `<h1>` volgt nog steeds een `<h2 class="h1">` met een link naar dezelfde pagina.
- Swatches laden de master-afbeelding (`img_url: 'master'`) voor 30 px.
- `myshopify.com`-links (PDP-contactblok en B2B-inloglink).
- `.pd-btn`-onderschepping (zie §2.1).

### 2.5 Kleine punten
- H1 van `/collections/hout-1` is *"Houten wandpanelen"*. Het product is een houtlook op een bamboekern met PVC-laag, dus *"Houtlook wandpanelen"* is juister en past bij de SEO-titel.
- `/collections/wandpanelen` (*"Wandpanelen kopen"*) en `/collections/bamboepanelen-samples` (*"Bamboe wandpanelen"*) blijven concurrerende hoofdcategorieën; de H1 lost de kannibalisatie niet op.
- Er zijn meer apps actief dan in eerdere audits stond: **XO Insert Code** (header + body), **Shopify Inbox**, **Mida heatmaps** en **Rez pre-order**. XO Insert Code kan extra scripts injecteren die niet in het theme staan; de inhoud daarvan is niet via de theme-bestanden te controleren.

---

## 3. Advies

1. **Niet publiceren voordat §2.1 is getest.** Een showroomafspraak is een van de belangrijkste conversies van de site.
2. **Kies één basis.** Er zijn nu drie werkkopieën: *H1-test* (vandaag), *Copy of Hyper* (vandaag bewerkt, nog niet beoordeeld) en het dev theme *PUREDECO — LUXURY B2B — DEVELOPMENT* (25 sep). *H1-test* ligt het dichtst bij live en heeft de minste wijzigingen, dus het laagste risico. Logisch is om dit als basis te nemen en de AVG-fix, de PDP-fixes en de `myshopify`-links uit het dev theme erin over te zetten.
3. Daarna in de preview controleren: homepage (H1 in de broncode), een collectiepagina (zichtbare H1 + kruimelpad), een productpagina via Google-achtige directe link (kruimelpad), en de showroomknoppen.
