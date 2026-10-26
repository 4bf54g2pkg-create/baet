# Wat een staalaanvraag werkelijk waard is — en wat dat verandert

**26 oktober 2026.** Naar aanleiding van de vraag: *"uit staalvragen komen echte
orders later?"* Antwoord: **ja.** Hieronder het getal, en de drie conclusies uit
mijn Meta-audit die daardoor sneuvelen.

---

## 1. Het cohort

499 klanten die tussen **12 mei en 12 oktober 2026** een staal aanvroegen, gevolgd
tot vandaag. Bron: Shopify Admin API, klantniveau.

| Rijpingsduur | Aanvragers | Kochten later panelen | Conversie | Paneelomzet per aanvrager |
|---|---:|---:|---:|---:|
| ≥ 30 dagen | 365 | 28 | 7,7% | € 57,74 |
| **≥ 60 dagen** | **287** | **20** | **7,0%** | **€ 57,07** |
| ≥ 90 dagen | 180 | 16 | **8,9%** | € 72,26 |

Wie converteert, besteedt gemiddeld **€ 718,75** (mediaan € 559,80; laagste € 124,95,
hoogste € 1.939,10).

### Hoe lang het duurt

| | Aandeel van de omzetters |
|---|---:|
| binnen 7 dagen | 28,6% |
| binnen 14 dagen | 45,7% |
| binnen 30 dagen | 82,9% |
| binnen 60 dagen | 91,4% |

Mediaan **16 dagen**, gemiddeld 23 dagen.

[FEIT] **71,4% van de omzet valt buiten Meta's venster van 7 dagen klik.** Meta ziet
die orders dus nooit — en mijn audit zag ze daarom ook niet.

---

## 2. De waarde van één staalaanvraag

| | |
|---|---:|
| Paneelomzet per aanvrager (60 dagen rijp) | € 57,07 incl btw |
| ÷ 1,21 × 69,7% marge | **€ 32,88 brutomarge** |
| Marge op het staal zelf (€ 6,95 verkoop, € 6,95 kostprijs) | € 0,00 |
| **Waarde van een staalaanvraag** | **€ 32,88** |

Dat is het **plafond** voor wat je per staalaanvraag aan advertentiekosten mag betalen.
Bij 90 dagen rijping loopt het op naar € 41,63, dus € 32,88 is eerder een vloer dan
een plafond.

Conservatief, als je alleen meetelt wat buiten Meta's venster valt en dus zeker niet
dubbel geteld wordt: **€ 23,48**.

[FEIT] **Dit cijfer had ik al.** In het dashboard staat sinds september een
staalplafond van € 33,26, berekend uit de marge over 28 dagen. Het cohort komt nu
onafhankelijk op € 32,88 uit — een bevestiging van binnen een procent.
**Ik heb dat plafond in de Meta-audit niet toegepast en alleen de directe orderwaarde
geteld. Dat is mijn fout, en het is de reden dat drie conclusies verkeerd waren.**

---

## 3. Wat dit met de Meta-cijfers doet

Model: voor elke aankoop die een staal is, reken € 32,88 marge; voor elke echte
order, de werkelijke marge (gemiddelde echte order over 7–26 oktober: € 489,45 incl
btw = € 281,94 marge). Aantallen stalen en echte orders per advertentie zijn
afgeleid uit de conversiewaarde die Meta rapporteert.

| Advertentie | Kosten | Aank. | Per aank. | **Oud** | **Nieuw** | Conservatief |
|---|---:|---:|---:|---:|---:|---:|
| zakelijk verbouwen | € 394,31 | 24 | € 16,43 | +€ 1.754 | **+€ 2.234** | +€ 2.078 |
| Marmerlook va 125 | € 435,01 | 26 | € 16,73 | +€ 569 | **+€ 1.226** | +€ 1.012 |
| **diaan creator 1** | € 492,45 | 32 | € 15,39 | **−€ 75** | **+€ 819** | +€ 528 |
| diaan creator 2 | € 82,30 | 4 | € 20,57 | −€ 66 | +€ 49 | +€ 12 |
| Nieuwe wandpanelen | € 160,15 | 5 | € 32,03 | −€ 65 | +€ 71 | +€ 27 |
| video 3 | € 23,55 | 0 | — | −€ 24 | −€ 24 | −€ 24 |
| Video led profiel japans | € 15,28 | 0 | — | −€ 15 | −€ 15 | −€ 15 |
| **Totaal** | **€ 1.603** | **91** | € 17,62 | **+€ 2.077** | **+€ 4.360** | **+€ 3.617** |

**Meta is ongeveer twee keer zo winstgevend als mijn audit zei.**

### De toets die geen aannames nodig heeft

Kost een aankoop minder dan € 32,88, dan is hij winstgevend — ook als het een staal is.

| | Per aankoop | Onder plafond? |
|---|---:|---|
| diaan creator 1 | € 15,39 | ja, ruim |
| zakelijk verbouwen | € 16,43 | ja, ruim |
| Marmerlook va 125 | € 16,73 | ja, ruim |
| Feeds (plaatsing) | € 14,34 | ja, ruim |
| diaan creator 2 | € 20,57 | ja |
| Stories (plaatsing) | € 24,18 | krap |
| Reels (plaatsing) | € 25,29 | krap |
| Nieuwe wandpanelen | € 32,03 | krap |
| video 3 / Video led profiel japans | geen aankopen | nee — nul waarde |

---

## 4. Drie conclusies uit mijn audit die vervallen

### Vervalt 1 — `diaan creator 1` verliest geen geld
Ik noemde die advertentie "het zuiverste bewijs van wat er mis is": de goedkoopste
aankopen, het grootste budget, verlies. Dat laatste is onjuist. **Bij € 15,39 per
aankoop tegen een plafond van € 32,88 is dit de efficiëntste inkoop van je account.**
Het algoritme koos niet verkeerd; mijn rekenmethode was verkeerd.

### Vervalt 2 — Reels zijn geen verliespost van € 234
Met de cohortwaarde: **+€ 83** (of −€ 20 in de conservatieve lezing). Dat is
ongeveer break-even, niet de ramp die ik beschreef. Het advies "Reels uit" trek ik in.
Reels zijn de zwakste van de leverende plaatsingen, maar niet aantoonbaar verliesgevend.

### Vervalt 3 — de aangepaste conversie van € 20 moet je NIET maken
Dit was fase 1 van mijn plan, en het zou **de meest efficiënte aankoop van je
account uit het optimalisatiesignaal hebben gesneden.** Stalen kosten je € 15,39 en
zijn € 32,88 waard. Meta daarop laten optimaliseren is precies goed.

**Maak die conversie niet aan als optimalisatiedoel.** Wel nuttig als *meetinstrument*,
om stalen en echte orders in je rapportage te kunnen scheiden — maar niet om op te sturen.

---

## 5. Wat er dan wél mis is — en waarom jouw splitsing precies de juiste ingreep is

Het probleem is niet dat stalen waardeloos zijn. Het probleem is de **verhouding**:

| | Kosten per aankoop | Waarde | Verhouding |
|---|---:|---:|---:|
| Staalaanvraag | € 15,39 | € 32,88 | 2,1× |
| Echte order (gemiddeld € 489,45) | € 16,43 | € 281,94 | **17,2×** |

Voor Meta is beide "1 conversie", en ze kosten ongeveer hetzelfde (€ 15,39 tegen
€ 16,43). Het algoritme is dus indifferent — terwijl een echte order **acht keer**
zo rendabel is.

[FEIT] Met één gedeeld budget koopt Meta daarom ongeveer evenveel van beide.
**Met gescheiden budgetten kan het geen geld van zakelijk naar stalen schuiven, en
bepaal jij de verdeling op grond van de echte economie.**

Jouw instinct was dus goed, en de splitsing alléén is de ingreep. Het
conversie-event hoeft niet aangeraakt.

### Herzien budgetadvies

Nu: zakelijk € 14,08/dag, particulier € 43,17/dag.
Beide kanten zijn winstgevend, dus dit is geen kwestie van wegsnijden maar van
voorrang. Rendement op advertentiekosten: zakelijk 5,7×, Marmerlook 2,8×,
diaan creator 1 1,7×.

| | Zakelijk | Particulier | Totaal |
|---|---:|---:|---:|
| Nu | € 14 | € 43 | € 57 |
| **Variant A — zelfde budget** | € 25 | € 35 | € 60 |
| **Variant B — groeien** | € 40 | € 40 | € 80 |

Variant B is verdedigbaar omdat élke leverende advertentie onder het plafond zit.
Twee kanttekeningen: je prepaid saldo loopt dan sneller leeg, en de 7,0% conversie
is een gemiddelde over bestaand verkeer — bij opschalen naar koudere doelgroepen
zakt die waarschijnlijk. Reken dus niet lineair.

In beide varianten geldt: **maximaal +30% per stap, minimaal 4 dagen tussen stappen.**

---

## 6. Wat uit de audit onveranderd overeind blijft

| Bevinding | Waarom hij blijft staan |
|---|---|
| `video 3` en `Video led profiel japans` pauzeren | Nul aankopen op 30 dagen. Nul waarde, ongeacht het plafond. € 38,83 weg. |
| Advantage+ doelgroep UIT op zakelijk | Gaat niet over staalwaarde maar over of je zakelijke targeting bindt. Nu mag Meta eruit stappen. |
| 12 restplaatsingen uit | € 10,34, nul aankopen. |
| `InitiateCheckout` repareren | 45 aankopen tegen 18 gestarte checkouts blijft onmogelijk. |
| `diaan creator 2` | Was "stoppen". Nu: **grensgeval** (+€ 49 of +€ 12). Zwak creatief, maar economisch ongeveer neutraal. Lage inzet — € 82 per 30 dagen. |
| `Nieuwe wandpanelen` | Was "verliesgever". Nu: **krap** (€ 32,03 tegen plafond € 32,88). Niet opschalen, niet per se stoppen. |

---

## 7. De grootste conclusie van allemaal

Die 7,0% conversie van staal naar paneel wordt gehaald **zonder enige opvolging**.

[FEIT] Nul procent herstel op verlaten checkouts. Nul opvolgmails ooit verstuurd.
Geen e-mailmarketingapp geïnstalleerd. Mediaan 16 dagen tussen staal en paneelorder —
precies het venster waarin een opvolgmail zou landen.

Reken mee: tilt opvolging de conversie van 7,0% naar 9,0%, dan stijgt de waarde van
een staalaanvraag van € 32,88 naar € 42,28. Bij ongeveer 106 staalorders per maand
is dat **circa € 1.000 extra brutomarge per maand, zonder één euro extra advertentiebudget.**

En het verhoogt tegelijk het plafond waaronder je advertenties winstgevend zijn,
dus je kunt dan méér voor een staalaanvraag betalen dan je concurrent.

De opvolgflow uit `05-OPVOLGFLOW-STALEN.md` is daarmee niet een los klusje maar de
hoogst renderende onbenutte ingreep in het hele bedrijf — hoger dan welke
budgetverschuiving in Meta ook.

---

# AANVULLING — Zoho doet wél opvolging (correctie op punt 7)

**26 oktober 2026.** De opdrachtgever meldde: "zoho doen we al opvolging."
Dat is juist, en punt 7 hierboven is daarmee gedeeltelijk onjuist. Hieronder wat ik
in Shopify heb kunnen vaststellen.

## De app en wat hij mag

[FEIT] In de 24 geïnstalleerde apps staat:

| App | Ontwikkelaar | Toegangsrechten |
|---|---|---|
| **Zoho Flow** | PureDeco (eigen app) | `read_all_orders`, `read_orders`, `customer_read_orders` |

Drie rechten, alle drie alleen-lezen en alle drie op **orders**.

Daaruit volgt precies waarom mijn eerdere bevinding en jouw uitspraak allebei kloppen:

| Groep | Kan Zoho die zien? | Wordt er opgevolgd? |
|---|---|---|
| **Staalbestellers** (plaatsten een order van € 6,95) | **Ja** — dat is een order | **Ja**, volgens jou |
| **Verlaten checkouts** (bestelden nooit) | **Nee** — geen checkout-recht | **Nee**, 0% herstel staat overeind |

Een staalaanvraag ís een order. Een verlaten checkout is dat niet. Zoho Flow heeft
geen enkel checkout-recht, dus die groep is technisch onbereikbaar voor deze app.
**Mijn conclusie "nog nooit een opvolgmail verstuurd" ging over verlaten checkouts
en blijft daar geldig; voor staalbestellers was hij onjuist.**

[FEIT] Zoho Flow heeft ook geen `write_marketing_events`. Daarom is in Shopify geen
spoor van die mails te zien: geen marketingactiviteiten, geen toeschrijving. Niet
omdat er niets gebeurt, maar omdat deze app het niet terugmeldt.

## Wat dit met mijn rekensom doet

**Punt 7 hierboven is ingetrokken.** Ik schreef dat de 7,0% conversie "zonder enige
opvolging" wordt gehaald en dat opvolging circa € 1.000 extra marge per maand zou
opleveren. Als Zoho al mailt, is **7,0% juist de mét-opvolging-score**. De winst zit
dan niet in opvolging *toevoegen* maar in de bestaande flow *verbeteren* — en dat is
een kleinere, maar concretere kans.

De waarde van een staalaanvraag (€ 32,88) verandert hier niet door: die is gemeten op
de werkelijke uitkomst, inclusief wat Zoho al doet.

## Drie dingen die nu wél de echte vragen zijn

### 1. Mogen die mensen gemaild worden?

[FEIT] Steekproef van 60 staalaanvragers uit het cohort, marketingtoestemming in Shopify:

| | Aantal | Aandeel |
|---|---:|---:|
| `SUBSCRIBED` | 11 | **18,3%** |
| `NOT_SUBSCRIBED` | 49 | **81,7%** |

*Methodologische kanttekening:* ik wilde dit over alle 499 meten, maar Shopify's
`customersCount` negeerde mijn filters — alle vier de varianten gaven 685 terug.
Die uitkomst is dus onbruikbaar en ik heb hem verworpen. Bovenstaande cijfers komen
uit een handmatige steekproef van 60 klanten op klantniveau.

**Ruim vier op de vijf staalbestellers heeft geen marketingtoestemming in Shopify.**
Als Zoho die groep marketingmails stuurt, is de vraag op welke grondslag. Een
servicebericht over het bestelde staal is verdedigbaar; een reeks met aanbiedingen
is dat niet zonder toestemming. Dat is geen verwijt en ik ben geen jurist — maar het
moet je wel bekend zijn welke grondslag Zoho gebruikt.

Opvallend in dezelfde steekproef, met de nadruk op *klein*:

| | Herhaalorder | |
|---|---:|---:|
| Mét toestemming (n=11) | 5 | **45,5%** |
| Zonder toestemming (n=49) | 6 | **12,2%** |

[VERMOEDEN] Dat verschil is groot, maar n=11 is te klein om er beleid op te bouwen,
en het is waarschijnlijk deels omgekeerde causaliteit: wie zich inschrijft, had al
meer koopintentie. Toch wijst het dezelfde kant op: de bereikbare groep is waar de
conversie zit, en die groep is nu 18%.

### 2. Komen die mails aan? Dit is nu de hoogste prioriteit

Hier komt de SPF-controle terug die al sinds de audit openstaat, en nu is hij
dringend geworden. Als Zoho mail verstuurt namens `puredeco.nl` en SPF en DKIM zijn
daar niet op ingericht, dan landt je opvolging in de spambox. **Dan is die 7,0%
geen inhoudelijk resultaat maar een technisch geremd resultaat** — en is de
goedkoopste winst in je hele bedrijf een DNS-record.

Dat maakt deze vier controles nu de belangrijkste openstaande actie:

| Controle op `puredeco.nl` | Waar het om gaat |
|---|---|
| **SPF** | Staan **Zoho én Shopify** er beide in? Eén SPF-record, beide verzenders erin. |
| **DKIM** | Is er een Zoho-selector, naast `shopifyemail`? |
| **DMARC** | Bestaat het record, en op welk beleid? |
| **MX** | Waar komt inkomende post binnen? |

### 3. Verlaten checkouts blijven volledig onbenut

Dat is een andere groep en Zoho kan er niet bij. 28 echte prospects,
€ 9.088,45 aan waarde, 0% herstel. Daarvoor is nog steeds geen oplossing ingericht.

## Wat ik van jou nodig heb om de Zoho-flow te kunnen beoordelen

Ik kan niet in Zoho kijken — die connector is niet gekoppeld, en bij drie bronnen
is er ook geen plek voor. Om te kunnen zeggen of de flow goed of slecht presteert:

1. Welk Zoho-product? (Campaigns, Marketing Automation, CRM)
2. Hoeveel mails zitten er in de reeks, en op welke dagen na de staalorder?
3. Open- en klikpercentages
4. Op welke grondslag wordt er gemaild — toestemming of service?

Met de open- en klikcijfers plus de uitkomst die ik in Shopify kan meten
(staal → paneelorder per maandcohort) kan ik de flow wél beoordelen en gericht
verbeteren. Zonder die cijfers is elk advies over de inhoud gokken.

## Voetnoot bij de maandcijfers

Ik heb gekeken of er een moment is waarop de conversie omhoog springt — dat zou
aangeven wanneer de Zoho-flow is gaan draaien. Conversie binnen 30 dagen per
maandcohort: mei 3,4%, juni 8,2%, juli 3,8%, augustus 6,0%, september 12,5% (n=32).
Te veel ruis en te kleine aantallen om er iets uit te lezen. Geen bewijs voor of
tegen een effect.
