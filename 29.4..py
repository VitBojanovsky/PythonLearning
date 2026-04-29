from math import pow
cele_cislo = int(input("Zadejte celé číslo: "))
kladne = False
if(cele_cislo>=0): 
    kladne = True
sude = False
if(cele_cislo % 2 == 0):
    sude = True

if(kladne==False):
    cele_cislo = cele_cislo * -1
    kladne = True
    print("Zaporne")
else:
    print("Kladne")
milimetry = cele_cislo * 1000
if(cele_cislo == 0):
    print("S 0 nepocitam")
else:
    print(f"{cele_cislo}m = {milimetry}mm a cislo je sude = {sude} obvod = {4*cele_cislo} obsah = {pow(cele_cislo,2)}")

