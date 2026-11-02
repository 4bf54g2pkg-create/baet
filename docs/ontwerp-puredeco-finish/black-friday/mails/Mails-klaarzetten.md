# De Wandweek · mails klaarzetten in Shopify Email

Alles staat klaar. Jij hoeft alleen te **kopiëren, plakken en inplannen** (± 10 minuten per mail). Shopify laat het aanmaken van mails niet via een koppeling toe, daarom moet dit ene stukje in het beheer.

**Al geregeld (door Claude):**
- Doelgroep **"Wandweek VIP 2026"** bestaat (iedereen met tag `wandweek-vip`). Shopify Email stuurt alleen naar wie toestemming heeft gegeven.
- Agendabestand in Shopify Files: `https://cdn.shopify.com/s/files/1/0940/4075/2394/files/wandweek-vip-avond.ics?v=1793632217` (do 26/11 20:00–23:00, herinnering 15 min vooraf).
- Alle afbeeldingen staan al in Shopify Files (zie per mail).
- Alle kortingen staan ingepland; in de mail hoeft geen code.

**Algemeen voor alle 3:** Shopify-beheer → **Marketing → Campagnes → Campagne maken → Shopify Email** → kies een lege template. Afzendernaam: **PureDeco**. Kleuren (Thema-instellingen in de editor): tekst `#151413`, knop `#151413` met witte tekst, achtergrond secties `#F5F2EC`.

---

## Mail 1 · Welkom, VIP (automatisch)

Deze verstuurt zichzelf zodra iemand VIP wordt. Dat gaat via **Shopify Flow** (gratis app van Shopify).

**Stap A · e-mail maken:** Shopify-beheer → **Marketing → Automatiseringen → Automatisering maken → Aangepaste automatisering maken** (opent Flow).
1. **Trigger:** "Customer tags added" (Klanttags toegevoegd).
2. **Voorwaarde:** "Customer tags" bevat `wandweek-vip`.
3. **Actie:** "Send marketing email" (Marketingmail verzenden) → **Mail bewerken** en vul in zoals hieronder.
4. **Activeren.**
5. **Testen:** meld je op de site aan als VIP met een e-mailadres dat nog niet in de winkel staat. Komt mail 1 binnen een paar minuten? Klaar. Komt hij niet, verander dan de trigger in **"Customer created"** (Klant aangemaakt) met dezelfde voorwaarde.

| Veld | Tekst |
|---|---|
| Onderwerp | Je bent VIP. Dit krijg jij straks 🗝️ |
| Voorbeeldtekst | Do 26 november 20:00 ben jij 12 uur eerder binnen. |

Blokken van boven naar beneden:

1. **Tekst (klein, gecentreerd, zwarte balk):** DE WANDWEEK · 26 – 30 NOVEMBER
2. **Kop / logo:** PureDeco-logo
3. **Afbeelding:** uit Bestanden: `generated_2Fshopify_3Af9yvx9-zm.myshopify.com_2F1793565871079_0.png` (lichte wand met bank)
4. **Tekst (klein, bruin, hoofdletters):** WELKOM BIJ DE WANDWEEK
5. **Kop:** Je staat op de lijst. Dit krijg jij straks.
6. **Tekst:**
   - **Tot 25% korting.** 15% vanaf € 400, 20% vanaf € 800, 25% vanaf € 1.500.
   - **12 uur eerder binnen.** Donderdag 26 november om 20:00. Iedereen anders pas vrijdag 08:00.
   - **Gratis High Tack-koker bij elk paneel.** Zit vanzelf in je pakket.
   - **€ 6,95 staalverzending terug.** Bestel nu tot 5 stalen. Bestel je in De Wandweek, dan krijg je de € 6,95 terug.
7. **Tekst:** **Jouw kleur uitverkocht? Maakt niet uit.** Ook op pre-order krijg je de Wandweek-korting, en je betaalt nu maar 50%.
8. **Knop:** Bestel nu je stalen (tot 5) → `https://puredeco.nl/pages/sample?utm_source=email&utm_medium=email&utm_campaign=wandweek&utm_content=welkom-stalen`
9. **Knop (omlijnd):** Zet 26 november 20:00 in je agenda → `https://cdn.shopify.com/s/files/1/0940/4075/2394/files/wandweek-vip-avond.ics?v=1793632217`
10. **Tekst (lichtbeige vlak):** **Belangrijk:** je VIP-korting werkt alleen als je bent ingelogd met dít e-mailadres. Inloggen gaat met een code per e-mail, een wachtwoord is niet nodig.

**Stap B · ook de VIP's van vóór de automatisering:** wie zich al aanmeldde vóór je de Flow activeerde, krijgt mail 1 niet. Stuur die eenmalig als campagne naar doelgroep "Wandweek VIP 2026" (zelfde inhoud).

---

## Mail 2 · Je bent binnen (ingepland)

**Marketing → Campagne maken → Shopify Email.**

| Veld | Tekst |
|---|---|
| Aan | Doelgroep **Wandweek VIP 2026** |
| Onderwerp | De deur is open. Alleen voor jou. |
| Voorbeeldtekst | Tot 25% korting. Iedereen anders pas morgen om 08:00. |
| Inplannen | **donderdag 26 november 2026, 20:00** (niet eerder: dan werkt de korting nog niet) |

Blokken:

1. **Tekst (zwarte balk):** NU LIVE VOOR VIP'S · T/M MAANDAG 23:59
2. **Kop / logo:** PureDeco-logo
3. **Afbeelding:** uit Bestanden: `bamboepanelen-hout-813-natural-oak-detail.jpg`
4. **Tekst (klein, bruin):** JE BENT BINNEN
5. **Kop:** Black Friday is begonnen. Voor jou 12 uur eerder.
6. **Tekst (groot, drie kolommen of drie regels):** **15%** vanaf € 400 · **20%** vanaf € 800 · **25%** vanaf € 1.500
7. **Tekst (beige vlak):** Voorbeeld · 4 panelen 813 Natural Oak: ~~€ 679,80~~ **€ 577,83** + 4 gratis kokers
8. **Tekst:** Plus: **gratis bezorging** in Nederland vanaf € 500. Heb je stalen besteld? Dan krijg je de **€ 6,95 terug**.
9. **Tekst:**
   1. **Log in** met het e-mailadres waarmee je VIP werd.
   2. **Kies je wand** en vul je maten in de calculator in.
   3. **Je korting** zie je in je winkelwagen en bij de kassa.
10. **Knop:** Log in en kies je wand → `https://puredeco.nl/customer_authentication/login?return_to=%2Fcollections%2Fwandpanelen%3Futm_source%3Demail%26utm_medium%3Demail%26utm_campaign%3Dwandweek%26utm_content%3Dvip-live`
11. **Tekst:** **Is jouw kleur uitverkocht?** Bestel als pre-order: zelfde korting, nu 50% betalen, levering in week 2 (11–15 januari).
12. **Tekst (klein, grijs):** Morgen om 08:00 gaat de deur open voor iedereen.

---

## Mail 3 · Laatste dag (ingepland)

| Veld | Tekst |
|---|---|
| Aan | Doelgroep **E-mailabonnees** (bestaat al) |
| Onderwerp | Laatste dag: vannacht 23:59 is het voorbij |
| Voorbeeldtekst | Tot 20% korting op je nieuwe wand (VIP tot 25%). |
| Inplannen | **maandag 30 november 2026, 09:00** |

Blokken:

1. **Tekst (zwarte balk):** LAATSTE DAG · DE WANDWEEK
2. **Kop / logo:** PureDeco-logo
3. **Tekst (klein, bruin):** NOG ÉÉN DAG
4. **Kop:** Vannacht om 23:59 is het voorbij.
5. **Afbeelding:** uit Bestanden: `generated_2Fshopify_3Af9yvx9-zm.myshopify.com_2F1776693455240_0.png` (vrouw bij wand)
6. **Tekst (groot):** **10%** vanaf € 400 · **15%** vanaf € 800 · **20%** vanaf € 1.500
7. **Tekst:** **VIP?** Log in en je krijgt 5% extra: 15, 20 of 25%.
8. **Tekst:**
   - **Gratis koker bij elk paneel.** Zit vanzelf in je pakket.
   - **Gratis bezorging vanaf € 500.** In Nederland.
   - **Uitverkocht? Toch korting.** Pre-order met dezelfde korting, nu 50% betalen, levering in week 2.
9. **Knop:** Kies je wand → `https://puredeco.nl/collections/wandpanelen?utm_source=email&utm_medium=email&utm_campaign=wandweek&utm_content=laatste-dag`
10. **Tekst (klein, gecentreerd):** Twijfel je over een kleur? Stuur ons een WhatsApp via puredeco.nl, we helpen je vandaag nog.

---

## Controle vóór verzenden (per mail)
- **Testmail** naar jezelf sturen (knop "Test versturen") en op je telefoon bekijken.
- Klik elke knop één keer aan.
- Mail 2: na het inloggen moet je op de collectie wandpanelen uitkomen. Zo niet, laat het Claude weten.
