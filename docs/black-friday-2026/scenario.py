cogs, vz, betaal, retour, cadeau = 0.45, 35.0, 0.02, 0.04, 14.0
base_orders, aov = 40, 480.0
def run(budget, cpl, vcv, cold_k, aovf, cpm=18, cpc=0.40):
    vips = budget*0.45/cpl + 450
    orders = base_orders*0.75 + vips*vcv + budget*0.55/1000*cold_k
    lijst = orders*aov*aovf; omzet = lijst*(1-0.14)
    cad = orders*0.7*cadeau; staal = orders*0.4*6.95   # VIP krijgt de staalverzending (€6,95) terug bij bestelling; ~40% van de kopers vroeg een staal
    bruto = omzet - lijst*cogs - omzet*betaal - omzet*retour*0.5 - orders*vz
    bijdrage = bruto - cad - staal - budget
    impr = budget*0.85/cpm*1000; bereik = impr/3.2; clicks = budget*0.85/cpc + 21689/3*1.15
    marge_per_order = (bruto - cad - staal)/orders
    return dict(bereik=bereik, bezoekers=clicks, vips=vips, orders=orders, aov=omzet/orders, omzet=omzet, cad=cad, staal=staal,
                bruto=bruto, bijdrage=bijdrage, roas=omzet/budget, cv=orders/clicks, be_orders=budget/marge_per_order, mpo=marge_per_order)
geen = None
for budget in (2500, 5000, 10000):
    for sc, args in (('cons',(5.0,0.025,5,1.10)),('real',(3.5,0.04,7,1.18)),('amb',(2.5,0.06,9,1.25))):
        r = run(budget,*args)
        print(f"{budget:>5} {sc:4} bereik {r['bereik']:7.0f} bezoek {r['bezoekers']:6.0f} VIP {r['vips']:5.0f} orders {r['orders']:4.0f} cv {r['cv']*100:4.2f}% AOV {r['aov']:4.0f} omzet {r['omzet']:7.0f} cadeau {r['cad']:5.0f} staal {r['staal']:5.0f} bruto {r['bruto']:7.0f} bijdrage {r['bijdrage']:7.0f} ROAS {r['roas']:4.1f} BE-orders {r['be_orders']:4.0f} marge/order {r['mpo']:4.0f}")
