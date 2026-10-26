# Effectmeting na golf 1 — stand 26 oktober 2026

**Ingreep:** 21 oktober. Gepauzeerd in Google Ads: PMAX, Search | Japandi,
Search | Ruimtegericht, Search | Hout, Search | Concurrenten.
**Meta is met opzet niet aangeraakt.**

**Vergelijking:** basis 7–20 oktober (14 dagen) tegen 22–25 oktober (4 volle dagen).
21 oktober is de ingreepdag en valt buiten beide vensters; 26 oktober is nog niet compleet.

---

## 0. Wat ik wel en niet kon meten

| Bron | Status |
|---|---|
| Shopify Admin API (orders, omzet) | [FEIT] gelezen op 26 okt |
| Shopify Analytics (sessies, bron, checkout) | [FEIT] gelezen op 26 okt |
| Google Ads via Windsor | **[ONBEKEND] — geblokkeerd** |
| Meta Ads via Windsor | **[ONBEKEND] — geblokkeerd** |

Windsor geeft op elke leesvraag terug:

> *"reads are paused because you have 5 accounts connected and your Free plan includes 1 account"*

Er zijn 5 connectoren gekoppeld (facebook, google_ads, googleanalytics4, instagram,
searchconsole) op een plan dat er 1 toestaat. **Alle advertentiedata is daardoor
onleesbaar** — ook de cijfers van 22–25 oktober die ik hiervoor nodig had.
Alles hieronder komt dus uit Shopify, niet uit de advertentieplatformen.

---

## 1. Je gevoel is juist: de stalen zijn gehalveerd

| | 7–20 okt | 22–25 okt | Verschil |
|---|---:|---:|---:|
| **Staalorders** | **6,43/dag** | **3,25/dag** | **−49%** |
| Paneelorders | 1,07/dag | 0,75/dag | −30% |
| Orders totaal | 7,50/dag | 4,00/dag | −47% |

90 staalorders in 14 dagen tegen 13 in 4 dagen. Dat is geen ruis — dat is een halvering.

De −30% op panelen is **níet** betrouwbaar: dat zijn 3 orders in 4 dagen tegen 15 in
14 dagen. Bij die aantallen zegt een procentueel verschil niets.

---

## 2. De oorzaak is Meta, niet de Google-pauzes

Sessies per bron, per dag:

| Dag | direct | search | social | totaal | |
|---|---:|---:|---:|---:|---|
| 19 okt | 134 | 100 | 157 | 391 | |
| 20 okt | 116 | 119 | 148 | 383 | |
| **21 okt** | 161 | 97 | 168 | 426 | ← ingreep |
| 22 okt | 120 | 61 | 133 | 314 | |
| 23 okt | 111 | 54 | 75 | 240 | |
| **24 okt** | 50 | 65 | **10** | 125 | ← Meta valt stil |
| **25 okt** | 56 | 73 | **0** | 129 | |
| 26 okt (deel) | 32 | 16 | 3 | 51 | |

Uitgesplitst naar netwerk:

| Dag | Facebook | Instagram |
|---|---:|---:|
| 21 okt | 101 | 67 |
| 22 okt | 68 | 65 |
| 23 okt | 39 | 36 |
| 24 okt | **1** | **8** |
| 25 okt | **0** | **0** |
| 26 okt | **0** | 3 |

**Facebook staat sinds 24 oktober op nul. Instagram sinds 25 oktober.**

Dat kan niet door golf 1 zijn veroorzaakt: er is geen Meta-campagne gepauzeerd,
alleen Google-campagnes. De Google-pauze is terug te zien in `search`
(98 → 63 sessies/dag, −36%) en dat is ongeveer wat je verwacht als je PMAX,
Shopping-vraag en drie zoekgroepen weghaalt.

De daling in `direct` (−42%) hangt vermoedelijk samen met Meta: verkeer uit de
Facebook- en Instagram-app komt deels zonder herkenbare referrer binnen, en
terugkerende bezoekers die eerder via Meta kwamen vallen mee weg. [VERMOEDEN]

### Waarom het geen meetfout is

Als Meta nog liep maar de tagging kapot was, zou `direct` **stijgen** terwijl
`social` daalt. `direct` daalt juist mee. Bovendien dalen de orders (7,5 → 4,0/dag)
en de bereikte checkouts (12 op 21 okt → 2 op 24 okt). Het verkeer is echt weg.

### Mogelijke oorzaken — geen van de drie is vastgesteld

[VERMOEDEN] De vorm van de curve (168 → 133 → 75 → 9 → 0) is een
afbouw, niet een harde stop. Dat past bij:

1. een bereikt **accountbestedingslimiet** of maandbudgetplafond;
2. een **mislukte betaling** of verlopen betaalmiddel;
3. een **accountbeperking** of afgekeurde advertenties.

Een handmatige pauze geeft meestal een harde stop van de ene dag op de andere,
geen afbouw over drie dagen. Welke van de drie het is, kan ik niet zien zolang
Windsor dicht staat.

---

## 3. De omzet is niet ingezakt

| | 7–20 okt | 22–25 okt |
|---|---:|---:|
| Netto-omzet (ex btw) | € 330,49/dag | € 458,41/dag |
| Brutomarge bij 69,7% | € 230,35/dag | € 319,51/dag |

Dat is **+39%** — maar lees dat niet als winst van de ingreep.
Van de € 1.833,65 netto-omzet in het venster komt **€ 1.247,98 (68%) uit één order**
van 23 oktober (#2559, € 1.510,06 incl btw). Haal die order weg en de omzet ligt
onder de basis. Vier dagen met één grote order kunnen geen trend aantonen.

Wat je er wél uit mag lezen: **de omzet is niet gekelderd** terwijl het verkeer
halveerde en de staalorders halveerden. Dat is consistent met wat de analyse van
14 dagen al zei — het weggehaalde verkeer kocht vooral stalen van € 6,95 zonder marge.

---

## 4. Wat dit betekent voor de stalen

Stalen leveren per stuk geen marge op (verkoopprijs € 6,95, kostprijs € 6,95).
De halvering kost dus op dit moment geen geld. **Maar** je hebt zelf gezegd dat
stalen later tot paneelverkoop leiden, en dat is ook wat het staalcohort liet zien.

Daarmee is de halvering een **vertraagd** risico: de panelen die deze
staalaanvragers over twee tot zes weken zouden kopen, komen er niet.
Zolang de opvolging per e-mail nog niet staat (0% herstel op verlaten checkouts,
nog nooit een opvolgmail verstuurd) wordt elk gemist staal ook echt niet meer opgepikt.

---

## 5. Wat er nu moet gebeuren

### Door jou, vandaag

1. **Open Meta Ads Manager en kijk waarom de levering is gestopt.**
   Kijk op drie plekken: Facturering (openstaand bedrag, betaalmiddel),
   Accountoverzicht (bestedingslimiet, accountstatus) en de campagnestatus zelf.
   Dit is urgent: elke dag zonder Meta is een dag zonder staalinstroom.

2. **Zet Windsor weer open.** Vijf connectoren op een plan voor één betekent dat ik
   geen enkel advertentiecijfer meer kan lezen. Twee opties:
   upgraden, of terugbrengen naar één connector — maar dan verlies ik het zicht op
   de andere vier, en ik kan Google en Meta niet meer tegen elkaar afzetten.
   Mijn voorkeur is upgraden; anders is Google Ads de connector die het meeste oplevert.

### Door mij, zodra ik weer data heb

3. De dag-7-meting (28 oktober) afmaken met de werkelijke Google-kosten en
   conversies van 22–28 oktober, inclusief de kannibalisatietoets.
4. De staalinstroom per bron opnieuw meten zodra Meta weer loopt, zodat we weten
   hoeveel van de 6,43 stalen per dag daadwerkelijk van Meta kwam.

### Blijft open uit eerdere rondes

5. Shopify → Instellingen → Meldingen → Verlaten afrekenpoging aanzetten.
6. De drie `Local actions` en `Clicks to call` op Secundair zetten.
7. SPF-controle op puredeco.nl (staan Zoho **én** Shopify erin?) voor fase 2
   van de opvolgaudit.

---

## 6. Conclusie in één alinea

De Google-pauzes doen wat ze moesten doen: het zoekverkeer daalt met 36% en de
omzet volgt niet mee naar beneden. Maar daar bovenop is Meta sinds 24 oktober
volledig stilgevallen, en dat is niet iets wat wij hebben gedaan. Jouw gevoel over
de staalorders is correct — die zijn gehalveerd — en de belangrijkste oorzaak daarvan
is Meta, niet golf 1. Zolang Meta stilstaat én Windsor dicht staat, kan ik het
effect van golf 1 niet zuiver meten: de twee veranderingen lopen door elkaar.
