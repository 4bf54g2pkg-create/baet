# ads/ — advertentie-ROI

`dashboard/index.html` is de broncode van de dashboardpagina die in het ROI-dashboard staat
(https://claude.ai/artifact/9PVzn4wwdwqcGsVE5wrn9Y). De pagina leest negen bronnen: acht live over de laatste 30 dagen
Meta Ads per advertentie en per dag, Google Ads per campagne, per advertentiegroep en per dag
(via GA4), GA4 per bron/medium, de Shopify-verkoopadministratie per orderbron en de Shopify-orderregels (waaruit de brutomarge en de staalverhouding worden gerekend), plus een opgeslagen cohortbestand met de staalaanvragers en hun latere orders.

Elke bron draait met de eigen toegang van de lezer; iedereen die het dashboard opent, voert
die live vragen zelf uit tegen de gekoppelde Windsor.ai- en Shopify-connectoren.

De analyse en het advies staan in `docs/02-ADVERTENTIE-ROI.md`.

Er is in dit onderdeel niets gewijzigd aan advertentieaccounts, conversietracking, GA4,
pixels, feeds of het Shopify-theme — uitsluitend gelezen.

Het cohortbestand `cohort-staalaanvragers.json` is een opgeslagen momentopname: het vraagt de
volledige orderhistorie in meerdere opvragingen, wat een dashboardpagina niet in een keer kan doen.
Iedereen die het dashboard kan openen ziet die opgeslagen rijen, met klantnummers maar zonder namen
of adressen.
