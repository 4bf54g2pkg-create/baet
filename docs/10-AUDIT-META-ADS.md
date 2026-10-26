# Audit Meta Ads — advertentieaccount PureDeco (1266095837740836)

**Versie 2 — 26 oktober 2026.** Versie 1 stond op een venster van 14 dagen
(10–23 oktober). Een terechte vraag van de opdrachtgever over de kosten per aankoop
van `Nieuwe wandpanelen` liet zien dat dat venster op drie punten een verkeerd beeld
gaf. Deze versie rust op **30 dagen (26 september – 25 oktober)** en noemt bij elke
conclusie of die over beide vensters standhoudt.

**Bron:** Meta Marketing API via Windsor, gelezen 26 oktober. **Er is niets gewijzigd.**

## Rekenbasis

Conversiewaarden van Meta zijn ordertotalen **inclusief btw** (gecontroleerd:
staalorders komen binnen als exact € 6,95). Brutomarge 69,7% over omzet ex btw.
Break-even ROAS = 1,21 / 0,697 = **1,74**. Winst = waarde / 1,21 × 0,697 − kosten.

> **Alle ROAS-cijfers zijn Meta's eigen toeschrijving** (7 dagen klik / 1 dag weergave)
> en overschatten vrijwel zeker het eigen aandeel. **De absolute hoogte is
> onbetrouwbaar; de onderlinge rangorde niet**, want op elke advertentie en elke
> plaatsing rust hetzelfde model. Alle conclusies berusten op die vergelijking.

---

## 0. Wat ik in versie 1 fout had

### Fout 1 — `Nieuwe wandpanelen` is geen winnaar
Ik noemde de advertentie winstgevend en adviseerde er budget naartoe te schuiven.

| | 14 dagen | 30 dagen |
|---|---:|---:|
| Kosten | € 64,48 | € 160,15 |
| Aankopen | 4 | 5 |
| Kosten per aankoop | € 16,12 | **€ 32,03** |
| ROAS | 2,45 | **1,03** |
| Winst | +€ 26,36 | **−€ 65,31** |

In de zestien dagen buiten mijn venster gaf deze advertentie € 95,67 uit voor
**één aankoop van € 6,95**. Mijn venster van 14 dagen ving precies haar enige
goede twee weken. Over 30 dagen heeft ze de **hoogste kosten per aankoop van alle
advertenties die überhaupt converteren** en zit ze onder break-even.
**Advies E uit versie 1 is ingetrokken.**

### Fout 2 — Instagram Stories moest níet uit
Ik adviseerde Stories en Reels samen uit te zetten. Dat was voor Stories verkeerd:

| Plaatsing | 14d ROAS | 14d winst | 30d ROAS | 30d winst |
|---|---:|---:|---:|---:|
| instagram / stories | 0,41 | −€ 130,49 | **2,20** | **+€ 103,95** |
| instagram / feed | 1,73 | −€ 0,40 | **2,29** | **+€ 123,70** |

Instagram Stories staat over 30 dagen **boven** break-even. Had je mijn advies
uitgevoerd, dan had je een winstgevende plaatsing uitgezet. Reels blijven wél slecht
(zie punt 3) — het waren de Reels, niet de Stories.

### Fout 3 — de advertentieset "Video's" verliest geen geld
Over 14 dagen stond die op −€ 42,59; over 30 dagen op **+€ 323,12**.

### Fout 4 — mijn "beste hook"-claim was op een onbruikbare maat gebouwd
Ik noemde `Nieuwe wandpanelen` de beste hook van het account op grond van
afspelingen per vertoning (88,8%). Die maat is ongeschikt:

[FEIT] Op Audience Network is het aantal afspelingen **exact gelijk** aan het aantal
vertoningen — 39 op 39, 32 op 32, 41 op 41, 23 op 23, 3 op 3. Een afspeling wordt dus
geteld zodra de video automatisch start, niet wanneer iemand blijft kijken. De maat
meet de plaatsing, niet je creatief.

[FEIT] `video_continuous_2_sec_watched_actions` — de maat die een echte hook zou meten —
staat op **0 voor alle zeven advertenties**. Meta vult dat veld voor dit account niet.
**Ik kan hookkwaliteit dus helemaal niet meten.** Die claim had ik niet moeten maken.

---

## 1. De kern over 30 dagen: twee winnaars, vijf verliezers

| Advertentie | Kosten | Aank. | Per aank. | AOV | ROAS | Winst | Zelfde beeld bij 14d? |
|---|---:|---:|---:|---:|---:|---:|---|
| **zakelijk verbouwen** | € 394,31 | 24 | € 16,43 | **€ 155,40** | **9,46** | **+€ 1.754,06** | ja (9,64) |
| **Marmerlook va 125** | € 435,01 | 26 | € 16,73 | € 67,02 | **4,01** | **+€ 568,67** | onderschat (1,91) |
| diaan creator 1 | **€ 492,45** | **32** | **€ 15,39** | € 22,64 | 1,47 | −€ 75,13 | ja (1,50) |
| diaan creator 2 | € 82,30 | 4 | € 20,57 | € 6,95 | 0,34 | −€ 66,29 | ja (0,16) |
| Nieuwe wandpanelen | € 160,15 | 5 | **€ 32,03** | € 32,93 | 1,03 | −€ 65,31 | **nee** (2,45) |
| video 3 | € 23,55 | 0 | — | — | 0,00 | −€ 23,55 | ja |
| Video led profiel japans | € 15,28 | 0 | — | — | 0,00 | −€ 15,28 | ja |
| **Totaal** | **€ 1.603,05** | **91** | € 17,62 | € 70,21 | 3,99 | **+€ 2.077,18** | |

Twee winstgevende advertenties: **+€ 2.322,73**. Vijf verlieslatende: **−€ 245,55**.

### `diaan creator 1` is het zuiverste bewijs van wat er mis is
Dit is de **grootste budgetpost van het account** (€ 492,45) en haalt de
**meeste aankopen** binnen (32) tegen de **laagste kosten per aankoop** (€ 15,39).
En het verliest geld, op beide vensters (ROAS 1,50 en 1,47 — opvallend stabiel,
dus geen venstertoeval).

Gemiddelde orderwaarde: € 22,64. Dat is nauwelijks boven de staalprijs.
Precies hierom geeft het algoritme er het meeste budget aan: het is opgedragen
aantallen te kopen, en dit is de goedkoopste bron van aantallen in het account.

### `Marmerlook va 125` had ik onderschat
Over 14 dagen leek die marginaal (+€ 21). Over 30 dagen is het de tweede winnaar:
ROAS 4,01, 26 aankopen, AOV € 67,02, **+€ 568,67**. Dit is de advertentie die
budget verdient — niet `Nieuwe wandpanelen`.

---

## 2. Advertentiesets over 30 dagen: het budget zit nog steeds verkeerd

| Set | Kosten | % budget | Aank. | AOV | ROAS | Winst | Bereik | Freq. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Video's | € 1.208,74 | **75,4%** | 67 | € 39,69 | 2,20 | +€ 323,12 | 24.833 | 3,40 |
| zakelijke doelgroep | € 394,31 | **24,6%** | 24 | € 155,40 | **9,46** | **+€ 1.754,06** | 8.798 | 3,09 |

[FEIT] Campagnebudget (CBO) € 60,00/dag, biedstrategie `LOWEST_COST_WITHOUT_CAP`,
geen budget op setniveau. **Drie kwart van het budget gaat naar de set die een
vijfde van de winst maakt.** Deze conclusie staat op beide vensters.

Frequentie 3,09 op een bereik van 8.798 in 30 dagen: de zakelijke set is niet
verzadigd. Er is ruimte om te groeien.

---

## 3. Plaatsingen over 30 dagen: het zijn de Reels

| Plaatsing | Kosten | % budget | Aank. | Waarde | ROAS | Winst | 14d gelijk? |
|---|---:|---:|---:|---:|---:|---:|---|
| facebook / feed | € 516,87 | 32,2% | 35 | € 4.461,56 | **8,63** | **+€ 2.053,13** | ja |
| instagram / stories | € 386,92 | 24,1% | 17 | € 852,15 | 2,20 | +€ 103,95 | **nee** |
| instagram / feed | € 385,33 | 24,0% | 25 | € 883,68 | 2,29 | +€ 123,70 | **nee** |
| instagram / reels | € 157,63 | 9,8% | 6 | € 41,70 | **0,26** | **−€ 133,61** | ja (0,49) |
| facebook / reels | € 120,61 | 7,5% | 5 | € 34,75 | **0,29** | **−€ 100,59** | ja (0,19) |
| facebook / stories | € 24,17 | 1,5% | 0 | € 0,00 | 0,00 | −€ 24,17 | ja |
| facebook / profile_feed | € 0,91 | 0,1% | 3 | € 115,09 | 126,47 | +€ 65,39 | ja |
| 12 overige plaatsingen | € 10,34 | 0,6% | 0 | € 0,00 | 0,00 | −€ 10,34 | ja |

Gegroepeerd:

| Groep | Kosten | % budget | ROAS | Winst |
|---|---:|---:|---:|---:|
| Feeds | € 903,12 | 56,3% | 6,05 | **+€ 2.242,21** |
| Stories | € 411,09 | 25,6% | 2,07 | +€ 79,77 |
| **Reels** | **€ 278,24** | **17,4%** | **0,27** | **−€ 234,20** |
| Overig | € 10,34 | 0,6% | 0,00 | −€ 10,34 |

[FEIT] **Reels kosten € 278,24 per 30 dagen en leveren € 76,45 op.** Van de
11 aankopen daaruit is de waarde € 41,70 en € 34,75 — dat is 6 × € 6,95 en 5 × € 6,95.
Louter stalen. Dit beeld is identiek op beide vensters: ROAS 0,26 tegen 0,49 en
0,29 tegen 0,19. Geen venstertoeval.

Facebook Stories voegt daar € 24,17 aan toe voor nul aankopen, en de twaalf
restplaatsingen € 10,34 voor nul aankopen.

---

## 4. De hoofdoorzaak: er wordt op aantallen geoptimaliseerd, niet op waarde

[FEIT] Beide advertentiesets staan op `adsset_optimization_goal: OFFSITE_CONVERSIONS` —
**maximaliseer het aantal conversies**, niet de waarde. Voor Meta telt een staal van
€ 6,95 dan precies zo zwaar als een order van € 1.500.

[FEIT] De pixel **stuurt waarde wél mee**: `action_values_purchase` is gevuld met
echte bedragen. Waarde-optimalisatie is technisch beschikbaar en wordt niet gebruikt.

Het gevolg is overal in dit rapport zichtbaar en het duidelijkst bij `diaan creator 1`:
de goedkoopste aankopen, de meeste aankopen, het grootste budget — en verlies.
Meta doet niets fout; de opdracht is verkeerd.

**Dit is dezelfde fout als bij Google Ads**, waar `Aankoop` een staal van € 6,95
als volwaardige conversie meetelt. Op beide platformen koop je aantallen in plaats
van omzet. Dat is de gemene deler achter vrijwel alles hier.

---

## 5. Meetfout: meer aankopen dan gestarte checkouts

Over 10–23 oktober: 2.495 landingspagina's → 107 keer winkelwagen → **18 checkouts
gestart** → **45 aankopen**.

[FEIT] Je kunt niet afrekenen zonder een afrekening te beginnen. Het
`InitiateCheckout`-event vuurt structureel te weinig. Ook winkelwagen → aankoop
(107 → 45, 42%) is onrealistisch hoog; normaal 10 tot 20%.

Dat is niet alleen rapportage: Meta gebruikt deze events om koopintentie te
herkennen. Een kapot trechtersignaal maakt de optimalisatie blinder.

---

## 6. Video-interactie zegt in dit account niets over winst

| Advertentie | Thruplay per vertoning | Winst over 30 dagen |
|---|---:|---:|
| Nieuwe wandpanelen | 10,8% | −€ 65,31 |
| Marmerlook va 125 | 8,1% | +€ 568,67 |
| diaan creator 1 | 5,5% | −€ 75,13 |
| diaan creator 2 | 1,3% | −€ 66,29 |
| **zakelijk verbouwen** | **0,1%** | **+€ 1.754,06** |

De winstgevendste advertentie van het account wordt vrijwel nooit bekeken
(277 afspelingen op 17.564 vertoningen) maar heeft de hoogste CTR (7,68%) en
de langste kijktijd onder wie wél kijkt (13,9 seconden). Deze advertentie werkt
via tekst en knop, niet via de video.

**Beoordeel creatives in dit account dus niet op video-interactie.** Er is geen
verband met winst, en de enige maat die een echte hook zou meten is niet gevuld.
`diaan creator 2` blijft slecht op élke maat (1,3% thruplay, ROAS 0,34 en 0,16).

### Knoppen
`zakelijk verbouwen` gebruikt als enige **CONTACT_US**. De andere gebruiken
SHOP_NOW, ORDER_NOW en LEARN_MORE. [VERMOEDEN] Zakelijke kopers willen contact,
geen afrekenknop — passend bij € 155,40 orderwaarde tegen € 22,64.

---

## 7. Structuur

| Punt | Waarde |
|---|---|
| Campagnes / sets / advertenties | 1 / 2 / 7 |
| Doel | `OUTCOME_SALES` |
| Biedstrategie | `LOWEST_COST_WITHOUT_CAP` (geen kostenplafond) |
| Budget | € 60,00/dag op campagneniveau (CBO) |
| Campagne gestart | 16 juni 2025 |
| Set "Video's" | 16 juni 2025 |
| Set "zakelijke doelgroep" | 13 april 2026 |

Zestien maanden op één campagne met één budget. De zakelijke doelgroep heeft
nooit een eigen budget gehad en kan dus niet los opschalen.

---

## 8. Herzien advies, op volgorde van opbrengst

### A. Geef `zakelijke doelgroep` een eigen campagne en budget — **staat**
Nu € 13,14/dag van het algoritme terwijl het € 1.754 per 30 dagen oplevert; de
rest krijgt € 40,29/dag voor € 323. Zolang beide uit één CBO-pot eten, kun je de
winnaar niet opschalen zonder de verliezer mee te voeden. Niet verzadigd (freq. 3,09).

### B. Zet **alleen Reels** uit — **bijgesteld**
Instagram Reels, Facebook Reels, Facebook Stories en de twaalf restplaatsingen:
samen € 313 per 30 dagen voor € 76 aan waarde.
**Instagram Stories en beide Feeds blijven staan** — die zijn winstgevend.
*Afweging:* minder plaatsingen betekent minder speelruimte in de veiling en kan de
CPM in de feeds opdrijven. Dat moet je na een week nameten.

### C. Stop met optimaliseren op aantallen — **staat**
Een **aangepaste conversie voor orders boven € 50** aanmaken en daarop optimaliseren
is bij dit volume beter dan waarde-optimalisatie (91 aankopen per 30 dagen, waarvan
een minderheid substantieel). Hiermee verdwijnt de staalvervuiling uit het signaal.
Dezelfde ingreep die Google Ads ook nodig heeft.

### D. `diaan creator 1` herzien — **nieuw, en groter dan ik dacht**
Grootste budgetpost van het account (€ 492,45) en verlieslatend op beide vensters.
Niet meteen pauzeren: 32 aankopen met AOV € 22,64 betekent dat het publiek er is,
maar verkeerd gericht. Zet eerst C door en kijk of het signaal de advertentie
naar betere kopers trekt; blijft de ROAS onder 1,74, dan stoppen.

### E. Geef `Marmerlook va 125` meer ruimte — **vervangt het oude advies E**
ROAS 4,01, AOV € 67,02, +€ 568,67. Dit is de tweede winnaar.
~~`Nieuwe wandpanelen` opschalen~~ — ingetrokken, zie punt 0.

### F. Zet `diaan creator 2` stop — **staat**
ROAS 0,34 en 0,16, 1,3% thruplay, −€ 66,29. Slecht op elke maat en elk venster.

### G. Beslis over `video 3` en `Video led profiel japans` — **staat**
Samen € 38,83 per 30 dagen voor nul aankopen, op 692 en 343 vertoningen in 14 dagen.
Dat zijn geen mislukkingen maar ongetoetste advertenties. Of een eigen testbudget,
of weghalen.

### H. Repareer het `InitiateCheckout`-event — **staat**

---

## 9. Wat ik kan uitvoeren en wat jij moet doen

| Actie | Wie |
|---|---|
| F — `diaan creator 2` pauzeren | **Ik**, na jouw akkoord |
| G — twee ongetoetste advertenties pauzeren | **Ik**, na jouw akkoord |
| A — nieuwe campagne + budget voor de zakelijke set | **Ik** kan campagne en budget aanmaken; doelgroep en creatives moet jij overzetten |
| E — budget naar `Marmerlook va 125` | Volgt uit A en B, of apart na jouw akkoord |
| B — plaatsingen beperken | **Jij** — niet via de koppeling te wijzigen |
| C — aangepaste conversie boven € 50 | **Jij** — conversie-instellingen vallen onder je eigen regel dat ik daar niet aan kom |
| D — `diaan creator 1` | Beslissen ná C, op nieuwe cijfers |
| H — `InitiateCheckout` | **Jij** of je themabeheerder; ik kan vaststellen waar het misgaat |

Ik voer niets uit tot je per punt zegt wat ik mag doen.

---

## 10. Les voor de methode

Drie van mijn vier onjuiste conclusies kwamen uit één keuze: een venster van
14 dagen bij ongeveer drie aankopen per dag. Bij die aantallen kan één order van
€ 1.500 of één magere week een advertentie van winnaar in verliezer veranderen.
Vanaf nu beoordeel ik advertenties op **30 dagen** en meld ik expliciet of een
conclusie op beide vensters standhoudt. De conclusies die dat doen —
`zakelijk verbouwen` als motor, de scheefgroei in het CBO-budget, Reels als
verliespost, en de optimalisatie op aantallen — zijn de conclusies waarop je
kunt handelen.
