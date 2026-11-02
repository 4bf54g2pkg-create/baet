"""PureDeco Black Friday 2026 - rekenmodel. Alle bedragen excl. btw tenzij anders vermeld.
Gemeten (Shopify, Meta, Google Ads, laatste 90 dagen): zie FEITEN. Aannames: zie AANNAMES - pas aan zodra marge/verzendkosten bekend zijn."""
FEITEN = dict(sessies_90d=21689, mobiel_aandeel=0.874, betaalde_bestellingen_90d=64, netto_omzet_90d=29470,
              staalbestellingen_90d=342, staalbestellingen_2026=617, meta_spend_90d=4750, google_spend_90d=2722)
A = dict(cogs_pct=0.45,          # inkoop + import als % van lijstprijs excl. btw  (ONBEKEND - vraag 1)
         verzend_per_order=35.0, # transport lange panelen per bestelling (ONBEKEND - vraag 2)
         betaal_pct=0.02, retour_pct=0.04, cadeau_kost=14.0)
def bijdrage(orders, aov_lijst, korting, cadeau_aandeel, ads):
    omzet = orders*aov_lijst*(1-korting)
    bruto = omzet - orders*aov_lijst*A['cogs_pct'] - omzet*A['betaal_pct'] - omzet*A['retour_pct']*0.5
    kost = orders*A['verzend_per_order'] + orders*cadeau_aandeel*A['cadeau_kost'] + ads
    return omzet, bruto-kost
# Kortingsvarianten, zelfde vraag-elasticiteit-aanname: extra orders t.o.v. 0% korting
basis_orders = 40   # verwacht zonder actie in 4 weken nov (30/mnd + seizoens-/advertentieeffect)
aov = 480.0         # lijstprijs excl. btw per bestelling (gemeten ~460)
print('KORTINGSVARIANTEN (zelfde budget 5000)')
for naam, korting, uplift, aovf, cad in [('Geen actie',0,1.0,1.0,0),('15% alles',0.15,1.9,1.0,0),('20% alles',0.20,2.2,1.0,0),
        ('25% alles',0.25,2.45,1.0,0),('30% alles',0.30,2.65,1.0,0),
        ('Staffel 10/15/20 + montagepakket >=600',0.14,2.15,1.18,0.7),('20% + gratis montagepakket',0.20,2.3,1.05,1.0)]:
    o=basis_orders*uplift; om,b=bijdrage(o,aov*aovf,korting,cad,5000 if naam!='Geen actie' else 2500)
    print(f'{naam:42s} orders {o:5.0f}  omzet {om:8.0f}  bijdrage na ads {b:8.0f}')
print()
print('BUDGETSCENARIO\'S (staffel + montagepakket), conservatief / realistisch / ambitieus')
for budget in (2500,5000,10000):
    for sc,cpl,vip_cv,cold_orders_per_k,aovf in [('cons',5.0,0.025,5,1.10),('real',3.5,0.04,7,1.18),('amb',2.5,0.06,9,1.25)]:
        lead_budget=budget*0.45; vips=lead_budget/cpl + 450   # +450 = bestaande staalaanvragers/klanten met toestemming (schatting)
        vip_orders=vips*vip_cv; staal_orders=0
        cold=budget*0.55/1000*cold_orders_per_k
        orders=basis_orders*0.75+vip_orders+cold   # 25% van basis schuift naar VIP/campagne (kannibalisatie)
        om,b=bijdrage(orders,aov*aovf,0.14,0.7,budget)
        roas=om/budget; print(f'€{budget:>6} {sc:5s} VIP {vips:5.0f} (CPL €{cpl})  orders {orders:4.0f}  AOV {aov*aovf*(1-0.14):4.0f}  omzet {om:7.0f}  ROAS {roas:4.1f}  bijdrage {b:7.0f}')
    print()
# gevoeligheid
print('GEVOELIGHEID realistisch €5000: bijdrage bij andere cogs/verzendkosten')
for cogs in (0.35,0.45,0.55):
    for vz in (20,35,60):
        A['cogs_pct']=cogs; A['verzend_per_order']=vz
        vips=5000*0.45/3.5+450; orders=40*0.75+vips*0.04+5000*0.55/1000*7
        om,b=bijdrage(orders,aov*1.18,0.14,0.7,5000); print(f' cogs {cogs:.0%} verzend €{vz}: bijdrage {b:7.0f}')
