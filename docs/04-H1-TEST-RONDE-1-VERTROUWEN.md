# H1-TEST — RONDE 1: UITSTRALING & VERTROUWEN
**Theme:** Hyper kopie 5 okt (H1-test) · `194824929546` · **UNPUBLISHED**
**Datum:** 5 oktober 2026, 12:37–12:40 UTC
**Live theme (Hyper `188874326282`):** niet aangeraakt. Na de upload gecontroleerd: `updatedAt` nog steeds 2026-09-22T09:13:33Z.

Uitgangssituatie en nieuwe stand staan in `theme-h1/` (twee aparte commits, dus de diff toont precies wat er veranderd is). JSON-bestanden staan in de repo netjes ingesprongen; in Shopify zijn ze inhoudelijk identiek (na upload gecontroleerd per instelling).

---

## 1. Wat er veranderd is

### Vertrouwen: overal dezelfde, controleerbare beloftes
Alle beloftes volgen nu het **gepubliceerde beleid** (retourbeleid: 30 dagen; verzending: gratis in NL vanaf € 600).

| Plek | Was | Nu |
|---|---|---|
| Topbar | "Gratis verzending vanaf 600,-" · "Klanten beoordelen ons gemiddeld met een 9,4 op 10." · "Betaal later met Klarna" | "Gratis bezorging in Nederland vanaf € 600" · "3 jaar garantie op alle wandpanelen" · "Showroom in Herwen · persoonlijk advies op afspraak" |
| Homepage-USP's | **Klarna** als eerste · "90 dagen retourbeleid" | **3 jaar garantie** als eerste · "30 dagen bedenktijd" |
| Productpagina-iconen | "Gratis verzending boven € 600" · "90 dagen tevredenheidsgarantie" · "3 jaar fabrieksgarantie" · "Leverbaar binnen 3-6 werkdagen" | "Gratis bezorging in NL vanaf € 600" · "30 dagen bedenktijd" · "3 jaar garantie" · "Showroom in Herwen" |
| Quick-view | "€ 500" · "90 dagen" | gelijk aan productpagina |
| Winkelmand | "✌🏼 GRATIS VERZENDING BOVEN €600!" · "Pair Well With" | "Gratis bezorging in Nederland vanaf € 600" · "Maak je wand compleet" |
| Collectiepagina | lopende band met "90 dagen bedenktijd" | band uitgezet (tekst ook gecorrigeerd naar 30 dagen) |

### Levertijd op de productpagina: eerlijk
Was: altijd *"Op voorraad. Binnen 3-6 werkdagen in huis"*, ook bij voorraad −58.
Nu, op basis van de gekozen variant bij het laden van de pagina:
- voorraad > 0 → ● *"Op voorraad · binnen 3–6 werkdagen geleverd"* (groen bolletje)
- voorraad ≤ 0 → ● *"Op bestelling · levertijd tot 10 weken. Wij bevestigen de leverdatum na je bestelling."* (brons bolletje)
- staat er een verwachte leverdatum in het productveld, dan wint die (zoals voorheen).

### Demo-resten en twijfelachtige elementen weg
- Badge **"garace - where design meet function -"** (homepage, samplepagina) en **"garage - where design meets function -"** (4× over-ons): uit.
- Badge **"Save 99$"** op het 8 mm-blok: leeg.
- Demo-sectie **"Special Offers / promocode GARA10 / Select lamp from $170"**: verwijderd uit het theme.
- **Anonieme testimonials** (kop "Testimonials", geen namen, op 3 pagina's identiek) op over-ons en samplepagina: uit. Ze kosten meer vertrouwen dan ze opleveren; terugzetten zodra er echte reviews met naam zijn.
- Instagram-tekst: *"…op onze website!!"* → *"Deel je wand met #puredeco.nl — de mooiste projecten tonen we hier."*
- PDP-contactblok: zichtbare link `https://puredeco-3.myshopify.com/faqs` → "veelgestelde vragen".
- Lege Twitter/TikTok-iconen en de taalkiezer (er is maar één taal) uit; landkiezer blijft (België).

### Header & footer
- Twinkelend sterretje op "wandpanelen" en de groene knop-CSS uit de header weg.
- Header-knoppen: groene pillen → *Showroomafspraak* als rustige omlijnde knop, *Gratis advies* als tekstlink.
- Footer: emoji (📞 ✉️ 📍) vervangen door gewone tekst met werkende `tel:`- en `mailto:`-links, plus *"PureDeco B.V. · KvK 97720925"*.
- Nieuwsbrief: *"Meld je aan en ontvang 5% korting op je eerste bestelling."* → *"Inspiratie en nieuwe decors in je inbox — met 5% welkomstkorting"* (aanbod blijft, toon rustiger).

### Productpagina
- Klarna-blok (roze logo + "Betaal in 3 delen: € …") direct onder de prijs → één rustige regel **onder** de koopknop.
- Betaaliconen: grijze kaart met afgeronde hoeken → een dunne lijn erboven; *"Alle prijzen zijn inclusief btw."* is nu zichtbaar.
- Dubbele producttitel (`<h1>` + verborgen `<h2>`-link) → alleen `<h1>`; de link blijft in de quick-view.
- Kleurbolletjes laden een afbeelding van 90 px in plaats van de master (tot 2048 px).

### Visuele laag (`assets/puredeco-premium.css`, batch 2)
- Koppen 500 in plaats van 700/800; iets strakkere letterafstand; `text-wrap: balance`.
- Prijzen: kortingsprijs niet meer rood maar inkt; oude prijs in steengrijs; kortingslabel als dunne omlijning.
- Productkaarten: titel 400, prijs 500, rustige zoom (3%) bij hover.
- Topbar: kleinere, rustige letter met wat letterafstand; minder hoog (padding 16/18 → 8/8).
- Feature cards en contactblok: gewichten 700/800 → 500, linkkleur groen → inkt.
- Alles in één bestand; terugdraaien = dat bestand leegmaken.

### Techniek
- **AVG:** `console.log` van het e-mailadres van ingelogde klanten verwijderd.
- **Afspraakknoppen:** het BookX-blok is om 12:28 door een collega teruggezet. Daarnaast onderschept het script nu alleen nog knoppen met `href="javascript:…"` (de afspraakknoppen). Gewone `.pd-btn`-links (partner, samples) navigeren weer naar hun pagina, in plaats van de agenda te openen.

---

## 2. Keuzes die ik voor u heb gemaakt (makkelijk terug te draaien)

| Keuze | Waarom | Terugdraaien |
|---|---|---|
| **30 dagen** in plaats van 90 | Dat staat in het gepubliceerde retourbeleid en de FAQ; dat is juridisch bindend | Als 90 dagen de bedoeling is: eerst het retourbeleid aanpassen, dan de 5 teksten |
| **9,4/10-score weg** uit de topbar | Geen bron, en drie verschillende scores op de site | Terugzetten met bron en link (bijv. naar Google-reviews) |
| **Klarna** uit de merklagen (topbar, homepage-USP) | Leest als "duur, maar je kunt afbetalen"; staat nog steeds op de PDP en in de checkout | Tekstblok in topbar terugzetten |
| **Anonieme testimonials** uit | Zien er nep uit, ook als ze echt zijn | Sectie weer aanzetten |

---

## 3. Testlijst voor de preview

Open de preview van theme **"Hyper kopie 5 okt (H1-test)"** (Shopify-admin → Online winkel → Thema's → ··· → Voorbeeld) en controleer:

- [ ] **Showroompagina** `/pages/showroom`: "Plan je afspraak" (hero, midden, locatiekaart) opent de BookX-agenda; "Interesse? Neem contact op" en de sampleknop gaan naar hun pagina.
- [ ] **Header**: Showroomafspraak = omlijnde knop, Gratis advies = tekstlink; geen sterretje; topbar rouleert de drie nieuwe teksten.
- [ ] **Homepage**: USP-balk begint met "3 jaar garantie"; geen "Save 99$", geen "garace"-badge.
- [ ] **Productpagina** met voorraad (bv. *Hout 811*) → groen "Op voorraad"; zonder voorraad (bv. *Japandi 621 White*, voorraad −1) → "Op bestelling · tot 10 weken". Klarna-regel staat onder de koopknop.
- [ ] **Productpagina** bij een product met korting: prijs niet rood.
- [ ] **Winkelmand**: rustige verzendregel, "Maak je wand compleet".
- [ ] **Footer**: telefoon en e-mail klikbaar, geen emoji.
- [ ] **Mobiel**: header-knoppen en topbar passen; niets valt buiten beeld.

Klopt iets niet of oogt het anders dan bedoeld: het staat allemaal in `theme-h1/` en is per bestand terug te zetten.

---

## 4. Volgende ronde (voorstel, nog niet uitgevoerd)

1. **Typografie**: een serif voor de grote koppen (bijv. Cormorant of Libre Baskerville) naast Instrument Sans. Dit is de grootste stap richting "interieurmerk", maar ook het meest zichtbaar. Dus eerst uw akkoord na het zien van ronde 1.
2. **Homepage-volgorde**: van 12 secties terug naar ±8; tweede slideshow (B2B) en Instagram-feed lager of eruit.
3. **Hero met zichtbare kop** in HTML in plaats van tekst in het beeld. Daarvoor is een beeld zonder ingebakken tekst nodig.
4. **Productkaarten**: één beeldverhouding (4:5) en het kortingspercentage-label weg.
5. **Engelse restteksten** in de theme-instellingen ("Not sure where to start?").
6. ~~**WhatsApp-nummer**~~ — opgelost: productpagina gebruikte `wa.me/31850870490`; nu overal **0316 700214** (`wa.me/31316700214`), op aanwijzing van de opdrachtgever.
