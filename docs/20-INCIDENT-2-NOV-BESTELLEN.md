# Incident 2 november 2026 — "online bestellen niet mogelijk"

Aanleiding: klantmelding. Onderzoek uitgevoerd op het **live** thema
`H2 kopie 1 nov (chat WhatsApp)` (196032332042, assets onder `/t/10/`).
**Er is tijdens dit onderzoek niets gewijzigd.**

---

## 1. Bewezen defect: de vaste koopbalk sterft na één klik

### Wat er gebeurt

In `layout/theme.liquid` staat op twee plaatsen:

```js
document.body.classList.add("modal-show");
```

Eenmaal bij de AJAX-add-to-cart-handler, eenmaal op elke `.product-form__submit`.
**Nergens in het thema wordt die class weer verwijderd** — niet in `theme.js`,
niet in `cart.js`, niet in de paginacode. Geteld: 2× toegevoegd, 0× verwijderd.

In `assets/puredeco-premium.css` van H2 staat sinds 1 november deze regel:

```css
body.modal-show .pdh__bar,
html:has(cart-drawer[open]) .pdh__bar,
body.modal-show .pse-bar,
html:has(cart-drawer[open]) .pse-bar,
body.modal-show .pd-wa,
html:has(cart-drawer[open]) .pd-wa {
  transform: translateY(150%) !important;
  opacity: 0 !important;
  pointer-events: none !important;
}
```

En in `assets/theme.css` (het basisthema Hyper) staat:

```css
.body-no-scrollbar,.modal-show,.modal-showing,.search-open{overflow:hidden;...}
.modal-show button.product-samples-widget__trigger,.modal-show div#shopify-chat{display:none}
```

`modal-show` is de **eigen class van het modal-systeem van het thema**
(`theme.js`: `this.classes={show:"modal-show",showing:"modal-showing"}`). De
PureDeco-scripts zetten die class buiten dat systeem om op `<body>`, dus het
thema weet niet dat hij er weer af moet.

### Gemeten in een echte mobiele browser (iPhone 13, 390×844)

| | Vóór de klik | Na één klik op "In winkelwagen" |
|---|---|---|
| classes op `<body>` | (geen) | **`modal-show`** |
| `body` overflow | `visible` | `hidden` |
| `.pdh__bar` pointer-events | `auto` | **`none`** |
| `.pdh__bar` opacity | `1` | **`0`** |

Gevolg: de vaste koopbalk onderaan is na één klik **onzichtbaar en
onklikbaar** tot de pagina herladen wordt. Hetzelfde geldt voor de samplebalk
(`.pse-bar`), de WhatsApp-knop (`.pd-wa`), de triggerknop van de samples-app en
de chat.

### Wanneer is dit ontstaan

| Thema | `modal-show` in puredeco-premium.css |
|---|---|
| H1-Kopie (t/8) | **0 voorkomens** |
| H2 — LIVE (t/10) | **3 voorkomens** |

De regel is dus toegevoegd bij de publicatie van H2 op **1 november 22:23**.
De `classList.add`-aanroepen bestonden al eerder, maar hadden tot dat moment
geen effect op de koopbalk.

---

## 2. Wat aantoonbaar WEL werkt

Alles serverzijdig en in de browser getest:

| Stap | Resultaat |
|---|---|
| `GET /products/602-hout-wood-classic.js` | 200 · variant beschikbaar · € 99,95 |
| Klik op de hoofdkoopknop `.pdh__cta` | winkelwagen 0 → **1 item** |
| `POST /cart/add` | **HTTP 200** |
| `GET /cart.js` | 1 item, € 99,95 |
| Winkelwagenlade | opent, zichtbaar, knop "Afrekenen" niet disabled |
| Checkout-pagina (directe URL) | **HTTP 200**, 315 KB, Klarna · iDEAL · Mollie aanwezig |
| Verzendzones | NL 3 actieve tarieven · BE 2 · Internationaal 1 |
| Productpublicatie | actief, `inventoryPolicy: CONTINUE` op alle varianten |

**De hoofdknop en de winkelwagen functioneren dus.** Het defect uit punt 1 is
echt en ernstig, maar ik heb er geen volledige onmogelijkheid om te bestellen
mee kunnen reproduceren.

---

## 3. Wat ik NIET heb kunnen testen

- **De Shop Pay-doorverwijzing.** `/checkout` stuurt door naar
  `shop.app/.../shoppay` (`redirect_source=checkout_universal_redirect`). Mijn
  omgeving blokkeert `shop.app`, dus die stap is van hieruit onbereikbaar. De
  `chrome-error` die mijn test opleverde is **mijn proxy**, geen winkelstoring.
  Dit blijft het enige onbeproefde punt in de keten.
- De betaalstap zelf (zou een echte order aanmaken).
- Desktop; alle metingen zijn mobiel.

---

## 4. Het signaal in de orderdata

| Order | Datum | Bedrag |
|---|---|---|
| #2608 t/m #2598 | 31 okt 07:12 – 2 nov 02:03 | **11× € 6,95** (stalen) |
| **#2597** | **31 okt 06:17** | **€ 511,16** ← laatste niet-staalorder |

**Sinds 31 oktober 06:17 is er geen paneelorder meer binnengekomen.** Bij het
eerder vastgestelde tempo van ongeveer één paneelorder per dag zijn dat er
ruwweg twee die ontbreken.

Staalorders komen wél binnen, en die lopen via de conceptorder van de Product
Samples-app — dus **langs de gewone winkelwagen en checkout heen**. Dat verschil
past bij een storing in het reguliere bestelpad, maar bewijst die niet.

---

## 5. Voorgestelde reparatie

**Minimaal en veilig:** verwijder in `layout/theme.liquid` de twee regels

```js
document.body.classList.add("modal-show");
```

De CSS-regel bevat al `html:has(cart-drawer[open])`, en die doet precies
hetzelfde werk **en herstelt zichzelf** zodra de lade sluit. De `modal-show`-
selectors zijn dus overbodig.

Alternatief als de class per se moet blijven: haal hem weer weg bij het sluiten
van de lade. Dat is meer code voor hetzelfde resultaat.

**Ik kan dit niet zelf doen.** Het betreft het gepubliceerde thema; de
Shopify-koppeling blokkeert schrijfacties op het MAIN-thema technisch, en de
afspraak is dat het live thema read-only is. Twee routes:

1. De eigenaar verwijdert de twee regels in de code-editor van het live thema.
2. Ik voer het door in H3 (ongepubliceerd) en de eigenaar publiceert dat.

---

## 6. Openstaande vraag

Wat heeft de klant precies gezien en gedaan? Mobiel of desktop, welk product,
en waar liep het vast — knop deed niets, winkelwagen bleef leeg, of vastgelopen
op de afrekenpagina? Dat bepaalt of het defect uit punt 1 de oorzaak is of dat
er nog iets anders speelt in de Shop Pay-stap.
