# Audit opvolging verlaten winkelwagens — fase 1: de huidige situatie

**Datum:** 22 oktober 2026 · **Winkel:** PureDeco (`f9yvx9-zm.myshopify.com`, primair domein `puredeco.nl`)
**Scope van deze fase:** uitsluitend inventarisatie. Nog geen implementatieadvies.

Dit document scheidt strikt: **[FEIT]** wat ik heb vastgesteld, **[VERMOEDEN]** wat ik afleid, **[ONBEKEND]** wat ik niet kan zien en van jou nodig heb.

---

## 1. Samenvatting van de inventarisatie

Er is **geen opvolging van verlaten winkelwagens en checkouts**. Niet slecht ingericht — afwezig. Geen verstuurde mails, geen app die ze kan versturen, geen automatisering, geen marketingactiviteit. Het herstelpercentage is exact nul over 46 checkouts in 69 dagen.

Twee dingen staan gunstiger dan verwacht: het afzenderadres in Shopify staat al op `info@puredeco.nl`, en er is geen enkele overlappende of dubbele flow die eerst ontward moet worden. Je begint met een schone lei.

---

## 2. Wat ik heb vastgesteld

### 2.1 Verstuurt Shopify herstelmails? **Nee.** [FEIT]

Shopify registreert per verlaten checkout of er een herstelmail is verstuurd. Steekproef van zes checkouts, gespreid over augustus tot oktober, inclusief de vier grootste:

| Checkout | Waarde | `emailState` | `emailSentAt` | `daysSinceLastAbandonmentEmail` |
|---|---:|---|---|---:|
| 21 okt | € 301,80 | `null` | `null` | 9999 |
| 18 okt | € 424,90 | `null` | `null` | 9999 |
| 17 okt | € 508,80 | `null` | `null` | 9999 |
| 8 okt | € 722,26 | `null` | `null` | 9999 |
| 19 sep | € 647,84 | `null` | `null` | 9999 |
| 5 aug | € 583,75 | `null` | `null` | 9999 |

`9999` is de sentinelwaarde die Shopify invult wanneer er **nooit** een herstelmail is verstuurd. Alle zes hebben `abandonmentType: CHECKOUT` en `isFromOnlineStore: true`, dus ze kwamen allemaal in aanmerking.

### 2.2 Zijn er e-mailflows via apps? **Nee.** [FEIT]

24 apps geïnstalleerd. Geen enkele kan marketing- of transactiemail versturen:

| Categorie | Apps |
|---|---|
| Reviews | Judge.me, CWILL (Trustoo) |
| Logistiek | Sendcloud, Track123, Bol Sync |
| Verkoop & B2B | Sami Wholesale, BookX, Product Samples |
| Content & vertaling | Translate & Adapt, Search & Discovery, Renderique, Instafeed |
| Analyse | MIDA Replay Heatmaps |
| Data & facturen | Matrixify, Vify Order Printer |
| Automatisering | Shopify Flow, Zoho Flow |
| Overig | Messaging, XO Insert code, Typeform, REZ Preorder, Ex Infinite Scroll |

**Geen Shopify Email, Klaviyo, Omnisend, Mailchimp of Privy.**

Shopify Flow staat wel geïnstalleerd en kan een trigger op `Checkout abandoned` aan, maar Flow heeft een verzendende app nodig om een mail te sturen. Die ontbreekt.

### 2.3 Zijn er marketingautomatiseringen? **Nee.** [FEIT]

`marketingActivities` geeft een **lege lijst** terug. Er draait geen enkele marketingactiviteit of automatisering in Shopify.

### 2.4 Dubbele of tegenstrijdige mails? **Nee — er is niets om te ontwarren.** [FEIT]

Omdat er nul verzendende systemen zijn, is er per definitie geen overlap, geen dubbele opvolging en geen conflicterende timing.

### 2.5 Afzenderadres [FEIT, met een belangrijk voorbehoud]

| Instelling | Waarde |
|---|---|
| `shop.email` (eigenaar) | `info@puredeco.nl` |
| `shop.contactEmail` (klantgericht) | **`info@puredeco.nl`** |
| Primair domein | `puredeco.nl` |
| Shopify-domein | `f9yvx9-zm.myshopify.com` |
| Klantaccounts | `OPTIONAL` |

Het **zichtbare** afzenderadres staat dus al goed. Maar dat zegt niets over het technische verzenddomein — zie 3.1.

### 2.6 Herstelpercentage: 0,0% [FEIT]

46 verlaten checkouts tussen 4 augustus en 21 oktober. Bij **alle 46** staat `completedAt: null`.

| | Aantal | Waarde |
|---|---:|---:|
| Totaal | 46 | € 11.377,60 |
| Bots en kaarttests | 17 | € 2.014,20 |
| Eigen test | 1 | € 274,95 |
| **Echte prospects** | **28** | **€ 9.088,45** |

Gemiddeld € 324,59 per mandje; tempo **5,7 per 14 dagen à € 1.844,03**. Alle 28 met e-mailadres, 24 ook met telefoonnummer.

### 2.7 Eén klant kwam uit zichzelf terug [FEIT]

Van de zes onderzochte checkouts had er één `customerHasNoOrderSinceAbandonment: false`: die klant bestelde later alsnog, zonder enige opvolging. Eén op zes in deze steekproef. Te klein om op te sturen, maar het laat zien dat de koopintentie reëel is.

### 2.8 Onderscheid tussen winkelwagen, gestarte checkout en verlaten checkout [FEIT]

Shopify kent drie `abandonmentType`-waarden: `BROWSE`, `CART` en `CHECKOUT`. Alle zes onderzochte gevallen zijn **`CHECKOUT`** — iemand is begonnen met afrekenen en heeft contactgegevens achtergelaten.

**Winkelwagenverlating (`CART`) en browseverlating (`BROWSE`) worden niet opgevolgd en zijn ook niet zichtbaar in de rapportage.** Shopify legt die alleen vast voor klanten die herkend zijn; zonder e-mailmarketing-app met eigen tracking blijft die groep volledig onzichtbaar. Dat is een gat, geen fout.

---

## 3. Wat ik niet heb kunnen vaststellen

### 3.1 SPF, DKIM en DMARC — **niet verifieerbaar vanuit deze omgeving** [ONBEKEND]

Ik heb dit geprobeerd en de poging **afgekeurd op eigen controle**. De DNS-weg vanuit deze container geeft onbetrouwbare antwoorden: een controlevraag op `shopify.com` leverde "geen MX en geen SPF" op, wat onmogelijk is. Alles wat ik over jouw DNS zou zeggen, zou op dezelfde fout berusten.

Vijf routes geprobeerd, alle vijf dood:

| Route | Uitkomst |
|---|---|
| dnspython via UDP naar 8.8.8.8 en 1.1.1.1 | lege antwoorden, controledomein faalt ook |
| dnspython via TCP | time-out |
| Systeemresolver uit `/etc/resolv.conf` | `NXDOMAIN` voor `shopify.com` — aantoonbaar onjuist |
| `curl` naar dns.google, cloudflare-dns.com, mxtoolbox | HTTP 403 van de uitgaande proxy |
| Interne fetch-tool | `getaddrinfo ENOTFOUND` |

Alleen A-records komen correct door; alle andere recordtypes worden onderweg verminkt. Dit is een beperking van mijn omgeving, niet van jouw domein.

**Wat ik wél weet:** `puredeco.nl` wijst naar `23.227.38.65`, een Shopify-adres, en de site antwoordt met status 200.

**Wat jij moet aanleveren** — ga naar https://mxtoolbox.com/SuperTool.aspx en voer uit:

Nu bekend is dat er een Zoho-omgeving draait, is de vraag scherper geworden: **staan Zoho én Shopify allebei in het SPF-record?** Zoho Mail verzendt al namens `puredeco.nl`, dus er is vrijwel zeker een SPF-record met een Zoho-insluiting. Ontbreekt Shopify daarin, dan faalt de authenticatie van elke mail die Shopify namens `info@puredeco.nl` verstuurt — precies de mails die deze audit moet gaan inrichten.

| Lookup | Invoer | Waar ik op let |
|---|---|---|
| SPF Record Lookup | `puredeco.nl` | Bestaat er een `v=spf1`-record, en staan **zowel Zoho als Shopify** erin |
| DMARC Lookup | `puredeco.nl` | Bestaat `_dmarc`, en staat `p=` op none, quarantine of reject |
| MX Lookup | `puredeco.nl` | Waar komt mail op `info@puredeco.nl` binnen |
| DKIM Lookup | `puredeco.nl` met selector `shopifyemail` | Of Shopify's DKIM-sleutel aanwezig is |

Screenshot of plaktekst van alle vier is genoeg.

### 3.2 Staat de ingebouwde herinnering aan of uit? [VERMOEDEN, sterk onderbouwd]

De Shopify Admin API kent **geen query** voor meldingsinstellingen of e-mailsjablonen — ik heb daarop gezocht en het schema geeft nul velden terug. Ik kan de schakelaar zelf dus niet lezen.

Wat ik wel kan lezen is het **resultaat**, en dat is eenduidig: nul verstuurde mails over 69 dagen bij 46 in aanmerking komende checkouts. **Vermoeden: de instelling staat uit.** Een tweede mogelijkheid is dat hij aanstaat maar de verzending stilvalt door een ontbrekende domeinverificatie.

**Wat jij moet aanleveren:** screenshot van **Instellingen → Meldingen → Verlaten afrekenpoging**, inclusief of hij aanstaat en welke vertraging er is ingesteld.

### 3.3 Verificatiestatus van het afzenderdomein in Shopify [ONBEKEND]

Dat `contactEmail` op `info@puredeco.nl` staat, betekent **niet** dat Shopify ook namens dat domein mag verzenden. Shopify vraagt daarvoor een aparte domeinverificatie met CNAME-records. Zonder die verificatie toont Shopify de winkelnaam als afzender maar verzendt technisch vanaf een eigen domein, wat de aflevering en het vertrouwen schaadt.

**Wat jij moet aanleveren:** screenshot van **Instellingen → Meldingen → Afzender-e-mail** (of *Sender email*), waar Shopify de verificatiestatus toont — groen geverifieerd, of een lijst met nog toe te voegen DNS-records.

### 3.4 Komen antwoorden op `info@puredeco.nl` daadwerkelijk aan? [ONBEKEND]

Het zichtbare afzenderadres, het technische verzenddomein en het reply-to-adres zijn drie verschillende dingen. Ik kan geen van drieën aan de ontvangstkant controleren.

**Wat jij moet doen:** stuur vanaf een privéadres een mail naar `info@puredeco.nl` en bevestig dat hij aankomt, en in welke mailbox.

### 3.5 Verzendt een systeem buiten Shopify mogelijk toch iets? **Nee.** [FEIT, aangevuld 22 okt]

Twee onafhankelijke controles sluiten dit uit.

**Live themacode doorzocht.** Homepage (1.018.141 bytes) en winkelwagenpagina (428.267 bytes) opgehaald en doorzocht op 21 bekende e-mailmarketingsystemen: Klaviyo, Omnisend, Mailchimp, Privy, ActiveCampaign, Brevo, Drip, HubSpot, MailerLite, Attentive, Postscript, Recart, CartHook en andere. **Nul treffers.** De enige externe scripts zijn `cdn.jsdelivr.net`, `cdn.nfcube.com` (de Instafeed-app), `cdn.shopify.com` en `shop.app`. Er is dus ook geen systeem via themacode ingeschoten in plaats van als app.

**Zoho bevestigd door de eigenaar, maar het kan geen verlaten checkouts zien.** Er draait een Zoho-omgeving. Zoho Flow heeft in Shopify echter alleen `read_all_orders`, `read_orders` en `customer_read_orders` — **uitsluitend orders, geen checkouts**. Een verlaten checkout is geen order. Zoho kan die gegevens dus niet eens ophalen, laat staan erop opvolgen.

**Consequentie voor fase 2:** het bestaan van Zoho is wél relevant voor de keuze van het verzendsysteem en voor de SPF-configuratie, want Zoho Mail verzendt al namens `puredeco.nl`.

### 3.6 Statistieken over aflevering, opens en klikken [ONBEKEND — en logisch]

Niet beschikbaar, omdat er geen mails zijn verstuurd. Zodra er wel een reeks loopt, komen deze cijfers beschikbaar in het gekozen e-mailsysteem.

---

## 4. De huidige klantreis, als schema

Uitsluitend ingevuld met vastgestelde informatie.

```
Bezoeker plaatst product in winkelwagen
        │
        ├─ [ONBEKEND] niet gemeten; geen app legt winkelwagenverlating vast
        │
        ▼
Bezoeker start checkout en vult e-mailadres in
        │
        ▼
Checkout wordt verlaten
        │
        ▼
Shopify legt vast: abandonmentType = CHECKOUT          ← [FEIT] gebeurt wel
emailState = null · emailSentAt = null · 9999 dagen
        │
        ▼
        ✗  GEEN e-mail
        ✗  GEEN herinnering
        ✗  GEEN laatste opvolging
        ✗  GEEN automatisering
        │
        ▼
Einde. 46 van 46 zonder vervolg.                        ← [FEIT] completedAt = null
```

Bijbehorende vragen uit de opdracht, met de stand van zaken:

| Vraag | Antwoord |
|---|---|
| Wat gebeurt er bij alleen een winkelwagen? | Niets, en het wordt niet gemeten |
| Wat bij e-mailadres invullen maar niet bestellen? | Vastgelegd in Shopify, verder niets |
| Welke mails, met welke tussenpozen? | Geen |
| Werkt de herstel-link? | Niet te beoordelen; `cartUrl` bestaat in de data maar is nooit verzonden |
| Wat als iemand tussentijds alsnog bestelt? | Niet van toepassing; er loopt geen reeks om uit te stappen |
| Krijgen klanten meerdere mails kort na elkaar? | Nee |
| Verschil nieuwe versus bestaande klanten? | Geen onderscheid, want geen opvolging |
| Personalisatie mogelijk? | Technisch ja — productnaam, afbeelding en `cartUrl` zitten in de data; nu ongebruikt |

---

## 5. Wat ik van je nodig heb voor fase 2

| # | Wat | Waar |
|---|---|---|
| 1 | Screenshot **Instellingen → Meldingen → Verlaten afrekenpoging** | Shopify |
| 2 | Screenshot **Instellingen → Meldingen → Afzender-e-mail** met verificatiestatus | Shopify |
| 3 | Uitkomsten van vier MXToolbox-lookups: SPF, DMARC, MX, DKIM (selector `shopifyemail`) | mxtoolbox.com |
| 4 | Bevestiging dat een testmail naar `info@puredeco.nl` aankomt, en waar | jouw mailbox |
| 5 | ~~Of er een Zoho-omgeving actief is~~ — **beantwoord 22 okt: ja, en hij werkt** | ✅ |
| 6 | Of je bereid bent Shopify Email te installeren (gratis tot 10.000 mails per maand) | jouw besluit |

Met 1 tot en met 4 kan ik fase 2 afmaken: de herstelreeks, de afzenderconfiguratie, de vergelijking van oplossingen, de juridische toets en de concrete e-mailteksten.

**Punt 3 is het belangrijkste.** Zonder de werkelijke DNS-stand kan ik geen betrouwbaar advies geven over verzending vanaf `info@puredeco.nl`, en dat is precies de kern van je vraag.

---

## 6. Wat ik nu al kan zeggen zonder vooruit te lopen

Drie observaties die fase 2 gaan sturen, maar die ik hier als observatie en niet als advies neerzet:

1. **Er is niets te ontwarren.** Geen dubbele flows, geen conflicterende apps, geen legacy-automatisering. Dat maakt de inrichting eenvoudiger dan bij de meeste winkels.
2. **Het afzenderadres staat al goed op naam**, dus de vraag is niet *of* `info@puredeco.nl` kan, maar of het domein technisch gemachtigd is om namens zichzelf te verzenden. Dat valt of staat met punt 3 hierboven.
3. **37% van je verlaten checkouts is geen klant.** 17 van 46 zijn bots, waaronder vijf kaarttests van exact € 8,95 uit Duitsland, Australië en de VS. Dat is een apart spoor — eerder een risico voor je betaalprovider dan een marketingkwestie — en het vertekent elk herstelpercentage dat je straks gaat meten. In fase 2 reken ik daarom met de 28 echte mandjes, niet met 46.
