# Wijzigingslog 2 november 2026

## Mobiel menu: "Wandpanelen" verwijst nu direct naar de collectie

**Uitgevoerd na expliciet akkoord ("Route A, haal subitems weg").**

### Wat er is gewijzigd

Navigatiemenu `pd-mobiel` (`gid://shopify/Menu/317420699914`): de **tien
subitems** onder "Wandpanelen" zijn verwijderd. Het item zelf blijft
`/collections/wandpanelen`.

Verwijderd: Hout · Beton ciré · Travertin · Japandi · Leer · Art ·
Doorlopend marmer · Akupanelen · Accessoires · Alle decors

Onaangeroerd: de zeven andere hoofditems (Installatie, Inspiratie, Projecten,
Studio Herwen, Samples, Veelgestelde vragen, Contact) en het **desktopmenu**
`pd-hoofdmenu`.

### Waarom dit werkt

`snippets/menu-drawer.liquid` kiest de vorm van een menu-item zo:

```liquid
{%- if link.links != blank or enable_mega_menu -%}
  {%- render 'menu-drawer-details' -%}   → <summary> zónder href
{%- else -%}
  <a href="{{ link.url }}">              → directe link
{%- endif -%}
```

Zolang er subitems waren, werd de kop een `<summary>` zonder enkele `<a href>`.
Tikken kon dan alleen openklappen. Geen bug — zo is het Hyper-thema gebouwd.

### Waarom een menuwijziging en geen codewijziging

Dit is **winkeldata**, geen themacode. Daardoor werkt het direct op het live
thema én op elke themakopie die later wordt gepubliceerd. Een codewijziging in
`menu-drawer-details.liquid` had in elke kopie opnieuw doorgevoerd moeten worden;
er zijn inmiddels elf thema's.

### Wat de bezoeker niet kwijtraakt

De collectiepagina toont op mobiel al een eigen navigatie (`pc-nav`) met negen
links: Alle wandpanelen, Houten wandpanelen, Naadloze wandpanelen, Japandi,
Leerlook, Art, Marmerlook, Akupanelen, Accessoires. Het submenu was daarvan een
dubbeling.

**Wel kwijt uit het mobiele menu:** de snelkoppelingen naar Beton ciré
(`/products/concrete-smoke-691-betonlook`) en Travertin
(`/products/wandpaneel-travertine-ivory-851`). Dat zijn producten, geen
collecties, en ze stonden niet in `pc-nav`. Beide blijven vindbaar in de
collectie Wandpanelen zelf.

### Verificatie (echte browser, iPhone 13)

| Controle | Voor | Na |
|---|---|---|
| Vorm van het item | `<summary>`, `href: null` | `<a href="/collections/wandpanelen">` |
| Na de tik | submenu klapte open | `/collections/wandpanelen` |
| H1 op de bestemming | — | "Wandpanelen met bamboekern" |
| Desktop `pd-hoofdmenu` | 11 sublinks | 11 sublinks, ongewijzigd |

`menuUpdate` gaf `userErrors: []` en alle acht hoofditems terug.

**Backup:** `backups/pd-mobiel-VOOR-2026-11-02.json` — de volledige oude
structuur met alle item-ID's, zodat de subitems in één handeling terug te
zetten zijn.

---

## Belangrijk: de themasituatie is veranderd sinds 31 oktober

| Thema | Rol | Bijgewerkt |
|---|---|---|
| **H2 kopie 1 nov (chat WhatsApp)** · 196032332042 | **MAIN (live)** | 1 nov 22:23 |
| H3 kopie 2 nov (Black Friday) · 196045603082 | ongepubliceerd | 2 nov 09:34 |
| Hyper kopie 5 okt (H1-test) · 194824929546 | ongepubliceerd | 2 nov 09:13 |
| Hyper origineel · 188874326282 | ongepubliceerd | 1 nov |

**De PureDeco-themalijn staat live.** Gemeten op de homepage:

| | 31 okt (Hyper) | 2 nov (H2) |
|---|---|---|
| `<title>` | `PureDeco` | `Wandpanelen met bamboekern \| Houtlook & naadloos \| PureDeco` |
| HTML-gewicht | 1.020.688 bytes | **452.136 bytes** |
| `puredeco-premium.css` | niet geladen | geladen |

En op `/collections/wandpanelen` staat nu `<h1 class="pc-head__h">Wandpanelen met
bamboekern</h1>` — waar eerder **nul** H1-elementen stonden.

**Gevolg voor het auditrapport (`docs/18`):** dat is een audit van H1-Kopie, dat
inmiddels twee generaties achterloopt op wat live draait. De bevindingen over
code en structuur gelden grotendeels nog, maar de nulmetingen van het live thema
zijn achterhaald. Bij een volgende audit is H2 (of de dan gepubliceerde kopie)
het juiste onderwerp.
