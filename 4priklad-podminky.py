print("Zadej okolni teplotu v Celsiich: ")
teplota = float(input())
if(teplota<0):
    print("Je pod nulou, venku je zima.")
elif(teplota>=0 and teplota<=15):
    print("Je chladno.")
elif(teplota>15 and teplota<=25):
    print("Je prijemne.")
elif(teplota>25):
    print("Je horko.")
