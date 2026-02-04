'''''
print("Zadej okolni teplotu v Celsiich: ")
teplota = float(input())
if(teplota<0):
    if(teplota< -15):
        print("Je extremne zima, venku hrozi omrzliny.")
    else:
        print("Je pod nulou, venku je zima.")

elif(teplota>=0 and teplota<=15):
    print("Je chladno.")
elif(teplota>15 and teplota<=25):
    print("Je prijemne.")
elif(teplota>25):
    print("Je horko.")
'''''

print("Zadejte cislo: ")
cislo = float(input())
'''''
if(cislo<10):
    print("cislo je jednociferne")
elif(cislo>=10 and cislo<100):
    print("cislo je dvojciferne")
elif(cislo>=100 and cislo<1000):
    print("cislo je trojciferne")
'''''
cislo_str = str(cislo)
pocet_cifer = len(cislo_str)
print(f"cislo ma {pocet_cifer-2} cifer")
