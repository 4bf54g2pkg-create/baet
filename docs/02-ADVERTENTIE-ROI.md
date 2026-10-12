# Advertentie-ROI per advertentie — Meta Ads en Google Ads

Periode: **laatste 30 dagen** (voortschrijdend). Daarvoor stond de meting nog niet goed ingericht,
dus oudere perioden zijn bewust weggelaten. Alle cijfers komen live uit het Meta-advertentieaccount
PureDeco (via Windsor.ai), de GA4-property PureDeco en de Shopify-administratie van puredeco.nl.
Er is in dit onderzoek niets gewijzigd aan advertentieaccounts, conversietracking, GA4, pixels,
feeds of het live Shopify-theme.

Opgegeven door PureDeco en in de berekening gebruikt: **inkoopprijs € 30 per paneel**, en **stalen
leveren geen winst**.

Dashboard: https://claude.ai/artifact/9PVzn4wwdwqcGsVE5wrn9Y
Broncode van de dashboardpagina: `ads/dashboard/index.html`

---

## 1. De uitkomst in één alinea

In 30 dagen ging er **€ 2.734,38** naar advertenties. Op de omzet die Meta en Google zelf
toeschrijven, en met € 30 inkoop per paneel, blijft daar **€ 117,71 brutowinst** van over — en dat is
nog vóór jouw eigen verzendkosten, verwerking, retouren en vaste lasten. Het gaat dus ongeveer
quitte, en dat gemiddelde verbergt het echte verhaal: **€ 1.978,63 van die € 2.734,38 (72%) zit in
advertenties en campagnes die stuk voor stuk verlies maken**, terwijl vier van de dertien
€ 755,75 kosten en € 1.908,09 brutowinst opleveren.

## 2. De marge, uit de eigen verkopen gerekend

De marge is niet aangenomen maar berekend uit alle verkopen van de laatste 30 dagen, met de
betaalde prijs per stuk per artikel en maat:

| | |
|---|---:|
| Verkochte panelen vanaf € 30 per stuk | 157 stuks |
| Omzet daarvan | € 9.677,65 |
| Gemiddelde verkoopprijs per paneel | € 61,64 |
| Inkoopwaarde (157 × € 30) | € 4.710,00 |
| Brutowinst op panelen | € 4.967,65 |
| **Brutomarge** | **51,3%** |
| **Break-even ROAS** | **1,95** |

Buiten de rekensom gelaten, omdat daar geen winst op zit of de inkoopprijs niet bekend is:
**172 gratis weggegeven stuks**, **181 stuks die onder de inkoopprijs zijn verkocht** (samen
€ 3.370,62, gemiddeld € 18,62 per stuk) en **€ 1.102,25** aan profielen, montagekit en akoestische
panelen.

> **Dit is de vraag waar de marge op staat of valt.** Die 181 stuks à gemiddeld € 18,62 — zijn dat
> stalen, dan is 51,3% juist. Zijn het volwaardige panelen, dan worden ze onder de inkoopprijs
> verkocht en zakt de brutomarge naar **22,3%** met een break-even ROAS van **4,49**, en dan is
> vrijwel geen enkele advertentie meer rendabel. Een paar voorbeelden van die regels: *Japandi 823
> Taupe Dark* 38 stuks voor € 446,15 (€ 11,74 per stuk), *Travertine Ivory 851* 32 stuks voor
> € 446,14 (€ 13,94), *Japandi 821 Light* 19 stuks voor € 115,65 (€ 6,09), *Japandi 824 Taupe*
> 41 stuks voor € 1.040,95 (€ 25,39). Het dashboard rekent met 51,3% en laat het andere scenario
> ernaast zien.

## 3. Meta Ads per advertentie (30 dagen)

Netto waarde = de conversiewaarde van Meta min € 6,95 per conversie (verzendkosten van een
stalenorder, geen winst). Brutowinst = netto waarde × 51,3% − spend.

| Advertentie | Spend | CPC | Conv. | Waarde (Meta) | Netto waarde | ROAS | Brutowinst | ROI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| zakelijk verbouwen | 410,63 | 0,23 | 25 | 3.036,25 | 2.862,50 | 7,39 | **+1.058,72** | +258% |
| Marmerlook va 125 | 296,93 | 0,23 | 21 | 1.679,67 | 1.533,72 | 5,66 | **+490,35** | +165% |
| diaan creator 1 | 637,43 | 0,26 | 30 | 575,23 | 366,73 | 0,90 | **−449,18** | −70% |
| Nieuwe wandpanelen | 178,73 | 0,25 | 8 | 55,60 | 0,00 | 0,31 | **−178,73** | −100% |
| diaan creator 2 | 69,62 | 0,29 | 3 | 20,85 | 0,00 | 0,30 | **−69,62** | −100% |
| video 3 | 18,74 | 0,28 | 0 | 0,00 | 0,00 | 0,00 | **−18,74** | −100% |
| Video led profiel japans | 14,08 | 0,36 | 0 | 0,00 | 0,00 | 0,00 | **−14,08** | −100% |
| **Totaal** | **1.626,16** | 0,24 | **87** | **5.367,60** | **4.762,95** | **3,30** | **+818,72** | +50% |

*Nieuwe wandpanelen* en *diaan creator 2* hebben een netto waarde van exact nul: elke conversie die
Meta eraan toeschrijft was precies € 6,95 waard. Dat zijn stalenaanvragen, geen verkopen.

## 4. Google Ads per campagne (30 dagen, GA4)

De GA4-productomzet is al zonder verzendkosten, dus die gaat ongewijzigd × 51,3% − kosten.

| Campagne | Kosten | CPC | Trans. | Productomzet | ROAS | Brutowinst |
|---|---:|---:|---:|---:|---:|---:|
| PMAX - Campagne - PureDeco.nl | 401,74 | 0,63 | 3 | 0,00 | 0,00 | **−401,74** |
| Search \| Wandpanelen | 353,77 | 1,09 | 5 | 0,00 | 0,00 | **−353,77** |
| Search \| Concurrenten | 231,53 | 1,82 | 1 | 0,00 | 0,00 | **−231,53** |
| Shopping \| Bamboepanelen | 72,99 | 0,12 | 4 | 0,00 | 0,00 | **−72,99** |
| Brand \| PureDeco Protection | 29,54 | 0,26 | 5 | 431,70 | 14,61 | **+192,06** |
| Brand \| PureDeco Protection NL-BE | 18,65 | 0,23 | 2 | 361,60 | 19,39 | **+166,96** |
| **Totaal** | **1.108,22** | 0,23 | **20** | **793,30** | **0,72** | **−701,01** |

Dit is de scherpste bevinding van de 30-daagse periode: **van de € 1.108,22 Google Ads-kosten
leverde € 1.060,03 nul euro productomzet op**, en de € 48,19 die wél omzet opleverde zit in twee
merkcampagnes die vrijwel droogstaan. De grootste campagne, *PMAX - Campagne - PureDeco.nl*, kostte
€ 401,74 en had 3 transacties met € 0,00 productomzet. In de 90-daagse blik leek deze campagne nog
rendabel; die ROAS kwam volledig uit één order van 1 augustus — buiten de goed gemeten periode.

Per advertentiegroep valt op: *Wandpanelen algemeen* € 281,16 (4 transacties, € 0,00),
*Thuispaneel* binnen Concurrenten € 104,39 (€ 3,60 per klik, 1 transactie, € 0,00),
*Paneli* € 90,31 (0 transacties).

## 5. Drie bronnen, dezelfde advertenties, drie antwoorden

| Bron | Orders | Omzet | Toewijzing |
|---|---:|---:|---|
| Meta Ads Manager | 87 | 5.367,60 | 7 dagen na klik, 1 dag na weergave, over apparaten |
| GA4 laatste klik | 45 | **0,00** | laatste klik van de sessie |
| Shopify administratie | 42 | **185,00** | verwijzer van de order, brutoproductomzet |

GA4 schrijft over 30 dagen **nul euro** productomzet toe aan betaald Facebook, bij 3.546 sessies en
37 transacties. Shopify boekt € 185,00: facebook 16 orders met € 185,00 productomzet, instagram
26 orders met **€ 0,00** productomzet en wél € 143,50 verzendkosten.

Oorzaak, aantoonbaar: een order waarin alleen verzendkosten zijn betaald telt in beide platforms mee
als aankoop, met die verzendkosten als waarde. Op **16 van de 27** dagen met minstens één
toegeschreven aankoop lag de gemiddelde waarde per aankoop onder € 10 — dat betreft **41 van de 87**
aankopen (47%), vrijwel allemaal exacte veelvouden van € 6,95.

## 6. Advies

### Nu stoppen — € 1.978,63 per 30 dagen vrij, zonder één euro winst op te geven

Elk van deze is op zichzelf verlieslatend; samen kosten ze 72% van het advertentiebudget.

1. **PMAX - Campagne - PureDeco.nl** — € 401,74, nul productomzet. Niet pauzeren zonder eerst te
   kijken of hij met *PMax_NL (Adscale)* op dezelfde feed concurreert; die laatste stond in deze
   30 dagen praktisch stil.
2. **Search | Wandpanelen** — € 353,77 bij € 1,09 per klik, vijf transacties, nul omzet. De
   advertentiegroep *Wandpanelen algemeen* is er alleen al € 281,16 van.
3. **Search | Concurrenten** — € 231,53, één transactie, nul omzet. Bieden op merknamen van
   concurrenten levert hier niets op.
4. **diaan creator 1** — € 637,43, de grootste post bij Meta (39% van de Meta-spend), ROAS 0,90 en
   € 449,18 verlies. Dertig conversies met gemiddeld € 19,17 waarde: stalenaanvragers.
5. **Nieuwe wandpanelen** en **diaan creator 2** — samen € 248,35 met een netto waarde van exact
   nul. Elke toegeschreven aankoop was precies het verzendtarief.
6. **video 3** en **Video led profiel japans** — samen € 32,82 en nul conversies. Te klein om van te
   leren.
7. **Shopping | Bamboepanelen** — € 72,99 aan heel goedkope klikken (€ 0,12) die alleen tot
   nul-omzetorders leiden. Niet per se stoppen: dit is de goedkoopste traffic die je hebt. Eerst de
   bestemming nakijken — waar landen die 607 klikken, en waarom koopt niemand daar.

### Opschalen — de vier die geld opleveren

8. **zakelijk verbouwen** — € 410,63 in, € 1.058,72 brutowinst eruit, ROI 258%. Dit is met afstand
   je beste advertentie en hij krijgt maar een kwart van het Meta-budget. Verhoog stapsgewijs
   (20–30% per week, niet in één sprong) en kijk per week of de waarde per conversie boven de
   € 100 blijft. Zakt die naar het verzendtarief, dan is de schaalgrens bereikt.
9. **Marmerlook va 125** — ROI 165%, zelfde aanpak. Samen met *zakelijk verbouwen* zijn dit de
   enige twee Meta-advertenties met een waarde per conversie boven € 70: ze trekken kopers, geen
   stalenaanvragers.
10. **Brand | PureDeco Protection** en **NL-BE** — € 48,19 samen voor € 359,02 brutowinst. De enige
    Google-campagnes die geld opleveren, en ze staan vrijwel droog. Let op: merkzoekwoorden
    kannibaliseren voor een deel het organische resultaat, dus de werkelijke winst is kleiner dan de
    ROAS suggereert. Test met een verdubbeld budget en beoordeel betaald plus organisch op het merk
    samen, niet de campagne alleen.

### Eerst de meting repareren — dit gaat vóór elke budgetbeslissing

11. **Scheid de stalenaanvraag van de aankoop.** Zolang een order van € 0,00 product plus € 6,95
    verzendkosten als `Purchase` wordt doorgegeven, leren beide platforms dat een stalenaanvraag
    het doel is. Voorstel: stuur voor orders die alleen stalen bevatten een eigen gebeurtenis (bij
    Meta een `Lead` of `SubmitApplication`, bij Google een aparte conversieactie die *niet*
    meetelt voor biedingen) en houd `Purchase` voor betaalde orders. Zet Meta daarna op
    conversiewaarde in plaats van conversies, met een minimum-ROAS van 1,95.
    *Dit raakt conversietracking. Ik voer hier niets uit zonder expliciete toestemming; dit is een
    voorstel, geen uitgevoerde wijziging.*
12. **Zet UTM's op alle advertentielinks.** Van de 167 orders in deze 30 dagen hebben 73 orders
    (€ 8.118,41 productomzet) geen enkele verwijzer in Shopify. Dat is 44% van de orders zonder
    herkenbare bron.
13. **Herstel de zelfverwijzingen.** Shopify ziet 16 orders (€ 2.125,76) met verwijzer `puredeco`
    en één met `mollie`: het eigen domein en de betaalpagina worden als bron geregistreerd. Dat
    vervuilt elke bron-toewijzing.
14. **Stuur de echte orderwaarde server-side door** (Shopify → Meta Conversions API, met order-id
    voor ontdubbeling), zodat Meta op omzet optimaliseert in plaats van op pixelwaarde.
15. **Zet de prijsstelling recht.** De 181 stuks die onder de inkoopprijs van € 30 zijn verkocht,
    zijn óf verkeerd geprijsde panelen óf stalen met een verkeerde variantnaam. In beide gevallen
    is het een probleem: in het eerste geval verlies per order, in het tweede een marge die niet
    te meten is.

### De getallen die nog ontbreken

16. **Wat levert een aangevraagd staal later op?** Van de klanten met een staalorder: welk
    percentage kocht binnen 90 en 180 dagen betaald, en voor hoeveel? Zonder dat getal is een
    negatieve winst per advertentie geen bewijs dat de advertentie waardeloos is — alleen dat hij
    zich binnen 30 dagen niet terugbetaalt. Dit is niet uit ShopifyQL te halen
    (`customer_type` bestaat daar niet) en vraagt een analyse op orderniveau per klant.
17. **Is € 30 inkoop de prijs voor élk paneel?** De gemiddelde verkoopprijs loopt van € 6,09 tot
    € 239,60 per stuk en de maten verschillen (280×122, 280×60, 280×366). Eén inkoopprijs voor
    alles maakt de marge per advertentie grover dan nodig.

### Wat dit onderzoek niet kan zeggen

Geen van deze cijfers zegt welk deel van de omzet ook zonder advertenties was gekomen. Dat vraagt
een test waarin een deel van het bereik bewust geen advertenties ziet (geo-holdout of een
conversion-lift-studie bij Meta). Door de korte periode van 30 dagen verschuift bovendien één grote
order de winst van een advertentie merkbaar: *zakelijk verbouwen* haalt zijn winst uit een handvol
orders. Lees de uitschieters met die korte periode in gedachten.

## 7. Veiligheid

Tijdens dit onderzoek is uitsluitend gelezen. Er is niets gewijzigd in: Meta Ads, Google Ads,
Performance Max, Shopping, Merchant Center, productfeeds, GA4, pixels, conversietracking,
landingspagina's, URL's, het live Shopify-theme of het development-theme. Er zijn geen claims over
certificeringen, brandklassen, akoestiek, levertijden, voorraad, reviews, projecten of referenties
gebruikt of verzonnen. De enige niet-gemeten getallen in dit rapport zijn de twee die PureDeco zelf
heeft opgegeven: € 30 inkoop per paneel, en stalen zonder winst.
