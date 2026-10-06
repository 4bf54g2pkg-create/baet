# H1-TEST — RONDE 2: SERIF VOOR DE GROTE KOPPEN
**Theme:** Hyper kopie 5 okt (H1-test) · `194824929546` · **UNPUBLISHED**
**Datum:** 6 oktober 2026, 07:03–07:05 UTC
**Live theme:** niet aangeraakt (laatste wijziging: 2026-10-05 13:33 UTC, WhatsApp-link door opdrachtgever).

## Wat er veranderd is

### Theme-instellingen (`config/settings_data.json`)
| Instelling | Was | Nu | Effect |
|---|---|---|---|
| Lettertype koppen | Instrument Sans 500 | **Cormorant 500** (serif) | Grote koppen krijgen de uitstraling van een interieurmerk |
| Schaal koppen | 100 | 110 | Cormorant oogt kleiner bij dezelfde maat; dit compenseert |
| Schaal koppen mobiel | 70 | 85 | Koppen op mobiel niet meer 30% kleiner |
| Productkaart-titel | lettertype koppen, 600 | **lettertype tekst**, 400 | Productnamen blijven strak en leesbaar in sans |
| Subkoppen | 700 | 500 | Minder zwaar |
| Navigatie | 700 | 500 | Menu rustiger |
| Knoppen | 700, "Hoofdletter Per Woord" | 500, geen transformatie | "Bekijk de collectie" i.p.v. "Bekijk De Collectie" |
| Lege winkelmand | "Not sure where to start? Try these collections:" | "Weet je niet waar je moet beginnen? Bekijk deze collecties:" | Geen Engels meer |

### Visuele laag (`assets/puredeco-premium.css`, sectie "Ronde 2")
- h1–h3 en display-koppen: serif, letterafstand −0,005em, regelhoogte 1,12.
- h4–h6 en kleine bloktitels (iconen, USP's, FAQ-vragen) blijven **Instrument Sans**: Cormorant is op kleine maten te dun.
- Navigatie, knoppen, prijzen en productkaarten blijven Instrument Sans.

## Lessen voor volgende uploads
- Shopify weigert `settings_data.json` **stil** (geen foutmelding) als één waarde buiten het schema valt. Hier: `heading_scale` moet in stappen van 5 (112 → 110). Altijd na upload teruglezen.

## Testlijst (preview H1-test)
- [ ] Homepage-koppen ("Breed assortiment wandpanelen", "Onze Bestsellers", …) in serif.
- [ ] Productpagina: producttitel in serif, prijs en knoppen in sans.
- [ ] Productkaarten: titels in sans.
- [ ] Menu en knoppen: geen hoofdletter per woord, niet vet.
- [ ] Mobiel: koppen niet te groot of afgebroken.
- [ ] FAQ-vragen en USP-titels leesbaar (sans).

## Terugdraaien
Theme-editor → Thema-instellingen → Typografie → Koppen terug naar Instrument Sans. CSS-regels: sectie "Ronde 2" uit `puredeco-premium.css` verwijderen.
