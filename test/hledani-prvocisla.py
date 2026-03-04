import math
print("Zadejte cislo: ")
cislo = int(input())
if cislo < 2:
    prvocislo = False
else:
    odmocnina_cisla = math.sqrt(cislo)
    prvocislo = True
    for i in range(2, int(odmocnina_cisla) + 1):
        if cislo % i == 0:
            prvocislo = False
            break
print(prvocislo)