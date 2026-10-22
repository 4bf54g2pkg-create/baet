# Verlaten checkouts — hoe het nu staat en wat er beter kan

**Opgesteld:** 22 oktober 2026 · **Bron:** Shopify Admin API, winkel PureDeco
**Aanleiding:** "ik win niks terug van afgebroken checkout"

---

## Samenvatting in drie zinnen

Je wint niets terug omdat er **niets is ingericht**: in 69 dagen is er geen enkele herstelmail verstuurd, er is geen e-mailmarketing-app geïnstalleerd, en van de 46 verlaten checkouts is er **nul** alsnog afgerekend. De 28 echte prospects daarin vertegenwoordigen **€ 9.088,45** aan panelen, gemiddeld € 324,59 per mandje. Het goede nieuws is dat de oplossing gratis is en ongeveer twintig minuten kost.

---

## 1. Hoe het nu is ingesteld

### 1.1 Er gaat geen enkele herstelmail uit

Dit is geen vermoeden. Shopify houdt per verlaten checkout bij of er een herstelmail verstuurd is. Steekproef van zes checkouts, verspreid over augustus tot oktober, inclusief de grootste:

| Veld | Waarde bij alle zes |
|---|---|
| `emailState` | `null` |
| `emailSentAt` | `null` |
| `daysSinceLastAbandonmentEmail` | **9999** |
| `abandonmentType` | `CHECKOUT` |
| `isFromOnlineStore` | `true` |

`9999` is de waarde die Shopify invult wanneer er **nooit** een mail is verstuurd. Alle zes checkouts kwamen uit de gewone webshop, dus ze zouden allemaal in aanmerking komen.

**Conclusie: de automatische herinnering voor verlaten checkouts staat uit.**

### 1.2 Er is geen enkele e-mailmarketing-app geïnstalleerd

24 apps staan geïnstalleerd. Geen daarvan kan marketingmail versturen:

| Categorie | Apps |
|---|---|
| Reviews | Judge.me, CWILL (Trustoo) |
| Logistiek | Sendcloud, Track123, Bol Sync |
| Verkoop & B2B | Sami Wholesale, BookX, Product Samples |
| Content & vertaling | Translate & Adapt, Search & Discovery, Renderique, Instafeed |
| Analyse | MIDA Replay Heatmaps |
| Data & facturen | Matrixify, Vify Order Printer |
| Automatisering | **Shopify Flow**, Zoho Flow |
| Overig | Messaging, XO Insert code, Typeform, REZ Preorder, Ex Infinite Scroll |

**Geen Shopify Email, geen Klaviyo, geen Omnisend, geen Mailchimp, geen Privy.**

Shopify Flow staat er wel, en die kan een automatisering voor verlaten checkouts bouwen — maar Flow kan zelf geen mail versturen. Daar is een verzendende app voor nodig die er niet is.

### 1.3 Het herstelpercentage is exact nul

46 verlaten checkouts tussen 4 augustus en 21 oktober. Bij **alle 46** staat `completedAt: null`: geen enkele is alsnog afgerekend.

| | Aantal | Waarde |
|---|---:|---:|
| Totaal in Shopify | 46 | € 11.377,60 |
| Bots en kaarttests | 17 | € 2.014,20 |
| Eigen test | 1 | € 274,95 |
| **Echte prospects** | **28** | **€ 9.088,45** |

Gemiddeld mandje van een echte prospect: **€ 324,59**. Tempo: **5,7 verlaten mandjes per 14 dagen, samen € 1.844,03**.

**Alle 28 hebben een e-mailadres. 24 hebben ook een telefoonnummer.**

### 1.4 Eén signaal dat de vraag echt is

Van de zes onderzochte checkouts had er één `customerHasNoOrderSinceAbandonment: false` — die klant heeft later alsnog besteld, uit zichzelf, zonder dat iemand hem benaderde. Eén op zes komt dus vanzelf terug. Met opvolging zou dat hoger moeten liggen.

---

## 2. Wat het nu kost

De 28 echte mandjes zijn samen € 9.088,45 inclusief btw, oftewel **€ 7.511,12 ex btw**. Tegen je gemeten brutomarge van 73,9% is dat **€ 5.550,71 aan brutomarge** die langsliep zonder dat er één mail achteraan ging.

Dat hele bedrag binnenhalen is onmogelijk — de meeste mensen die afhaken, haken af. Maar nul procent is geen natuurwet, het is een instelling.

---

## 3. Wat er beter kan, op volgorde

### Stap 1 — Zet de ingebouwde herinnering aan (gratis, 2 minuten)

**Instellingen → Checkout → Verlaten afrekenpogingen** → aanzetten.

Shopify stuurt dan automatisch een mail met een link terug naar het volle mandje. Stel de vertraging in op **10 uur**: lang genoeg om niet opdringerig te zijn, kort genoeg om binnen dezelfde koopimpuls te vallen.

Dit kost niets, vereist geen app, en werkt vanaf het moment dat je het aanzet.

### Stap 2 — Installeer Shopify Email (gratis tot 10.000 mails per maand)

De ingebouwde herinnering is één mail. Een reeks werkt beter. Met Shopify Email plus de al geïnstalleerde Shopify Flow kun je bouwen:

| Moment | Inhoud |
|---|---|
| Na 1 uur | "Je mandje staat klaar" — alleen de link, geen korting |
| Na 24 uur | De panelen uit het mandje met foto, plus de gratis-sample-optie als alternatief |
| Na 72 uur | Laatste herinnering, eventueel met verzendkosten vergoed |

⚠️ Geef **geen productkorting** in de eerste twee mails. Je marge is 73,9%, maar je mandjes zijn groot: 10% op € 324,59 is € 32,46 weg per order. Verzendkosten vergoeden kost je minder en werkt in deze categorie meestal even goed.

### Stap 3 — Benader de staande 28 handmatig

Die 28 mandjes staan er nu en krijgen geen automatische mail met terugwerkende kracht. De grootste vijf:

| Datum | Waarde | In het mandje |
|---|---:|---|
| 8 okt | € 722,26 | Japandi 619 Jade ×4 + kit + profielen |
| 19 sep | € 647,84 | Hout 812 Walnut Deep ×4 |
| 5 aug | € 583,75 | Japandi 821 Light ×4 |
| 17 okt | € 508,80 | Japandi 824 ×3 + eindprofiel |
| 18 okt | € 424,90 | Japandi 823 Taupe Dark ×2 |

Samen € 2.887,55. Alle vijf met telefoonnummer.

⚖️ **Mailen over hun eigen achtergelaten mandje mag.** Telefonisch benaderen van consumenten voor verkoop vereist in Nederland voorafgaande toestemming, tenzij het een bestaande klant is. Bel je toch, doe het dan als service ("ik zag dat de bestelling niet is doorgekomen") en niet als verkoopgesprek.

### Stap 4 — Doe iets aan de bots

**17 van de 46 verlaten checkouts, 37%, zijn geen klanten.** Twee patronen:

1. **Kaarttesten.** Vijf checkouts van exact € 8,95 (High Tack Montagekit) uit Duitsland, Australië en de VS, met telefoonnummers als `+4930125272` en `02 9250 5813`. Dit is het klassieke patroon van iemand die gestolen kaartnummers test op je checkout met het goedkoopste artikel.
2. **Geautomatiseerde tests.** Twaalf checkouts van `quiet.harbor503+...@ilovemyemail.net` en wegwerpadressen op protonmail, steeds in paren van dertig seconden, allemaal met hetzelfde telefoonnummer `623568711`.

Waarom dit meer is dan vervuilde data: kaarttesten leidt tot chargebacks, en te veel chargebacks kost je je betaalprovider. Zet in **Instellingen → Checkout** de botbescherming en reCAPTCHA aan, en overweeg een limiet op het aantal betaalpogingen per IP.

---

## 4. Wat het realistisch oplevert

Eerlijk gerekend, op je eigen cijfers en een normaal herstelpercentage voor deze categorie:

| Herstel | Orders per 69 dagen | Omzet ex btw | Brutomarge |
|---|---:|---:|---:|
| 5% | 1,4 | € 375,56 | **€ 277,54** |
| 10% | 2,8 | € 751,11 | **€ 555,07** |
| 15% | 4,2 | € 1.126,67 | **€ 832,61** |

Omgerekend naar jouw rapportageperiode: **€ 56 tot € 169 brutomarge per 14 dagen**, structureel, voor eenmalig twintig minuten werk en nul euro aan kosten.

**Zet dat in verhouding.** Dit is kleiner dan de opvolgflow voor staalaanvragers uit het hoofdrapport (+€ 1.838 per 14 dagen) en kleiner dan wat golf 1 zojuist aan verlies wegnam (€ 321,21 per 14 dagen). Maar het is gratis, het loopt vanzelf, en het staat nu op precies nul.

---

## 5. Wat ik niet heb kunnen vaststellen

| Wat | Waarom |
|---|---|
| Of de herinnering ooit **aan** heeft gestaan en later uitgezet is | De Admin API geeft de instelling zelf niet terug, alleen het resultaat ervan. Dat resultaat is eenduidig: nooit een mail verstuurd. |
| Hoeveel checkouts er vóór 4 augustus waren | Shopify bewaart verlaten checkouts beperkt; 4 augustus is de oudste die de API teruggeeft. |
| Of de bots ook echte betaalpogingen deden | Daarvoor is inzage in je betaalprovider nodig, niet in de Shopify Admin API. |

---

## 6. Samengevat

| | Nu | Na stap 1 en 2 |
|---|---|---|
| Herstelmails verstuurd | **0** | automatisch, binnen een uur |
| E-mailmarketing-app | **geen** | Shopify Email, gratis |
| Herstelpercentage | **0,0%** | 5 tot 15% is normaal |
| Brutomarge per 14 dagen | **€ 0** | € 56 tot € 169 |
| Kosten | — | € 0 |
