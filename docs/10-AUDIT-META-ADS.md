# Audit Meta Ads — advertentieaccount PureDeco (1266095837740836)

**Venster:** 10–23 oktober 2026 (14 dagen) — het laatste aaneengesloten venster
met levering. Vanaf 24 oktober stond het account stil wegens de onbetaalde rekening.
**Bron:** Meta Marketing API via Windsor, gelezen 26 oktober.
**Er is niets gewijzigd.** Dit is een beoordeling, geen ingreep.

## Rekenbasis

Conversiewaarden van Meta zijn ordertotalen **inclusief btw** (gecontroleerd:
staalorders komen binnen als exact € 6,95). Brutomarge 69,7% over de omzet ex btw.
Break-even ROAS op deze basis = 1,21 / 0,697 = **1,74**.
Winst = waarde / 1,21 × 0,697 − kosten.

> **Let op bij alle ROAS-cijfers hieronder:** dit is Meta's eigen toeschrijving
> (7 dagen klik / 1 dag weergave). Meta claimt over dit venster € 3.243,59 incl btw,
> terwijl Shopify over een vergelijkbaar venster € 4.626,79 ex btw aan netto-omzet
> registreerde — Meta claimt dus een fors deel van de totale omzet en overschat
> vrijwel zeker zijn aandeel. **De absolute ROAS is onbetrouwbaar; de onderlinge
> rangorde is dat niet**, want op elke advertentie en elke plaatsing rust hetzelfde
> toeschrijvingsmodel. Alle conclusies hieronder berusten op die vergelijking,
> niet op de absolute hoogte.

---

## 1. De kern: één advertentie draagt het hele account

| Advertentie | Kosten | Aankopen | Waarde | ROAS | AOV | Winst |
|---|---:|---:|---:|---:|---:|---:|
| **zakelijk verbouwen** | € 239,83 | 10 | € 2.312,31 | **9,64** | **€ 231,23** | **+€ 1.092,14** |
| Nieuwe wandpanelen | € 64,48 | 4 | € 157,70 | 2,45 | € 39,42 | +€ 26,36 |
| Marmerlook va 125 | € 213,35 | 10 | € 407,45 | 1,91 | € 40,74 | +€ 21,35 |
| diaan creator 1 | € 239,09 | 20 | € 359,18 | 1,50 | € 17,96 | −€ 32,19 |
| diaan creator 2 | € 43,44 | 1 | € 6,95 | 0,16 | € 6,95 | −€ 39,44 |
| video 3 | € 12,86 | 0 | € 0,00 | 0,00 | — | −€ 12,86 |
| Video led profiel japans | € 5,82 | 0 | € 0,00 | 0,00 | — | −€ 5,82 |
| **Totaal** | **€ 818,87** | **45** | **€ 3.243,59** | 3,96 | € 72,08 | **+€ 1.049,55** |

`zakelijk verbouwen` levert € 1.092,14 winst. Alle zes andere advertenties samen
leveren **−€ 42,59**. Het account is winstgevend dankzij één advertentie.

Zet `zakelijk verbouwen` en `diaan creator 1` naast elkaar: vrijwel identieke
kosten (€ 239,83 tegen € 239,09), maar € 2.312,31 tegen € 359,18 aan waarde.
`diaan creator 1` haalt **twee keer zoveel aankopen** binnen (20 tegen 10) en
toch 6,4× minder omzet. Gemiddelde orderwaarde € 17,96 tegen € 231,23.

**[CORRECTIE op mijn eerdere rapport.]** Ik heb Meta eerder getypeerd als een
"staalmachine" met weinig verspilling. Dat klopte voor de advertentieset Video's,
maar is onjuist voor het account als geheel: destijds had ik alleen aankoop-aantallen,
geen conversiewaarden. `zakelijk verbouwen` is op dit moment het winstgevendste
dat je op beide platformen hebt draaien.

---

## 2. Per advertentieset: het budget zit aan de verkeerde kant

| Advertentieset | Kosten | % budget | Aankopen | Waarde | ROAS | AOV | Winst |
|---|---:|---:|---:|---:|---:|---:|---:|
| Video's | € 579,04 | **70,7%** | 35 | € 931,28 | 1,61 | € 26,61 | **−€ 42,59** |
| zakelijke doelgroep | € 239,83 | **29,3%** | 10 | € 2.312,31 | 9,64 | € 231,23 | **+€ 1.092,14** |

[FEIT] De campagne draait op **campagnebudget (CBO) van € 60,00 per dag**
(`campaign_daily_budget: 6000`), met `LOWEST_COST_WITHOUT_CAP` als biedstrategie en
geen budget op advertentiesetniveau. Meta verdeelt dus zelf — en geeft **71% aan de
set die verlies draait en 29% aan de set die alle winst maakt**.

Dat is geen fout van Meta. Zie punt 4: het algoritme doet exact wat het is opgedragen.

---

## 3. De grootste losse hefboom: plaatsingen

| Plaatsing | Kosten | Aankopen | Waarde | ROAS | Winst |
|---|---:|---:|---:|---:|---:|
| facebook / feed | € 316,50 | 17 | € 2.828,81 | **8,94** | **+€ 1.312,98** |
| instagram / stories | € 170,52 | 10 | € 69,50 | **0,41** | −€ 130,48 |
| instagram / feed | € 167,27 | 10 | € 289,68 | 1,73 | −€ 0,40 |
| facebook / reels | € 72,14 | 2 | € 13,90 | **0,19** | −€ 64,13 |
| instagram / reels | € 71,09 | 5 | € 34,75 | **0,49** | −€ 51,08 |
| facebook / stories | € 14,82 | 0 | € 0,00 | 0,00 | −€ 14,82 |
| 12 overige plaatsingen | € 6,53 | 1 | € 6,95 | — | −€ 3,06 |

Samengevat:

| Groep | Kosten | % budget | Waarde | ROAS | Winst |
|---|---:|---:|---:|---:|---:|
| **Feeds** | € 484,43 | 59,2% | € 3.125,44 | **6,45** | **+€ 1.315,92** |
| **Stories + Reels** | € 329,98 | **40,3%** | € 118,15 | **0,36** | **−€ 261,92** |
| Overig | € 4,46 | 0,5% | € 0,00 | 0,00 | −€ 4,46 |

[FEIT] **Veertig procent van je budget gaat naar Stories en Reels en komt terug
als € 0,36 per besteide euro.** € 23,57 per dag, en de 17 aankopen daaruit zijn
vrijwel allemaal stalen: Instagram Stories 10 aankopen à gemiddeld € 6,95,
Instagram Reels 5 aankopen voor € 34,75 samen, Facebook Reels 2 voor € 13,90.
Exact € 6,95 per stuk. Dat zijn geen klanten, dat zijn staalaanvragers.

[VERMOEDEN] De oorzaak is waarschijnlijk **creatief, niet de plaatsing zelf**:
je video's zijn vermoedelijk liggend of vierkant en werken niet in een verticaal
schermvullend formaat. Dat is te testen, maar niet voor € 330 per veertien dagen
zonder opzet.

---

## 4. De hoofdoorzaak: er wordt op aantallen geoptimaliseerd, niet op waarde

[FEIT] Beide advertentiesets staan op `adsset_optimization_goal: OFFSITE_CONVERSIONS`.
Dat betekent: **maximaliseer het aantal conversies.** Niet de waarde ervan.

Voor Meta telt een staal van € 6,95 dan precies zo zwaar als een order van € 1.500.
Het algoritme koopt dus rationeel de goedkoopste conversies die het kan vinden — en
dat zijn stalen. Meta doet niets fout; de opdracht is verkeerd.

[FEIT] De pixel **stuurt wél waarde mee** — `action_values_purchase` is gevuld met
echte bedragen (€ 6,95, € 2.312,31). Waarde-optimalisatie is dus technisch beschikbaar
en wordt alleen niet gebruikt.

**Dit is exact dezelfde fout als bij Google Ads**, waar `Aankoop` een staal van
€ 6,95 als volwaardige conversie meetelt. Op beide platformen koop je aantallen
in plaats van omzet. Dat is de gemene deler achter vrijwel alles in dit rapport.

---

## 5. Meetfout: er zijn meer aankopen dan gestarte checkouts

| Stap | Aantal |
|---|---:|
| Landingspagina bekeken | 2.495 |
| Toegevoegd aan winkelwagen | 107 |
| Checkout gestart | **18** |
| Aankopen | **45** |

[FEIT] 45 aankopen tegen 18 gestarte checkouts is onmogelijk — je kunt niet afrekenen
zonder een afrekening te beginnen. Het `InitiateCheckout`-event vuurt dus structureel
te weinig. Ook de stap winkelwagen → aankoop (107 → 45, 42%) is onrealistisch hoog;
normaal ligt die tussen 10 en 20%.

Dat is niet alleen een rapportagekwestie: Meta gebruikt deze events als signaal om
koopintentie te herkennen. Een kapot trechtersignaal maakt de optimalisatie blinder.

---

## 6. Creatief: hook en vasthouden

| Advertentie | Plays/vertoningen | p25/plays | Volledig uitgekeken | Thruplay |
|---|---:|---:|---:|---:|
| Nieuwe wandpanelen | **88,8%** | 32,4% | **12,1%** | 12,2% |
| Marmerlook va 125 | 55,6% | 20,2% | 7,8% | **14,6%** |
| diaan creator 2 | 48,2% | 17,0% | **2,5%** | 2,6% |
| diaan creator 1 | 44,6% | 13,1% | 5,5% | 12,4% |
| zakelijk verbouwen | 1,6% | 26,0% | 7,6% | 7,6% |
| video 3 | 14,5% | 18,0% | 5,0% | 16,0% |
| Video led profiel japans | \<50 plays — te weinig vertoond om te beoordelen | | | |

- **`Nieuwe wandpanelen` heeft de beste hook van het account** (88,8% van de
  vertoningen leidt tot een afspeling) én het beste vasthouden (12,1% kijkt volledig uit).
  En het is winstgevend. Toch kreeg het maar € 64,48 van € 818,87 — 7,9% van het budget.
- **`diaan creator 2` is creatief zwak**: 2,5% kijkt uit, ROAS 0,16. Dit is niet een
  kwestie van te weinig budget, dit werkt gewoon niet.
- `zakelijk verbouwen` speelt nauwelijks af (1,6%) maar heeft wel de hoogste CTR
  (7,68%) en de langste kijktijd (13,9 seconden) onder wie wél kijkt. Deze advertentie
  werkt via de tekst en de knop, niet via de video.
- `Marmerlook va 125` en `diaan creator 1` zijn de enige twee met
  `ABOVE_AVERAGE` op kwaliteit, interactie én conversie. De rest staat op `UNKNOWN`
  (te weinig vertoningen in het beoordelingsvenster).

### Knoppen
`zakelijk verbouwen` — de winnaar — gebruikt **CONTACT_US**. De verliezers gebruiken
SHOP_NOW, ORDER_NOW en LEARN_MORE. [VERMOEDEN] Zakelijke kopers willen contact,
geen afrekenknop. Dat sluit aan bij de orderwaarde van € 231,23 tegen € 17,96.

---

## 7. Structuur

| Punt | Waarde |
|---|---|
| Campagnes | 1 |
| Advertentiesets | 2 |
| Advertenties | 7 (waarvan 2 vrijwel niet vertoond) |
| Doel | `OUTCOME_SALES` |
| Biedstrategie | `LOWEST_COST_WITHOUT_CAP` (geen kostenplafond) |
| Budget | € 60,00/dag op campagneniveau (CBO) |
| Campagne gestart | **16 juni 2025** |
| Set "Video's" gemaakt | 16 juni 2025 |
| Set "zakelijke doelgroep" gemaakt | 13 april 2026 |

Zestien maanden op één campagne met één budget. Er is nooit gesplitst, dus de
zakelijke doelgroep heeft nooit een eigen budget gehad en kan niet los opschalen.

---

## 8. Wat er moet gebeuren — op volgorde van opbrengst

### A. Haal `zakelijke doelgroep` uit de gedeelde pot — grootste winst
Verplaats naar een **eigen campagne met eigen budget**. Nu krijgt de set
€ 17,13/dag van het algoritme terwijl hij € 1.092 winst per 14 dagen maakt; de
verliesgevende set krijgt € 41,36/dag. Zolang beide uit één CBO-pot eten, kun je
de winnaar niet opschalen zonder de verliezer mee te voeden.
Bereik 6.810 bij een frequentie van 2,58 over 14 dagen — nog niet verzadigd,
dus er is ruimte om te groeien.

### B. Zet Stories en Reels uit — € 23,57/dag die € 0,36 per euro teruggeeft
Handmatige plaatsingen, alleen Feeds aanhouden. Audience Network, Threads,
Marketplace, Search en right-hand column kunnen tegelijk weg (€ 4,46 voor nul aankopen).
*Afweging:* minder plaatsingen betekent minder speelruimte in de veiling en kan de
CPM in de feeds opdrijven. Dat moet je na een week nameten. Bij een ROAS van 0,36
op 40% van het budget weegt dat risico niet op tegen het verlies dat je nu neemt.
Verticale creatives apart testen kan later, met een eigen budget en een eigen opzet.

### C. Stop met optimaliseren op aantallen
Twee routes, de tweede is bij jouw volume de betere:
1. Optimalisatiedoel van `OFFSITE_CONVERSIONS` naar **waarde**. Werkt alleen met
   genoeg waardedragende conversies — met 45 aankopen per 14 dagen waarvan slechts
   een tiental substantieel, is dat krap.
2. **Een aangepaste conversie voor orders boven € 50** aanmaken en daarop optimaliseren.
   Daarmee verdwijnt de staalvervuiling uit het signaal zonder dat je waarde-optimalisatie
   nodig hebt. Dit is dezelfde ingreep die Google Ads ook nodig heeft.

### D. Zet `diaan creator 2` stop
2,5% kijkt uit, ROAS 0,16, −€ 39,44 per 14 dagen. Dit is geen budgetkwestie.

### E. Geef `Nieuwe wandpanelen` meer ruimte
Beste hook en beste vasthouden van het account, winstgevend, en kreeg 7,9% van het budget.

### F. Beslis over `video 3` en `Video led profiel japans`
692 en 343 vertoningen in veertien dagen. Dat zijn geen mislukkingen — die zijn
nooit getest. Of een eigen testbudget, of weghalen zodat ze de set niet vervuilen.

### G. Repareer het `InitiateCheckout`-event
Zie punt 5. Dit raakt zowel je rapportage als de kwaliteit van de optimalisatie.

---

## 9. Wat ik kan uitvoeren en wat jij moet doen

| Actie | Wie |
|---|---|
| D — `diaan creator 2` pauzeren | **Ik**, via de koppeling, na jouw akkoord |
| F — twee onvertoonde advertenties pauzeren | **Ik**, na jouw akkoord |
| A — nieuwe campagne + budget voor de zakelijke set | **Ik** kan campagne en budget aanmaken; de doelgroep en creatives moeten door jou worden overgezet |
| B — plaatsingen beperken | **Jij** — plaatsingen zijn niet via de koppeling te wijzigen |
| C — optimalisatiedoel / aangepaste conversie | **Jij** — conversie-instellingen zijn niet via de koppeling te wijzigen, en vallen onder je eigen regel dat ik daar niet aan kom |
| E — budget `Nieuwe wandpanelen` | Volgt vanzelf uit A en B, of apart na jouw akkoord |
| G — `InitiateCheckout` repareren | **Jij** of je themabeheerder; ik kan wel vaststellen waar het misgaat |

Ik voer niets uit tot je per punt zegt wat ik mag doen.
