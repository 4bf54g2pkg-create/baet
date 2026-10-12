# ads/ — advertentie-ROI

`dashboard/index.html` is de broncode van de dashboardpagina die in het ROI-dashboard staat
(https://claude.ai/artifact/9PVzn4wwdwqcGsVE5wrn9Y). De pagina leest zeven live bronnen:
Meta Ads per advertentie en per dag, Google Ads per campagne, per advertentiegroep en per dag
(via GA4), GA4 per bron/medium, en de Shopify-verkoopadministratie per orderbron.

Elke bron draait met de eigen toegang van de lezer; iedereen die het dashboard opent, voert
die zeven vragen zelf uit tegen de gekoppelde Windsor.ai- en Shopify-connectoren.

De analyse en het advies staan in `docs/02-ADVERTENTIE-ROI.md`.

Er is in dit onderdeel niets gewijzigd aan advertentieaccounts, conversietracking, GA4,
pixels, feeds of het Shopify-theme — uitsluitend gelezen.
