# Advertentie-ROI per advertentie — Meta Ads en Google Ads

> ⚠️ **VERVALLEN CIJFERS — lees eerst `03-CMO-RAPPORT-14D.md`.**
> Twee getallen in dit document zijn te hoog. De marge van 78,6% en de break-even ROAS van 1,26
> zijn berekend op regelprijzen **zonder de orderkortingen af te trekken**. Met de kortingen
> correct toegerekend is de marge **73,9%** (7–20 okt) respectievelijk **67,0%** (23 sep–6 okt) en
> de break-even ROAS **1,35** respectievelijk **1,49**. Daardoor zakt ook de verwachte brutowinst
> per staalaanvraag van €45,83 naar **€33,26**. De analyse-opzet en de cohortmethode in dit
> document blijven geldig; alleen die bedragen zijn achterhaald.

**Periode advertenties: laatste 30 dagen** (12 september — 12 oktober 2026). Daarvoor stond de meting
niet goed, dus oudere perioden blijven eruit. **Het doorkooppercentage van staalaanvragers** komt uit
een langere orderhistorie (12 mei — 12 oktober 2026), omdat een staal dat vandaag de deur uitgaat nog
niet gekocht kan hebben. Dat getal komt uit de orders van de winkel zelf en niet uit advertentietags,
dus de kwaliteit van die tags speelt er geen rol in.

Opgegeven door PureDeco: **inkoopprijs € 30 per paneel**. Alles verder komt uit het Meta-advertentie-
account, de GA4-property en de Shopify-orderregels.

Dashboard: https://claude.ai/artifact/9PVzn4wwdwqcGsVE5wrn9Y
Broncode: `ads/dashboard/index.html` · Cohortbestand: `ads/cohort-staalaanvragers.json`

---

## 1. Correctie op de vorige versie

De vorige analyse zette de grens tussen staal en paneel op € 30 per stuk en haalde daarmee stalen en
panelen door elkaar. Dat was fout. Uit de **orderregels** blijkt de catalogus eenduidig:

| Prijs per stuk | Wat het is | Stuks (5 maanden) |
|---|---|---:|
| € 0,00 | gratis staal | 1.452 |
| € 8,95 | High Tack Montagekit | 89 |
| € 23,95 | profielen (eind-, hoek-, tussen-) | 126 |
| € 49,95 / € 65,00 / € 70,00 | akoestische panelen, sierlatten | 23 |
| **€ 89,95 — € 599,00** | **wandpanelen** | **405** |

Tussen € 70 en € 89,95 zit niets. Een paneel kost gemiddeld **€ 140,44** in de laatste 30 dagen.
Daarmee is de marge heel anders dan eerder gemeld.

## 2. De marge, uit de orderregels

| | |
|---|---:|
| Verkochte panelen (30 dagen) | 111 stuks |
| Paneelomzet | € 15.588,50 |
| Gemiddelde verkoopprijs per paneel | € 140,44 |
| Inkoopwaarde (111 × € 30) | € 3.330,00 |
| Brutowinst op panelen | € 12.258,50 |
| **Brutomarge** | **78,6%** |
| **Break-even ROAS** | **1,27** |
| Gemiddelde paneelomzet per paneelorder | € 677,76 |

Een break-even ROAS van 1,27 in plaats van 2,50 verandert het oordeel over bijna elke advertentie.

## 3. Wat een staalaanvraag werkelijk waard is

Dit is het getal waar de hele strategie op draait, en het staat in de administratie:

| | |
|---|---:|
| Staalaanvragers met minstens 30 dagen de kans | 365 |
| Daarvan kocht later panelen | 28 |
| **Doorkooppercentage** | **7,7%** |
| Mediaan aantal dagen tot de paneelorder | 16 dagen |
| Gemiddelde paneelomzet per doorgekomen klant | € 752,62 |
| **Verwachte brutowinst per staalaanvraag** | **€ 45,40** |

7,7% × € 752,62 × 78,6% marge = **€ 45,40 per aangevraagd staal**, gemiddeld over álle aanvragers —
ook de 92% die nooit terugkomt. Over de volle vijf maanden komt **41% van alle paneelomzet** van
klanten die eerder een staal aanvroegen.

De advertentiekosten per toegeschreven conversie zijn **€ 25,55**. Een staalaanvraag is dus ruim
winstgevend ingekocht — zolang het fysieke staal niet te veel kost. Zie punt 6.

## 4. Meta Ads per advertentie (30 dagen)

*Brutowinst nu* = netto waarde (conversiewaarde min € 6,95 verzendkosten per conversie) × 78,6%
marge − spend. *Pijplijn* = de toegeschreven staalaanvragen × € 45,40.

| Advertentie | Spend | CPC | Conv. | €/conv. | ROAS | Brutowinst nu | Pijplijn | Verwacht totaal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| zakelijk verbouwen | 410,63 | 0,23 | 25 | 16,43 | 7,39 | +1.840,39 | +943,29 | **+2.783,68** |
| Marmerlook va 125 | 296,93 | 0,23 | 21 | 14,14 | 5,66 | +909,16 | +850,70 | **+1.759,86** |
| diaan creator 1 | 637,43 | 0,26 | 30 | 21,25 | 0,90 | −349,04 | +1.337,49 | **+988,45** |
| Nieuwe wandpanelen | 178,73 | 0,25 | 8 | 22,34 | 0,31 | −178,73 | +363,22 | **+184,49** |
| diaan creator 2 | 69,62 | 0,29 | 3 | 23,21 | 0,30 | −69,62 | +136,21 | **+66,59** |
| video 3 | 18,74 | 0,28 | 0 | — | 0,00 | −18,74 | 0,00 | **−18,74** |
| Video led profiel japans | 14,08 | 0,36 | 0 | — | 0,00 | −14,08 | 0,00 | **−14,08** |
| **Totaal** | **1.626,16** | 0,25 | **87** | 18,69 | 3,30 | **+2.119,33** | **+3.630,90** | **+5.750,24** |

**Stresstest.** De pijplijnkolom gebruikt Meta's eigen toewijzing, en die is optimistisch: Shopify
schrijft maar 42 orders aan Facebook en Instagram toe tegenover de 87 die Meta claimt. Reken je met
Shopify's eigen 42 orders, dan is de pijplijn 42 × € 45,40 = € 1.906,80 tegenover € 1.626,16 spend —
**ook dan betaalt Meta zich terug.** Dat is het strengste scenario dat de data toelaat.

## 5. Google Ads per campagne (30 dagen, GA4)

| Campagne | Kosten | CPC | Trans. | Productomzet | Brutowinst nu | Pijplijn | Verwacht totaal |
|---|---:|---:|---:|---:|---:|---:|---:|
| PMAX - Campagne - PureDeco.nl | 401,74 | 0,63 | 3 | 0,00 | −401,74 | +136,21 | **−265,53** |
| Search \| Wandpanelen | 353,77 | 1,09 | 5 | 0,00 | −353,77 | +227,01 | **−126,76** |
| Search \| Concurrenten | 231,53 | 1,82 | 1 | 0,00 | −231,53 | +45,40 | **−186,13** |
| Shopping \| Bamboepanelen | 72,99 | 0,12 | 4 | 0,00 | −72,99 | +181,61 | **+108,62** |
| Brand \| PureDeco Protection | 29,54 | 0,26 | 5 | 431,70 | +309,94 | +198,09 | **+508,03** |
| Brand \| PureDeco Protection NL-BE | 18,65 | 0,23 | 2 | 361,60 | +265,71 | +66,58 | **+332,29** |
| **Totaal** | **1.108,22** | 0,23 | **20** | **793,30** | **−484,38** | **+854,90** | **+370,52** |

Per advertentiegroep: *Wandpanelen algemeen* € 281,16 (4 transacties, € 0,00 omzet), *Thuispaneel*
€ 104,39 bij € 3,60 per klik, *Paneli* € 90,31 met nul transacties.

**Samen: € 2.734,38 advertentiekosten, € 1.634,95 brutowinst nu, € 4.485,80 pijplijn, verwacht
totaal € 6.120,75** — vóór de kostprijs van de verstuurde stalen, de verzendkosten die PureDeco
zelf betaalt, verwerking, retouren en vaste lasten.

## 6. De enige vraag die nog openstaat, en hij beslist alles

In 30 dagen zijn er **400 stalen** weggegeven in **139 staalorders** (2,9 per order). Dat is
**3,6 gratis stalen per verkocht paneel**. De klant betaalt € 6,90 verzendkosten per staalorder.

| Per staalorder | |
|---|---:|
| Verwachte brutowinst uit de staalaanvraag | + € 45,40 |
| Verzendkosten die de klant betaalt | + € 6,90 |
| Advertentiekosten per toegeschreven conversie | − € 25,55 |
| **Ruimte voor de fysieke staalorder** | **€ 26,75** |
| Bij 2,9 stalen per order | |
| **Break-even kostprijs per staal** | **€ 9,29** |

Kost een staal minder dan € 9,29, dan is de staalmachine winstgevend en mogen de advertenties die
stalen aanbrengen juist harder lopen. Kost een staal meer, dan is elk extra staal verlies, hoe
goedkoop de klik ook was.

**Dit is niet academisch.** In de catalogus staan de gratis stalen onder dezelfde artikelnamen en
dezelfde maten als de volwaardige panelen (bijvoorbeeld "Wandpaneel Hout 810 Noir Oak", variant
"260 cm x 122 cm / 5mm Stomp"), met prijs nul. Zijn dat werkelijk panelen van volle maat, dan kost
elk staal de volle € 30 inkoop en loopt de rekening op tot **€ 12.000 per 30 dagen** — ruim vier keer
de advertentiekosten, en dan is het hele model verlieslatend. Zijn het kleine stalen van een paar
euro, dan is dit het beste kanaal dat PureDeco heeft.

**Wat ik nodig heb:** de kostprijs van één staal (materiaal + verpakking + wat PureDeco zelf aan
verzending betaalt). Eén getal, en de hele analyse wordt een afrekening in plaats van een inschatting.

## 7. Advies

### Direct stoppen — € 264,35 per 30 dagen, zonder enig verlies

Deze drie zijn negatief in élk scenario:

1. **Search | Concurrenten** — € 231,53 voor één conversie bij € 1,82 per klik (advertentiegroep
   *Thuispaneel* € 3,60 per klik). Bieden op merknamen van concurrenten levert hier niets op.
2. **video 3** en **Video led profiel japans** — € 32,82 en nul conversies. Te klein om van te leren.

### Herbouwen in plaats van stoppen

3. **PMAX - Campagne - PureDeco.nl** (€ 401,74, drie conversies, nul productomzet) en
   **Search | Wandpanelen** (€ 353,77, vijf conversies, nul productomzet). Die kopen uitsluitend
   staalaanvragen in, maar dúúr: € 134 en € 71 per conversie, tegen € 18,69 bij Meta. Ze zijn niet
   waardeloos, ze zijn te duur. Zet ze op de staalaanvraag als conversiedoel mét de juiste waarde
   (punt 6 hieronder) en een doel-CPA rond de € 25; halen ze dat niet binnen twee weken, dan uit.
   Controleer eerst of PMAX met *PMax_NL (Adscale)* op dezelfde feed concurreert — die laatste stond
   deze 30 dagen praktisch stil.
4. **Shopping | Bamboepanelen** — € 72,99 bij € 0,12 per klik, de goedkoopste traffic die er is, en in
   de pijplijn al positief (+€ 108,62). Laten staan en de bestemmingspagina nakijken: 607 klikken
   leidden tot vier staalorders en nul panelen.

### Opschalen — hier zit het geld

5. **zakelijk verbouwen** is met afstand je beste advertentie: € 410,63 in, € 2.783,68 verwacht
   eruit, ROAS 7,39, € 16,43 per conversie en de hoogste waarde per conversie van allemaal. Hij
   krijgt maar een kwart van het Meta-budget. Verhoog met 20–30% per week (niet in één sprong, dan
   herijkt Meta de doelgroep) en kijk wekelijks of de waarde per conversie boven € 100 blijft. Zakt
   die naar het verzendtarief, dan is de schaalgrens bereikt. Dit is ook het zakelijke segment waar
   PureDeco naartoe wil — de advertentie bewijst dat die doelgroep werkt.
6. **Marmerlook va 125** — ROAS 5,66, zelfde aanpak.
7. **Brand | PureDeco Protection** en **NL-BE** — € 48,19 samen voor € 840 verwachte winst, de enige
   Google-campagnes die geld opleveren, en ze staan vrijwel droog. Verdubbel het budget. Let op dat
   merkzoekwoorden deels organisch verkeer opeten: beoordeel betaald plus organisch op het merk
   samen.
8. **diaan creator 1** mag blijven draaien, maar op de proef. € 637,43 is 39% van het Meta-budget
   voor dertig staalaanvragen en vrijwel geen directe omzet. In de pijplijn is hij positief
   (+€ 988,45), maar dat hangt volledig aan het doorkooppercentage. Meet over zes weken of de
   staalaanvragers uit deze advertentie net zo vaak terugkomen als het gemiddelde van 7,7%; zo niet,
   dan is zijn pijplijnwaarde lager dan hier staat en gaat hij eruit.

### De meting goed zetten — dit is de grootste hefboom die je hebt

9. **Geef de staalaanvraag zijn gemeten waarde.** Nu gaat een staalorder als `Purchase` met € 6,95
   als waarde naar beide platforms. Daardoor denken de biedalgoritmes dat een staalaanvraag
   € 6,95 waard is, terwijl hij € 45,40 brutowinst oplevert. Stuur de staalorder als eigen
   gebeurtenis met **waarde € 45,40** en houd `Purchase` voor echte paneelorders met de
   werkelijke orderwaarde. Dan kunnen Meta en Google voor het eerst op echte waarde bieden in
   plaats van op verzendkosten. Zet daarna Meta op conversiewaarde met een minimum-ROAS van 1,3
   en Google op doel-ROAS 1,3.
   *Dit raakt conversietracking. Ik voer hier niets van uit zonder jouw expliciete toestemming;
   dit is een voorstel met een uitvoeringsplan.*
10. **Stuur de echte orderwaarde server-side door** (Shopify → Meta Conversions API, met order-id
    voor ontdubbeling).
11. **UTM's op alle advertentielinks.** Van de 167 orders in deze 30 dagen hebben 73 orders
    (€ 8.118,41 productomzet) geen enkele verwijzer in Shopify — 44% van de orders zonder
    herkenbare bron. En herstel de zelfverwijzingen: 16 orders komen binnen met verwijzer
    `puredeco`, één met `mollie`.

### De staalmachine beter maken — hier ligt de grootste winst

12. **Elk procentpunt doorkoop is € 823 brutowinst per maand waard** bij de huidige 139 staalorders
    per 30 dagen (1,39 extra klanten × € 752,62 × 78,6%). Van 7,7% naar 12% is **€ 3.540 per maand**,
    zonder één euro extra advertentiebudget. Dit is veruit de goedkoopste groei die er ligt.
13. **Bouw een opvolgreeks op de staalorder.** De mediaan is 16 dagen tussen staal en order: er is
    tijd en er wordt nu niets mee gedaan. Drie contactmomenten — dag 2 ("je staal is onderweg" met
    een montagevideo), dag 7 (rekenhulp: hoeveel panelen heb ik nodig voor mijn wand), dag 14
    (persoonlijk aanbod met een termijn). Meet het doorkooppercentage per week in dit dashboard.
14. **Maak van de staalkosten een voucher.** Vraag € 9,95 voor de staalbox in plaats van alleen
    verzendkosten, en geef dat bedrag terug als korting op de eerste paneelorder. Dat dekt de
    kostprijs van het staal, filtert de verzamelaars eruit, en geeft elke aanvrager een reden om
    terug te komen. Dit is de standaardoplossing in materiaalverkoop en het is hier precies de
    ingreep die punt 6 oplost.
15. **Beperk het aantal stalen per order.** Nu gemiddeld 2,9, en 3,6 gratis stalen per verkocht
    paneel. Een maximum van drie met een duidelijke keuzehulp verlaagt de kosten zonder de
    conversie te raken.
16. **Zet een zakelijke staalbox apart.** Er bestaat al een "Sample box (Volledig b2b)" van € 5,95;
    daarvan is er in vijf maanden één verkocht. *zakelijk verbouwen* bewijst dat de zakelijke
    doelgroep de hoogste orderwaarde heeft — geef die doelgroep een eigen aanvraagroute met
    projectgegevens erbij, zodat de opvolging gericht kan.

### Wat er nog niet gemeten is

17. **Het doorkooppercentage per bron.** De 7,7% is gemeten over álle staalaanvragers, niet alleen
    die uit advertenties. Of een aanvrager uit een Meta-video net zo vaak terugkomt als iemand die
    via organisch zoeken binnenkwam, is nu niet te zien. Met UTM's op de advertentielinks (punt 11)
    wordt dat na zes weken wél meetbaar, en dan is de pijplijnwaarde per advertentie exact.
18. **Hoeveel van de omzet ook zonder advertenties was gekomen.** Dat vraagt een test waarin een
    deel van het bereik bewust geen advertenties ziet (geo-holdout of een conversion-lift-studie bij
    Meta). Tot die tijd is alles hierboven toewijzing, geen oorzaak.

## 8. Over de data

De orderhistorie bevat een **bulk-import van 11 mei 2026** (tientallen orders binnen vier minuten met
afwijkende datums). Die valt buiten alle berekeningen hier; de cohortanalyse begint op 12 mei 2026.

## 9. Veiligheid

Uitsluitend gelezen. Er is niets gewijzigd in: Meta Ads, Google Ads, Performance Max, Shopping,
Merchant Center, productfeeds, GA4, pixels, conversietracking, landingspagina's, URL's, het live
Shopify-theme of het development-theme. Geen claims over certificeringen, brandklassen, akoestiek,
levertijden, voorraad, reviews, projecten of referenties. Het enige niet-gemeten getal in dit rapport
is de inkoopprijs van € 30 per paneel, door PureDeco zelf opgegeven. De kostprijs van een staal is
onbekend en is nergens ingevuld.
