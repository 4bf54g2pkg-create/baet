# PUREDECO.NL — VOLLEDIGE ANALYSE DOOR DE OGEN VAN DE KLANT
**Fase 1 · analyse · er is niets gewijzigd**
**Datum:** 5 oktober 2026
**Perspectief:** e-commerce design · UX/UI · luxury branding · CRO · productfotografie · motion · SEO · development

---

## 0. HOE DEZE ANALYSE TOT STAND KWAM

| | |
|---|---|
| **Bron** | Live theme *Hyper* (`188874326282`): alle templates, header/footer/overlay en theme-instellingen; volledige catalogus (71 producten, waarvan 42 actief), 16 collecties, 10 menu's, 11 pagina's, 7 blogartikelen, alle shopbeleidsteksten, verzendprofielen, markten, betaalinstellingen en review-metafields. Alles opgehaald via de Shopify Admin API (alleen lezen). |
| **Gewijzigd** | **Niets.** Geen theme, product, menu of instelling is aangeraakt. |
| **Live theme** | Laatst gewijzigd 22-09-2026 09:13 UTC; sinds de vorige audit dus ongewijzigd. Alle bevindingen uit `01-AUDIT-RAPPORT.md` over de live code gelden nog steeds. |
| **Beperking** | De netwerkpolicy van deze omgeving blokkeert `puredeco.nl` en `cdn.shopify.com`. Ik heb de site dus **niet gerenderd gezien**. Oordelen over code, content, data, structuur en beloftes zijn hard. Oordelen over pixel-spacing, animatie, laadsnelheid en de mobiele weergave zijn afgeleid uit de instellingen en staan in §14 als *te verifiëren in de browser*. |
| **Let op** | Vandaag (5 okt) zijn er in de store twee themes bewerkt door iemand anders: **"Hyper kopie 5 okt (H1-test)"** (nieuw, 11:52 UTC) en **"Copy of Hyper"** (09:40 UTC). Daarnaast staat er nog een niet-gepubliceerd development theme met de P0-fixes uit fase 2. Er wordt dus parallel aan drie kopieën gewerkt. Dat moet afgestemd worden vóór er iets live gaat. |

---

## 1. HET OORDEEL IN ÉÉN ALINEA

PureDeco heeft een **beter product dan de website laat zien**. Een groot formaat (280 × 122 cm), een 8 mm naadloos kliksysteem, doorlopend marmer over drie panelen, een bamboekern, aluminium profielen in vijf kleuren, een eigen showroom en een B2B-programma: dat is een propositie waarmee je je kunt onderscheiden. De website verpakt dat nu als **een gemiddelde Nederlandse actie-webshop**. Een permanente kortingslaag, AI-beelden, tegenstrijdige beloftes, vrijwel geen zichtbare reviews en zichtbare restanten van een demo-thema maken dat een klant die voor het eerst binnenkomt **geen enkele reden ziet om hier te kopen en niet bij een concurrent**. Het verschil met een premium interieurmerk zit niet in een paar CSS-regels, maar in **bewijs, consistentie en rust**.

### Positionering op dit moment

```
goedkoop ─────────────── normale webshop ─────────────── premium merk
                    ▲
                PureDeco nu
          (normale webshop, met signalen richting goedkoop)
```

### Scorekaart (1–10, premium-interieurmaatstaf)

| Onderdeel | Score | Kern |
|---|---|---|
| Merkuitstraling & eerste indruk | **3** | Korting, Klarna en drie topbar-boodschappen domineren; geen merkbelofte in tekst |
| Beeldmateriaal | **3** | 53 van 185 productbeelden AI-gegenereerd; geen enkele productvideo; hero is AI-beeld met tekst erin |
| Vertrouwen & social proof | **2** | 4 van 42 producten hebben een review (elk 1); drie verschillende scores op de site; anonieme testimonials |
| Consistentie van beloftes | **2** | Retour 30 of 90 dagen? Gratis verzending vanaf € 500 of € 600? Samples gratis of € 6,95? |
| Navigatie & informatiearchitectuur | **4** | "ACTIE" eerst; "Wandpanelen" linkt naar de verkeerde collectie; geen materiaalstructuur |
| Productpagina | **4** | Goede basis (tabs, metafields, sticky ATC), maar geen m²-prijs, geen calculator, geen specs, geen reviews |
| Collectiepagina's | **3** | Geen H1, geen kruimelpad, geen hero; verborgen ChatGPT-code in de omschrijving |
| Winkelmand & checkout | **5** | Shopify-checkout, wallets en verzendbalk zijn solide; € 65 verzendkosten zonder uitleg is een grote drempel |
| Catalogusdata | **3** | 37 van 42 actieve producten zonder volledige SKU; negatieve voorraad; inconsistente varianten |
| SEO-fundament | **5** | Meta's sterk verbeterd sinds september; H1's, kannibalisatie en interne links nog niet |
| Techniek & stabiliteit | **4** | Debugcode, JS-fouten en een AVG-lek staan nog live (opgelost in dev theme, niet gepubliceerd) |

---

## 2. DE EERSTE 10 SECONDEN — ALS KLANT BINNENKOMEN

Dit is wat een bezoeker op de homepage achter elkaar te zien krijgt, gereconstrueerd uit de live configuratie:

| # | Wat de klant ziet | Wat de klant denkt |
|---|---|---|
| 1 | **Topbar** met drie wisselende berichten: *"Gratis verzending vanaf 600,-"* · *"Klanten beoordelen ons gemiddeld met een 9,4 op 10."* · *"Betaal later met Klarna"*. Plus e-mail en telefoonnummer. | "Een webshop die op prijs en betaalgemak verkoopt." `600,-` is marktkraam-notatie, geen merknotatie. |
| 2 | **Header** met twee CTA-knoppen (*Showroomafspraak*, *Gratis advies*) en een menu dat begint met **ACTIE**. "Wandpanelen" twinkelt met een sterretje-animatie. | Drie dingen roepen tegelijk om aandacht. Het eerste woord in het menu is korting. |
| 3 | **Hero**: één beeld (`ChatGPT_Image_8_sep_2026…png`, AI) waarin de tekst is ingebakken, plus de knop *Bekijk de collectie*. Er is geen kop in HTML. | Mooi plaatje, maar wat is PureDeco? De belofte is niet scanbaar, niet vertaalbaar en op mobiel klein. |
| 4 | **USP-balk**, als eerste: *"Betaal flexibel met Klarna"*, daarna *"Naadloze afwerking"*, *"Snelle levering"*, *"90 dagen retourbeleid"*. | Het eerste argument van het merk is gespreid betalen. Bij een product van € 100–600 zegt dat "duur, maar je kunt het afbetalen". |
| 5 | Slider *"Breed assortiment wandpanelen"* met Hout, Japandi, Leer en Marmer. Die linken naar filter-URL's op `/collections/all`. | Werkt, maar landt op een generieke "alle producten"-pagina. |
| 6 | *"Alle voordelen van bamboepanelen op een rij"*: zes claims (waterafstotend, E0, buigbaar, UV, B1, montage). | Interessant, maar geen bewijs: geen certificaat, geen test, geen foto. |
| 7 | *"Onze Bestsellers"*: 24 producten. | Er zijn ~30 panelen, waarvan er 24 "bestseller" zijn. Dat is geen selectie meer. |
| 8 | B2B-slide *"Groei samen met PureDeco"* → *Partner worden*. | Een consument leest dit als ruis. |
| 9 | *"8 mm naadloze klik-systeem panelen"* met een badge die is ingesteld op **"Save 99$"**. | Als die badge rendert: dollarteken op een NL-site, een demo-restant. *(verifiëren)* |
| 10 | *"Nieuwe Collectie"*, *"Gratis interieuradvies"* met badge **"garace - where design meet function -"**, Instagram-feed, feature cards, contactblok. | Na tien secties weet de klant nog steeds niet waarom PureDeco beter is dan de bouwmarkt of een Bol.com-aanbieder. |

**Conclusie:** de homepage is een **opsomming van alles wat het thema kan**, niet een verhaal. Een premium merk vertelt in drie schermen: *wie we zijn → wat het materiaal is → bewijs dat het werkt → kies je oppervlak*.

---

## 3. WAAROM ZOU IEMAND HIER KOPEN? — DE ONDERSCHEIDENDE KRACHT

### Wat PureDeco écht heeft (en wat concurrenten vaak niet hebben)

| Troef | Waar het nu staat | Zichtbaarheid |
|---|---|---|
| **Groot formaat 280 × 122 cm** (3,4 m² per paneel) | Alleen als variantwaarde | ❌ Niet gecommuniceerd. Dit is hét verschil met smalle lamellen en PVC-stroken. |
| **8 mm naadloos kliksysteem** | USP-balk, één homepageblok, collectie | ⚠️ Genoemd, nooit uitgelegd met beeld of video |
| **Doorlopend marmer** (3 panelen = één ononderbroken plaat van 280 × 366 cm) | Productnaam | ❌ Het meest luxe product van de catalogus, zonder eigen verhaal |
| **Prints die per paneel verschillen** (geen herhaling) | Diep in de productomschrijving | ❌ Dé reden waarom het er echt uitziet. Onzichtbaar. |
| **Showroom in Herwen** | Header-CTA, showroompagina | ⚠️ Er is geen foto van de echte showroom of het team |
| **Aluminium profielen in 5 kleuren** | Accessoires | ⚠️ Wordt niet als systeem verkocht ("de complete wand") |
| **3 jaar garantie** | PDP-iconen, retourbeleid | ⚠️ Genoemd, niet uitgelegd |
| **Bamboekern** | Overal | ⚠️ Overgecommuniceerd, zie hieronder |
| **B2B / maatwerk toplagen** | Feature card, `/pages/form` | ❌ Geen enkel project als bewijs |

### Het eerlijke materiaalverhaal: een risico dat nu onder de radar zit

De eigen teksten van PureDeco zeggen op verschillende plekken iets anders over hetzelfde paneel:

- Productmetafield (alle hout/leer/Japandi/art/beton-panelen): *"De toplaag bepaalt de uitstraling en structuur, gevolgd door **een laag gerecycled PVC**, een stevige bamboekern en een gerecyclede onderlaag."*
- Product-FAQ: *"een toplaag van **gerecycled PVC**"*
- Over-ons: *"bamboekern en een **gerecyclede PVC-toplaag**"*
- Homepage feature card: *"De toplagen worden vervaardigd uit **100% gerecyclede materialen**"*
- Over-ons (Engelse, actieve tekst): *"bamboo, **FSC-certified wood**, and recycled felt"*
- Homepage: *"Milieuvriendelijk door bamboekern (E0)"*, *"Brandvertragend (B1)"*, *"UV-bescherming – dus geen verkleuring"*

**Waarom dit telt:** een premium klant (en zeker een architect) vraagt naar de opbouw. Als de site "bamboe, duurzaam, milieuvriendelijk" roept en het product een PVC-toplaag heeft, voelt dat als verbloemen zodra de klant het ontdekt. Daarnaast vallen claims als "100% gerecycled", "milieuvriendelijk", "FSC" en "B1" onder de regels voor duurzaamheids- en productclaims (ACM-leidraad, EU-regels tegen greenwashing): **ze moeten met een certificaat of testrapport onderbouwd kunnen worden**.

**Premium-advies (richting, nog niet uitvoeren):** draai het om. Communiceer de opbouw open en technisch, met een doorsnede-illustratie: *"Hybride wandpaneel: bamboekern voor stabiliteit en buigbaarheid, gerecyclede toplaag voor een vocht- en krasbestendig oppervlak."* Zet onder elke claim het document. Dat oogt professioneler dan "milieuvriendelijk" en is juridisch veilig.

---

## 4. TEGENSTRIJDIGE BELOFTES — DE GROOTSTE VERTROUWENSKILLER

Een premium merk zegt overal hetzelfde. PureDeco zegt nu op verschillende plekken iets anders:

| Onderwerp | Wat de site zegt | Waar | Wat werkelijk geldt |
|---|---|---|---|
| **Retourtermijn** | **90 dagen** retourbeleid / tevredenheidsgarantie / bedenktijd | Homepage-USP, PDP-iconen, quick-view, collectie-marquee, SEO-meta *Hout* | **30 dagen** (retourbeleid + FAQ) |
| **Retour geopend product** | "Geopende of gebruikte producten kunnen niet worden geretourneerd" | Retourbeleid | ⚖️ Bij koop op afstand mag een consument een product uitpakken om het te beoordelen. Laat deze zin **juridisch toetsen**. |
| **Gratis verzending** | vanaf **€ 600** | Topbar, cart, PDP | ✅ Klopt voor **NL** |
| | vanaf **€ 500** | Quick-view | ❌ |
| | — | België | ❌ **België betaalt altijd € 95**, ook boven € 600. De topbar belooft het Belgische bezoekers wel. |
| **Verzendkosten onder € 600** | Niet zichtbaar op de site | — | **€ 65** (NL) / **€ 95** (BE). Staat alleen in het beleid en in de checkout. |
| **Samples** | "Je ontvangt de samples **gratis** binnen 2 werkdagen" | Samplepagina | Samples € 0, verzending **€ 6,95** (NL) / **€ 9,95** (BE). Elders staat wél "alleen verzendkosten". |
| **Klantbeoordeling** | **9,4 / 10** | Topbar | Geen bron vermeld |
| | **4,9 / 5** (Google Reviews) | Collectie *Wandpanelen* | Geen widget, geen link |
| | **4,8 / 5** | Showroompagina | Geen bron vermeld |
| | 4 producten met **1 review** | Judge.me | De enige meetbare reviews op de site |
| **Levertijd** | "Op voorraad. Binnen 3-6 werkdagen in huis" | PDP (fallback voor **elk** product) | Alle 83 varianten staan op **"doorverkopen bij geen voorraad"**. Niet op voorraad = **tot 10 weken** volgens het beleid. |
| | "Voor 12:00 besteld" | Theme-instelling | Niet in lijn met 3-6 werkdagen |
| **WhatsApp** | `wa.me/31316700214` | Homepage | Twee verschillende nummers |
| | `wa.me/31850870490` | Productpagina | |
| **Profielkleuren** | zwart, **grijs**, goud, brons, wit | FAQ | Antraciet, zwart, wit, brons, goud (product) |
| **Schade bij levering** | Antwoord gaat over terugbetaling na retour | FAQ | Verkeerd antwoord gekopieerd |

**Waarom dit zwaarder weegt dan elk designprobleem:** een klant die € 1.500 aan wandpanelen overweegt, zoekt actief naar retour- en verzendinformatie. Vindt hij twee verschillende antwoorden, dan is het vertrouwen weg, ongeacht hoe mooi de site is. En bij een retourgeschil is "90 dagen" op de homepage bindend.

---

## 5. ANALYSE PER ONDERDEEL

Legenda perceptie: 🔴 goedkoop · 🟡 normale webshop · 🟢 premium

### 5.1 Homepage 🔴🟡
- **12 secties**, waarvan 2× een slideshow, 2× een featured collection met placeholder-instellingen (*"Collections"*, *"Button label"*), een Instagram-feed met de tekst *"…wie weet staat jouw foto binnenkort op onze website!!"* (dubbel uitroepteken).
- **Geen `<h1>`.** De belofte zit in het hero-beeld.
- De sectie *"Wandpanelen specialist voor interieur & projecten"* claimt projecten voor *"hotels, ziekenhuizen en overheidsinstanties"*. Er is nergens één project te zien. Een claim zonder bewijs verzwakt het merk meer dan dat hij helpt.
- De homepage-feature card *"Dé wandpanelen specialist van Nederland"* is een superlatief zonder onderbouwing.
- Typografie in die sectie: `heading_weight 700`, `title_weight 800`, zwart op wit. Zwaar en schreeuwend.

### 5.2 Navigatie & header 🔴
- **Desktopmenu:** `ACTIE · Wandpanelen · Akupanelen · Accessoires · FAQ`.
  - "ACTIE" eerst: korting is het eerste wat het merk aanbiedt.
  - **"Wandpanelen" linkt naar `/collections/bamboepanelen-samples`** (titel "Bamboepanelen"), niet naar `/collections/wandpanelen`. Beide bevatten vrijwel dezelfde 31–32 producten.
  - Voorloopspaties in `" Accessoires"` en `" FAQ"`.
  - Geen mega-menu, geen materiaalnavigatie (Hout · Marmer · Japandi · Leer · Beton · Travertin · Art), geen ingang voor inspiratie, showroom, samples of zakelijk.
- **Mobiel menu (9 items):** typefouten **"Zakelijik"** en **"Verkoopparters"**; anders dan desktop.
- **Header-CTA's:** twee knoppen naast het menu, plus een twinkelend sterretje op "wandpanelen". Drie concurrerende signalen.
- **Topbar:** drie roterende boodschappen + contactgegevens. Premium merken hebben één rustige regel, of geen.

**Wat een klant mist:** "Ik wil een marmeren wand." Er is geen pad *Marmer → mat/glanzend/doorlopend*. Hij moet in "Wandpanelen" door 31 kaarten scrollen.

### 5.3 Collectie- en categoriepagina's 🔴
- **Geen kruimelpad, geen collectie-hero, geen `<h1>`** (de rich-text-kop rendert als `<h2>`).
- **In vier collectieomschrijvingen staat geplakte ChatGPT-interface-HTML**: `Bamboepanelen`, `Akupanelen` (samples), `Actie` en `Nieuwe Collectie`. Daarin onder meer `data-message-model-slug="gpt-5-5"`, een leeg chatformulier (`<form data-type="unified-composer">`), `id="thread-bottom-container"` en in *Nieuwe Collectie* een wrapper met de klassen **`flex h-svh w-screen`** (= een blok van een volle schermhoogte en -breedte). Dit staat in de broncode van live pagina's. Gevolgen:
  - iedereen die de broncode bekijkt (concurrent, journalist, Google) ziet dat de tekst uit ChatGPT is geplakt;
  - afhankelijk van welke CSS-klassen het thema toevallig kent, kan dit **lege ruimte of layoutfouten** geven; op *Nieuwe Collectie* het grootste risico *(verifiëren)*;
  - een `<form>` en `<main id="main">` midden in de pagina botsen met de echte pagina-structuur (dubbele `id="main"`, toegankelijkheid).
- **Bestsellers = 24 van ~30 panelen.** Geen curatie.
- **"Actie" (8) én "Sale" (9)**: twee kortingscollecties.
- **Kannibalisatie:** `wandpanelen` (31) vs `bamboepanelen-samples` (32); `akupanelen` (2) vs `akupanelen-samples` (6).
- **Producten die in geen enkele hoofdcollectie staan:** *Wandpaneel metaal* en *Wandpaneel solide kleuren* zijn actief, maar zitten niet in "Wandpanelen". Een klant die metaal of een effen kleur zoekt, vindt ze via het menu niet.
- **Lege collectie** `/collections/samples` (0 producten) is gepubliceerd.
- Onderaan een lopende marquee met *"90 dagen bedenktijd"* (fout, zie §4) en één leeg tekstblok.

### 5.4 Productpagina 🟡
**Wat goed is:** tabs met materiaal/duurzaamheid/montage uit metafields, sticky add-to-cart, "Vaak samen gekocht", sample-app, betaalinformatie, prijs incl. btw vermeld.

**Wat een premium klant mist:**

| Mist | Waarom het telt |
|---|---|
| **Prijs per m²** | € 99,95 per paneel van 280 × 122 cm = **€ 29,26/m²**. € 139,95 voor 260 × 122 cm = **€ 44,12/m²**. Klanten vergelijken per m² met stucwerk, tegels en lamellen. Nu moet hij zelf rekenen, en de formaten verschillen per product. |
| **Calculator "hoeveel panelen heb ik nodig?"** | De belangrijkste vraag bij wandbekleding. De onafgemaakte pagina `/pages/ai-visualizer` ("…inclusief het aantal panelen dat je nodig hebt") staat niet live. |
| **Specificatietabel** | Afmeting, dikte, gewicht, systeem, opbouw, brandklasse, emissieklasse, buigstraal, toepassing, artikelnummer. Nu verspreid in proza, in USP-lijstjes of nergens. |
| **Reviews** | Het Judge.me-reviewwidget op de PDP staat **uit**; alleen de sterrenbadge staat aan (en toont bij 38 van 42 producten niets). De testimonialsectie staat ook uit. |
| **Video** | **0 van 42** actieve producten heeft een video of 3D-model. Voor een product dat draait om textuur, glans, klikken en buigen is dit de grootste gemiste kans. |
| **Montage-uitleg in beeld** | Montage staat als tekst in een tab. |
| **Echte voorraad- en levertijdinformatie** | Fallback "Op voorraad. Binnen 3-6 werkdagen in huis" verschijnt voor elk product, ook bij voorraad −58. |
| **B2B-route** | Geen "projectofferte", geen downloads. |

**Daarnaast:**
- 4 iconen met 2 foutieve/inconsistente beloftes (*90 dagen*, *Leverbaar binnen 3-6 werkdagen*).
- Klarna-blok met berekening "Betaal in 3 delen" direct onder de prijs: koopkracht-framing.
- Betaaliconen: Maestro · Mastercard · PayPal · Visa. **iDEAL ontbreekt in de iconen**, terwijl dat in Nederland de dominante betaalmethode is *(verifiëren of iDEAL actief is in de checkout)*.
- Contactblok op de PDP linkt naar `https://puredeco-3.myshopify.com/faqs` (ander domein én dode link).
- Variantkiezer heeft het label `size_title: color` (Engels).

### 5.5 Varianten & productstructuur 🔴
De catalogus is half omgebouwd van "één product met kleurvarianten" naar "één product per decor", en die twee systemen staan nu naast elkaar:

| Groepsproduct (actief) | Losse decorproducten (actief) |
|---|---|
| *Wandpaneel hout* (9 varianten: 602, 607, 615, 810, 811, 812) | *Wandpaneel Hout 602*, *607*, *615*, *810*, *811*, *812* |
| *Wandpaneel Art* (840–843, **lege omschrijving**, metafield bevat letterlijk `field_674440a04df8c`) | *Wandpaneel Art 840*, *841*, *842*, *843* |
| *Wandpaneel metaal* (663, 664) | *Wandpaneel Metaal 663* |
| *Wandpaneel solide kleuren* (857, 656–659; **"Chaste" twee keer**: 857 én 657) | (alle losse versies op concept) |

Gevolg: in zoekresultaten en "alle producten" ziet een klant hetzelfde paneel twee keer, met mogelijk een andere prijs en andere foto's.

**Optienamen en -waarden zijn niet uniform:**
- Formaat heet `Formaat` of `Afmeting`; dikte heet `Afwerking` of `Dikte`.
- Waarden: `280x122` · `280 x 122` · `280 × 122 cm` · `280 cm x 122 cm`; en `8mm Naadloos` · `8mm (Naadloos)` · `8mm naadloos` · `8mm (naadloos)` · `5mm` · `5mm Stomp` · `5mm stomp`.
- Shopify-filters groeperen op exacte optienaam en -waarde. **Het filter "8 mm naadloos" valt daardoor uiteen in vier aparte waarden en twee aparte filters.** De belangrijkste keuze van de klant (stomp of naadloos) is dus niet goed te filteren.

**Prijsfouten:**
- *Travertine Ivory 851*: doorgestreepte prijs **€ 169,95 is lager dan de verkoopprijs € 179,95**.
- *Japandi 823 Taupe Dark*: doorgestreepte prijs = verkoopprijs (€ 179,95).

### 5.6 Afbeeldingen 🔴
- **185 productbeelden** op 42 actieve producten (gemiddeld 4,4). Een premium interieurmerk zit op 8–12: frontaal, detail/macro, strijklicht, roomscene, montage, dikte/profiel, schaal met persoon, kleurvergelijking.
- **53 van 185 (29%) zijn AI-gegenereerd** (bestandsnaam `generated_…`, alt-tekst *"… Renderique Photo 1"*). **27 van 42 producten** hebben minstens één AI-beeld; bij **18 producten** is de helft of meer AI.
- Alt-teksten als *"632. Mat marmer - White Rock - Renderique Photo 1"* lekken de toolnaam naar Google Afbeeldingen en screenreaders.
- **Formaatmix:** 162 vierkant, 13 staand, 10 liggend; resoluties 864–2560 px door elkaar. In een productraster geeft dat onrustige kaarten.
- *Japandi 824 Taupe* heeft als hoofdbeeld `624.jpg`. *Japandi 620* toont de foto van 619 (uit de vorige audit, nog niet gecontroleerd of hersteld).
- Hero- en collectiebeelden zijn PNG's van 1,5–5,9 MB, veelal AI.

**Oordeel fotograaf:** een AI-beeld van een wandpaneel laat zien hoe een wand *zou kunnen* zijn. Een klant die € 1.000+ uitgeeft, wil zien hoe het *is*: het licht op de nerf, de naad (of het ontbreken ervan), de rand bij een stopcontact. Dat is precies wat AI niet geloofwaardig levert, en daarom zijn echte beelden hier het sterkste premiumsignaal dat er is.

### 5.7 Video & motion 🔴
- **0 productvideo's.** Eén YouTube-embed op de over-ons-pagina. De homepageblok *custom-content* heeft een lege video-slot.
- Motion die wél aanwezig is, is van het verkeerde soort: twinkelend sterretje in het menu, lopende marquee-banden, roterende topbar, parallax-opties.
- **Ontbrekend, met de meeste conversiewaarde:** 6–10 seconden loops van (1) klikken van twee naadloze panelen, (2) buigen van een paneel, (3) strijklicht over een textuur, (4) doorlopend marmer dat over drie panelen aansluit.

### 5.8 CTA's & buttons 🟡
- Twee knopsystemen tegelijk live: thema-knoppen (0 px radius) en `.pd-btn` (pil, `#55884d`). Alle `a.pd-btn.pd-btn-primary` worden via JS onderschept en openen de afsprakenmodule.
- `buttons_transform: capitalize` → *"Bekijk De Collectie"*.
- Placeholder *"Button label"* staat in drie secties in de configuratie.
- Te veel primaire knoppen per scherm (header: 2, hero: 1, elke sectie: 1). Niets stuurt.

### 5.9 Kleuren, typografie, iconen, spacing 🟡
*(Uitgebreid in `01-AUDIT-RAPPORT.md` §B–C en het dev-designsysteem; hier alleen de klantimpact.)*
- Eén lettertype (Instrument Sans) voor koppen én tekst, veel 700/800-gewicht → oogt als SaaS of sportshop, niet als interieurmerk.
- Demo-rood `#c4301c` als accent; twee kapotte kleurschema's (wit op bijna-wit, zwart op zwart).
- Emoji als iconen (📞 ✉️ 📍 in de footer, ✌🏼 in de cart, ⭐ in collectietekst).
- `heading_mobile_scale: 70` → koppen op mobiel 30% kleiner.
- Sectieritme 40–60 px; premium interieur werkt met 96–140 px.

### 5.10 Cards 🟡
- Productkaarten met sale-badge (*percentage*), quick-view-knop, kleurswatches, titel tot 2 regels.
- Titels als *"Wandpaneel Concrete Smoke 691 | Betonlook | Puredeco"* en *"Wandpaneel Hout 811 Walnut Classic 8 mm Naadloos"* maken kaarten ongelijk lang en lezen als SEO-titels.
- **22 van 42 actieve producten (52%) tonen een doorgestreepte prijs.** Als de helft van de collectie permanent "in de aanbieding" is, leest de klant: de normale prijs is fictief.

### 5.11 Banners & USP's 🔴
- USP-volgorde op de homepage: Klarna → naadloos → levering → retour. **Kwaliteit, materiaal en bewijs ontbreken.**
- Drie plekken met USP-rijen die elkaar herhalen (topbar, homepage-balk, PDP-iconen, marquee) met onderling verschillende cijfers.
- Kortingsframing op vier niveaus: menu (ACTIE), cards (badges), footer (*"5% korting op je eerste bestelling"*), PDP (Klarna in 3 delen).

### 5.12 Reviews, trust & social proof 🔴
- **Judge.me: 4 reviews in totaal** zichtbaar op productniveau (Eindprofielen, Marmer 666, Japandi 621, Montagekit — elk 1× 5 sterren).
- Het PDP-reviewwidget staat **uit**.
- De testimonials (samplepagina, over-ons) zijn **anoniem**, met als kop telkens het woord *"Testimonials"*, en zijn identiek op drie pagina's. Zo zien neptestimonials eruit, ook als ze echt zijn.
- Drie verschillende scores (9,4/10 · 4,9/5 · 4,8/5) zonder bron of link.
- Geen keurmerk (Thuiswinkel Waarborg, WebwinkelKeur, Trusted Shops), geen certificaatlogo's, geen pers, geen "bekend van", geen projectlogo's.
- Positief: KvK, btw-nummer, adres, telefoon, IBAN en ODR-link staan correct in de juridische pagina's.

**Wat dit kost:** voor een onbekend merk met een product van € 100–600 per stuk is social proof de belangrijkste conversiefactor na prijs. Er staan nu bijna nul geloofwaardige signalen.

### 5.13 Verzend- en retourinformatie 🔴
- **€ 65 verzendkosten onder € 600** is voor groot-formaat panelen begrijpelijk (palet/koerier), maar **wordt nergens uitgelegd of getoond vóór de checkout**. Rekenvoorbeeld: 2 panelen à € 99,95 = € 199,90 + € 65 = **+33%**. Zonder uitleg ("transport op maat voor platen van 2,8 m, met afspraak") voelt dat als een valkuil en verlaat de klant de checkout.
- België betaalt altijd € 95 (zie §4).
- Een internationale verzendzone (VS, Australië, Japan, VK, …) staat op **€ 19,95 vast**, goedkoper dan Nederland. Er is geen actieve markt voor die landen, dus waarschijnlijk werkt deze zone niet, maar als hij ooit actief wordt, verkoop je panelen van 2,8 m naar Australië voor € 19,95. **Opruimen.**
- Duitsland staat als markt op *concept*. Voor het doel "één van de beste interieurwebshops van Europa" ben je nu feitelijk een **NL + BE**-webshop.
- Er is één verzend- en retourpagina, maar die heet in het menu *"Verzending & Retourneren"* en linkt naar het retourbeleid (`/policies/refund-policy`, titel "Terugbetalingsbeleid").

### 5.14 Productinformatie & content 🟡
- Productomschrijvingen zijn 120–260 woorden, consistent opgebouwd. Prima basis.
- **33 van 42** omschrijvingen bevatten ChatGPT-kopieerartefacten (`data-start` / `data-end`-attributen).
- De materiaal-tab is bij 30+ producten **letterlijk dezelfde tekst**. Generiek, en duplicate content.
- Blog: 7 artikelen, allemaal geplaatst op **9 maart 2026 tussen 05:45 en 05:57** (12 minuten). Sindsdien niets. Titel en URL van *"5 Creatieve toepassingen van bamboepanelen"* staan op de handle `tips-voor-het-onderhouden-van-je-bamboepanelen-1`.
- De vier "inspiratie showcase"-artikelen (keuken Pandora Slate, kantoor Japandi, uitbouw leer, wc marmer) zijn het begin van een projectlaag. Dat zijn de meest waardevolle stukken content op de site *(verifiëren: echte foto's?)*.

### 5.15 Over ons, showroom, zakelijk 🔴
- **Over ons** rendert actief een badge **"garage - where design meets function -"** (vier keer), en heeft een tekstblok met Engelse tekst (*"What we stand for"*, *"How it started"*) dat uit staat, terwijl dezelfde tekst in het Nederlands wél staat. Uitgeschakeld maar aanwezig: *"Meet Our Team"* met de demo-namen *Nicootitto, Jake Nakos, Diana Simun, Quaid Lagan*, een FAQ over een *"Lace Contour Plunge Bra"*, en *"Bow Chair"*-teksten.
- **Geen echte mensen.** Geen oprichter, geen team, geen foto van de showroom. Voor een merk dat "persoonlijk advies van echte specialisten" belooft, is dat het grootste gat in de over-ons-pagina.
- **Zakelijk:** pagina heet `form`, URL `/pages/form`. Verkooppartners op `/pages/verkoopparters` (typefout in URL en titel).

### 5.16 Footer 🟡
- Nieuwsbrief met *"5% korting"* als eerste blok.
- Contactblok met emoji; e-mailadres zonder `mailto:`.
- Een juridisch footermenu bestaat (`juridisch`) maar is in het live theme niet gekoppeld *(in dev theme wel)*.
- Geen betaal- en keurmerklogo's, geen showroomadres met openingstijden en route.

### 5.17 Winkelmand & checkout 🟡🟢
- **Goed:** cart-drawer, verzenddoel-balk, verzendkostencalculator in de winkelwagen, notitieveld, Shopify-checkout met Shop Pay, Apple Pay en Google Pay, Klarna.
- **Minder:** *"✌🏼 GRATIS VERZENDING BOVEN €600!"* (caps + emoji) in de drawer; *"Pair Well With"* en *"Not sure where to start?"* in het Engels; geen upsell van de juiste profielen en kit bij panelen (het "complete wand"-moment ontbreekt in de cart).
- **Te verifiëren in de browser:** iDEAL zichtbaar en als eerste? Bedrijfsnaam/btw-veld voor B2B? Afleverafspraak bij palletlevering?

### 5.18 Zoeken & filters 🟡
- Standaard Shopify-zoekfunctie, zonder eigen configuratie in het template.
- Zoekresultaten tonen groepsproducten en decorproducten door elkaar (zie §5.5).
- Filters zijn versnipperd door inconsistente optienamen (zie §5.5).
- Materiaalfilter werkt via metafield `custom.tag_filter` (Hout, Japandi, Leer, Marmer). Dat is een goede basis.
- **Ontbrekend:** filters op *afwerking (mat/glans)*, *kleurtoon (licht/midden/donker)*, *toepassing (badkamer/keuken/plafond)*, *systeem (stomp/naadloos)* als één schoon filter.

### 5.19 SEO 🟡
**Sterk verbeterd sinds september:** 13 van 16 collecties hebben nu een SEO-titel en meta-description, met goede zoekwoorden. Blijft open:
- Geen `<h1>` op home en collecties (live).
- Kannibalisatie *wandpanelen* vs *bamboepanelen-samples*; *akupanelen* dubbel; *actie* vs *sale*.
- Homepage linkt naar filter-URL's in plaats van naar de echte materiaalcollecties (`/collections/hout-1`, `/japandi`, `/leer`, `/doorlopend-marmer`, `/kunst`).
- Producten: **4 van 42** hebben een eigen SEO-titel/description; `productType` is overal leeg.
- AI-tooling in alt-teksten (`Renderique Photo 1`).
- ChatGPT-HTML in collectieomschrijvingen (onnodige DOM, verdachte signalen).
- Blog stil sinds maart; geen materiaal- of toepassingsgidsen ("wandpanelen badkamer", "marmerlook wand keuken", "naadloze wandpanelen vs stucwerk") — precies de zoekvragen waarop een specialist hoort te ranken.

### 5.20 Snelheid & techniek 🔴 *(code-bevindingen, live sinds maart; opgelost in het dev theme, nog niet gepubliceerd)*
- `alert('yes')` bij formulierverzending; twee JS-fouten op elke pagina (`booking_cta` zonder null-check); `console.log` van het e-mailadres van ingelogde klanten (AVG).
- Swatches laden de **master-afbeelding** (tot 2048 px) voor een rondje van 30 px.
- ~204 KB render-blocking CSS, ~329 KB JS vóór apps; acht apps met eigen scripts (Judge.me, Product Samples, Samita, Instafeed, BookEasy, Google, Facebook, Bol.com).
- Hero en sfeerbeelden als PNG van 1,5–5,9 MB.
- `setTimeout`-hacks van 2, 5 en 15 seconden.

### 5.21 Mobiel & desktop *(afgeleid uit instellingen — verifiëren)*
- Mobiele sticky bar staat uit; sticky add-to-cart staat aan (goed).
- Topbar met drie roterende teksten + contactgegevens neemt op mobiel kostbare hoogte.
- Koppen op 70% (`heading_mobile_scale`).
- Mobiele hero is een aparte AI-PNG (941 × 1671, 2,1 MB) met ingebakken tekst, dus de leesbaarheid hangt af van het beeld.
- Logo-instellingen tot 400 px breed op desktop.

---

## 6. CATALOGUSDATA IN CIJFERS

| Meting | Waarde |
|---|---|
| Producten totaal / actief / concept / unlisted | 71 / 42 / 27 / 2 |
| Actieve producten met video of 3D | **0** |
| Gemiddeld aantal beelden per actief product | 4,4 (min 1, max 13) |
| AI-gegenereerde productbeelden | **53 / 185 (29%)** |
| Actieve producten met volledige SKU's | **5 / 42** |
| Actieve producten met eigen SEO-titel | 4 / 42 |
| Actieve producten met doorgestreepte prijs | **22 / 42 (52%)** |
| Varianten op "doorverkopen bij geen voorraad" | **83 / 83** |
| Producten met negatieve voorraad | 6 (o.a. *Hout 810*: −58, *Hout 812*: −52, *Japandi 620*: −4) |
| Omschrijvingen met ChatGPT-kopieersporen | 33 / 42 |
| Collecties met geplakte ChatGPT-interface-HTML | 4 / 16 |
| Producten met ≥ 1 review | 4 / 42 |
| Concept-producten met prijs € 0,00 | 18 |

**Over die negatieve voorraad:** −58 en −52 betekent dat er ten minste 110 panelen verkocht zijn die er niet waren. Dat zijn klanten die "binnen 3-6 werkdagen" lazen en tot 10 weken wachten. Dat is de bron van negatieve reviews die nooit verschijnen, en van retouren en klachten.

---

## 7. PRIJS & PERCEPTIE

1. **Permanente korting = geen echte prijs.** 52% van de producten doorgestreept, twee kortingscollecties, ACTIE als eerste menu-item, 5% nieuwsbriefkorting. Een premium klant leest: *"De echte prijs is lager, ik wacht op de volgende actie."*
2. **Juridisch aandachtspunt:** bij een prijsverlaging moet de doorgestreepte "van"-prijs de laagste prijs van de afgelopen 30 dagen zijn (Omnibus-richtlijn). Bij doorlopend doorgestreepte prijzen is dat lastig te verdedigen. *Laat dit toetsen.*
3. **Prijsanker ontbreekt.** Zonder m²-prijs vergelijkt de klant € 139,95 met een PVC-strook van € 15 bij de bouwmarkt. Met m²-prijs, en de vergelijking met stucwerk/tegels inclusief arbeid, wordt PureDeco ineens logisch.
4. **Klarna voorop** bij een product van € 100–600 signaleert "duur voor jou". Premium merken tonen gespreid betalen in de cart, niet als eerste USP.

---

## 8. DE VIER VRAGEN, BEANTWOORD

### Waarom zou iemand hier kopen en niet bij een concurrent?
**Op dit moment: omdat het toevallig bij hen in Google bovenaan stond, of omdat de prijs in de actie goed was.** De echte redenen (groot formaat, naadloos klikken, prints zonder herhaling, doorlopend marmer, showroom, profielsysteem, garantie) staan er wel, maar verstopt, ongeordend en zonder bewijs. De site concurreert nu op prijs en betaalgemak, precies het terrein waar Bol.com en de bouwmarkt winnen.

### Goedkoop product, normale webshop of premium interieurmerk?
**Normale webshop, met duidelijke signalen richting goedkoop.** De goedkoop-signalen: ACTIE als eerste menu-item, 52% doorgestreept, emoji en caps, "600,-", anonieme testimonials, AI-beelden, demo-resten ("garage – where design meets function", "Save 99$"), tegenstrijdige cijfers. De premium-signalen: het product zelf, de showroom, de prijsklasse, het naadloze systeem. Die laatste zijn sterk genoeg om op te bouwen.

### Wat maakt PureDeco onderscheidend?
1. **Groot formaat, naadloos geklikt**: één wand, geen lamellen, geen voegen.
2. **Echtheid van het oppervlak**: prints die per paneel verschillen; doorlopend marmer over drie platen.
3. **Showroom + persoonlijk advies** in Herwen: tastbaar, menselijk.
4. **Compleet systeem**: paneel + profiel in 5 kleuren + kit, met 3 jaar garantie.
5. **B2B-capaciteit**: maatwerk toplagen, partnerprogramma.

Dit is genoeg voor een merk. Het moet alleen de **hoofdrol** krijgen in plaats van korting.

### Waar voelt de website gedateerd, druk, goedkoop of onduidelijk?

| Gedateerd | Druk | Goedkoop | Onduidelijk |
|---|---|---|---|
| Twinkelende sterretjes, marquees | Topbar met 3 boodschappen + contact | ACTIE eerst, 52% doorgestreept | Retour 30 of 90 dagen |
| Emoji als iconen | Header met 2 CTA's + menu | "600,-", caps + ✌🏼 | Verzendkosten € 65 nergens vooraf |
| Blog stil sinds maart | 12 homepage-secties | AI-beelden | Welke collectie is "Wandpanelen"? |
| Demo-restanten | 4 USP-rijen met andere cijfers | Anonieme testimonials | Stomp vs naadloos: filter versnipperd |
| Eén font, alles vet | Klarna overal | 5% nieuwsbriefkorting als eerste footerblok | Drie verschillende reviewscores |

---

## 9. WAT DE BESTE INTERIEURMERKEN IN EUROPA ANDERS DOEN

Patronen die premium materiaal- en interieurmerken gemeen hebben, afgezet tegen PureDeco:

| Patroon bij premium | PureDeco nu |
|---|---|
| **Eén zin merkbelofte**, in HTML, groot, met veel ruimte | Tekst in een AI-beeld |
| **Materiaal als held**: macro-fotografie, strijklicht, textuur die je bijna voelt | 1080 px vierkante plaatjes, deels AI |
| **Projecten als bewijs**: echte ruimtes, met locatie, ontwerper en toegepaste materialen | Geen enkel project |
| **Rust**: veel wit, weinig kleur, max. één primaire knop per scherm | 12 secties, overal knoppen |
| **Specificeerbaarheid**: artikelnummer, datasheet, certificaten om te downloaden | 5/42 SKU's, geen downloads |
| **Samples als premium ervaring**: een mooie samplebox, gecureerd per stijl | Sample-app met *"+ €0,00 inc. BTW"* |
| **Mensen**: oprichter, team, ambachtslieden, met naam en gezicht | "Team member 1/2/3", demo-namen |
| **Prijs met vertrouwen**: geen doorstrepingen, wel duidelijke m²-prijs en transparante bezorging | Permanente korting, verzendkosten verborgen |
| **Content die helpt kiezen**: materiaalgidsen, toepassingen, vergelijkingen | 7 blogposts, allemaal op één ochtend |
| **Eén stem**: alle beloftes gelijk, overal | Zie §4 |

---

## 10. DE TIEN GROOTSTE PROBLEMEN (KLANTPERSPECTIEF, GEPRIORITEERD)

| # | Probleem | Klanteffect | Soort |
|---|---|---|---|
| 1 | **Tegenstrijdige retour-, verzend- en reviewbeloftes** (§4) | Vertrouwen weg; juridisch bindend | Content / juridisch |
| 2 | **Oversell zonder waarschuwing** (83/83 varianten, voorraad tot −58, "Op voorraad" als fallback) | Klant wacht weken i.p.v. dagen | Data / operatie |
| 3 | **Geen social proof** (4 reviews, widget uit, anonieme testimonials) | Geen reden om een onbekend merk te vertrouwen | Content / app-config |
| 4 | **Permanente korting als identiteit** (ACTIE, 52% doorgestreept, 5%, Klarna voorop) | Leest als goedkoop; wachten op actie | Commerciële keuze |
| 5 | **Beeldmateriaal**: 29% AI, 0 video's, hero als AI-afbeelding met tekst | Geen bewijs van het echte product | Fotografie |
| 6 | **€ 65 verzendkosten pas in de checkout** | Afhaken bij de laatste stap | UX / content |
| 7 | **Navigatie**: "Wandpanelen" → verkeerde collectie, geen materiaalstructuur, metaal en effen niet vindbaar | Klant vindt niet wat hij zoekt | IA |
| 8 | **Geen m²-prijs, geen calculator, geen specs** op de PDP | Kan niet vergelijken of plannen | PDP |
| 9 | **Rommel in de broncode en content**: ChatGPT-HTML in collecties, demo-resten ("garage…", "Save 99$"), debugcode en AVG-lek live | Onprofessioneel; risico op layoutfouten en privacyklachten | Techniek / content |
| 10 | **Catalogusstructuur**: dubbele producten (groep + decor), versnipperde varianten, prijsfouten | Verwarring, kapotte filters | Data |

---

## 11. WAT AL GOED IS — NIET WEGGOOIEN

- Shopify-checkout met wallets, Klarna en verzendcalculator in de cart.
- Sticky add-to-cart, "vaak samen gekocht", sample-app.
- Productmetafields voor materiaal, duurzaamheid en montage.
- Materiaalcollecties bestaan al (hout, japandi, leer, doorlopend marmer, kunst, 8 mm naadloos), met inmiddels goede SEO-titels.
- Juridische basis (KvK, btw, IBAN, ODR, algemene voorwaarden, privacybeleid) is volledig.
- 30 redirects van de oude WooCommerce-site.
- Showroom en BookEasy-afspraakmodule.
- Vier inspiratie-artikelen die als eerste projectcases kunnen dienen.
- Het development theme bevat al de P0-codefixes en een designsysteem (warm palet, één knopsysteem, h1-hero), nog ongepubliceerd.

---

## 12. WAT IK IN FASE 2 ZOU VOORSTELLEN (RICHTING — NOG NIETS UITVOEREN)

**Spoor A — Vertrouwen (week 1, laag risico, hoogste rendement)**
Alle beloftes gelijktrekken (één bron voor retour, verzending, levertijd, samples, score); oversell beperken of eerlijk tonen ("levertijd 6–10 weken"); verzendkosten vooraf uitleggen; reviewwidget aan + reviewverzoeken na levering; P0-codefixes uit het dev theme publiceren.

**Spoor B — Opruimen (week 1–2)**
ChatGPT-HTML uit collecties, demo-resten, groepsproducten vs decorproducten, optienamen uniform, prijsfouten, AI-alt-teksten, typefouten in menu's.

**Spoor C — Merk & beleving (week 2–6)**
Homepage als verhaal (belofte → materiaal → bewijs → keuze); navigatie op materiaal; PDP met m²-prijs, calculator, specificatietabel, video; collecties met hero, H1 en toepassing; rustig designsysteem (al in dev theme).

**Spoor D — Bewijs (doorlopend, de echte premiumhefboom)**
Echte fotografie (macro, strijklicht, roomscenes, montage); 4 korte productvideo's; 3–5 echte projecten; team en showroom in beeld; certificaten als download.

---

## 13. BESLISSINGEN DIE U MOET NEMEN VÓÓR FASE 2

1. **Retour:** 30 of 90 dagen? (Nu staat op de homepage 90 en in het beleid 30.)
2. **Korting:** blijven "ACTIE" en doorgestreepte prijzen? Zo ja, waar: in het menu of alleen in een aparte saleomgeving?
3. **Verzending België:** ook gratis vanaf € 600, of de topbar per land aanpassen?
4. **Oversell:** mogen klanten doorbestellen bij nul voorraad? Zo ja, welke levertijd tonen we dan?
5. **Reviews:** welke score is echt (9,4 · 4,9 · 4,8), en waar komt die vandaan? Mag die als widget op de site?
6. **Materiaalclaims:** welke certificaten bestaan er voor B1, E0, UV, "100% gerecycled", FSC? Wat niet bewezen kan worden, gaat eruit.
7. **Fotografie & video:** budget en planning voor een echte productshoot en 3–5 projecten?
8. **Catalogusmodel:** één product per decor (aanbevolen) of één product met kleurvarianten?
9. **Themes:** wie werkt er in "Hyper kopie 5 okt (H1-test)" en "Copy of Hyper", en welk theme is de basis voor de volgende release?
10. **Europa:** wanneer Duitsland (markt staat op concept) en welke landen daarna?

---

## 14. TE VERIFIËREN IN DE BROWSER

Omdat `puredeco.nl` en de Shopify-CDN vanuit deze omgeving geblokkeerd zijn:

- [ ] Rendert *"Save 99$"* op het 8 mm-blok van de homepage?
- [ ] Geeft de ChatGPT-HTML op `/collections/nieuwe-collectie` (`h-svh w-screen`) lege ruimte of een layoutbreuk? En op `/collections/actie`, `/collections/bamboepanelen-samples`?
- [ ] Mobiele weergave van de hero, topbar en header (hoogte boven de vouw).
- [ ] Core Web Vitals (LCP, CLS, INP) via PageSpeed Insights voor home, collectie en PDP.
- [ ] Staat iDEAL in de checkout, en bovenaan?
- [ ] Wat ziet een Belgische bezoeker in de topbar en de cart?
- [ ] Opent een `pd-btn`-knop de afsprakenmodule in plaats van te navigeren?
- [ ] Is de foto van *Japandi 620* inmiddels gecorrigeerd?
- [ ] Zijn de beelden in de vier inspiratie-artikelen echte projectfoto's?
- [ ] Rich Results Test: dubbele `Product`-entiteiten (thema + Judge.me)?

---

*Einde fase 1. Er is niets gewijzigd aan de live website, aan de themes of aan de catalogus. Fase 2 start pas na uw akkoord en uw antwoorden op §13.*
