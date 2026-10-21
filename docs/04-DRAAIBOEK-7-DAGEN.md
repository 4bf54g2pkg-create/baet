# Draaiboek — 7 dagen, klik voor klik

Hoort bij `03-CMO-RAPPORT-14D.md`. Elke stap staat hier zo uitgeschreven dat je hem kunt
uitvoeren zonder terug te hoeven zoeken waarom. Per stap: waar je moet zijn, wat je precies
invult, en wat je mag verwachten.

**Uitgangspunt dat nu vaststaat:** de kostprijs van een staal is **€6,95 per zending**, niet per
staaltje. De klant betaalt precies de kostprijs, dus de staaltransactie is kostenneutraal en de
volledige verwachte brutowinst van **€33,26 per staalaanvraag** blijft staan, zonder aftrek.
Daarmee is het CPA-plafond **€33,26** en het operationele streefdoel **€25**.

**Twee dingen die je nooit moet doen zolang de staalconversie op €6,95 geregistreerd staat:**
overstappen op "Conversiewaarde maximaliseren" of tROAS in Google, en overstappen op
waarde-optimalisatie in Meta. Beide sturen weg van je winstgevendste conversie.

---

## DAG 1 — Twee ingrepen, nul risico

### 1.1 Google Ads: de winkelwagenconversie op Secundair zetten

**Waarom:** twee problemen in één conversieactie.

Ten eerste staan er **twee** primaire conversieacties voor "Toevoegen aan winkelwagen", met de
status "Vereist aandacht". Dat verdubbelt het signaal.

Ten tweede, en zwaarder: de **conversiewaarde** van deze actie is enorm. GA4 meet over 7–20 oktober
231 toevoegingen aan de winkelwagen met 995 artikelen en een waarde van **€ 143.571,55**. Per
artikel is dat € 144,29 — precies de gemiddelde paneelprijs, dus de tag rekent correct en het
bedrag is niet fout. Het is hoog omdat mensen gemiddeld 4,3 panelen tegelijk in het mandje leggen
en een paneel € 90 tot € 599 kost.

Maar daartegenover staan 77 aankopen met **€ 2.958,15**: slechts **2,1%** van die mandjeswaarde
wordt betaald, en 117 van de 231 toevoegingen worden weer verwijderd. Staat deze actie op Primair
en loopt er ergens een waarde-gebaseerde biedstrategie, dan optimaliseert Google op € 143.572 aan
mandjes in plaats van op € 2.958 aan omzet: een factor **48**. Dat is een plausibele verklaring voor
het gedrag van PMax (€ 104,55 per conversie, ROAS 0,55, twee periodes op rij).

"Aankoop" is wél goed ingericht: dat is de enige primaire aankoopactie (11,00 conversies, €843,65),
en `adscale_purchase` staat correct op Secundair met identieke cijfers.

**Waar:** Google Ads → **Doelen** → **Conversies** → **Overzicht** → klik op de groep
**"Toevoegen aan winkelwagen"**.

**Wat je doet:** zet **beide** acties op **Secundair**, niet alleen één van de twee.
1. Open de eerste actie → **Instellingen bewerken** → **Primaire of secundaire actie** →
   **Secundair** → **Opslaan**.
2. Hetzelfde voor de tweede.
3. Controleer in het overzicht dat **"Aankoop"** daarna de enige primaire conversieactie is.

Je verliest hier geen meting mee: de cijfers blijven zichtbaar in de rapportage, ze wegen alleen
niet meer mee in het bieden. Een winkelwagen is een diagnostisch signaal, geen biedoel.

**Let op:** zet *nooit* `adscale_purchase` op Primair. Dan verdubbelt je aankoopsignaal onmiddellijk.

**Verwacht effect:** schoner biedsignaal, en het wegnemen van een conversiewaarde die 48× hoger is
dan de werkelijke omzet. Geen verschil in conversieaantallen.
**Risico:** nihil. **Betrouwbaarheid:** hoog. **Prioriteit:** 1.

### 1.2 Bevestig dat Search | Concurrenten uit blijft

**Waarom:** 0 conversies in de laatste 14 dagen, 0 in de 14 daarvoor, 0 over de volledige
30-daagse zoektermexport. €76,99 besteed in 14 dagen, volledig verloren. Kwaliteitsscore 3. Binnen
die campagne ging €85,60 van de €138,83 zoekwoordbudget naar het brede zoekwoord `paneli` en
€42,43 naar AI Max voor 30 klikken.

**Waar:** Google Ads → **Campagnes** → zoek **Search | Concurrenten** → status moet
**Gepauzeerd** zijn.

**Verwacht effect:** €5,50 per dag bespaard. **Risico:** nihil. **Prioriteit:** 1.

---

## DAG 2 — Uitsluitingen en drie Meta-advertenties pauzeren

### 2.1 Uitsluitingslijst aanmaken

**Waarom:** €90,71 over 30 dagen naar zoektermen met **0 conversies**: €64,96 aan
concurrentmerken en €25,75 aan Engelse/buitenlandse termen. Dit is gemeten op het zichtbare deel
van €553,53 van de €1.124,73 accountkosten, dus de werkelijke verspilling is hoger.

**Waar:** Google Ads → **Campagnes** → **Doelgroepen, zoekwoorden en inhoud** →
**Zoekwoorden** → tabblad **Uitsluitingszoekwoorden** → **+** →
**Uitsluitingszoekwoordenlijst maken**.

**Naam de lijst:** `Uitsluitingen — merken en buitenlands`

**Stap A — concurrentmerken (zet deze op "woordgroep", met aanhalingstekens):**

```
"thuispaneel"
"paneli"
"benacci"
"akupanel"
"pure panels"
"style for walls"
"wooduo"
"enmod"
"full decor"
"woodupp"
"naturewall"
```

Dit kostte respectievelijk €20,52 · €10,99 · €8,72 · €7,56 · €3,77 · €3,38 · €3,25 · €3,23 ·
€2,97 · €0,57, samen **€64,96 met 0 conversies**. `naturewall` staat erbij als preventie; die
kostte nog niets.

> **Pas op met `"paneli"`:** als woordgroep sluit dit ook `duvar paneli`, `wall paneling` en
> `wood paneling wall` uit — allemaal gewenst, want alle drie leverden 0 conversies. Maar het
> sluit **niet** `panelen` of `wandpanelen` uit, want een woordgroep-uitsluiting matcht alleen
> het hele woord. Dat is precies goed.

**Stap B — Engelse/buitenlandse termen (zet deze op "exact", met blokhaken):**

[3 meter wall panel]
[acoustic panels]
[ahşap panel]
[bamboo wood metal plate]
[blue panels]
[dark walnut wood]
[dark walnut wood panel]
[deco pvc panel]
[deco wall tiles]
[decorating wall panels]
[dekor panel]
[exclusive decor]
[fabric texture wall panel]
[feisen decor]
[felt right wall panels]
[flexible travertine wall panels]
[fluted wall panel]
[fluted wood wall panel]
[japandi wall]
[leather panels]
[marble and wood review]
[marble wall panels]
[marble wall plate]
[metal wall]
[metal wall panels interior]
[orac wall panels]
[panel brown]
[panel de madera liso para pared]
[panel de nogal]
[panel drewniany scienny]
[panel ryflowany na wymiar]
[steel wall cladding]
[stick on wood panels]
[stucco wall panels]
[suede panels]
[travertine panel]
[travertine soft stone panels]
[travertine wall]
[travertine wall panels]
[veneer wood wallpaper]
[wall boards]
[wall deco panel]
[wall decor panels]
[wall decoration for bedroom]
[wall panel]
[wall panel kitchen backsplash]
[wall panel wood look]
[wall panels]
[wall panels hornbach]
[walnut wood panels]
[walnut wood panels for walls]
[white panels]
[wood grain curved board]
[wood panel]
[wood panel wall]
[wood veneer wall cladding]
[wood veneer wall panels]
[wooden panel]
[wooden wall panels]
[wpc wall panel]

Samen 60 termen, **€25,75 met 0 conversies**.

**Stap C — koppel de lijst** aan: **PMAX - Campagne - PureDeco.nl** en **Search | Wandpanelen**.
Google Ads → **Tools** → **Gedeelde bibliotheek** → **Uitsluitingslijsten** → selecteer de lijst →
**Toepassen op campagnes**.

**Verwacht effect:** €90,71 per 30 dagen bespaard plus betere signaalkwaliteit voor PMax.
**Risico:** laag. De exacte uitsluitingen raken alleen die precieze zoekterm.
**Betrouwbaarheid:** hoog. **Prioriteit:** 2.

### 2.2 Meta: drie advertenties pauzeren

**Waar:** Meta Ads Manager → campagne **Puredeco - onfluence** → ad set **Video's**.

| Advertentie | Ad ID | Kosten 14d | Resultaat | Zekerheid |
|---|---|---:|---|---|
| video 3 | 120229514950000057 | € 12,89 | 0 conversies op 52 klikken | Hoog |
| Video led profiel japans | 120234060598460057 | € 5,02 | 0 conversies op 16 klikken | Hoog |
| Nieuwe wandpanelen | 120241781668780057 | € 66,35 | 3 conversies, CPA € 22,12 | **Middel** |

**Over "Nieuwe wandpanelen":** CPA €22,12 zit onder het plafond van €33,26, en de CPA verbeterde
zelfs van €34,94. Dit is dus geen verliespost maar je zwakste presterende advertentie **met**
volume: conversieratio 0,90% tegen 1,97% voor diaan creator 1. Je pauzeert hem om het budget naar
een 2,2× effectievere creative te verplaatsen, niet omdat hij geld kost. **Wil je voorzichtig zijn,
laat deze dan staan** en neem alleen de twee nullen weg; dan schaal je in stap 3.1 met €4,74 minder.

**Hoe:** per advertentie de schuifknop naar **Uit**. Niet verwijderen — je wil de historie houden.

**Verwacht effect:** €6,02 tot €11,04 per dag vrij. **Prioriteit:** 2.

---

## DAG 3 — Opschalen, in één stap

### 3.1 Meta: budgetten verhogen

**Waarom in één stap en niet gefaseerd:** de ad set werkt met campagnebudgetoptimalisatie. Elke
budgetwijziging herstart de leerfase. Drie kleine stappen betekent drie keer leerfase; één stap
betekent één keer.

**Waar:** Meta Ads Manager → **Puredeco - onfluence** → per advertentie het budget.

| Advertentie | Ad ID | Nu | Naar | Wijziging | Onderbouwing |
|---|---|---:|---:|---:|---|
| diaan creator 1 | 120244727461840057 | € 16,98/d | **€ 30,00/d** | +€ 13,02 (+77%) | CPA €10,80 = 32% van het plafond. CPA verbeterde van €15,30 → €10,80 bij 14% **minder** budget. Conversieratio 1,97%, 3.535 post-engagements, 17 keer opgeslagen. |
| Marmerlook va 125 | 120251672142850057 | € 16,37/d | **€ 24,00/d** | +€ 7,63 (+47%) | CPA €14,33. Frequentie 1,83 = laagste van de grote drie, dus de meeste kopruimte. 58 add-to-carts à €7.906,90 = hoogste koopintentie. |
| diaan creator 2 | 120244728990010057 | € 3,24/d | **€ 8,00/d** | +€ 4,76 (+147%) | CPA verbeterde van €33,22 → €15,14. Pas 3 conversies, dus bewust een laag absoluut bedrag. |
| zakelijk verbouwen | 120243049922840057 | € 17,58/d | **€ 16,00/d** | −€ 1,58 (−9%) | **Niet pauzeren** — CPA €24,61 zit onder het plafond. Maar de CPA verslechterde van €14,78 → €24,61 (+66%) terwijl het budget 67% omhoog ging, met de hoogste frequentie (2,57) en de laagste conversieratio (0,75%). Vriest hier tot hij hersteld is. |

**Verwacht effect:** +8 tot +14 conversies per 14 dagen.
**Risico:** diaan creator 1 gaat 1,8× in budget. Verwacht dat zijn CPA van €10,80 naar €14–18
beweegt — nog ruim onder het plafond. **Afbreekpunt: als zijn CPA op dag 10 boven €25 staat, terug
naar €20/dag.** **Betrouwbaarheid:** middel-hoog. **Prioriteit:** 2. **Herbeoordelen:** dag 10.

### 3.2 Google: brandcampagnes verdubbelen

**Waarom:** samen €48,74 in 14 dagen voor 9 conversies = **€5,42 gemiddeld**, zes keer goedkoper
dan het accountgemiddelde van €26,83. Ze zijn gelimiteerd door hun eigen minibudget, niet door de
markt.

| Campagne | Nu | Naar | Onderbouwing |
|---|---:|---:|---|
| Brand \| PureDeco Protection NL-BE | € 1,65/d | **€ 4,00/d** | € 5,79/transactie, ROAS 15,08, CTR 42,11% |
| Brand \| PureDeco Protection | € 1,83/d | **€ 4,00/d** | € 5,11/transactie, CTR 38,30% |

**Waar:** Google Ads → **Campagnes** → campagne selecteren → **Instellingen** → **Budget**.

**Verwacht effect:** +3 tot +6 conversies per 14 dagen à circa €6.
**Risico:** nihil — bij merkzoekwoorden is het volume begrensd door de vraag, dus je budget raakt
niet zomaar op aan slecht verkeer. **Betrouwbaarheid:** hoog. **Prioriteit:** 2.

### 3.3 Google: Shopping iets omhoog

| Campagne | Nu | Naar | Onderbouwing |
|---|---:|---:|---|
| Shopping \| Bamboepanelen | € 5,43/d | **€ 9,00/d** | € 15,20/conversie zit ruim onder het plafond. CPC is €0,07 — uitzonderlijk goedkoop. |

**Maar let op:** 1.024 klikken leverden 707 sessies en 5 conversies = 0,49% conversieratio, en de
kosten per transactie liepen op van €11,32 naar €15,20 terwijl de kosten 236% stegen. Dit is een
kanaal met geweldige klikprijs en matige klikkwaliteit. **Zet daarom een harde controle op dag 10:
als de kosten per conversie boven €25 komen, terug naar €5,43.**

**Hypothese om te controleren, geen conclusie:** de campagne heet "Bamboepanelen" maar bamboe staat
in geen enkele top-25 verkooplijst van de laatste 14 dagen. Je bestverkopende panelen zijn Japandi
824 Taupe (28 orders), Doorlopend Marmer 689 Beverly Gold Slate (5 orders, €495,04 netto, hoogste
contributiemarge per order in het assortiment), Hout 812 Walnut Deep (23) en Marmer 670 Pandora
Slate (19). Kijk of de feed en de productgroepen daarop staan afgestemd.

---

## DAG 4 — PMax-besluit

**De cijfers:** €209,10 in 14 dagen voor 2 transacties = **€104,55 per conversie**, 3,1× het
plafond van €33,26. ROAS 0,55 tegen een break-even van 1,35. Dit is geen uitschieter: vorige
periode was het €107,22. Twee periodes, 28 dagen, €423,55 besteed, 4 transacties.
**Geschat verlies: €142,58 per 14 dagen.**

**Twee opties:**

**(a) Pauzeren** → €14,94/dag vrij, direct €142 per 14 dagen bespaard. Verdedigbaar: de data zegt
dit twee periodes op rij.

**(b) Nog 14 dagen op €13/dag, mét de uitsluitingen van dag 2** → en op **dag 18 definitief
beslissen**. Afbreekpunt: als de kosten per conversie dan nog boven €50 liggen, pauzeren.

**Mijn advies is (b)**, om twee redenen. PMax is het enige kanaal in je account dat buiten
zoekintentie werkt en dus nieuw publiek bereikt dat later via een ander kanaal terugkomt — dat is
niet meetbaar maar wel reëel. En de uitsluitingen van dag 2 zijn nog niet getest: PMax kocht 3.549
verschillende zoektermen voor 337 zichtbare klikken, en een flink deel van de €221,09 zichtbare
PMax-kosten ging naar termen die nu uitgesloten worden.

**Dit is het minst zekere advies in dit draaiboek.** De data zegt "stoppen"; ik zeg "nog één
ronde", omdat €142 per 14 dagen een acceptabele prijs is voor een eerlijke test na de
uitsluitingen. Kies (a) als je liever direct zekerheid hebt.

---

## DAG 5 — De grootste winstpost: opvolging staalaanvragers

**De cijfers:** 90 staalaanvragen in 14 dagen. 7,7% van de staalaanvragers koopt later panelen,
gemiddeld voor €752,62 incl. btw, mediaan na **16 dagen**. **41,2% van al je paneelomzet** komt van
mensen die eerder een staal aanvroegen. En er is **geen enkele opvolging**.

**Elke procentpunt die je die 7,7% verhoogt is ongeveer €414 brutowinst per 14 dagen**
(0,9 extra paneelorder × €459,70 brutomarge), zonder één euro mediabudget. Van 7,7% naar 12% is
circa **+€1.838 per 14 dagen**.

Dit is groter dan alle budgetwijzigingen in dit draaiboek bij elkaar.

De teksten staan in **`05-OPVOLGFLOW-STALEN.md`**. Het instellen in Shopify (of je e-mailtool)
doe jij, of je geeft mij daar apart toestemming voor.

---

## DAG 6 — Fundament en retargeting

### 6.1 Aparte conversieactie voor staalaanvragen

**Waarom dit de zwaarste trackingfout in je account is:** het staalproduct staat op €0,00 en de
€6,95 is een verzendkostenregel. Daardoor lezen Meta's `purchase`, GA4's `purchase_revenue` én
Shopify's `net_sales` een staalorder als **€6,95**, terwijl die **€33,26** waard is — een
onderwaardering van **4,8×**. Elke waarde-gebaseerde biedstrategie stuurt dus wég van je
winstgevendste conversie.

Het bewijs staat in Meta's eigen actiewaarden: *zakelijk verbouwen* rapporteert €69,50 waarde op 10
aankopen = **exact 10 × €6,95**. Hetzelfde bij *diaan creator 2* (€20,85 op 3) en *Nieuwe
wandpanelen* (€20,85 op 3).

**Wat je maakt:** Google Ads → **Doelen** → **Conversies** → **+ Conversieactie** → **Website** →
een actie die alleen vuurt op staalorders, met een **vaste waarde van €25** (niet €33,26 — €25 is
het streefdoel, met marge).

**Zet hem eerst op Secundair.** Pas als je twee weken hebt gezien dat de aantallen kloppen met
Shopify, overweeg je Primair. **Risico: middel** — een nieuwe conversieactie op de verkeerde stand
veroorzaakt dubbeltelling. Dit is de enige stap in dit draaiboek waar een fout echt iets kost.

### 6.2 Meta retargeting op afgebroken paneelwinkelwagens

**Waarom:** Meta leverde in 14 dagen **131 add-to-cart-events met een gezamenlijke waarde van
€19.384,66**, en daaruit kwam **0 paneelorder** in last-click attributie. Dat is het grootste
meetbare gat in de hele funnel. Er is op dit moment geen enkele retargeting-ad set; alles is
prospecting.

**Wat je maakt:** nieuwe ad set in **Puredeco - onfluence**:
- **Doelgroep:** website-bezoekers met `AddToCart` zonder `Purchase`, venster **14 dagen**
- **Budget:** € 8,00/dag
- **Creative:** begin met *Marmerlook va 125* — die heeft de hoogste add-to-cart-waarde (€7.906,90)
- **Optimalisatiedoel:** aankopen op **aantal**, niet op waarde

**Verwacht effect:** zelfs 2% herstel van die 131 winkelwagens is circa 2,6 orders. Bij de huidige
gemiddelde paneelorder is dat **+€150 tot €450 per 14 dagen** tegen €112 mediakosten.
**Betrouwbaarheid:** middel.

---

## DAG 7 — Hermeten

Haal alle cijfers uit deel 1 van het rapport opnieuw op en werk het dashboard bij.
Beslispunten:

| Check | Drempel | Actie bij overschrijding |
|---|---|---|
| CPA diaan creator 1 | onder € 18 | boven € 25 → terug naar € 20/dag |
| CPA zakelijk verbouwen | onder € 20 | boven € 33,26 → pauzeren |
| Kosten/conversie Shopping | onder € 25 | boven € 25 → terug naar € 5,43/dag |
| Kosten/conversie PMax (dag 18) | onder € 50 | boven € 50 → pauzeren |
| Totale CPA account | onder € 25 | boven € 33,26 → alle verhogingen terugdraaien |
| Verkochte panelen | 36+ per 14 dagen | onder 30 → oorzaak zoeken, niet budget verhogen |

---

## Budgetoverzicht

| Platform | Advertentie / campagne | Nu | Scenario B |
|---|---|---:|---:|
| Meta | diaan creator 1 | € 16,98 | € 30,00 |
| Meta | Marmerlook va 125 | € 16,37 | € 24,00 |
| Meta | zakelijk verbouwen | € 17,58 | € 16,00 |
| Meta | diaan creator 2 | € 3,24 | € 8,00 |
| Meta | Nieuwe wandpanelen | € 4,74 | € 0,00 |
| Meta | video 3 | € 0,92 | € 0,00 |
| Meta | Video led profiel japans | € 0,36 | € 0,00 |
| Meta | *retargeting (nieuw, vanaf dag 6)* | — | € 8,00 |
| Google | PMAX - Campagne | € 14,94 | € 13,00 |
| Google | Search \| Wandpanelen | € 10,91 | € 12,00 |
| Google | Shopping \| Bamboepanelen | € 5,43 | € 9,00 |
| Google | Search \| Concurrenten | € 5,50 | € 0,00 |
| Google | Brand \| Protection | € 1,83 | € 4,00 |
| Google | Brand \| Protection NL-BE | € 1,65 | € 4,00 |
| | **Totaal t/m dag 5** | **€ 100,44** | **€ 120,00** |
| | **Totaal vanaf dag 6** | | **€ 128,00** |

€120/dag = €3.650/maand. €128/dag = €3.894/maand.

---

## Bijlage — Windsor schrijfrechten aanzetten

Als je dit aanzet, kan ik de **Meta**-budgetwijzigingen van dag 3 zelf doorvoeren in plaats van ze
alleen voor te schrijven. Google Ads blijft buiten bereik, want die connector is niet gekoppeld.

**Wat er nu misgaat.** Elke poging tot een schrijfactie geeft letterlijk deze foutmelding:

> *"Write actions are disabled for the Windsor user info@puredeco.nl. Enable them in Settings >
> API Access ('Enable write actions for Claude, ChatGPT & API')."*

**Wat je doet:**
1. Ga naar windsor.ai en log in als **info@puredeco.nl**.
2. **Settings** → **API Access**.
3. Zet **"Enable write actions for Claude, ChatGPT & API"** aan.
4. Zeg het hier, dan test ik met één leesactie of de rechten daadwerkelijk doorkomen.

**Hoe ik er daarna mee omga.** Elke wijziging leg ik éérst aan je voor met de exacte waarde die ik
ga zetten, en pas na jouw "ja" voer ik hem uit. Ik raak nooit je conversie-instellingen,
pixels of tracking aan — dat heb je expliciet voorbehouden, en dat blijft zo.

**Wat dit níet oplost.** Google Ads blijft onbereikbaar. Daar zijn twee aparte dingen voor nodig:
de `google_ads`-connector in Windsor koppelen (die stuitte eerder op het passkey-scherm van
Google), en een account met **Standaard**-toegang tot het Google Ads-account — "Alleen lezen" is
niet genoeg voor schrijfacties. Een tweede Google-account met Standaard-toegang omzeilt de
passkey-blokkade.

> Een eerdere opmerking van mij hierover was fout en ik wil hem niet laten staan: ik adviseerde
> SMS of een authenticator-app voor dat passkey-scherm. Windsor's eigen documentatie zegt dat
> SMS-codes en authenticator-apps **niet** werken en dat een nieuwe passkey tot 7 dagen kan duren.
