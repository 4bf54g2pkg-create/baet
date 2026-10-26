# Oorzaak Meta-stilstand + meting golf 1 — 26 oktober 2026

Windsor staat weer open (facebook, google_ads, googleanalytics4). Hieronder de
cijfers die ik op 26 oktober niet kon lezen, en de oorzaak van de Meta-stilstand.

---

## 1. Oorzaak gevonden: de Meta-rekening is niet betaald

Accountgegevens van advertentieaccount 1266095837740836 (PureDeco):

| Veld | Waarde |
|---|---|
| `account_status` | **UNSETTLED** |
| `spend_cap` | 0 |
| `amount_spent` | 1.896.682 (= € 18.966,82 sinds de start) |

[FEIT] **`UNSETTLED` betekent dat er een openstaand, onbetaald bedrag op het
advertentieaccount staat.** Meta stopt de levering tot dat bedrag is voldaan.

[FEIT] `spend_cap` staat op 0. Dat betekent **geen bestedingsplafond**. Een bereikt
budgetplafond is dus uitgesloten — dat was een van mijn drie hypotheses van vanmorgen
en die valt hiermee af. Een accountblokkade of afgekeurde advertenties valt ook af:
die geven een andere status (`DISABLED`).

### Wanneer het misging

Dagelijkse Meta-kosten, campagne "Puredeco - onfluence" (de enige actieve campagne):

| Dag | Kosten | Klikken | Bereik |
|---|---:|---:|---:|
| 19 okt | € 60,16 | 345 | 4.689 |
| 20 okt | € 56,81 | 290 | 4.036 |
| 21 okt | € 61,29 | 361 | 4.916 |
| 22 okt | € 58,96 | 269 | 4.644 |
| **23 okt** | **€ 35,55** | 169 | 2.706 |
| 24 okt | **—** | — | — |
| 25 okt | **—** | — | — |
| 26 okt | **—** | — | — |

De levering is **in de loop van 23 oktober gestopt** (€ 35,55 tegen een gemiddelde van
€ 60,19) en staat sindsdien volledig stil. Dat sluit exact aan op de Shopify-sessies:
Facebook nul vanaf 24 oktober, Instagram vanaf 25 oktober.

### Wat je moet doen

Meta Ads Manager → **Facturering** (Billing). Daar staat het openstaande bedrag.
Betaal het en controleer het betaalmiddel: een `UNSETTLED`-status komt vrijwel altijd
van een afgewezen afschrijving — verlopen kaart, bereikte kaartlimiet of een
geweigerde automatische incasso. Zodra de betaling binnen is, gaat de levering
doorgaans binnen enkele uren weer aan; de campagne zelf hoeft niet opnieuw opgezet.

---

## 2. Correctie op mijn dag-3-meting

Google-kosten per dag:

| Dag | Google | Meta | waarvan Brand (Google) |
|---|---:|---:|---:|
| basis 7–20 okt | € 40,25 | € 60,19 | — |
| 21 okt (ingreep) | € 34,84 | € 61,29 | € 2,94 |
| 22 okt | € 21,73 | € 58,96 | € 5,16 |
| 23 okt | € 22,96 | € 35,55 | € 3,94 |
| 24 okt | € 14,59 | **€ 0** | € 0,63 |
| 25 okt | € 15,29 | **€ 0** | € 1,52 |
| 26 okt (deel) | € 3,30 | € 0 | € 2,11 |

Over 22–25 oktober komt Google uit op € 18,64/dag — slechts 8% boven mijn
oorspronkelijke voorspelling van € 17,31. Dat ziet eruit als een betere uitkomst
dan de € 22,35/dag die ik op 24 oktober rapporteerde.

**Dat is schijn.** Vanaf 24 oktober stond Meta stil, en dat drukt de Google-kosten mee
naar beneden. Het duidelijkst bij de Brand-campagnes: € 4,01/dag over 21–23 oktober
tegen € 1,07/dag over 24–25 oktober. Minder Meta-bereik betekent minder mensen die
daarna op "puredeco" zoeken, dus minder brandklikken.

[FEIT] **Het zuivere meetvenster voor golf 1 is daarom alleen 22–23 oktober:
€ 40,25 → € 22,35/dag, een daling van 44%.** Mijn meting van dag 3 was de juiste;
de lagere cijfers van 24–25 oktober zijn vervuild door de Meta-stilstand.

De kannibalisatiehypothese (PMAX nam vraag weg bij de eigen Search- en
Shopping-campagnes) blijft daarmee staan voor 22–23 oktober, maar is **niet te
toetsen** zolang Meta stilstaat. Dat schuift op naar de meting ná het herstel.

---

## 3. Google-conversies na de ingreep — richting goed, bewijs ontbreekt

22–25 oktober: € 74,56 kosten, 5 conversies, € 634,80 conversiewaarde incl btw
(= € 524,63 ex btw). ROAS ex btw **7,04** tegen een break-even van 1,43 en een
basis van 1,24.

Drie redenen om dit niet als bewijs te lezen:

1. De € 634,80 is **één order** (#2566, 24 oktober), toegeschreven aan
   Brand | PureDeco Protection — een merkcampagne vangt een order die er
   vermoedelijk ook zonder was gekomen.
2. De overige 4 conversies hebben **conversiewaarde € 0**: dat zijn staalorders.
3. De conversievertraging van Google is voor 24–26 oktober nog niet uitgewerkt.

Wel het vermelden waard: vier van de vijf conversies met waarde nul bevestigen
opnieuw dat `Aankoop` een staal van € 6,95 als volwaardige conversie meetelt.

---

## 4. Wat Meta en Google samen nu kosten en opleveren

| | basis 7–20 okt | 22–25 okt |
|---|---:|---:|
| Google | € 40,25/dag | € 18,64/dag |
| Meta | € 60,19/dag | € 23,63/dag |
| **Advertentiekosten** | **€ 100,44/dag** | **€ 42,27/dag** |
| Brutomarge (Shopify, 69,7%) | € 230,35/dag | € 319,51/dag |
| **Resultaat na advertentiekosten** | **€ 129,91/dag** | **€ 277,24/dag** |

[VERMOEDEN] Dit ziet eruit als een verdubbeling van het resultaat, maar het venster
is vier dagen lang en 68% van de omzet komt uit één order. Bovendien is een deel van
de "winst" geleend: de Meta-stilstand bespaart nu € 60/dag en halveert tegelijk de
staalinstroom, waarvan de paneelverkoop over twee tot zes weken komt. Die rekening
komt later.

---

## 5. De werkelijke les: Meta en Google zijn niet los te beoordelen

De Brand-kosten die wegvallen zodra Meta stopt (€ 4,01 → € 1,07/dag) zijn het harde
bewijs dat Meta vraag aanjaagt die Google vervolgens binnenhaalt. Meta's eigen ROAS
onderschat dus zijn waarde, en de ROAS van de Brand-campagnes overschat die van
henzelf — zij oogsten wat Meta heeft gezaaid.

Dat betekent: **Meta afrekenen op € 6,95-staalorders alleen is te streng.** Zodra de
betaling rond is en de levering herstelt, moet de volgende meting het staalcohort
volgen naar paneelomzet, niet naar staalomzet.

---

## 6. Volgende stappen

1. **Jij, vandaag:** openstaand bedrag betalen in Meta Ads Manager → Facturering,
   en het betaalmiddel vernieuwen.
2. **Ik, na herstel:** zeven dagen schoon meten met Meta én Google actief, inclusief
   de kannibalisatietoets die nu niet kan.
3. **Blijft open:** verlaten-afrekenpoging aanzetten in Shopify, de drie
   `Local actions` en `Clicks to call` op Secundair, en de SPF-controle voor fase 2
   van de opvolgaudit.
