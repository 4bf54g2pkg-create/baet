# Advertentie-ROI — dashboard en brondata

## Het dashboard

`https://claude.ai/artifact/9PVzn4wwdwqcGsVE5wrn9Y` — "Advertentierendement PureDeco".
De pagina staat hier als `dashboard/index.html` en in het artefact als `files/index.html`.

Het dashboard vergelijkt de **laatste 14 volledige dagen** met de **14 dagen daarvoor**. Die twee
vensters worden afgeleid uit de nieuwste dag in de Meta-dagreeks, die altijd tot en met gisteren
loopt. Vandaag telt dus nooit half mee, en de periodes schuiven automatisch mee met de kalender.

## Datasets

Alle acht querydatasets zijn live: ze lopen bij elke keer dat iemand het dashboard opent opnieuw,
met de toegang van die lezer zelf.

| Dataset | Bron | Venster |
|---|---|---|
| `shopify_dagen` | Shopify, ShopifyQL per dag | 30 dagen t/m vandaag |
| `shopify_bronnen` | Shopify, ShopifyQL per verwijzer per dag | 30 dagen t/m vandaag |
| `shopify_regels` | Shopify Admin API, 250 recentste orders met orderregels | — |
| `meta_ads_dagen` | Meta Ads via Windsor.ai, per advertentie per dag | 28 dagen t/m gisteren |
| `google_campagnes_14d` | GA4 via Windsor.ai, per campagne | 14 dagen t/m gisteren |
| `google_campagnes_28d` | GA4 via Windsor.ai, per campagne | 28 dagen t/m gisteren |
| `google_dagen` | GA4 via Windsor.ai, betaalde kanalen per dag | 28 dagen t/m gisteren |
| `ga4_kanalen_14d` | GA4 via Windsor.ai, per kanaalgroep | 14 dagen t/m gisteren |
| `staal_cohort` | Bijgevoegd bestand, handmatig bijgewerkt | 12 mei t/m 12 oktober 2026 |

De vorige Google-periode wordt berekend als het verschil tussen de reeks van 28 dagen en die van
14 dagen: Windsor kent geen venster met een verschuiving.

## Waar de cijfers vandaan komen

**Marge.** Uit de orderregels. Een regel vanaf €89 per stuk is een verkocht paneel, een regel tot
€7,50 een gratis staal, de rest accessoires. Kortingen op orderniveau worden proportioneel over de
regels verdeeld — zonder die stap valt de marge te hoog uit. Inkoopprijs €30 per paneel.

**Waarde van een staalaanvraag.** Doorkooppercentage × gemiddelde paneelomzet van een doorkoper ÷
btw × de brutomarge over de volle 28 dagen. Die 28-daagse marge is bewust gekozen: bij dertien
paneelorders per veertien dagen is één projectorder meer of minder al genoeg om de marge van één
periode flink te laten springen.

**Google per advertentie bestaat niet in dit dashboard.** De Windsor-connector `google_ads` is niet
gekoppeld en de Supermetrics-proefperiode verliep op 9 oktober 2026. Google staat op
campagneniveau, met kosten uit GA4. Die kostenbasis is gevalideerd: over 19 september tot 18
oktober sommeerde hij exact naar de accounttotalen in de Google Ads-export (€1.124,73 en 2.634
klikken).

## Het staalcohort

`cohort-staalaanvragers.json` — één rij per klant die ooit een gratis staal aanvroeg, met de datum
van die eerste staalorder, of er daarna panelen zijn gekocht, na hoeveel dagen en voor hoeveel
omzet. Opgebouwd uit de orders van 12 mei tot en met 12 oktober 2026; de bulk-import van 11 mei
2026 valt er bewust buiten.

Dit is een momentopname, geen live query: het opbouwen vraagt de volledige orderhistorie in
meerdere opvragingen, en dat kan een dashboardpagina niet bij elke keer openen doen. **Iedereen die
het dashboard kan openen, kan dit bestand lezen.** Er staan klantnummers in, geen namen of
adressen.

## Ruwe data

`raw/` staat in `.gitignore`: die bestanden bevatten klantnummers. De drie dumps die op 12 oktober
per ongeluk zijn gecommit, staan nog wel in de git-historie.

## De rapporten

| Bestand | Inhoud |
|---|---|
| `../docs/03-CMO-RAPPORT-14D.md` | Het managementrapport over de laatste 14 dagen |
| `../docs/04-DRAAIBOEK-7-DAGEN.md` | Klik-voor-klik uitvoering, met de volledige uitsluitingslijst |
| `../docs/05-OPVOLGFLOW-STALEN.md` | Teksten voor de opvolging van staalaanvragers |
| `../docs/02-ADVERTENTIE-ROI.md` | De eerdere 30-daagse analyse; de marge- en staalwaardecijfers daarin zijn achterhaald |
