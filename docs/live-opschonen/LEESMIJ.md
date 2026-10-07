# "Thuispaneel" uit het live thema (Hyper) halen

Op de live site is "Thuispaneel" voor bezoekers nergens zichtbaar (alle 78 sitemap-pagina's doorzocht).
Het staat nog op 8 plekken in de themacode: 4× in uitgeschakelde secties en 4× als standaardtekst.
Claude kan het live thema niet bewerken (geblokkeerd), dus dit doe je zelf in ca. 5 minuten.

Shopify admin → Online Store → Themes → Hyper (live) → ⋯ → Edit code. Per bestand: alles selecteren, plakken, Save.

| Bestand in Shopify | Plak de inhoud van |
|---|---|
| sections/topbar.liquid | sections-topbar.liquid (regel 564: e-mail → info@puredeco.nl) |
| sections/showroom-partner.liquid | sections-showroom-partner.liquid (3× Thuispaneel → PureDeco) |
| templates/page.showroom.json | templates-page.showroom.json (verborgen slideshow met link naar thuispaneel.nl verwijderd) |
| templates/page.verkoopparters.json | templates-page.verkoopparters.json (verborgen sectie 'Showroom partner' met Thuispaneel-teksten verwijderd) |

Alternatief voor de twee templates: in de theme-editor (Customize) op de pagina Showroom de verborgen sectie "Slideshow" verwijderen
en op de pagina Verkoopparters de verborgen sectie "Showroom partner" verwijderen.

Daarnaast (geen Thuispaneel, wel netjes): in snippets/menu-drawer.liquid regels 124 en 137
`https://puredeco-3.myshopify.com/pages/` vervangen door `/pages/` (mobiel menu: Showroomafspraak en Gratis advies).

In H1-test is alles al opgeschoond.
