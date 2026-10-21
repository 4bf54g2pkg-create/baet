# CMO-managementrapport — advertentierendement PureDeco

**Analyseperiode:** 7 t/m 20 oktober 2026 (14 volledige dagen, vandaag uitgesloten)
**Vergelijkingsperiode:** 23 september t/m 6 oktober 2026 (14 dagen)
**Rapportdatum:** 21 oktober 2026
**Valuta:** EUR. Bedragen zijn exclusief btw tenzij expliciet anders vermeld.

---

## 0. Databronnen, dekking en beperkingen

Verplicht vooraf, omdat het de betrouwbaarheid van elk cijfer hieronder bepaalt.

| Bron | Toegang | Granulariteit | Gebruikt voor |
|---|---|---|---|
| Shopify Admin API + ShopifyQL | Volledig (lezen) | Order- en orderregelniveau | Gerealiseerde omzet, marge, orders, AOV, kortingen, retouren, nieuwe klanten, staalcohort |
| Meta Ads (via Windsor.ai) | Volledig (lezen) | **Per advertentie**, incl. actietypes en actiewaarden | Meta-kosten, bereik, frequentie, CTR, CPC, CPM, conversies, conversiewaarde |
| Google Analytics 4 (via Windsor.ai) | Volledig (lezen) | Campagneniveau + kanaalniveau | Google-kosten en -klikken per campagne, last-click transacties en omzet per kanaal |
| Google Ads API | **Geen toegang** | — | — |
| Google Ads CSV-export (handmatig) | Eenmalig, 19 sep – 18 okt 2026 | Zoekterm + campagne + advertentiegroep | Zoektermverspilling, campagnetypetotalen |
| Google Tag Manager | **Geen toegang** | — | — |
| Merchant Center | **Geen toegang** | — | — |

### Wat dit rapport niet kan
1. **Google Ads per advertentie is niet beschikbaar.** De Windsor-connector `google_ads` is niet gekoppeld; de Supermetrics-proefperiode is op 9 oktober 2026 verlopen. Google wordt daarom op **campagneniveau** geanalyseerd met kosten en klikken uit GA4. Die GA4-kosten zijn gevalideerd: over 19 sep – 18 okt sommeren ze tot **€1.124,73 en 2.634 klikken**, precies gelijk aan de accounttotalen in de Google Ads-export. De kostenbasis is dus betrouwbaar; alleen het niveau is grover.
2. **Geen browserinspectie, geen tag-debugger, geen dataLayer-inspectie.** De trackingaudit in deel 4 is gebaseerd op de HTML-broncode van puredeco.nl, de ruwe actietypes uit de Meta API, de GA4-data en twee schermafbeeldingen van Google Ads Conversies. Waar iets alleen *aannemelijk* is, staat dat erbij.
3. **Geen Conversions API-, Event Match Quality- of domeinverificatiegegevens.** Die velden levert de connector niet.
4. **Er is geen incrementaliteitstest gedaan.** Alle "winst per advertentie" hieronder is attributiewinst, geen bewezen incrementele winst.

### Eén essentieel gegeven dat ik nodig heb (zie deel 10)
Is de **€6,95 kostprijs van een staal per zending of per staaltje?** 90 staalorders in 14 dagen bevatten samen **287 staaltjes** (gemiddeld 3,19 per order), terwijl de klant **één keer €6,95** betaalt. Per zending is het rekensommetje nul; per staaltje is het −€1.369,15 in 14 dagen. Dit is het enige cijfer dat de hoofdconclusie van dit rapport kan omdraaien.

---

## 1. Management dashboard

| KPI | 7–20 okt | 23 sep–6 okt | Verschil |
|---|---:|---:|---:|
| Shopify netto-omzet (ex btw, na korting en retour) | € 4.626,79 | € 5.577,19 | **−17,0%** |
| Shopify brutobedrag (total sales, incl. btw en verzending) | € 6.840,30 | € 7.760,18 | −11,9% |
| Google Ads spend | € 563,48 | € 562,30 | +0,2% |
| Meta Ads spend | € 842,66 | € 748,51 | +12,6% |
| **Totale advertentiekosten** | **€ 1.406,14** | **€ 1.310,81** | **+7,3%** |
| Platformgerapporteerde ROAS (Meta + Google samen) | 1,79 | 2,31 | −22,5% |
| Blended MER (netto-omzet / ad spend) | 3,29 | 4,25 | **−22,6%** |
| Contributiewinst na advertenties | **€ 1.650,57** | **€ 2.953,36** | **−44,1%** |
| ROI op advertentiebudget | **117%** | **225%** | −108 pp |
| Aantal bestellingen | 105 | 76 | **+38,2%** |
| Gemiddelde orderwaarde (netto) | € 44,07 | € 73,38 | **−39,9%** |
| Verkochte panelen (stuks) | **36** | **70** | **−48,6%** |
| Advertentiekosten per verkocht paneel | **€ 39,06** | **€ 18,73** | **+108,5%** |
| Break-even ROAS (op gerealiseerde paneelmarge) | 1,35 | 1,49 | — |
| Aandeel nieuwe klanten | 90% (94/105) | 82% (62/76) | +8 pp |

**De kern van deze tabel in één zin:** de advertentiekosten stegen 7,3%, het aantal orders steeg 38%, maar het aantal verkochte panelen halveerde en de contributiewinst viel 44% terug. Je koopt méér orders voor meer geld, maar het zijn bijna allemaal gratis staalaanvragen in plaats van panelen.

### Hoe de contributiewinst is berekend

| Component | 7–20 okt | 23 sep–6 okt | Bron |
|---|---:|---:|---|
| Paneelomzet ex btw, na regel- én orderkorting | € 4.136,71 | € 6.364,17 | Shopify orderregels |
| Inkoopkosten panelen (36 × €30 / 70 × €30) | − € 1.080,00 | − € 2.100,00 | Jouw opgave: €30 per paneel |
| **Brutomarge op panelen** | **€ 3.056,71 (73,9%)** | **€ 4.264,17 (67,0%)** | |
| Advertentiekosten | − € 1.406,14 | − € 1.310,81 | Meta + GA4 |
| **Contributiewinst na advertenties** | **€ 1.650,57** | **€ 2.953,36** | |

**Wat hier wél in zit:** paneelomzet ex btw, regelkortingen, orderkortingen, inkoopkosten panelen, advertentiekosten.
**Wat hier niet in zit (en dus een overschatting veroorzaakt):** betaalproviderkosten, werkelijke verzendkosten, verpakking, retourbehandeling, overhead. Ook de marge op accessoires (€588,47 ex btw deze periode, €382,88 vorige) is **niet** meegerekend, want daarvan ken ik de inkoopprijs niet — dat veroorzaakt een onderschatting. Netto per saldo is €1.650,57 een redelijke bovengrens voor de contributiewinst; de werkelijke waarde ligt daaronder.

> ⚠️ **Correctie op mijn eerdere rapport.** In `docs/02-ADVERTENTIE-ROI.md` noemde ik een marge van 78,6% en een break-even ROAS van 1,26. Dat was te hoog: ik rekende met de regelprijzen zonder de **orderkortingen** af te trekken. Eén order (#2408, 28 sep) had alleen al €1.106,01 orderkorting. Met de kortingen correct toegerekend is de marge **73,9%** (laatste 14 dagen) respectievelijk **67,0%** (vorige 14 dagen), en de break-even ROAS **1,35** respectievelijk **1,49**. Alle cijfers in dit rapport gebruiken de gecorrigeerde waarden.

### De waarde van een staalaanvraag — gecorrigeerd

Uit het eigen ordercohort (365 staalaanvragers die minimaal 30 dagen de kans hebben gehad om terug te kopen, gemeten vanaf 12 mei 2026):

| | Waarde |
|---|---:|
| Staalaanvragers met 30+ dagen historie | 365 |
| Daarvan later panelen gekocht | 28 |
| **Doorkooppercentage** | **7,7%** |
| Gemiddelde paneelomzet van een doorkoper (incl. btw) | € 752,62 |
| Mediaan | € 534,83 |
| Mediane tijd tot eerste paneelorder | 16 dagen |
| **Verwachte brutowinst per staalaanvraag** | **€ 33,26** |

Rekenwijze: 7,7% × (€752,62 / 1,21) × 73,9% marge = **€33,26**. Dit is het **plafond** van wat een staalaanvraag mag kosten. Eerder noemde ik €45,83; dat was gebaseerd op de te hoge marge. Gevoeligheidsanalyse: bij 5% doorkoop is het plafond €21,68, bij 10% €43,35. **Ik adviseer €25 als operationeel streefdoel**, zodat er marge zit tussen doelstelling en plafond.

---

## 2. Alle advertenties, gesorteerd op financiële impact

### 2a. Meta — per individuele advertentie (7–20 okt)

Alle zeven advertenties zitten in één campagne, **"Puredeco - onfluence"**, verdeeld over twee ad sets: *Video's* (6 advertenties) en *zakelijke doelgroep* (1 advertentie).

| # | Advertentie | Ad ID | Kosten | Impr. | Klikken | CTR | CPC | CPM | Freq. | Conv. | CR | CPA | Vorige CPA | Winst¹ | ROI¹ | Status |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | diaan creator 1 | 120244727461840057 | € 237,69 | 17.340 | 1.119 | 6,45% | € 0,21 | € 13,71 | 2,20 | 22 | 1,97% | **€ 10,80** | € 15,30 | **+€ 494,03** | **+208%** | 🟢 GROEN |
| 2 | Marmerlook va 125 | 120251672142850057 | € 229,22 | 17.319 | 1.197 | 6,91% | € 0,19 | € 13,24 | 1,83 | 16 | 1,34% | **€ 14,33** | € 15,31 | **+€ 302,94** | **+132%** | 🟢 GROEN |
| 3 | zakelijk verbouwen | 120243049922840057 | € 246,07 | 17.352 | 1.341 | 7,73% | € 0,18 | € 14,18 | 2,57 | 10 | 0,75% | € 24,61 | € 14,78 | +€ 86,53 | +35% | 🟡 GEEL |
| 4 | diaan creator 2 | 120244728990010057 | € 45,42 | 3.818 | 163 | 4,27% | € 0,28 | € 11,90 | 1,69 | 3 | 1,84% | € 15,14 | € 33,22 | +€ 54,36 | +120% | 🟡 GEEL |
| 5 | Nieuwe wandpanelen | 120241781668780057 | € 66,35 | 4.415 | 332 | 7,52% | € 0,20 | € 15,03 | 1,98 | 3 | 0,90% | € 22,12 | € 34,94 | +€ 33,43 | +50% | 🟡 GEEL |
| 6 | video 3 | 120229514950000057 | € 12,89 | 670 | 52 | 7,76% | € 0,25 | € 19,24 | 1,43 | 0 | 0,00% | — | — | −€ 12,89 | −100% | ⚪ GRIJS |
| 7 | Video led profiel japans | 120234060598460057 | € 5,02 | 245 | 16 | 6,53% | € 0,31 | € 20,49 | 1,50 | 0 | 0,00% | — | — | −€ 5,02 | −100% | ⚪ GRIJS |
| | **Totaal Meta** | | **€ 842,66** | **61.159** | **4.220** | **6,90%** | **€ 0,20** | **€ 13,78** | — | **54** | **1,28%** | **€ 15,60** | € 17,41 | **+€ 953,38** | **+113%** | |

¹ Winst en ROI zijn gerekend op de **gecorrigeerde waarde van €33,26 per staalaanvraag**, niet op de door Meta gerapporteerde omzet. Reden: deel 3 laat zien dat Meta's omzetcijfer niet verifieerbaar is. Dit is **verwachte toekomstige brutowinst**, geen al gerealiseerd geld.

**Meta's eigen ROAS-claim:** €1.674,38 conversiewaarde / €842,66 = **1,99**. Die mag je niet gebruiken — zie deel 3.

**Metrieken die verbeterden:** CTR steeg op alle zeven advertenties, CPC daalde op alle zeven, CPM daalde op vijf van de zeven. Meta wordt goedkoper en de creatives worden beter aangeklikt. Frequentie is nergens alarmerend (hoogste 2,57 over 14 dagen); er is **geen creative fatigue** aantoonbaar.

### 2b. Google — per campagne (7–20 okt)

Per advertentie niet beschikbaar (zie deel 0). Kosten en klikken komen uit GA4; omzet is GA4 last-click.

| # | Campagne | Type | Kosten | Impr. | Klikken | CTR | CPC | Sessies | Trans. | GA4-omzet | ROAS² | €/trans. | Vorige €/trans. | Status |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | PMAX - Campagne - PureDeco.nl | Perf. Max | € 209,10 | 14.833 | 439 | 2,96% | € 0,48 | 249 | 2 | € 139,95 | **0,55** | **€ 104,55** | € 107,22 | 🔴 ROOD |
| 2 | Search \| Wandpanelen | Search | € 152,68 | 2.603 | 167 | 6,42% | € 0,91 | 123 | 5 | € 279,90 | 1,52 | € 30,54 | € 106,16 | 🟡 GEEL |
| 3 | Search \| Concurrenten | Search | € 76,99 | 1.352 | 88 | 6,51% | € 0,87 | 66 | **0** | € 0,00 | **0,00** | — | — | 🔴 ROOD (al gestopt) |
| 4 | Shopping \| Bamboepanelen | Shopping | € 75,98 | 40.619 | 1.024 | 2,52% | **€ 0,07** | 707 | 5 | € 0,00 | — | € 15,20 | € 11,32 | 🟡 GEEL |
| 5 | Brand \| PureDeco Protection | Search | € 25,57 | 235 | 90 | 38,30% | € 0,28 | 85 | 5 | € 0,00 | — | **€ 5,11** | € 10,93 | 🟢 GROEN |
| 6 | Brand \| PureDeco Protection NL-BE | Search | € 23,17 | 228 | 96 | 42,11% | € 0,24 | 88 | 4 | € 422,80 | **15,08** | **€ 5,79** | € 11,20 | 🟢 GROEN |
| | **Totaal Google** | | **€ 563,48** | **59.870** | **1.904** | **3,18%** | **€ 0,30** | **1.318** | **21** | **€ 842,65** | **1,24** | **€ 26,83** | € 62,48 | |

² ROAS = GA4-omzet ex btw / kosten. Break-even is **1,35**.

**Google totaal zit met een ROAS van 1,24 onder break-even (1,35)** op gerealiseerde omzet alleen.

Reken je de staalaanvragen mee, dan ziet het er anders uit. Van de 21 transacties leverden **10 exact €0,00 omzet** op (de 5 van Shopping en de 5 van Brand | Protection) — dat zijn per definitie staalorders. De overige 11 transacties delen samen €842,65, oftewel €76,60 gemiddeld, terwijl een paneelorder gemiddeld boven de €250 ligt: daar zitten dus naar schatting 3 paneelorders en 8 staalaanvragen in. Omdat ik dat niet exact kan splitsen (daarvoor is transactie-ID-niveau nodig dat GA4 hier niet levert) geef ik een bandbreedte:

- **Ondergrens** (10 staalaanvragen): €696,40 ex btw omzet × 73,9% = €514,64 brutomarge + 10 × €33,26 = €332,60 toekomstwaarde = €847,24 → **ROI +50%**
- **Bovengrens** (18 staalaanvragen): €514,64 + 18 × €33,26 = €598,68 → €1.113,32 → **ROI +98%**

Google is dus winstgevend, maar **de helft tot twee derde van dat resultaat is verwachte toekomstwaarde, geen geld op de bank.**

### 2c. Top 10 om te behouden of op te schalen

Er zijn er maar vijf die het verdienen; ik verzin de rest niet.

| Rang | Platform | Advertentie / campagne | Reden | Actie |
|---|---|---|---|---|
| 1 | Meta | diaan creator 1 | CPA €10,80 bij 22 conversies = 32% van het plafond. CPA verbeterde van €15,30 naar €10,80 bij 14% minder budget. | Budget +75% |
| 2 | Google | Brand \| PureDeco Protection NL-BE | €5,79 per transactie, ROAS 15,08, 42% CTR. Goedkoopste conversie in het hele account. | Budget verdubbelen |
| 3 | Google | Brand \| PureDeco Protection | €5,11 per transactie, 38% CTR. Beschermt je eigen merknaam. | Budget verdubbelen |
| 4 | Meta | Marmerlook va 125 | CPA €14,33 bij 16 conversies, laagste frequentie (1,83) van de grote drie = meeste ruimte om op te schalen. | Budget +40% |
| 5 | Meta | diaan creator 2 | CPA verbeterde van €33,22 naar €15,14. Nog maar 3 conversies, dus voorzichtig. | Budget +75% (vanaf laag niveau) |

### 2d. Top 10 grootste potentiële budgetverspillers

| Rang | Platform | Waar | Kosten 14d | Geschat verlies | Bewijs |
|---|---|---|---:|---:|---|
| 1 | Google | PMAX - Campagne | € 209,10 | **−€ 142,58** | 2 transacties, €104,55 per stuk tegen een plafond van €33,26. ROAS 0,55. Twee periodes op rij hetzelfde (€107,22 vorige periode). |
| 2 | Google | Search \| Concurrenten | € 76,99 | **−€ 76,99** | 0 conversies in 14 dagen, 0 in de 14 daarvoor, 0 over de hele 30-daagse export. Jij hebt deze al gestopt — goed besluit. |
| 3 | Meta | zakelijk verbouwen | € 246,07 | risico, geen verlies | CPA verslechterde van €14,78 naar €24,61 (+66%) terwijl het budget met 67% omhoog ging. Hoogste frequentie (2,57) en laagste conversieratio (0,75%) van de drie grote. Nog wel onder het plafond. |
| 4 | Google | Zoektermen: concurrentmerken | € 64,96³ | −€ 64,96 | `thuispaneel` €20,52 · `paneli` €10,99 · `benacci` €8,72 · `akupanel` €7,56 · `wooduo`, `enmod`, `pure panels`, `style for walls`, `full decor`, `woodupp`. Samen 0 conversies. |
| 5 | Google | Zoektermen: Engels/buitenlands | € 25,75³ | −€ 25,75 | 60 zoektermen zonder Nederlands woord, 0 conversies. O.a. `wall decor panels`, `panel ryflowany na wymiar`, `steel wall cladding`, `marble and wood review`. |
| 6 | Google | PMAX brede zoektermen | onbekend | niet te berekenen | PMax kocht 3.549 verschillende zoektermen voor 337 zichtbare klikken. Slechts 49% van de Google-kosten is zichtbaar in het zoektermenrapport; de rest is niet te auditen. |
| 7 | Meta | video 3 | € 12,89 | −€ 12,89 | 0 conversies, 52 klikken. Te weinig budget voor een uitspraak, maar levert niets. |
| 8 | Meta | Video led profiel japans | € 5,02 | −€ 5,02 | 0 conversies, 16 klikken. |
| 9 | Google | Shopping \| Bamboepanelen | € 75,98 | geen verlies, wel lek | 1.024 klikken → 707 sessies → 5 conversies = 0,49% conversieratio. CPC is briljant (€0,07) maar de klikkwaliteit is laag. Kosten stegen 236% (€22,64 → €75,98) terwijl de kosten per transactie opliepen van €11,32 naar €15,20. |
| 10 | Shopify | Afgebroken paneelwinkelwagens | — | **gemiste omzet** | Over de hele winkel ging **€ 143.571,55** aan panelen de winkelwagen in (995 artikelen in 231 acties) en kwam **€ 2.958,15** eruit als aankoop: **2,1%**. 117 van de 231 toevoegingen werden weer verwijderd. Van de Meta-kant specifiek: 131 add-to-cart-events met € 19.384,66 waarde, en daaruit 0 paneelorders in last-click. Dit is geen verspilling maar het grootste gat in de funnel. |

³ Gemeten over 19 sep – 18 okt 2026 (de enige beschikbare Google-native zoektermexport), op het zichtbare deel van €553,53 van de €1.124,73 accountkosten.

---

## 3. Platformrapportage versus Shopify-waarheid

Dit is het belangrijkste deel van het rapport. Alle drie de bronnen zijn onafhankelijk en zeggen hetzelfde.

| Bron | Meta-toegeschreven orders (14d) | Meta-toegeschreven **paneelomzet** |
|---|---:|---:|
| Meta Ads (7-daagse klik + 1-daagse weergave) | 54 aankopen | claimt € 1.674,38 conversiewaarde |
| GA4 (last-click, kanaal Paid Social) | 26 transacties | **€ 0,00** |
| Shopify (order referrer `facebook` + `instagram`) | 25 orders | **€ 0,00** productomzet (€166,80 total sales = alleen verzendkosten) |

**GA4 rapporteert over 28 dagen aan Paid Social: 3.901 sessies, 43 transacties, € 0,00 omzet.** Niet één van de 43 transacties die GA4 aan Meta toeschrijft bevatte een paneel. Shopify bevestigt dat onafhankelijk.

### Waar komt Meta's €1.674,38 dan vandaan?

Uit de ruwe actiewaarden per advertentie:

| Advertentie | Aankopen | Meta-waarde | Waarde ÷ aankopen | Interpretatie |
|---|---:|---:|---:|---|
| zakelijk verbouwen | 10 | € 69,50 | € 6,95 | **exact 10 × €6,95** → alle tien zijn staalaanvragen |
| diaan creator 2 | 3 | € 20,85 | € 6,95 | **exact 3 × €6,95** → alle drie staalaanvragen |
| Nieuwe wandpanelen | 3 | € 20,85 | € 6,95 | **exact 3 × €6,95** → alle drie staalaanvragen |
| diaan creator 1 | 22 | € 373,08 | € 16,96 | 22 × €6,95 = €152,90; de resterende €220,18 is vermoedelijk één paneelorder |
| Marmerlook va 125 | 16 | € 1.190,10 | € 74,38 | 16 × €6,95 = €111,20; de resterende €1.078,90 is vermoedelijk 2–3 paneelorders |

**Conclusie:** van Meta's €1.674,38 is **€375,30 (22%) simpelweg de €6,95 verzendkosten die de klant voor zijn staal betaalt** — geld dat per definitie geen winst is, want dat is precies de kostprijs. De resterende €1.299,08 zijn paneelorders die Meta claimt via weergave- of 7-daagse-klikattributie, maar die GA4 en Shopify aan Direct of Organisch toeschrijven.

Dat Meta die orders claimt is niet per definitie onjuist: **45 van de 105 Shopify-orders (43%) hebben helemaal geen referrer**, en daarin zit €4.700,65 aan total sales. Er is dus ruimte voor onzichtbare Meta-invloed. Maar het is **niet verifieerbaar**, en het betekent dat **Meta's ROAS van 1,99 geen enkele betekenis heeft als winstmaat**.

### Mogelijke dubbeltelling Google ↔ Meta
Meta claimt 54 aankopen, Google-campagnes 21 GA4-transacties, samen 75. Shopify registreerde 105 orders in dezelfde periode. Er is dus **ruimte** voor 75 toegeschreven orders zonder logische overlap, maar ik kan geen dubbeltelling uitsluiten: order-ID's komen niet terug in de platformrapportages waartoe ik toegang heb, en Meta's attributievenster (7 dagen klik) overlapt met Google's. **Tel de platformcijfers niet bij elkaar op.** Gebruik voor elke budgetbeslissing het Shopify-totaal als noemer, nooit de som van de platformen.

### En stijgende advertentiekosten versus stijgende Shopify-omzet?
**Nee, en dat is het alarmsignaal.** De kosten stegen met €95,33 (+7,3%) en de netto-omzet daalde met €950,40 (−17,0%). Er is deze periode **geen** positieve relatie tussen meer adverteren en meer omzet. Dat Shopify meer orders laat zien (105 vs 76) bewijst niets over incrementaliteit: het aantal verkochte panelen is bijna gehalveerd.

---

## 4. Trackingaudit

| Onderdeel | Status | Probleem | Impact | Oplossing |
|---|---|---|---|---|
| Google Ads conversietag `AW-16753512576` | ✅ Correct | Aanwezig in de HTML-broncode van puredeco.nl, samen met 11 gtag-events waaronder `purchase`. | — | Niets doen |
| GA4-tag `G-N9ZMX91VEZ` | ✅ Correct | Aanwezig. GA4-kosten per campagne sommeren exact naar Google's accounttotalen (€1.124,73 / 2.634 klikken over 19 sep–18 okt). | — | Niets doen |
| Google Tag `GT-WPTCFVT8` + Merchant Center `MC-Q1J3V03Z7L` | ✅ Correct | Beide aanwezig in de broncode. | — | Niets doen |
| Meta Pixel `1072431017618538` | ✅ Correct | Aanwezig. Stuurt `ViewContent`, `AddToCart`, `InitiateCheckout`, `AddPaymentInfo` en `Purchase` mét productwaarden (ViewContent gemiddeld €140,92 = de paneelprijs). Waardes zijn plausibel. | — | Niets doen |
| Google Ads primaire conversieactie | ✅ Correct | "Aankoop" is de enige primaire aankoopactie (11,00 conversies, €843,65). `adscale_purchase` staat op **Secundair** met identieke cijfers. Geen dubbeltelling in het biedsignaal. | Nu geen | **Laten staan.** Zet `adscale_purchase` nooit op Primair — dan verdubbelt het biedsignaal onmiddellijk. |
| Google Ads "Toevoegen aan winkelwagen" | 🔴 **Probleem** | Twee problemen tegelijk. Ten eerste staan er **twee** primaire conversieacties voor hetzelfde event, status "Vereist aandacht". Ten tweede, en zwaarder: de **conversiewaarde** van deze actie is enorm. GA4 meet over dezelfde 14 dagen 231 add-to-cart-acties met 995 artikelen en een waarde van **€ 143.571,55** — € 144,29 per artikel, precies de gemiddelde paneelprijs, dus de tag rekent correct. Maar daar staan 77 purchase-events met **€ 2.958,15** tegenover: **2,1%** van de mandjeswaarde wordt daadwerkelijk betaald, en 117 van de 231 toevoegingen worden weer verwijderd. | Dubbel geteld in het biedsignaal, én een conversiewaarde die 48× hoger is dan de werkelijke omzet. Elke waarde-gebaseerde biedstrategie stuurt daarmee op mandjes in plaats van op verkopen. Dit is een plausibele verklaring voor het gedrag van PMax (€ 104,55 per conversie, ROAS 0,55, twee periodes op rij). | **"Toevoegen aan winkelwagen" volledig op Secundair zetten**, niet alleen één van de twee. Het is een diagnostisch signaal, geen biedoel. Vereist jouw toestemming. |
| "Er ontbreekt een Google-tag op uw website" (waarschuwing bij Search \| Concurrenten) | 🟡 Verdacht → **vals alarm** | Er staan 0 `googletagmanager.com` container-scripts in de pagina-broncode. Shopify laadt pixels via de gesandboxte Customer Events-omgeving, waar Google's crawler niet bij kan. | Geen. De conversies komen aantoonbaar binnen (11,00 aankopen gemeten). | Negeren. Dit is het normale gedrag van Shopify-webpixels. |
| Shopify metafields `foxtheme.code_head` / `code_body` | ✅ Correct (leeg) | Beide bevestigd leeg via de Admin API. Er wordt dus niets dubbel via het thema geïnjecteerd. | — | Niets doen |
| **Conversiewaarde van een staalorder = € 6,95** | 🔴 **Probleem** | Het staalproduct staat op €0,00; de €6,95 is een verzendkostenregel. Zowel Meta's `purchase` als GA4's `purchase_revenue` als Shopify's `net_sales` lezen een staalorder daarom als €0 product / €6,95 waarde, terwijl de werkelijke verwachte waarde **€33,26** is — een onderwaardering van 4,8×. | **Dit is de grootste trackingfout in het account.** Elke waarde-gebaseerde biedstrategie stuurt wég van je meest winstgevende conversie. | Een aparte conversieactie voor staalaanvragen met een vaste waarde van €25–33 (zie actieplan). Vereist jouw toestemming. |
| Funnel-events: aankopen > checkouts | 🔴 **Probleem, in twee systemen bevestigd** | Meta: 131 `AddToCart` → **24** `InitiateCheckout` → **54** `Purchase`. GA4, onafhankelijk: 231 `add_to_cart` → **39** `begin_checkout` → **77** `purchase`. In beide systemen zijn er ongeveer twee keer zoveel aankopen als gestarte checkouts, wat technisch onmogelijk is. Per Meta-advertentie: diaan creator 1 heeft 3 checkouts en 22 aankopen; diaan creator 2 heeft 0 checkouts en 3 aankopen. | Het staalaanvraagproces vuurt geen checkout-event. Noch Meta noch Google kan daardoor op midden-funnel-signalen optimaliseren voor je belangrijkste conversiepad. Dat twee onafhankelijke systemen dezelfde verhouding laten zien, maakt een meetfout in één van de twee onwaarschijnlijk: het zit in het afrekenpad zelf. | Onderzoeken of de staalaanvraag via een ander (snel)afrekenpad loopt. Vereist tag-inspectie in de browser, wat ik vanuit deze omgeving niet kan. |
| Winkelwagen-doorstroom | 🟡 Verdacht | Van de 231 toevoegingen aan de winkelwagen worden er **117 weer verwijderd** (51%), en van de € 143.571,55 mandjeswaarde wordt € 2.958,15 betaald. GA4 registreert 77 aankopen waar Shopify 105 orders heeft (73%). | De helft van de mensen die een paneel in het mandje legt, haalt het er weer uit. Dat kan prijsgevoeligheid zijn, of verwarring over het aantal benodigde panelen en de profielen — maar het is niet te onderscheiden zonder sessie-opnames. | Geen trackingwijziging. Dit is de onderbouwing voor de retargeting-ad set op afgebroken winkelwagens (deel 9, dag 6). |
| Meta-conversiewaarde versus Shopify | 🔴 **Probleem** | Meta claimt €1.674,38; GA4 Paid Social en Shopify `facebook`/`instagram` rapporteren beide €0,00 productomzet over dezelfde 14 dagen. | Meta's ROAS is onbruikbaar als winstmaat. | Niet oplosbaar zonder een incrementaliteitstest (geo-holdout of conversion-lift). |
| Klik → sessie-verlies | 🟡 Verdacht | Meta: 4.220 klikken → 2.342 GA4-sessies (**−44,5%**). Google: 1.904 klikken → 1.318 sessies (**−30,8%**). | Voor Meta is 40–50% verlies normaal (in-app browser, bounce voordat de tag vuurt). 31% voor Google is aan de hoge kant en kan op laadsnelheid of consent duiden. | Consent Mode v2-configuratie en landingspagina-snelheid controleren. Vereist browserinspectie. |
| Shopify order-attributie | 🔴 Probleem | 45 van de 105 orders (43%) hebben géén `order_referrer`, met daarin €4.700,65 total sales. | Bijna de helft van je omzet is niet toe te wijzen aan een kanaal, in geen enkel systeem. | UTM-parameters consequent op alle advertentielinks; dat verkleint de blinde vlek. Vereist jouw toestemming. |
| Consent Mode v2 | ⚫ **Niet verifieerbaar** | Geen toegang tot GTM of de browserconsole. | Onbekend. Als Consent Mode niet goed staat, worden conversies structureel onder gerapporteerd. | Handmatige controle in Google Tag Assistant nodig. |
| Meta Conversions API / Event Match Quality / deduplicatie via `event_id` / domeinverificatie | ⚫ **Niet verifieerbaar** | De connector levert deze velden niet. | Als CAPI ontbreekt of niet dedupliceert, kan Meta conversies dubbel tellen. Gezien aankopen > checkouts is dat niet uit te sluiten. | Controleren in Meta Events Manager → Diagnostiek. |
| Enhanced Conversions (Google) | ⚫ **Niet verifieerbaar** | Niet te zien zonder Google Ads API-toegang. | Onbekend. | Controleren onder Doelen → Conversies → Instellingen. |
| Merchant Center feedkwaliteit | ⚫ **Niet verifieerbaar** | Geen toegang. | Onbekend. Relevant omdat Shopping 1.024 klikken leverde met 0,49% conversie. | Feedfouten controleren in Merchant Center. |

**Is de tracking goed genoeg om budgetbeslissingen op te baseren?** Voor **aantallen** ja: de conversieaantallen van Meta (54), GA4 (26) en Shopify (25) zijn onderling consistent zodra je rekening houdt met de attributievensters, en Google's 31,0 conversies tegen GA4's 26 transacties is een verschil van 19% — binnen de normale bandbreedte tussen attributiemodellen. Voor **waardes** nee: de staalorder-waardering van €6,95 en de onverifieerbare Meta-omzet maken elke ROAS-gebaseerde beslissing onbetrouwbaar. **Stuur daarom op CPA tegen het plafond van €33,26, niet op ROAS.**

---

## 5. Google Ads — diepteanalyse

### 1. Welke campagnes leveren daadwerkelijk winst op?
Twee, met zekerheid: **Brand | PureDeco Protection NL-BE** (€5,79 per transactie, ROAS 15,08) en **Brand | PureDeco Protection** (€5,11 per transactie). Samen kosten ze €48,74 in 14 dagen — **3,5% van je totale advertentiebudget** — en ze zijn je goedkoopste conversiebron. **Shopping | Bamboepanelen** is grensgevallig winstgevend: €15,20 per conversie tegen een plafond van €33,26, maar alle 5 conversies waren staalaanvragen.

**Search | Wandpanelen** verbeterde dramatisch: van €106,16 naar €30,54 per transactie, en van ROAS 0 naar 1,52 (break-even 1,35). Dit was vorige periode mijn zorgenkind en is nu net winstgevend. Houden en optimaliseren, niet opschalen tot er meer data is.

### 2. Waar wordt budget verspild?
**PMax, €209,10 in 14 dagen voor 2 transacties.** €104,55 per conversie is 3,1× het plafond. Dit is geen eenmalige uitschieter: vorige periode was het €107,22. Twee periodes, 28 dagen, €423,55 besteed, 4 transacties. Daarnaast €64,96 aan concurrentmerken en €25,75 aan Engelse/buitenlandse zoektermen (gemeten over 19 sep–18 okt), allebei met 0 conversies.

### 3. Welke producten verdienen meer budget?
Op basis van de bestverkopende panelen in de laatste 14 dagen (Shopify, netto-omzet):

| Product | Orders | Netto-omzet |
|---|---:|---:|
| Wandpaneel Japandi 824 Taupe | 28 | € 693,97 |
| Wandpaneel Doorlopend Marmer 689 Beverly Gold Slate | 5 | € 495,04 |
| Wandpaneel Hout 812 Walnut Deep | 23 | € 413,10 |
| Eenzijdige akupanelen | 4 | € 396,30 |
| Wandpaneel Marmer 670 Pandora Slate | 19 | € 392,41 |

**Wandpaneel Doorlopend Marmer 689** is de interessantste: 5 orders, €495,04 netto, bij een stukprijs van €599 incl. btw. Dat is je hoogste contributiemarge per order in het hele assortiment. En het sluit aan op je best presterende Meta-creative, *Marmerlook va 125*. Marmer verdient meer budget in Shopping en in Meta.

### 4. Welke producten moeten minder gepromoot worden?
Dat kan ik **niet betrouwbaar bepalen**: Shopping-prestaties per product vereisen Google Ads- of Merchant Center-toegang, die ik niet heb. Wat ik wel zie: Shopping heet "Bamboepanelen" maar bamboe staat in geen enkele top-25 verkooplijst van de afgelopen 14 dagen. Dat is een hypothese om te controleren, geen conclusie.

### 5. Welke zoektermen of campagnes zijn inefficiënt?
Concrete uitsluitingslijst, allemaal met 0 conversies over 19 sep–18 okt:

**Concurrentmerken (€64,96):** `thuispaneel`, `paneli`, `benacci`, `akupanel`, `wooduo`, `enmod`, `pure panels`, `style for walls`, `full decor`, `woodupp`
**Engels/buitenlands (€25,75, 60 termen):** `wall decor panels`, `panel ryflowany na wymiar`, `steel wall cladding`, `marble wall panels`, `travertine wall panels`, `marble and wood review`, `deco wall tiles`, `fluted wall panel`, `white panels`, `dekor panel` en 50 vergelijkbare

Binnen **Search | Concurrenten** (al gestopt) ging €85,60 van de €138,83 zoekwoordbudget naar het brede zoekwoord `paneli` en €42,43 naar AI Max voor 30 klikken, met kwaliteitsscore 3.

### 6. Zijn de biedstrategieën passend bij de marges?
**Nee, en dat is structureel.** Elke waarde-gebaseerde biedstrategie in dit account optimaliseert naar een conversiewaarde die voor een staalorder €6,95 is terwijl die order €33,26 waard is. De biedmachine ziet je winstgevendste conversie als je waardeloosste. Zolang de staalaanvraag niet correct gewaardeerd is, is **"Conversies maximaliseren" met een CPA-doel van €25 de juiste strategie** — niet "Conversiewaarde maximaliseren" of tROAS.

### 7. Waar ligt de grootste kans op winstgevende groei?
Bij **de brandcampagnes**: samen €48,74 voor 9 conversies à €5,42 gemiddeld. Dat is 6× goedkoper dan het accountgemiddelde (€26,83). Ze zijn gelimiteerd door hun eigen minibudget, niet door de markt. Hier is vrijwel risicoloos volume te halen.

---

## 6. Meta Ads — diepteanalyse

### Structuur
Eén campagne ("Puredeco - onfluence"), twee ad sets. De ad set *Video's* (6 advertenties, €596,59) en *zakelijke doelgroep* (1 advertentie, €246,07). Dat is een **slanke, gezonde structuur** — geen versnippering, genoeg budget per advertentie om te leren. Er is geen aantoonbare retargeting-ad set; alles lijkt prospecting. Dat is een gat (zie deel 8).

### Wat werkt en waarom
**diaan creator 1 is je beste advertentie in het hele account.** CPA €10,80, en belangrijker: 1,97% conversieratio op de klik, bijna 3× zo hoog als *zakelijk verbouwen* (0,75%). Hij haalde ook 3.535 post-engagements, 17 opslaan-acties en 20 likes bij €237,69 budget: de creative wordt niet alleen aangeklikt, hij wordt bewaard. Die combinatie (hoge CR + hoge saves) is het sterkste signaal dat de boodschap en de doelgroep kloppen.

**Marmerlook va 125 heeft de meeste kopruimte.** Frequentie 1,83 — de laagste van de drie grote — met 9.483 bereik en 43 saves. Hij is nog niet uitgeput en hij haalde 58 add-to-carts met een gezamenlijke waarde van €7.906,90: de hoogste koopintentie van alle creatives.

**zakelijk verbouwen is het probleemkind.** CTR is de hoogste van allemaal (7,73%) maar de conversieratio de laagste (0,75%), en de CPA verslechterde van €14,78 naar €24,61 terwijl het budget 67% omhoog ging. Frequentie 2,57 is de hoogste. De zakelijke doelgroep klikt graag maar bestelt zelden. Tegelijk: 34 add-to-carts met €4.669,90 waarde en 14 gestarte checkouts met €3.106,86 waarde, waarvan slechts 10 orders à €6,95 overbleven. **De zakelijke doelgroep legt panelen in de winkelwagen en koopt dan alleen stalen.** Dat is geen advertentieprobleem maar een conversieprobleem op de site: er is geen zakelijk aankooppad (geen projectprijs, geen offerteaanvraag, geen factuur-op-rekening).

### Creative fatigue
**Niet aantoonbaar.** Frequentie blijft overal onder 2,6 over 14 dagen, CTR steeg op alle zeven advertenties en CPM daalde op vijf. Er is geen reden om een goed lopende creative nu te vervangen.

### Attributie-instelling
Meta rapporteert op 7-daagse klik + 1-daagse weergave (af te leiden uit het feit dat Meta 54 aankopen claimt tegen GA4's 26 last-click). Dat is de standaard en niet verkeerd, maar het verklaart waarom Meta 2,1× meer conversies claimt dan GA4 ziet.

### Creatief advies, gekoppeld aan de data

| Advies | Onderbouwing |
|---|---|
| **Behouden:** diaan creator 1, Marmerlook va 125 | Beide ruim onder het CPA-plafond, verbeterende CTR en CPC, frequentie onder 2,2. |
| **Behouden maar herstellen:** zakelijk verbouwen | Niet pauzeren (CPA €24,61 zit onder het plafond van €33,26), maar het budget niet verder verhogen tot de CPA weer onder €18 staat. |
| **Vervangen:** video 3, Video led profiel japans | 0 conversies op 68 klikken samen. Te weinig data voor een harde afkeuring, maar ook geen reden om er budget in te houden. |
| **Testen — hook 1:** "Zie en voel het paneel in je eigen huis" op de *Marmerlook*-beelden | De marmer-creative heeft de hoogste add-to-cart-waarde (€7.906,90) en het hoogste stuksbedrag in de winkel (€599 Beverly Gold Slate). |
| **Testen — hook 2:** "Van staal naar wand in 16 dagen" | De eigen cohortdata zegt: de mediane doorkoper koopt 16 dagen na zijn staal. Die termijn benoemen maakt van een gratis staal een aankoopstap. |
| **Testen — hook 3:** een zakelijke variant met een projectpad | *zakelijk verbouwen* haalt 7,73% CTR maar 0,75% conversie. De interesse is er; het aankooppad ontbreekt. |
| **Nieuwe ad set:** retargeting op add-to-cart zonder aankoop | 131 add-to-carts met €19.384,66 waarde in 14 dagen leverden 0 paneelorders in last-click op. Dit is het grootste meetbare gat in de hele funnel. |

---

## 7. Shopify als financiële waarheidsbasis

| | 7–20 okt | 23 sep–6 okt | Verschil |
|---|---:|---:|---:|
| Brutobedrag (gross sales) | € 5.468,75 | € 8.343,16 | −34,4% |
| Kortingen | − € 329,76 | − € 1.596,13 | −79,3% |
| Retouren / terugbetalingen | − € 512,20 | − € 1.169,84 | −56,2% |
| **Netto-omzet** | **€ 4.626,79** | **€ 5.577,19** | **−17,0%** |
| Verzendkosten (ontvangen) | € 994,34 | € 835,91 | +19,0% |
| Btw | € 1.219,17 | € 1.347,08 | −9,5% |
| Total sales | € 6.840,30 | € 7.760,18 | −11,9% |
| Orders | 105 | 76 | +38,2% |
| Netto AOV | € 44,07 | € 73,38 | −39,9% |
| Nieuwe klanten | 94 (90%) | 62 (82%) | +8 pp |
| Terugkerende klanten | 11 (10%) | 14 (18%) | −8 pp |
| Paneelorders | 13 | 11 | +18,2% |
| Staalorders | 90 | 65 | +38,5% |
| Panelen verkocht | 36 | 70 | **−48,6%** |
| Staaltjes verzonden | 287 | 181 | +58,6% |
| Staaltjes per order | 3,19 | 2,78 | +14,7% |

**Er is geen enkele order die zowel panelen als stalen bevat.** 13 paneelorders en 90 staalorders, nul overlap, in beide periodes. De winkel heeft dus feitelijk twee gescheiden bedrijven: een staalaanvraagmachine en een paneelverkoop, verbonden door een gemiddelde wachttijd van 16 dagen.

### Omzet per kanaal (Shopify order referrer, 7–20 okt)

| Referrer | Orders | Brutobedrag | Netto-omzet | Total sales |
|---|---:|---:|---:|---:|
| *(geen referrer)* | 45 | € 4.039,59 | € 3.356,37 | € 4.700,65 |
| google / search | 23 | € 1.197,84 | € 1.039,10 | € 1.551,50 |
| puredeco (direct) | 11 | € 231,32 | € 231,32 | € 414,40 |
| facebook / social | 11 | € 0,00 | € 0,00 | € 76,45 |
| instagram / social | 10 | € 0,00 | € 0,00 | € 62,55 |
| instagram | 4 | € 0,00 | € 0,00 | € 27,80 |
| bing / search | 1 | € 0,00 | € 0,00 | € 6,95 |

**Alle 25 Meta-orders hebben €0,00 productomzet.** De €166,80 total sales is uitsluitend verzendkosten op gratis stalen. Google levert daarentegen €1.039,10 netto-omzet uit 23 orders.

### Is Shopify-omzet bewijs van advertentie-incrementaliteit?
**Nee.** 90% van de klanten in deze periode is nieuw, wat erop wijst dat de advertenties nieuw publiek aantrekken — maar het bewijst niet dat die mensen zonder advertenties níet gekomen waren. De grootste omzetbron is de bucket zónder referrer (€4.700,65), en die kan net zo goed uit organisch, mond-tot-mond of een eerder staal komen. **De enige manier om incrementaliteit vast te stellen is een holdout-test.** Die staat in het actieplan als optie, niet als aanbeveling: bij dit volume (13 paneelorders per 14 dagen) duurt een statistisch betrouwbare test maanden.

### Waarom halveerde de paneelverkoop?
Ik kan dit niet verklaren uit de beschikbare data en wil er niet naar gissen. Wat ik kan uitsluiten: het is niet de advertentiekwaliteit (CTR en CPC verbeterden overal), niet retouren (slechts één gedeeltelijk gerestitueerde order deze periode), niet kortingen (die daalden van €1.596 naar €330). Wat het **kan** zijn, in volgorde van waarschijnlijkheid:
1. **Toeval bij lage volumes.** 13 versus 11 paneelorders — maar 36 versus 70 panelen. Het verschil zit in de ordergrootte: vorige periode had drie grote orders (14, 11 en 4+6 panelen). Eén projectorder minder verklaart het grootste deel van het verschil.
2. Een seizoens- of prijsverandering die ik niet kan zien.
3. Een verslechterde paneel-landingspagina of voorraadprobleem.

Punt 1 is de meest waarschijnlijke verklaring en belangrijk voor de interpretatie: **lees de −48,6% niet als een trend maar als volatiliteit bij kleine aantallen.** Over de volle 28 dagen samen: 106 panelen, €10.500,88 ex btw, 69,7% marge.

---

## 8. Top 5 optimalisatiekansen, op verwachte winst

| # | Kans | Verwachte winst per 14 dagen | Mediakosten | Betrouwbaarheid |
|---|---|---:|---:|---|
| 1 | **Opvolging van staalaanvragers.** 90 staalaanvragen in 14 dagen, 7,7% koopt door, mediaan na 16 dagen. Tilt een e-mail/SMS-flow dat naar 12%, dan zijn dat ~4 extra paneelorders. | **+€ 1.838** | € 0 | Middel — 7,7% is gemeten, 12% is een aanname |
| 2 | **Retargeting op afgebroken paneelwinkelwagens.** 131 add-to-carts met €19.384,66 waarde, 0 paneelorders in last-click. Zelfs 2% herstel is één paneelorder. | **+€ 150 tot € 450** | € 100–150 | Middel |
| 3 | **PMax stoppen of herbouwen.** €209,10 voor 2 conversies à €104,55. Stoppen bespaart direct. | **+€ 142** | − € 209 | **Hoog** — twee periodes bevestigd |
| 4 | **Brandcampagnes verdubbelen.** €5,42 gemiddeld per conversie bij €48,74 totaalbudget. | **+€ 110 tot € 250** | + € 49 | Hoog |
| 5 | **Staalaanvraag correct gaan waarderen in de conversietracking** (€25–33 i.p.v. €6,95). | niet direct, maar het repareert elke biedstrategie | € 0 | Hoog |
| 6 | **Zakelijk aankooppad bouwen.** 14 gestarte checkouts met €3.106,86 waarde uit de zakelijke doelgroep, 10 orders à €6,95 als resultaat. | onbekend | € 0 | Laag — hypothese |

**Kans 1 is groter dan alle budgetwijzigingen in dit rapport samen.** Je koopt al 90 staalaanvragen per 14 dagen tegen een goede prijs; je laat 92% ervan onbenut weglopen.

---

## 9. Actieplan voor de komende 7 dagen

Huidige dagbudgetten, afgeleid uit de 14-daagse werkelijke uitgaven ÷ 14:

| Platform | Advertentie / campagne | Huidig dagbudget | Voorgesteld (Scenario B) | Wijziging |
|---|---|---:|---:|---:|
| Meta | diaan creator 1 | € 16,98 | € 30,00 | +€ 13,02 (+77%) |
| Meta | Marmerlook va 125 | € 16,37 | € 24,00 | +€ 7,63 (+47%) |
| Meta | zakelijk verbouwen | € 17,58 | € 16,00 | −€ 1,58 (−9%) |
| Meta | diaan creator 2 | € 3,24 | € 8,00 | +€ 4,76 (+147%) |
| Meta | Nieuwe wandpanelen | € 4,74 | € 0,00 | −€ 4,74 (pauzeren) |
| Meta | video 3 | € 0,92 | € 0,00 | −€ 0,92 (pauzeren) |
| Meta | Video led profiel japans | € 0,36 | € 0,00 | −€ 0,36 (pauzeren) |
| Google | PMAX - Campagne | € 14,94 | € 13,00 | −€ 1,94 (−13%, mét uitsluitingen) |
| Google | Search \| Wandpanelen | € 10,91 | € 12,00 | +€ 1,09 (+10%) |
| Google | Shopping \| Bamboepanelen | € 5,43 | € 9,00 | +€ 3,57 (+66%) |
| Google | Search \| Concurrenten | € 5,50 | € 0,00 | −€ 5,50 (blijft gestopt) |
| Google | Brand \| Protection | € 1,83 | € 4,00 | +€ 2,17 (+119%) |
| Google | Brand \| Protection NL-BE | € 1,65 | € 4,00 | +€ 2,35 (+142%) |
| | **Totaal** | **€ 100,44** | **€ 120,00** | **+€ 19,56 (+19%)** |

### Dag voor dag

**Dag 1 (vandaag, 21 oktober) — PRIORITEIT 1**
1. **Beantwoord de staalkostprijsvraag** (€6,95 per zending of per staaltje?). Dit gaat vóór alles: bij "per staaltje" verliest de staalmachine €1.369 per 14 dagen en moet het hele Meta-budget heroverwogen worden. *Betrouwbaarheid: n.v.t. — ik weet het simpelweg niet.*
2. **Google Ads — "Toevoegen aan winkelwagen":** zet één van de twee primaire conversieacties op Secundair. *Effect: schoner biedsignaal. Risico: nihil. Betrouwbaarheid: hoog. Vereist jouw toestemming.*
3. **Bevestig dat Search | Concurrenten uit blijft.** *Effect: €5,50/dag bespaard. Risico: nihil — 0 conversies in 30 dagen.*

**Dag 2**
4. **Uitsluitingen toevoegen** aan PMax en Search | Wandpanelen: de 10 concurrentmerken en de 60 Engelse/buitenlandse termen uit deel 5. *Effect: €90,71 per 30 dagen bespaard, en betere signaalkwaliteit. Risico: laag. Betrouwbaarheid: hoog.*
5. **Meta — pauzeer video 3, Video led profiel japans en Nieuwe wandpanelen.** *Effect: €6,02/dag vrij. Risico: laag; Nieuwe wandpanelen zat met €22,12 nog onder het plafond, dus dit is de minst zekere van de drie. Betrouwbaarheid: middel.*

**Dag 3**
6. **Meta — budget verhogen:** diaan creator 1 naar €30/dag, Marmerlook naar €24/dag, diaan creator 2 naar €8/dag. **In één stap, niet gefaseerd** — de ad set zit in campagnebudgetoptimalisatie, dus een wijziging herstart de leerfase; één keer is beter dan drie keer. *Effect: naar verwachting +8 tot +14 conversies per 14 dagen. Risico: CPA loopt op bij opschaling; diaan creator 1 gaat 1,8× in budget, verwacht dat zijn CPA van €10,80 naar €14–18 beweegt — nog ruim onder het plafond. Betrouwbaarheid: middel-hoog. Herbeoordelen: dag 10.*
7. **Google — brandcampagnes naar €4/dag elk.** *Effect: +3 tot 6 conversies per 14 dagen à ±€6. Risico: nihil. Betrouwbaarheid: hoog.*

**Dag 4**
8. **PMax-besluit.** Twee opties: (a) pauzeren en de €13/dag naar Shopping schuiven, of (b) nog 14 dagen met de uitsluitingen erin en dan definitief beslissen. **Mijn advies is (b)**, omdat PMax het enige kanaal is dat buiten zoekintentie werkt, en de uitsluitingen van dag 2 nog niet getest zijn. Als de CPA op dag 18 nog boven €50 ligt: pauzeren. *Betrouwbaarheid: middel. De data zegt "stoppen", maar het verlies is €142 per 14 dagen en een herbouwkans is dat waard.*

**Dag 5 — PRIORITEIT 2**
9. **Bouw de opvolgflow voor staalaanvragers.** Drie berichten: dag 2 (bevestiging + inspiratie), dag 7 ("hoe ziet het eruit bij daglicht?"), dag 14 (aanbod of montagehulp). Dit is kans 1 uit deel 8 en de grootste winstpost in dit rapport. *Effect: elke procentpunt doorkoop is ~€414 brutowinst per 14 dagen. Risico: nihil. Betrouwbaarheid: middel. Vereist jouw toestemming — dit raakt Shopify.*

**Dag 6**
10. **Maak een nieuwe conversieactie voor staalaanvragen** met een vaste waarde van €25, naast de bestaande aankoopactie. Dit is het fundament onder elke latere waarde-gebaseerde biedstrategie. *Risico: middel — een nieuwe conversieactie moet correct op Primair/Secundair staan, anders wordt er dubbel geteld. Vereist jouw toestemming en zorgvuldige uitvoering.*
11. **Zet de Meta-retargeting-ad set op** voor add-to-cart zonder aankoop, 14 dagen venster, €8/dag uit het Scenario B-budget.

**Dag 7**
12. **Hermeten.** Alle cijfers uit deel 1 opnieuw ophalen en het dashboard bijwerken. Beslispunten: is de CPA van diaan creator 1 onder €18 gebleven? Is de CPA van zakelijk verbouwen onder €20 gezakt? Levert Shopping nog steeds conversies onder €20?

### Wat ik expliciet níet adviseer
- **Niet overstappen op waarde-gebaseerd bieden** (tROAS, "conversiewaarde maximaliseren") op geen van beide platformen, zolang een staalaanvraag als €6,95 geregistreerd staat. Dat zou de biedmachine wegsturen van je winstgevendste conversie.
- **Niet €9,95 gaan rekenen voor het staalpakket** en geen limiet op het aantal stalen per order — tenzij het antwoord op vraag 1 "per staaltje" is. Dan verandert dat.
- **zakelijk verbouwen niet pauzeren.** CPA €24,61 zit onder het plafond. Alleen niet verder opschalen.
- **Geen nieuwe campagnestructuur in Google.** Je account is klein (€40/dag); meer campagnes betekent minder data per campagne.

---

## 10. Drie budgetscenario's

Alle bedragen zijn dagbudgetten. De bandbreedtes zijn scenario's met onzekerheid, geen voorspellingen: ze zijn gebaseerd op de CPA-spreiding van de laatste twee periodes en op de aanname dat de CPA bij opschaling 30–60% oploopt.

### Scenario A — Veilig: winst beschermen

| | Bedrag |
|---|---:|
| Dagbudget | **€ 85** (Meta € 54 · Google € 31) |
| Maandbudget | **€ 2.585** |
| Verschil met nu | −€ 15,44/dag (−15%) |

Alleen verspilling weghalen, niets opschalen: PMax pauzeren (−€14,94), Concurrenten uit (−€5,50), de drie Meta-nulproducenten pauzeren (−€6,02), uitsluitingen toevoegen, en €11 verschuiven naar de brandcampagnes en diaan creator 1.

**Verwachte uitkomst per 14 dagen:** 48–58 conversies (nu 75), contributiewinst **€1.500 – €1.950**, ROI **+120% tot +165%**.
**Risico:** laag. Je verliest het PMax-volume, dat deels wel degelijk nieuwe mensen bereikt die later via een ander kanaal terugkomen — dat is niet meetbaar en dus een reëel maar onbekend verlies.

### Scenario B — Gebalanceerd: gecontroleerde groei ⭐ aanbevolen

| | Bedrag |
|---|---:|
| Dagbudget | **€ 120** (Meta € 78 · Google € 42) |
| Maandbudget | **€ 3.650** |
| Verschil met nu | +€ 19,56/dag (+19%) |

De verdeling uit deel 9. Verspilling eruit, de drie bewezen winnaars erin, PMax op proef met uitsluitingen, en €8/dag voor de retargeting-test.

Let op: de retargeting-ad set uit dag 6 (€8/dag) zit **niet** in deze €120. Vanaf dag 6 komt het totaal daarmee op **€128/dag (€3.894/maand)**. Wil je strikt op €120 blijven, haal die €8 dan van *diaan creator 1* (naar €22/dag) — maar ik adviseer de €8 erbij te doen, want retargeting op 131 afgebroken winkelwagens is goedkoper publiek dan nieuw bereik.

**Verwachte uitkomst per 14 dagen:** 72–95 conversies, contributiewinst **€1.750 – €2.600**, ROI **+104% tot +155%**.
**Risico:** middel. De CPA van diaan creator 1 loopt bij 1,8× budget vrijwel zeker op; als die boven €25 komt moet je terug. Herbeoordelen op dag 10.
**Waarom dit mijn advies is:** het is het enige scenario dat tegelijk de twee bewezen verliesposten (PMax-overbesteding, Concurrenten) wegneemt én geld zet op de twee bewezen winnaars, zonder zoveel op te schalen dat de CPA-stijging het voordeel opeet.

### Scenario C — Agressief: groei met hoger risico

| | Bedrag |
|---|---:|
| Dagbudget | **€ 160** (Meta € 105 · Google € 55) |
| Maandbudget | **€ 4.867** |
| Verschil met nu | +€ 59,56/dag (+59%) |

Meta: diaan creator 1 €40, Marmerlook €30, zakelijk verbouwen €15, diaan creator 2 €10, retargeting €10. Google: Search | Wandpanelen €16, Shopping €14, PMax €15, brand €5 + €5.

**Verwachte uitkomst per 14 dagen:** 85–125 conversies, contributiewinst **€1.400 – €2.900**, ROI **+63% tot +130%**.
**Risico:** hoog, en wel om één concrete reden: **je weet nog niet hoeveel een staalaanvraag echt waard is.** Het hele verdienmodel van Meta hangt aan die €33,26, en dat getal rust op 28 doorkopers. Bij 5% doorkoop in plaats van 7,7% valt het plafond naar €21,68 en komt *zakelijk verbouwen* (€24,61) direct in de verliezen. Op €160/dag is dat een verlies van ongeveer €1.000 per maand voordat je het in de cijfers ziet.
**Ik adviseer C niet voordat** (a) de staalkostprijsvraag beantwoord is, en (b) de opvolgflow uit dag 5 minstens 14 dagen heeft gelopen en het doorkooppercentage daadwerkelijk is gestegen.

---

## 11. Executive summary

### 1. Hoe gezond zijn mijn advertenties op dit moment?
**Redelijk gezond maar snel verslechterend.** Op accountniveau is de ROI +117% en zit je ruim boven break-even (MER 3,29 tegen een break-even van 1,35). Maar de contributiewinst viel in 14 dagen met 44% terug (€2.953 → €1.651) terwijl je 7% méér besteedde, en de advertentiekosten per verkocht paneel verdubbelden van €18,73 naar €39,06. De advertenties zelf werden beter (CTR omhoog, CPC omlaag op alle zeven Meta-advertenties); wat verslechterde is de **mix**: je koopt steeds meer gratis staalaanvragen en steeds minder paneelorders.

### 2. Verdienen mijn advertenties echt geld, of lijkt dat alleen zo door platformattributie?
**Deels echt, en de platformcijfers zijn beduidend te rooskleurig.** Meta claimt €1.674,38 omzet. GA4 ziet €0,00 uit Paid Social. Shopify ziet €0,00 productomzet uit facebook en instagram. Alle 25 Meta-orders in Shopify waren gratis stalen waarvan alleen de €6,95 verzendkosten binnenkwamen. Meta's ROAS van 1,99 kun je niet gebruiken.

Wat **wel** echt is: Google leverde €1.039,10 netto-omzet uit 23 Shopify-orders, en de staalmachine is aantoonbaar waardevol — 7,7% van de staalaanvragers koopt binnen enkele weken panelen voor gemiddeld €752,62, en **41,2% van al je paneelomzet komt van mensen die eerder een staal aanvroegen**. Dat is gemeten in je eigen orderhistorie, niet geschat. Meta verdient dus geld, maar met vertraging en niet op de manier die Meta rapporteert.

### 3. Welke advertenties moet ik vandaag pauzeren?
| Pauzeren | Kosten/14d | Reden |
|---|---:|---|
| **PMAX - Campagne** (of 14 dagen op proef met uitsluitingen) | € 209,10 | €104,55 per conversie, 3,1× het plafond, twee periodes op rij |
| **Search \| Concurrenten** — houd gestopt | € 76,99 | 0 conversies in 30 dagen, kwaliteitsscore 3 |
| **video 3** | € 12,89 | 0 conversies |
| **Video led profiel japans** | € 5,02 | 0 conversies |
| **Nieuwe wandpanelen** (optioneel) | € 66,35 | €22,12 CPA is nog onder het plafond, maar het is je zwakste presterende creative met volume |

### 4. Welke advertenties moet ik vandaag opschalen?
| Opschalen | Van | Naar | Reden |
|---|---:|---:|---|
| **diaan creator 1** | € 16,98/dag | € 30/dag | CPA €10,80 = 32% van het plafond; CR 1,97% is bijna 3× het accountgemiddelde |
| **Marmerlook va 125** | € 16,37/dag | € 24/dag | CPA €14,33, laagste frequentie (1,83) = meeste kopruimte, hoogste add-to-cart-waarde |
| **Brand \| Protection NL-BE** | € 1,65/dag | € 4/dag | €5,79 per transactie, ROAS 15,08 |
| **Brand \| Protection** | € 1,83/dag | € 4/dag | €5,11 per transactie, 38% CTR |
| **diaan creator 2** | € 3,24/dag | € 8/dag | CPA verbeterde van €33,22 naar €15,14 |

### 5. Waar verlies ik het meeste geld?
In volgorde:
1. **Niet bij de advertenties, maar bij de opvolging.** 90 staalaanvragen in 14 dagen, waarvan 92% nooit terugkomt. Elke procentpunt die je die 7,7% kunt verhogen is ~€414 brutowinst per 14 dagen (0,9 extra paneelorder × €459,70 brutomarge), zonder één euro extra media.
2. **131 afgebroken paneelwinkelwagens met €19.384,66 waarde**, en geen enkele retargeting-advertentie die ze terugroept.
3. **PMax:** €209,10 per 14 dagen voor 2 conversies, dus circa €142 aantoonbaar verlies.
4. **Search | Concurrenten:** €76,99 volledig verloren (al gestopt).
5. **Zoektermverspilling:** €90,71 per 30 dagen aan concurrentmerken en buitenlandse zoektermen.
6. **De zakelijke doelgroep:** 14 gestarte checkouts met €3.106,86 aan panelen in de winkelwagen, waarvan 10 orders van €6,95 overbleven. Dat is geen advertentieprobleem maar een ontbrekend zakelijk aankooppad.

### 6. Is mijn tracking betrouwbaar genoeg om budgetbeslissingen op te baseren?
**Voor aantallen: ja. Voor waardes: nee.** De conversieaantallen van Meta, GA4, Google Ads en Shopify zijn onderling consistent zodra je de attributievensters meeneemt. De waardes zijn kapot: een staalorder wordt overal als €6,95 geregistreerd terwijl die €33,26 waard is, en Meta's omzetclaim is met geen enkele onafhankelijke bron te verifiëren.

**Praktische consequentie:** stuur op **kosten per conversie tegen een plafond van €33,26 en een streefdoel van €25**. Gebruik geen ROAS en geen waarde-gebaseerd bieden tot de staalconversie correct gewaardeerd is.

Drie dingen zijn bovendien niet verifieerbaar vanuit deze omgeving en kunnen de cijfers nog verschuiven: Consent Mode v2, Meta's Conversions API/deduplicatie, en de Merchant Center-feedkwaliteit. Daarvoor is browsertoegang of Google Ads API-toegang nodig.

### 7. Wat zijn de drie belangrijkste acties die ik nu moet uitvoeren?
1. **Beantwoord één vraag: is die €6,95 kostprijs per zending of per staaltje?** 287 staaltjes in 90 orders, de klant betaalt één keer €6,95. Per zending klopt mijn hele analyse. Per staaltje verlies je €1.369 per 14 dagen en moet het Meta-budget onmiddellijk terug. Dit is het enige getal dat mijn conclusie kan omdraaien.
2. **Bouw de opvolgflow voor staalaanvragers** (dag 2 / dag 7 / dag 14). Je hebt al 90 warme aanvragen per twee weken en gebruikt 7,7% ervan. Dit is de grootste winstpost in het hele rapport en kost geen mediabudget.
3. **Haal de bewezen verspilling eruit en zet het op de bewezen winnaars.** PMax terug of uit, Concurrenten uit, drie Meta-nulproducenten uit, de uitsluitingslijst erin — en het vrijgekomen geld naar diaan creator 1, Marmerlook en de twee brandcampagnes.

### 8. Hoe zou jij mijn budget verdelen als dit mijn eigen bedrijf was?
**Scenario B: €120 per dag, €3.650 per maand** — maar met één voorwaarde en één accentverschuiving.

De voorwaarde: ik zou **die staalkostprijsvraag eerst beantwoorden** voordat ik één euro extra naar Meta schuif. Het hele Meta-verhaal hangt aan de aanname dat een staal cost-neutraal is.

De accentverschuiving: ik zou **niet eerst opschalen, maar eerst de lekken dichten.** Concreet, in deze volgorde: eerst de verspilling eruit (dag 1–2, −€26/dag), dan de opvolgflow bouwen (dag 5, €0), en pas in week 2 opschalen met wat dan vrijkomt. De reden is simpel: **je bent nu goed in het kopen van staalaanvragen en slecht in het omzetten ervan.** Meer staalaanvragen kopen voordat je de omzetting hebt verbeterd, is harder trappen op een fiets met een losse ketting.

En het ongemakkelijke deel: op €120/dag is het maximum dat dit account kan opleveren, bij het huidige doorkooppercentage, ruwweg €2.600 contributiewinst per 14 dagen. Als jij hier echt een premium architectuurmerk van wil maken, dan zit de groei niet in €40/dag extra advertentiebudget maar in twee dingen die dit rapport alleen kan aanwijzen, niet oplossen: **de 16 dagen tussen staal en aankoop benutten**, en **een zakelijk aankooppad bouwen** voor de doelgroep die nu wel panelen in de winkelwagen legt maar alleen stalen afrekent.

---

## Bijlage — berekeningen en bronverwijzingen

| Cijfer | Berekening | Bron |
|---|---|---|
| Marge 73,9% | (€4.136,71 − €1.080,00) / €4.136,71 | Shopify orderregels, 7–20 okt, orderkorting proportioneel toegerekend |
| Break-even ROAS 1,35 | €4.136,71 / €3.056,71 | idem |
| Staalwaarde €33,26 | 0,077 × (€752,62 / 1,21) × 0,739 | `ads/cohort-staalaanvragers.json`, 365 rijpe cohortleden |
| Meta CPA €15,60 | €842,66 / 54 | Windsor → facebook, 7–20 okt |
| Google-kosten €563,48 | som van 6 campagnes | Windsor → googleanalytics4, gevalideerd tegen Google-export |
| Meta-waarde €1.674,38 | som van `onsite_web_app_purchase` actiewaarden | Windsor → facebook, actiewaarden per advertentie |
| Paid Social omzet €0,00 | GA4 `purchase_revenue`, kanaal Paid Social | Windsor → googleanalytics4, beide periodes |
| Zoektermverspilling €90,71 | €64,96 merken + €25,75 buitenlands | `ads/raw/zoektermen.csv`, 19 sep–18 okt |
| 41,2% paneelomzet uit staalaanvragers | eerder gemeten over 12 mei–12 okt | `ads/cohort-staalaanvragers.json` |

**Alles in dit rapport komt uit bovenstaande bronnen. Waar een getal niet beschikbaar was, staat "niet beschikbaar" of "niet verifieerbaar" — er is niets geschat zonder dat dat erbij staat.**
