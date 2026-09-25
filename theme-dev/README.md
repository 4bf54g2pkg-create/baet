# PUREDECO — LUXURY B2B — DEVELOPMENT (theme 194359853322)

Bronbestanden van het development-theme. **Het live theme (Hyper, 188874326282)
wordt hier nooit door geraakt.**

## Status per bestand

| Bestand | Staat in dev-theme | Toelichting |
|---|---|---|
| `assets/puredeco-design-system.css` | ✅ **gedeployd** | Nieuw. Designsysteem-laag. |
| `layout/theme.liquid` | ✅ **gedeployd** | P0 JS-fixes, laadt designsysteem. |
| `snippets/samita-custom.liquid` | ✅ **gedeployd** | AVG: console.log verwijderd. |
| `sections/header-group.json` | ✅ **gedeployd** | |
| `sections/footer-group.json` | ✅ **gedeployd** | |
| `sections/overlay-group.json` | ✅ **gedeployd** | |
| `templates/collection.json` | ✅ **gedeployd** | H1 + kruimelpad actief. |
| `templates/page.btbcta.json` | ⚠️ **deels** | Geüpload, maar `heading_tag` is door Shopify verwijderd — zie volgorde hieronder. |
| `sections/slideshow.liquid` | ⛔ **nog pushen** | Definieert `heading_tag` + tweede CTA. |
| `templates/index.json` | ⛔ **nog pushen** | Nieuwe homepage met h1. |
| `config/settings_data.json` | ⛔ **nog pushen** | Kleurenpalet + typografie. |
| `snippets/product-information-blocks.liquid` | ⛔ **nog pushen** | P0 PDP-fixes. |
| `templates/product.json` | ⛔ **nog pushen** | Dode link + demo-content. |

## Pushen — LET OP DE VOLGORDE

Shopify valideert sectie-instellingen tegen het schema van de sectie en
**verwijdert onbekende instellingen zonder foutmelding**. `slideshow.liquid`
moet daarom vóór `index.json` en `page.btbcta.json`.

```bash
shopify theme push --theme 194359853322 \
  --only sections/slideshow.liquid \
  --only snippets/product-information-blocks.liquid \
  --only config/settings_data.json

shopify theme push --theme 194359853322 \
  --only templates/index.json \
  --only templates/page.btbcta.json \
  --only templates/product.json
```

Controleer daarna dat de h1 terugkomt:
`templates/index.json` → hero-slide → `heading_tag: "h1"`.

## Nooit doen
- `--theme 188874326282` (= live) of `shopify theme publish`.
