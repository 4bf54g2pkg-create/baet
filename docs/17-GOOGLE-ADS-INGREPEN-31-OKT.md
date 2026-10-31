# Google Ads — ingrepen 31 oktober 2026

Uitgevoerd na expliciet akkoord. Alle wijzigingen zijn teruggelezen uit Google
en hieronder met hun campagne-id vastgelegd, zodat elke stap terug te draaien is.

## Wat is er gewijzigd

### 1. Merk-uitsluitingen in Search | Wandpanelen (22381603154)

Toegevoegd op campagneniveau:

| Zoekwoord | Matchtype |
|---|---|
| `puredeco` | PHRASE |
| `pure deco` | PHRASE |

**Waarom.** Er stonden al uitsluitingen `puredeco` en `pure deco` als **EXACT**.
Daardoor glipte de term `pure deco wandpanelen` (drie woorden, dus geen exacte
match) alsnog door naar de generieke campagne. Op 30 oktober kostte die term
3 klikken / € 2,34 = € 0,78 per klik, terwijl dezelfde zoekopdracht in de
brandcampagne € 0,45 per klik kostte. Met matchtype PHRASE is dat dicht.

**Terugdraaien:** `remove_negative_keywords` op campagne 22381603154.

### 2. Brandcampagnes samengevoegd

| Campagne | Id | Voor | Na |
|---|---|---|---|
| Brand \| PureDeco Protection | 24294113464 | ENABLED, geo = NL | **ENABLED, geo = NL + BE** |
| Brand \| PureDeco Protection NL-BE | 24285823800 | ENABLED, geo = NL + BE | **PAUSED** |

Uitvoeringsvolgorde bewust: eerst België toegevoegd aan 24294113464, daarna
24285823800 gepauzeerd. Zo was er geen moment zonder Belgische merkdekking.

De LANGUAGE- en DEVICE-criteria van 24294113464 zijn ongemoeid; alleen de
locatieset is vervangen (Google's `set_campaign_geo_targeting` vervangt de
volledige set, dus Nederland is expliciet meegestuurd).

**Terugdraaien:** `enable_campaign` op 24285823800 en
`set_campaign_geo_targeting` op 24294113464 terug naar alleen 2528.

## Twee correcties op mijn eigen advies

**De reden die ik voor samenvoegen gaf, was fout.** Ik stelde dat de twee
brandcampagnes tegen elkaar opbieden. Dat doet Google niet: binnen één account
laat Google per zoekopdracht alleen de campagne met de hoogste Ad Rank meedoen.
Er was dus **geen** CPC-opdrijving. De totale merkkosten bevestigen het —
€ 5,41 → € 5,97 → € 5,28 per dag over 28/29/30 oktober, vlak. De werkelijke
winst van samenvoegen is één budget en één geconcentreerd conversiesignaal voor
de biedautomaat, niet een directe besparing.

**De conversieverdeling was geen geldige keuzebasis.** Over 30 dagen stond
24294113464 op 11 conversies / € 1.474,50 uit € 47,26 en 24285823800 op
8 conversies / € 842,65 uit € 54,54. Omdat Google per zoekopdracht één van de
twee kiest, is "wie de order verdiende" grotendeels wie die veiling won. De
overblijvende campagne erft de zoekopdrachten van de ander.

Wat de keuze wél bepaalde: 24294113464 had het budget dat bij de werkelijke
merkvraag past (€ 5/dag tegen ~€ 5,3/dag feitelijke kosten), terwijl
24285823800 op € 2,50/dag stond en na samenvoeging budgetgelimiteerd zou raken.

## Wat ik 30 oktober niet kon verklaren

De sprong naar 7 staalorders op 30 oktober (negen dagen daarvoor maximaal 4,
gemiddeld 3,00 per dag) is uit de Google-data niet te herleiden:

- Budgetten identiek op 28, 29, 30 en 31 oktober.
- Geen nieuwe campagnes of advertentiegroepen.
- De drie advertentiegroepen die op 29 oktober 16:44 zijn heropend leverden
  op 30 oktober samen **0 klikken**: Japandi 2 vertoningen, Ruimtegericht 5,
  Hout 0.

Het bereik van Search verbreedde wel (17 → 31 → 43 unieke zoektermen over
28/29/30 oktober) en de nieuwe zoekwoorden horen bij precies die groepen, maar
zonder klikken kunnen ze de staalorders niet hebben veroorzaakt. Van de 7
stalen kwamen er 2 via een Google-landingspagina, 1 via de Facebook-app,
2 direct en 2 onbekend — breed, niet Google-specifiek.

Volgens de eigenaar is op 30 oktober het PMax-budget verhoogd en zijn de
groepen Japandi/Hout aangezet. De budgetverhoging is in de Windsor-data van
28 t/m 31 oktober niet terug te zien (PMax staat op alle vier dagen op € 15);
dat blijft een open punt.

## Openstaand, niet uitgevoerd

| Voorstel | Status |
|---|---|
| `marmerlook` / `marble` naar Shopping of eigen groep (CPC € 1,50 → ± € 0,15) | niet goedgekeurd |
| PMax drie dagen ongemoeid laten en dan beoordelen | ter beoordeling |

PMax-levering is sterk teruggevallen: 3.960 vertoningen (29 okt) → 312 (30 okt)
→ 318 (31 okt), met € 1,74 kosten op 31 oktober tegen een budget van € 15.
