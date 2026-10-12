# Advertentie-ROI per advertentie — Meta Ads en Google Ads

Periode: laatste 90 dagen (voortschrijdend). Alle cijfers komen live uit het Meta-advertentieaccount
PureDeco (via Windsor.ai), de GA4-property PureDeco en de Shopify-administratie van puredeco.nl.
Er is in dit onderzoek niets gewijzigd aan advertentieaccounts, conversietracking, GA4, pixels,
feeds of het live Shopify-theme.

Dashboard: https://claude.ai/artifact/9PVzn4wwdwqcGsVE5wrn9Y
Broncode van de dashboardpagina: `ads/dashboard/index.html`

---

## 1. Wat er is uitgezocht en waar de cijfers vandaan komen

| Vraag | Bron | Granulariteit |
|---|---|---|
| Wat kost elke Meta-advertentie en wat levert die volgens Meta op? | Meta Ads via Windsor.ai | per advertentie |
| Wat kost elke Google Ads-campagne en wat levert die op? | GA4 (`advertiser_ad_cost`, gekoppelde Google Ads-kosten) | per campagne en per advertentiegroep |
| Wat boekt de winkel werkelijk per orderbron? | Shopify Analytics (`FROM sales`) | per verwijzer |
| Hoeveel orders ziet de webanalyse per kanaal? | GA4, laatste klik | per bron/medium |

Google Ads is **niet** als eigen bron gekoppeld (niet in Windsor.ai, en de Supermetrics-proefperiode is
op 9 oktober verlopen). Daardoor loopt alles van Google via GA4. Gevolg: de granulariteit stopt bij
advertentiegroep; per advertentie-asset of advertentietekst is niet te meten zonder directe
Google Ads-koppeling. Voor Meta is per advertentie wél beschikbaar.

## 2. Meta Ads per advertentie (90 dagen)

| Advertentie | Spend | Clicks | CPC | Conv. | €/conv. | Waarde (Meta) | Waarde/conv. | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| zakelijk verbouwen | 1.225,01 | 5.052 | 0,24 | 50 | 24,50 | 4.088,90 | 81,78 | **3,34** |
| Marmerlook va 125 | 1.017,42 | 4.454 | 0,23 | 45 | 22,61 | 3.251,86 | 72,26 | **3,20** |
| diaan creator 1 | 954,58 | 3.618 | 0,26 | 38 | 25,12 | 628,83 | 16,55 | 0,66 |
| diaan creator 2 | 641,68 | 2.346 | 0,27 | 22 | 29,17 | 252,90 | 11,50 | 0,39 |
| Nieuwe wandpanelen | 387,50 | 1.364 | 0,28 | 17 | 22,79 | 551,08 | 32,42 | 1,42 |
| Video led profiel japans | 142,04 | 555 | 0,26 | 2 | 71,02 | 11,90 | 5,95 | 0,08 |
| video 3 | 90,44 | 388 | 0,23 | 2 | 45,22 | 12,90 | 6,45 | 0,14 |
| **Totaal** | **4.458,67** | **17.777** | **0,25** | **176** | **25,33** | **8.798,37** | **49,99** | **1,97** |

Alles zit in één campagne (*Puredeco - onfluence*) met twee advertentiesets: *zakelijke doelgroep*
(één advertentie) en *Video's* (zes advertenties).

## 3. Google Ads per campagne (90 dagen, GA4)

| Campagne | Kosten | Clicks | CPC | Trans. | €/trans. | Productomzet | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|
| PMAX - Campagne - PureDeco.nl | 999,51 | 1.688 | 0,59 | 11 | 90,86 | 1.682,51 | 1,68 |
| Search \| Concurrenten | 813,99 | 252 | **3,23** | 2 | 407,00 | 0,00 | **0,00** |
| Search \| Wandpanelen | 353,77 | 326 | 1,09 | 5 | 70,75 | 0,00 | **0,00** |
| PMax_NL [[All products]] (Adscale) | 350,75 | 1.379 | 0,25 | 16 | 21,92 | 721,45 | 2,06 |
| Brand (Adscale Magic Ads) | 141,62 | 432 | 0,33 | 8 | 17,70 | 0,00 | **0,00** |
| Shopping \| Bamboepanelen | 72,99 | 607 | 0,12 | 4 | 18,25 | 0,00 | **0,00** |
| Brand \| PureDeco Protection | 29,54 | 112 | 0,26 | 5 | 5,91 | 431,70 | 14,61 |
| Brand \| PureDeco Protection NL-BE | 18,65 | 80 | 0,23 | 2 | 9,33 | 361,60 | 19,39 |
| **Totaal** | **2.780,82** | **4.876** | **0,57** | **53** | **52,47** | **3.197,26** | **1,15** |

Per advertentiegroep valt vooral op: **Thuispaneel** binnen *Search | Concurrenten* kostte € 557,99
voor 135 clicks — € 4,13 per klik — met 2 transacties en € 0,00 productomzet.

De omzet van Google Ads viel in 90 dagen op **5 dagen**: € 191,58 · € 529,87 · € 1.682,51 · € 361,60
· € 431,70. Op de overige 85 dagen werd er wel € 20 tot € 55 per dag uitgegeven en kwam er
€ 0,00 productomzet uit. De ROAS van 1,15 rust dus op een handvol orders, niet op een stabiel patroon.

## 4. De kern: wat beide platforms een "aankoop" noemen

Drie bronnen, dezelfde Meta-advertenties, dezelfde 90 dagen:

| Bron | Orders | Omzet | Toewijzing |
|---|---:|---:|---|
| Meta Ads Manager | 176 | 8.798,37 | 7 dagen na klik, 1 dag na weergave, over apparaten |
| GA4 laatste klik | 78 | 161,96 | laatste klik van de sessie |
| Shopify administratie | 71 | **185,00** | verwijzer van de order, brutoproductomzet |

Over het **aantal** orders zijn GA4 en Shopify het eens (78 tegen 71). Over de **waarde** niet:
Meta claimt 48× zoveel als de winkel boekt. De verklaring is aantoonbaar in de administratie:

| Verwijzer | Kanaal | Orders | Brutoproductomzet | Verzendkosten |
|---|---|---:|---:|---:|
| facebook | social | 22 | 185,00 | 170,98 |
| instagram | social | 34 | **0,00** | 182,86 |
| instagram | (leeg) | 15 | **0,00** | 79,54 |

Negenenveertig Instagram-orders in 90 dagen met **nul** productomzet en wel verzendkosten: dat zijn
orders waarin alleen verzendkosten zijn betaald — de gratis stalen. Diezelfde orders tellen in Meta
mee als `Purchase` met de verzendkosten als waarde. Op 52 van de 70 dagen met minstens één
toegeschreven aankoop lag de gemiddelde waarde per aankoop **onder € 10**; dat betreft 110 van de
176 aankopen (63%). Vrijwel al die waarden zijn exacte veelvouden van € 5,95 (tot 27 augustus) of
€ 6,95 (daarna).

Hetzelfde geldt bij Google: élke transactie uit *Search | Wandpanelen*, *Search | Concurrenten*,
*Shopping | Bamboepanelen* en *Brand (Adscale)* — 19 van de 53 — had € 0,00 productomzet.

**Consequentie:** de biedalgoritmes van Meta en Google optimaliseren op het aanvragen van gratis
stalen, niet op verkoop. Dat is geen attributieruzie maar een meetfout met een stuurgevolg.

## 5. Van ROAS naar ROI

ROAS is omzet gedeeld door advertentiekosten; dat is geen winst. Break-even ROAS = 1 / brutomarge:

| Brutomarge | Break-even ROAS |
|---:|---:|
| 30% | 3,33 |
| 40% | 2,50 |
| 50% | 2,00 |
| 60% | 1,67 |

De werkelijke brutomarge van PureDeco is niet bekend en is in dit dashboard **niet verzonnen**: de
break-evenlijn staat op 2,50 als expliciete aanname van 40%. Op Meta's eigen cijfers halen bij 40%
marge alleen *zakelijk verbouwen* (3,34) en *Marmerlook va 125* (3,20) break-even. Bij 30% marge
haalt geen enkele advertentie het.

Totale advertentiekosten over 90 dagen: € 7.239,49. Totale winkelomzet in dezelfde periode:
€ 31.211,96. Advertentiekosten zijn dus 23,2% van de omzet.

## 6. Advies

### Nu stoppen of pauzeren — € 2.642,73 per 90 dagen (circa € 880 per maand)

1. **Search | Concurrenten** — € 813,99, € 3,23 per klik, € 0,00 productomzet. De advertentiegroep
   *Thuispaneel* alleen kost € 4,13 per klik. Bieden op merknamen van concurrenten tegen vier euro
   per klik zonder één betaalde order is niet te verdedigen op deze schaal.
2. **diaan creator 1 + diaan creator 2** — samen € 1.596,26 (36% van de Meta-spend) voor € 881,73
   aan geclaimde waarde; ROAS 0,66 en 0,39 op Meta's eigen, te gunstige cijfers. Waarde per conversie
   € 16,55 en € 11,50: vrijwel uitsluitend stalen.
3. **video 3** en **Video led profiel japans** — € 232,48 voor vier conversies van € 5,95 en € 6,45.
   Te klein om van te leren en op nul rendement.

### Houden en opschalen

4. **zakelijk verbouwen** (ROAS 3,34, waarde per conversie € 81,78) en **Marmerlook va 125**
   (3,20, € 72,26). Dit zijn precies de twee advertenties met de hoogste waarde per conversie: ze
   trekken kopers, niet stalenaanvragers. Verhoog hier stapsgewijs (20–30% per week, niet in één
   sprong) en meet of de waarde per conversie op peil blijft. Zakt die naar de verzendkostengrens,
   dan is de schaalgrens bereikt.
5. **Brand | PureDeco Protection** en **NL-BE** — € 48,19 samen voor € 793,30 omzet. Dit is de enige
   plek met een ROAS boven 10 en hij staat vrijwel droog. Let op: merkzoekwoorden kannibaliseren voor
   een deel het organische resultaat, dus de winst is kleiner dan de ROAS suggereert. Test met een
   verdubbeld budget en vergelijk het totaal van betaald plus organisch op het merk, niet alleen de
   campagne.
6. **PMax_NL (Adscale)** haalt met € 350,75 een ROAS van 2,06 en PMAX - Campagne - PureDeco.nl met
   € 999,51 een 1,68. De kleine haalt meer per euro. Voordat er budget verschuift: beide draaien op
   dezelfde productfeed en concurreren mogelijk met elkaar. Controleer de overlap voordat je de
   grote terugschroeft.

### Eerst de meting repareren — dit gaat vóór elke budgetbeslissing

7. **Scheid de stalenaanvraag van de aankoop.** Zolang een order van € 0,00 product plus € 6,95
   verzendkosten als `Purchase` wordt doorgegeven, leren beide platforms dat een stalenaanvraag het
   doel is. Voorstel: stuur voor orders die alleen stalen bevatten een eigen gebeurtenis (bij Meta
   een `Lead` of `SubmitApplication`, bij Google een aparte conversieactie die *niet* meetelt voor
   biedingen) en houd `Purchase` voor betaalde orders. Zet daarna Meta op conversiewaarde in plaats
   van conversies, en Google op de aankoopconversie alleen.
   *Dit raakt conversietracking. Ik voer hier niets uit zonder jouw expliciete toestemming; het is
   een voorstel met een uitvoeringsplan, geen uitgevoerde wijziging.*
8. **Zet UTM's op alle advertentielinks.** Van de 385 orders in 90 dagen hebben 168 orders
   (€ 20.068,04) geen enkele verwijzer in Shopify. Dat is 44% van de orders en 64% van de omzet
   zonder herkenbare bron. Zonder UTM's blijft elke ROI-discussie een schatting.
9. **Herstel de zelfverwijzingen.** Shopify ziet 49 orders (€ 3.092,13) met verwijzer `puredeco`,
   9 met `f9yvx9-zm` (de myshopify-domeinnaam) en 1 met `mollie`. Dat zijn orders waarbij het eigen
   domein of de betaalpagina als bron wordt geregistreerd — een configuratiefout die bron-toewijzing
   vervuilt.
10. **Stuur de echte orderwaarde server-side door** (Shopify → Meta Conversions API, met order-id
    voor ontdubbeling). Dan optimaliseert Meta op omzet in plaats van op pixelwaarde.

### De getallen die nog ontbreken

11. **Wat levert een aangevraagd staal later op?** Dat is de enige manier om te beoordelen of
    staal-gestuurde advertenties goed of slecht zijn. Nodig: van de klanten die een staalorder
    plaatsten, hoeveel procent kocht binnen 90 en 180 dagen een betaalde order, en voor hoeveel.
    Met dat percentage en de brutomarge wordt elke ROAS hierboven een echt ROI-getal. Dit is niet
    uit ShopifyQL te halen (`customer_type` bestaat daar niet); het vraagt een analyse op
    orderniveau per klant. Dat kan ik maken zodra je het zegt.
12. **Wat is de brutomarge per materiaalgroep?** Zonder dat getal is de break-evenlijn een aanname.

### Wat dit onderzoek niet kan zeggen

Geen van deze cijfers zegt welk deel van de omzet ook zonder advertenties was gekomen. Dat vraagt een
test waarin een deel van het bereik bewust geen advertenties ziet (geo-holdout of een
conversion-lift-studie bij Meta). Tot die tijd is per-advertentie-ROI een signaal om budget op te
verschuiven, geen afrekening.

## 7. Veiligheid

Tijdens dit onderzoek is uitsluitend gelezen. Er is niets gewijzigd in: Meta Ads, Google Ads,
Performance Max, Shopping, Merchant Center, productfeeds, GA4, pixels, conversietracking, landings-
pagina's, URL's, het live Shopify-theme of het development-theme. Er zijn geen claims over
certificeringen, brandklassen, akoestiek, levertijden, voorraad, reviews, projecten of referenties
gebruikt of verzonnen.
