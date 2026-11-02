# Black Friday-gereedheid — stand 2 november 2026

Black Friday valt op **vrijdag 27 november 2026**. Nog 3,5 week.
**Er is niets gewijzigd tijdens dit onderzoek.**

## Kort antwoord: nee, nog niet. Drie blokkades.

> Blokkade 3 is op 2 november ingetrokken — die was gebaseerd op een
> meetfout van mij. Blokkade 1, 2 en 4 staan.

Er staat veel klaar en de opzet is goed doordacht. Maar drie dingen moeten
eerst opgelost, en één daarvan kan je omzet kosten in plaats van opleveren.

---

## Wat er staat: "Wandweek"

| Start | Actie | Voor wie |
|---|---|---|
| 26 nov 19:00 | 15% v.a. € 400 · 20% v.a. € 800 · 25% v.a. € 1.500 | VIP-segment |
| 26 nov 19:00 | € 6,95 staalverzending terug | VIP-segment |
| 26 nov 19:00 | Gratis bezorging v.a. € 500 (NL) | iedereen |
| 27 nov 07:00 | 10% v.a. € 400 · 15% v.a. € 800 · 20% v.a. € 1.500 | iedereen |

Alle acht lopen af op 30 nov 22:59. Twaalf uur VIP-vroegtoegang.

In thema **H3** zit een snippet `pd-bf.liquid` (19.275 bytes) die op vier
plaatsen rendert: `head`, `bar` (boven de header), `popup` en `count`
(aftelteller). Plus 14 KB nieuwe CSS. De front-end is dus gebouwd.

---

## BLOKKADE 1 — De kortingsdrempels stapelen op elkaar

**Dit is de duurste.**

Alle acht Wandweek-kortingen staan op:

```
combinesWith: { orderDiscounts: true, productDiscounts: true, shippingDiscounts: true }
```

De zes percentagekortingen zijn **productkortingen** op de collectie
"Wandweek-actie". Shopify's eigen documentatie zegt letterlijk:

> *"Any number of product discounts can apply to the same line if this two-way
> match holds for every pair in the group."*

Een bestelling van € 1.500 haalt **alle drie de drempels tegelijk**: € 400,
€ 800 én € 1.500. Met stapelen aan staat er dus niet 20% maar **10% + 15% +
20% = 45%**.

En op 27 november vanaf 07:00 lopen de VIP- en publieksreeks náást elkaar. Een
VIP-klant boven € 1.500 raakt dan in theorie alle zes aan:

```
10% + 15% + 20% + 15% + 20% + 25% = 105%
```

Of Shopify dat daadwerkelijk zo uitrekent heb ik niet getest — dat zou een
echte order vragen. Maar de instelling **staat het expliciet toe**, en bij
getrapte kortingen hoort die juist uit te staan.

### Zo hoort het

| Korting | orderDiscounts | productDiscounts | shippingDiscounts |
|---|---|---|---|
| De zes percentages | **true** | **false** | **true** |
| € 6,95 staalverzending | **false** | **true** | **true** |
| Gratis bezorging | true | true | false |

Met `productDiscounts: false` op de percentages kiest Shopify vanzelf de
**beste** drempel in plaats van ze op te tellen, en blijft VIP 25% winnen van
publiek 20%. De € 6,95 en de gratis bezorging stapelen er dan netjes bovenop.

**Testen vóór 26 november.** Zet een testproduct op € 1.600, reken af met een
testorder en kijk wat er werkelijk wordt afgetrokken.

---

## BLOKKADE 2 — Het VIP-segment bevat één klant

Segment `Wandweek VIP 2026` = `customer_tags CONTAINS 'wandweek-vip'`,
aangemaakt op 2 november 10:35.

**Aantal klanten met die tag: 1** (van 1.653 in totaal).

Vier geplande kortingen en twaalf uur vroegtoegang gelden dus op dit moment
voor één persoon. De machine is gebouwd, het publiek ontbreekt.

Te doen: bepalen wie VIP is — bijvoorbeeld iedereen die ooit een staal
bestelde, of iedereen met minimaal één order — en die tag toekennen. Dat kan
met een segment-export plus Matrixify (staat geïnstalleerd), of via Shopify
Flow (idem).

---

## ~~BLOKKADE 3 — De bestelbug uit H2 zit ook in H3~~ — INGETROKKEN

**Deze blokkade bestaat niet.** Het "defect" berustte op een meetfout van mij:
ik mat met de winkelwagenlade nog open. Het thema ruimt `modal-show` correct
op zodra de lade sluit, en de CSS-regel is een bewuste reparatie van de
eigenaar. Volledige correctie in `docs/20-INCIDENT-2-NOV-BESTELLEN.md`.

Er hoeft dus **niets** aan H3 te gebeuren op dit punt.

De oorspronkelijke tekst stond hieronder en is onjuist:

| | `modal-show` in CSS | `classList.add` in theme.liquid |
|---|---|---|
| H2 (live) | 3× | 2× |
| **H3 (Black Friday)** | **3×** | **2×** |

Identieke regel, identieke scripts. Na één klik op een koopknop wordt de vaste
koopbalk `pointer-events: none` en `opacity: 0`, en niets zet dat terug.

**Publiceer je H3 op 26 november, dan gaat die bug mee de drukste dag van het
jaar in.** Repareren vóór publicatie: verwijder de twee regels
`document.body.classList.add("modal-show");` uit `layout/theme.liquid`.

---

## BLOKKADE 4 — Losse eindjes in de kortingen

**Een testkorting staat nu live.**
"TEST VIP-herkenning (€ 1) · verwijderen na test" — status ACTIVE, loopt tot
4 november, combineert met alles. De titel zegt het zelf.

**Vijf oude codes staan nog open:**

| Code | Korting | Loopt tot |
|---|---|---|
| TERUG5 | 5% | geen einddatum |
| SAMPLE10 | 10% (8 collecties) | geen einddatum |
| PUREDECO10! | 10% (8 collecties) | geen einddatum |
| PUREDECO5 | 5% | 5 dec |
| MONSTER5 | 5% | **30 nov** |

Alle vijf staan op `combinesWith: alles false`. Ze stapelen dus niet met
Wandweek — maar ze **verdringen** het wel: voert een klant PUREDECO10! in, dan
vervalt de automatische Wandweek-korting en houdt hij 10% over waar 20% had
gekund. Dat kost jou niets, maar het kost de klant iets en dat merk je in je
reviews.

Overweeg ze tijdens Wandweek uit te zetten, of tenminste SAMPLE10 en
PUREDECO10!.

---

## Wat wél goed staat

| | |
|---|---|
| Kortingsarchitectuur | VIP-vroegtoegang + drie drempels + gratis bezorging — commercieel sterk |
| Timing | VIP 26 nov 19:00, publiek 27 nov 07:00, einde 30 nov 22:59 |
| Front-end | `pd-bf.liquid` met balk, popup en aftelteller, plus 14 KB CSS |
| Verzendzones | NL 3 tarieven, BE 2, internationaal 1 — actief |
| Betaalmethodes | Klarna, iDEAL, Mollie aanwezig op de checkout |
| Voorraadbeleid | alle varianten `CONTINUE` — niets blokkeert verkopen |

---

## Risico dat ik niet kan wegnemen

**Voorraadbeleid `CONTINUE` op alles.** Niets blokkeert een verkoop, ook niet
bij negatieve voorraad. Op een gewone dag is dat handig. Op Black Friday met
drempels tot € 1.500 betekent het dat je meer kunt verkopen dan je hebt
liggen — met levertijden als gevolg. Nu al staan onder meer 810 Noir Oak 5 mm
op −83, 620 Japandi op −28 en 619 Jade op −18.

Dat is een voorraadbesluit, geen technisch probleem. Maar beslis het bewust
vóór 26 november.

---

## Volgorde

| Wanneer | Wat | Wie |
|---|---|---|
| Deze week | Blokkade 1: stapelen uitzetten en testen met een testorder | eigenaar |
| Deze week | Testkorting van € 1 verwijderen | eigenaar |
| Voor 20 nov | Blokkade 2: VIP-tag toekennen aan een echte doelgroep | eigenaar |
| Voor 20 nov | Oude codes uitzetten voor de actieperiode | eigenaar |
| Voor 24 nov | Voorraadbesluit per decor | eigenaar |
| 25 nov | H3 publiceren en de hele keten één keer doorlopen | samen |
