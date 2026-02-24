'''Zadavani cisel, koncim 0 a vypocitam primer bez 0'''

print("Dobre dopoledne, prosim zadejte cisla: ")
input1 = 0
konec = False
soucet = 0
pocet = 0
prumer = 0.0
while konec == False:
    print(f"Zadejte {pocet+1} cislo: (0 pro vypnuti)")
    input1 = float(input())
    if(input1 == 0):
        konec = True
    else:
        soucet += input1
        pocet += 1
if(pocet == 0):
    pocet = 1
print(f"Prumer je {soucet/float(pocet)}")
