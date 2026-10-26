# Plan: zakelijk scheiden van particulier in Meta Ads

**26 oktober 2026.** Uitvoeringsplan naar aanleiding van de audit
(`10-AUDIT-META-ADS.md`). **Er is nog niets gewijzigd.**

---

## 1. Je diagnose klopt — en er is een derde factor

Je zei: alles staat onder één campagne, er is € 60/dag, en stalen tellen even zwaar
als echte orders waardoor er te weinig naar zakelijk gaat. Dat is alle drie juist.
Wat de data daaraan toevoegt:

| Advertentieset | Kosten/dag* | % budget | AOV | ROAS | Winst per 30 dagen |
|---|---:|---:|---:|---:|---:|
| Video's (particulier) | € 43,17 | 75,4% | € 39,69 | 2,20 | +€ 323,12 |
| zakelijke doelgroep | **€ 14,08** | 24,6% | **€ 155,40** | **9,46** | **+€ 1.754,06** |

\* over 28 leverdagen (26 sep – 23 okt; 24 en 25 oktober stond het account stil).

[FEIT] Beide sets staan op `custom_event_type: PURCHASE` met
`optimization_goal: OFFSITE_CONVERSIONS` — maximaliseer het **aantal** conversies.
Een staal van € 6,95 weegt daarin precies zo zwaar als een order van € 1.500.

Het mechanisme is in één advertentie te zien: `diaan creator 1` levert de
**goedkoopste** aankopen van het account (€ 15,39) en krijgt daarom het **grootste
budget** (€ 492,45 per 30 dagen). Gemiddelde orderwaarde: € 22,64. Resultaat: −€ 75,13.
Het algoritme doet precies wat het is opgedragen.

### De derde factor die je nog niet kent

[FEIT] Op **beide** advertentiesets staat `targeting_automation.advantage_audience: 1`.
Advantage+ doelgroep staat aan. Dat betekent dat Meta je interessetargeting als
*suggestie* behandelt en daarbuiten mag zoeken.

Gecombineerd met "koop zoveel mogelijk conversies" is dat de versterker: Meta mag
je zakelijke doelgroep verlaten zodra het ergens anders goedkopere conversies vindt —
en goedkopere conversies zijn altijd stalen. **Je zakelijke targeting bindt op dit
moment niet.** Splitsen zonder dit aan te pakken lost maar de helft op.

---

## 2. Wat er precies in je account staat

| | Video's | zakelijke doelgroep |
|---|---|---|
| Ad set id | 120227638774980057 | **120243049922850057** |
| Leeftijd | 30–50 | 25–50 |
| Provincies | Gelderland, Overijssel | Drenthe, Gelderland, **Noord-Brabant, Utrecht**, Overijssel |
| Interesses | 12 × wonen/interieur + levensgebeurtenissen (pas verhuisd, pas getrouwd) | Interieurontwerp, Verbouwingen, **Ondernemerschap, Bouw, Onroerend goed** |
| Advantage+ doelgroep | aan | aan |
| Pixel | 1072431017618538 | 1072431017618538 |
| Conversie-event | PURCHASE | PURCHASE |

Campagne `Puredeco - onfluence` (id 120227638774910057), doel OUTCOME_SALES,
CBO € 60,00/dag, biedstrategie `LOWEST_COST_WITHOUT_CAP`, draait sinds 16 juni 2025.

---

## 3. Het plan in vijf fasen

Volgorde is belangrijk. Elke wijziging aan een advertentieset herstart de
leerfase. Dit plan is zo gebouwd dat **elke set precies één keer opnieuw leert**.

### Fase 1 — Schoon het signaal (jij, Gebeurtenissenbeheer, ~10 minuten)

Maak een aangepaste conversie:

| Veld | Waarde |
|---|---|
| Naam | **Aankoop boven € 20** |
| Gegevensbron | Pixel 1072431017618538 |
| Gebeurtenis | Purchase |
| Regel | `value` is groter dan `20` |

**Waarom € 20 en niet € 50.** Het doel is niet grote orders vinden, het doel is
stoppen met stalen tellen. Stalen zijn € 6,95 en € 7,95; een losse montagekit € 8,95.
Een drempel van € 20 sluit die uit en houdt élke echte order binnen. Bij € 50 gooi je
ook legitieme kleine orders weg en wordt het signaal onnodig dun.

Maak meteen ook **"Staalaanvraag"** aan (zelfde pixel, Purchase, `value` kleiner dan
`20`). Die gebruik je nu niet, maar je hebt hem nodig zodra de opvolgflow draait.

[FEIT] Dit is **additief**. Een aangepaste conversie leest bestaande gebeurtenissen
en verandert niets aan je pixel, je thema of je bestaande conversies.

### Fase 2 — Splitsen (ik, na jouw akkoord)

1. Hernoem `Puredeco - onfluence` → **`PureDeco | Particulier`**
2. Maak campagne **`PureDeco | Zakelijk`** (OUTCOME_SALES, gepauzeerd, dagbudget)
3. Dupliceer ad set `120243049922850057` naar die nieuwe campagne, inclusief de
   advertentie `zakelijk verbouwen`. De kopie neemt je targeting exact over —
   je hoeft niets opnieuw in te stellen en er gaat niets verloren.
4. Pauzeer de oude `zakelijke doelgroep` in de oude campagne
5. Pauzeer in `Video's` de vier verliesgevers: `diaan creator 2`,
   `Nieuwe wandpanelen`, `video 3`, `Video led profiel japans`
   (samen −€ 170,43 per 30 dagen). Blijven staan: `Marmerlook va 125` (+€ 568,67)
   en `diaan creator 1` (zie fase 5).

De particuliere kant wordt dus **niet** opnieuw opgebouwd — die houdt haar
leergeschiedenis. Alleen de zakelijke kant leert opnieuw, en dat is onvermijdelijk
als je wilt splitsen.

### Fase 3 — Instellingen (jij, in de interface, terwijl zakelijk nog gepauzeerd staat)

Per advertentieset, op **beide** kanten:

1. **Conversiegebeurtenis** → `Aankoop boven € 20`
2. **Plaatsingen** → handmatig. **Aan:** Facebook Feed, Instagram Feed,
   Instagram Stories. **Uit:** Facebook Reels, Instagram Reels, Facebook Stories,
   Audience Network, Threads, Marketplace, Search, rechterkolom.
   (Reels kostten € 278,24 per 30 dagen en leverden € 76,45 op.)
3. **Advantage+ doelgroep UIT** op `PureDeco | Zakelijk`.
   Dit is het punt uit 1. Zonder deze stap mag Meta je zakelijke doelgroep verlaten
   en is de splitsing half werk. Op de particuliere kant mag hij aan blijven.

Doe dit **vóór** het aanzetten, zodat het één leerfase is in plaats van drie.

### Fase 4 — Budget, in stappen

Nu: zakelijk € 14,08/dag, particulier € 43,17/dag.
Doel: die verhouding omdraaien. Maar niet in één keer — meer dan ongeveer
30% budgetverhoging per stap gooit een advertentieset terug de leerfase in.

| Dag | Zakelijk | Particulier | Totaal | Voorwaarde om door te gaan |
|---|---:|---:|---:|---|
| 0 | € 20 | € 40 | € 60 | — (start) |
| 4 | € 26 | € 34 | € 60 | ROAS zakelijk > 3 |
| 8 | € 34 | € 26 | € 60 | ROAS zakelijk > 3 |
| 12 | € 44 | € 18 | € 62 | ROAS zakelijk > 3 |

Start op € 20 — dat is al +42% ten opzichte van de € 14,08 die de set nu krijgt.
Zakt de ROAS onder 3, dan blijf je staan op het vorige niveau in plaats van door te gaan.
Onder 1,74 (break-even) stap je terug.

### Fase 5 — Handen eraf, dan meten

- **Zeven dagen niets wijzigen.** Elke bewerking herstart de leerfase. Dit is de
  stap die in de praktijk het vaakst wordt overgeslagen en het meeste kost.
- **Dag 7:** alleen kijken of de richting klopt. Nog geen oordeel — de aantallen
  zijn te klein.
- **Dag 14:** oordeel op winst per campagne: `waarde / 1,21 × 0,697 − kosten`.
- **Dag 14, besluit over `diaan creator 1`:** die verliest nu geld (ROAS 1,47 en 1,50
  op beide vensters) omdat hij op aantallen wordt beloond. Met het nieuwe signaal
  krijgt hij een eerlijke kans. Blijft de ROAS onder 1,74, dan stoppen.

---

## 4. Risico's — eerlijk

### De leerfase op de zakelijke kant wordt gereset
Onvermijdelijk bij splitsen. Reken op vijf tot zeven dagen onrustige resultaten,
mogelijk eerst slechter. Niet ingrijpen in die periode.

### Het echte knelpunt: je volume is te klein voor Meta's optimalisatie
[FEIT] Meta wil ongeveer **50 conversies per week per advertentieset** om de leerfase
te verlaten. Met een drempel van € 20 houd je naar schatting 15 tot 25 conversies
per 30 dagen over — ongeveer **5 per week**.

Beide campagnes zullen dus vrijwel zeker permanent op **"Beperkt leren"** blijven staan.
Dat is geen reden om het niet te doen: je signaal is nu actief verkeerd. **Een dun maar
juist signaal is beter dan een dik maar verkeerd signaal** — dat laatste is precies
waarom € 492 naar de advertentie met de laagste orderwaarde gaat.

Maar wees erop voorbereid: de levering wordt minder soepel en de kosten per
vertoning kunnen stijgen. Dat is de prijs van sturen op omzet in plaats van aantallen.

### Je verliest staalaanvragen
Dat is de bedoeling, en het is nu verdedigbaar omdat stalen geen marge hebben
(€ 6,95 verkoop tegen € 6,95 kostprijs) **en de opvolging niet draait**: nul procent
herstel op verlaten checkouts, nog nooit een opvolgmail verstuurd.

Zodra `05-OPVOLGFLOW-STALEN.md` live staat, verandert die rekensom en zet je een
aparte derde campagne op met een klein budget die op `Staalaanvraag` optimaliseert.
Pas dán hebben stalen aantoonbaar waarde.

### Minder plaatsingen kan je CPM in de feeds opdrijven
Minder speelruimte in de veiling. Nameten na een week.

---

## 5. De strategische vervolgstap — nu nog niet

`zakelijk verbouwen` is de enige advertentie met knop **CONTACT_US**, heeft de
hoogste CTR van het account (7,68%), een orderwaarde van € 155,40, en wordt
nauwelijks bekeken als video (277 afspelingen op 17.564 vertoningen).

[VERMOEDEN] Zakelijke kopers willen contact, geen afrekenknop.

Als dat klopt, is je grootste onbenutte kans een **offerte- of contactformulier op
de zakelijke pagina** met een campagne op doel `Leads`. Dat lost meteen het
volumeprobleem op: aanvragen zijn er veel meer dan aankopen, dus Meta krijgt eindelijk
genoeg signaal om goed te optimaliseren — én het sluit aan bij hoe deze kopers zich
werkelijk gedragen.

Dat is de echte sleutel om zakelijk voorbij € 40/dag te schalen. Niet nu doen:
eerst deze splitsing laten landen en meten.

---

## 6. Wie doet wat

| Fase | Actie | Wie |
|---|---|---|
| 1 | Aangepaste conversies `Aankoop boven € 20` en `Staalaanvraag` | **Jij** |
| 2 | Campagne hernoemen, nieuwe campagne, ad set dupliceren, oude pauzeren, 4 verliesgevers pauzeren | **Ik** |
| 3 | Conversiegebeurtenis, handmatige plaatsingen, Advantage+ uit op zakelijk | **Jij** |
| 4 | Budgetten zetten en elke 4 dagen bijstellen | **Ik**, na jouw akkoord per stap |
| 5 | Meten op dag 7 en 14 | **Ik** |

Ik voer fase 2 pas uit als jij fase 1 hebt gedaan én akkoord geeft. Zonder de
aangepaste conversie is splitsen zinloos: dan verdeel je hetzelfde verkeerde
signaal over twee campagnes.
