import math
def jeprvocislo(cislo): 
    if cislo < 2:
        prvocislo = False
    else:
        odmocnina_cisla = math.sqrt(cislo)
        prvocislo = True
        for i in range(2, int(odmocnina_cisla) + 1):
            if cislo % i == 0:
                prvocislo = False
                break
    return prvocislo

print("Zadejte zacatek: ")
zacatek = int(input())
print("Zadejte konec: ")
konec = int(input())

if(zacatek<0):
    zacatek = zacatek * -1
if(konec<0):
    konec = konec * -1
if(zacatek>konec):
    swap = konec
    konec = zacatek
    zacatek = swap
for i in range (zacatek,konec,1):
    print(f"{i} je prvocislo = {jeprvocislo(i)}")