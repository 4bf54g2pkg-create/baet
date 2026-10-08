# Casino-/spampagina's opschonen (stand 8 oktober 2026)

## Wat er aan de hand was
- In **mei 2026** toonde Google ruim **6.800 casino- en gokpagina's** onder `puredeco.nl`.
  - Voorbeelden: `/20-euro-no-deposit-bonus-casino/` en `/beste-goksite-…/`.
  - Samen kregen ze ~77.000 vertoningen en 351 klikken.
- Waarschijnlijk komen ze van de oude (WordPress-)site die op dit domein draaide. Die was gehackt.
- In de Shopify-winkel bestaan deze pagina's niet.

| Maand | Vertoningen casino-URL's | Aantal URL's |
|---|---|---|
| mei 2026 | 75.307 | 6.587 |
| jun 2026 | 344 | 163 |
| jul 2026 | 47 | 30 |
| aug 2026 | 25 | 19 |
| sep 2026 | 18 | 17 |

**Conclusie:** Google ruimt dit al vanzelf op. Elke spam-URL geeft nu een **404**: gecontroleerd op 60 willekeurige URL's, alle 404.

Verder is gecontroleerd:
- de sitemap bevat geen spam;
- `robots.txt` blokkeert ze niet. Dat is goed: Google moet de 404 kunnen zien.
- er bestaat geen Shopify-redirect naar spam.

## Wat we bewust NIET doen
- **Geen redirects van casino-URL's.** Ze blijven 404. Een redirect naar de homepage zou Google zien als "soft 404". Dat koppelt de spam juist aan je site.
- **Niet blokkeren in robots.txt.** Dan ziet Google de 404 niet meer, en blijven de URL's langer hangen.
- **Niet massaal disavowen.** Dat doe je alleen bij een handmatige actie, zie stap 2.
- **De 404-meldingen in Search Console niet "oplossen".** Die zijn hier juist goed.

## Wat jij nog moet doen in Google Search Console (5 minuten)
1. **Beveiliging en handmatige acties → Beveiligingsproblemen**: moet "Geen problemen gedetecteerd" zijn.
2. **Beveiliging en handmatige acties → Handmatige acties**: moet "Geen problemen gedetecteerd" zijn.
   - Staat daar iets over spam? Stuur me een screenshot. Dan maken we een herbeoordelingsverzoek en eventueel een disavow-bestand.
3. **Open `https://www.puredeco.nl` in je browser.** Het moet direct doorsturen naar `https://puredeco.nl`.
   - Zie je daar een oude WordPress-site of rare pagina's, laat het me weten. Dan draait de oude gehackte site nog ergens.
4. **Optioneel, Verwijderingen → Nieuw verzoek → "Alle URL's met dit voorvoegsel verwijderen".**
   - Dit verbergt de laatste restjes 6 maanden direct uit Google.
   - Bij ~18 vertoningen per maand is het niet nodig. Doe je het toch, gebruik dan alleen deze voorvoegsels. Ze kunnen nooit een echte Shopify-pagina raken:
     - `https://puredeco.nl/casino`
     - `https://puredeco.nl/beste-casino`
     - `https://puredeco.nl/nieuwe-casino`
     - `https://puredeco.nl/online-casino`
     - `https://puredeco.nl/live-casino`
     - `https://puredeco.nl/gok`
     - `https://puredeco.nl/beste-gok`
     - `https://puredeco.nl/legaal-`
     - `https://puredeco.nl/betrouwbaar`
     - `https://puredeco.nl/blackjack`
     - `https://puredeco.nl/bingo`
     - `https://puredeco.nl/roulette`
     - `https://puredeco.nl/keno`
     - `https://puredeco.nl/baccarat`
     - `https://puredeco.nl/craps`
     - `https://puredeco.nl/dobbelspel`
     - `https://puredeco.nl/krasloten`
     - `https://puredeco.nl/speelhal`
     - `https://puredeco.nl/amusementshal`
   - **Gebruik nooit** `/p`, `/b`, `/c`, `/products`, `/collections`, `/pages` of `/blogs` als voorvoegsel. Dan verdwijnt je eigen winkel uit Google.

## Wat er wél waarde heeft: oude winkel-URL's (voorstel, nog niet uitgevoerd)
Uit dezelfde data blijkt dat oude URL's van de vorige webshop nog vertoningen krijgen, maar een 404 geven. Met een 301-redirect gaat die waarde naar de juiste nieuwe pagina.

- `redirects-nieuw.csv` bevat **47 nieuwe redirects**. Voorbeelden:
  - de 20 oude `/faqs/…`-pagina's (samen 790 vertoningen) → `/pages/faqs`
  - `/product/end-profiles/` (309) → `/products/eindprofielen`
  - `/product/eenzijdig/` (218) → `/products/eenzijdig`
  - `/category/akupanelen/` (93) → `/collections/akupanelen`
  - oude blog-URL's → het juiste artikel in `/blogs/nieuws/`
- `redirects-wijzigen.csv` bevat **2 bestaande redirects** met een beter doel:
  - `/category/wandpanelen` (39 klikken, 664 vertoningen) wijst nu naar `/collections/bamboepanelen-samples`. Beter is `/collections/wandpanelen`, de pagina waarmee we op "wandpanelen" willen ranken.
  - `/de-voordelen-van-bamboepanelen` wijst nu naar "Over ons". Beter is het blogartikel met dezelfde titel.

Dit raakt **geen bestaande URL's van de winkel of de advertenties**. Het gaat alleen om oude adressen die nu niets tonen. Het is wel een wijziging op winkelniveau, dus ik voer het pas uit na jouw akkoord.

Je kunt het zelf doen via **Shopify-beheer → Content → Menu's → URL-omleidingen → Importeren**. Vink bij `redirects-wijzigen.csv` "Bestaande omleidingen overschrijven" aan. Of je geeft akkoord, dan zet ik ze er via de API in.

## Bestanden
- `spam-urls.csv`: alle 6.825 spam-URL's met klikken en vertoningen. Dit is naslag, er hoeft niets mee te gebeuren.
- `redirects-nieuw.csv` en `redirects-wijzigen.csv`: Shopify-importformaat.
