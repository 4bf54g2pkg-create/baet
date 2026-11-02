# Waarom je PureDeco nauwelijks terugvindt in Google

**Datum:** 2 november 2026 · **Onderzocht:** live thema H2 (196032332042)
**Er is niets gewijzigd tijdens dit onderzoek.**

---

## De korte versie

Je premisse klopt niet helemaal, en dat is belangrijk nieuws: **je site ís
geïndexeerd.** Ik heb het geverifieerd — homepage, collectiepagina's en
productpagina's komen gewoon terug in zoekresultaten.

Maar de zorg eronder klopt wél, en harder dan je denkt:

1. **Organisch levert 3,6% van je verkeer** — 309 sessies in 30 dagen, tegen
   4.440 uit betaald social. En het daalt.
2. **Je wordt op je eigen merknaam verslagen door Praxis en Brico.** Zij
   verkopen jouw panelen en hun pagina's staan boven die van jou.
3. **Google krijgt maar 79 URL's aangeboden** — dat is het plafond.
4. **Search Console lijkt niet geverifieerd**, dus je hebt geen zicht én je
   sitemap is waarschijnlijk nooit ingediend.

---

## 1. Bewijs dat je wél geïndexeerd bent

Zoekopdracht "wandpanelen puredeco" gaf onder meer terug:

| URL | Titel |
|---|---|
| `puredeco.nl/collections/wandpanelen` | Wandpanelen kopen |
| `puredeco.nl/` | PureDeco |
| `puredeco.nl/collections/leer` | Leerlook wandpanelen kopen |
| `puredeco.nl/collections/hout-1` | Houten wandpanelen kopen |
| `puredeco.nl/products/621-…`, `620-…`, `821-…` | productpagina's |

Let op: mijn zoekmachine is op de VS gericht. De **index** is wereldwijd
dezelfde, de **rangschikking** verschilt per land. Dat je pagina's hier
terugkomen bewijst dus dat ze geïndexeerd zijn; het zegt niets over je positie
op google.nl.

---

## 2. Het echte probleem: Praxis en Brico staan boven je

Zoekopdracht "puredeco wandpanelen bamboekern" gaf **geen enkele** puredeco.nl-URL
terug. Wel elf productpagina's van **Praxis** en één van **Brico**:

```
praxis.nl/…/puredeco-810-noir-oak-wandpaneel-houtlook-280x122/10714550
praxis.nl/…/puredeco-811-walnut-classic-wandpaneel-houtlook-260x122cm/10714545
praxis.nl/…/puredeco-812-walnut-deep-wandpaneel-houtlook-260x122-cm/10714543
praxis.nl/…/puredeco-823-japandi-dark-wandpaneel-260x122/10714549
praxis.nl/…/puredeco-wandpaneel-830-leather-taup-260x122cm/10714562
praxis.nl/…/puredeco-wandpaneel-leather-sand-260-x-122cm/10714541
praxis.nl/…/puredeco-wandpaneel-art-stucco-light-260x122/10714548
praxis.nl/…/puredeco-840-grain-blue-wandpaneel-260x120/10714554
praxis.nl/…/puredeco-wandpaneel-houtlook-wood-white-oak-280x122/10714546
praxis.nl/…/puredeco-wandpaneel-japandi-brown-280x122cm/10714559
brico.be/…/puredeco-wandpaneel-leerlook-280x122cm-khaki-leather/10589978
```

Dit is de kern van je vraag. Een webshop met 71 producten en 79 URL's in de
sitemap kan Praxis.nl niet verslaan op domeinautoriteit. Je eigen
verkooppartners kapen je merkverkeer.

**Dat is niet per se slecht** — er wordt wel verkocht. Maar de marge gaat naar
Praxis, en jij betaalt met Google Ads om op je eigen naam zichtbaar te blijven.
Dat verklaart ook waarom je twee Brand-campagnes nodig had.

### Een compliance-punt dat hieruit volgt

Praxis beschrijft de panelen als **"vochtbestendig, geluiddempend,
brandvertragend"**, Brico plaatst ze onder **"akoestische wandpanelen"**.

In je eigen thema staat in `snippets/pd-gids-tekst.liquid` letterlijk:

> *"Niet gebruiken: geluidsabsorberend (wandpanelen), hittebestendig,
> brandklasse, UV-bestendig, levertijden."*

Je partners doen dus claims die jij in je eigen content verboden hebt
verklaard. Als dat onjuist is, ligt het risico uiteindelijk bij jou als
fabrikant/leverancier. Waard om bij Praxis aan te kaarten.

Praxis rekent **€ 59,98 per m²**; jouw eigen site vermeldt € 26 tot € 57 per m².
Je bent dus goedkoper dan je eigen partner — maar onvindbaar.

---

## 3. Harde cijfers: organisch is 3,6%

GA4, laatste 30 dagen:

| Kanaal | Sessies | Key events |
|---|---:|---:|
| Paid Social | 4.440 | 43 |
| Paid Shopping | 1.297 | 9 |
| Paid Search | 730 | 23 |
| Direct | 704 | 14 |
| Organic Social | 485 | 10 |
| Cross-network | 476 | 6 |
| **Organic Search** | **309** | **6** |
| Unassigned | 58 | 21 |
| AI Assistant | 51 | 1 |
| Organic Shopping | 44 | 1 |
| Referral | 6 | 0 |

**Organisch zoeken = 3,6% van 8.601 sessies.** Voor een webshop is 25–40%
gebruikelijk. Je draait vrijwel volledig op betaald verkeer.

Erger: het daalt. Organische sessies per dag over de laatste twee weken:

```
20 okt  14      27 okt  13
21 okt   7      28 okt   8
22 okt  11      29 okt   6
23 okt  15      30 okt   4
24 okt  11      31 okt   3
25 okt  11       1 nov   6
26 okt   9       2 nov   8
```

Van gemiddeld 11 naar gemiddeld 6 per dag.

---

## 4. Technische bevindingen op het live thema

### Wat goed is — en dat is nieuw sinds de publicatie van de PureDeco-thema's

| Signaal | Status |
|---|---|
| `noindex` op hoofdpagina's | **geen enkele** |
| Canonicals | correct, zelf-verwijzend |
| `<h1>` per pagina | precies **1** op home, collecties, producten, samplepagina |
| Titels | uniek en beschrijvend op alle geteste pagina's |
| Schema collectiepagina | CollectionPage · BreadcrumbList · ItemList (35 items) · FAQPage (7 vragen) |
| Schema homepage | Organization · WebSite · SearchAction · MerchantReturnPolicy |
| Zichtbare tekst collectiepagina | ± **2.339 woorden** |
| Sitemap bereikbaar | HTTP 200 |

De SEO-techniek is dus in orde. Dit is **niet** meer het probleem.

### Wat stuk is

**A. `robots.txt` mist de `Sitemap:`-regel.**

`templates/robots.txt.liquid` loopt door `group.user_agent` en `group.rules`,
maar laat het blok `{{ group.sitemap }}` weg dat Shopify standaard meegeeft.
Resultaat: nergens in robots.txt staat waar je sitemap is. Gecontroleerd op de
live site: geen enkele Sitemap-regel.

Fatale fout? Nee — Google kan crawlen en indexeren zonder. Maar het is één
ontdekkingsroute minder, en gratis te repareren.

**B. Geen `google-site-verification` op de site.**

Geen enkele verificatie-metatag gevonden: niet voor Google, niet voor Bing, niet
voor Facebook of Pinterest. Dat wijst erop dat **Search Console niet via de
site is geverifieerd**. Gevolgen:

- Je sitemap is waarschijnlijk nooit ingediend
- Je ziet niet welke pagina's geïndexeerd zijn en welke niet
- Je ziet geen zoekopdrachten, posities of klikken
- Je krijgt geen melding bij crawlproblemen

Verificatie kan ook via DNS of via de Google-koppeling in Shopify, dus dit is een
aanwijzing en geen bewijs. **Dit is het allereerste wat je moet controleren.**

**C. Slechts 79 URL's in de sitemap.**

```
producten   45   (van 71 — de rest staat op DRAFT)
collecties  14   (van 16)
pagina's    11   (van 12)
artikelen    7
blogs        1
agentic      1
```

Dit is het plafond van je organische bereik. Hoeveel je ook optimaliseert: met
79 URL's kun je op weinig zoekopdrachten ranken. **26 producten staan op DRAFT.**

**D. De WooCommerce-migratie is onvolledig.**

Er staan 32 redirects. Enkele werken:

| Oude URL | Nu |
|---|---|
| `/category/wandpanelen/` | 301 → `/collections/wandpanelen` |
| `/product/hout/` | 301 → `/collections/hout-1` |

Maar deze geven **404**, terwijl Google ze nog toont of kent:

| Oude URL | Nu |
|---|---|
| `/kantoorruimte-in-japanse-stijl-japansestof-wandpanelen-akupanelen-puredeco/` | **404** |
| `/product/812-hout-walnut-deep/` | **404** |
| `/category/akupanelen/` | **404** |
| `/winkel/` | **404** |

Elke 404 op een oude, geïndexeerde URL is weggegooide linkwaarde. Het eerste
voorbeeld is een blogartikel dat Google nog in de resultaten toont — dat is
precies het soort pagina dat autoriteit opbouwt.

---

## 5. Waarom jij "geen resultaten" zag

Drie verklaringen, in volgorde van waarschijnlijkheid:

1. **Je zag Praxis en Brico in plaats van jezelf.** Op merk + producttermen is
   dat aantoonbaar wat er gebeurt.
2. **Je positie op google.nl is laag**, zonder dat je uit de index bent. Met
   6 organische sessies per dag sta je er wel, maar ziet vrijwel niemand je.
3. **Je keek naar een SERP vol advertenties.** Je eigen Brand-campagnes staan
   bovenaan; organisch staat daaronder, mogelijk onder de vouw.

Wat het **niet** is: een penalty, een noindex, een robots-blokkade of een
onbereikbare site. Dat heb ik alle vier uitgesloten.

---

## 6. Wat ik zou doen, op volgorde van opbrengst

| # | Actie | Waarom | Moeite |
|---|---|---|---|
| 1 | **Controleer of Search Console geverifieerd is** en dien de sitemap in | Zonder dit stuur je blind | 15 min |
| 2 | **26 DRAFT-producten activeren** of verwijderen | Verdubbelt je indexeerbare URL's | uren |
| 3 | **`{{ group.sitemap }}` terugzetten in robots.txt.liquid** | Gratis, 1 regel | 5 min |
| 4 | **Redirects aanvullen** voor de 404's van oude WooCommerce-URL's | Herstelt linkwaarde | 1–2 uur |
| 5 | **Praxis aanspreken** op de acoustische en brandclaims | Jouw aansprakelijkheid | 1 gesprek |
| 6 | **Teksten voor de 13 collecties zonder inhoud** | Nu heeft alleen wandpanelen, hout-1 en 8mm-naadloos echte tekst | weken |
| 7 | **Blog hervatten** — 7 artikelen is te weinig voor autoriteit | Praxis wint op autoriteit, niet op techniek | doorlopend |

### Wat geen zin heeft

Verder sleutelen aan titels, H1's of schema. Dat is nu in orde. Het probleem is
**bereik en autoriteit**, niet techniek.

---

## 7. Wat ik niet heb kunnen vaststellen

- **Je werkelijke posities op google.nl.** Mijn zoekmachine is VS-gericht en ik
  heb geen Search Console-toegang. Voor echte posities en zoekopdrachten is
  Search Console nodig.
- **Hoeveel van je 45 producturl's daadwerkelijk geïndexeerd zijn.** Alleen
  Search Console toont dekking.
- **Of Search Console werkelijk ontbreekt** of alleen via DNS/Shopify is
  geverifieerd.

Wil je hier verder op sturen, dan is een Search Console-koppeling in Windsor
(connector `searchconsole`) de ontbrekende schakel. Je hebt nu drie connectors:
facebook, google_ads en googleanalytics4.
