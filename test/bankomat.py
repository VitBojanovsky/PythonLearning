print("Zadejte cislo: ")
cislo = int(input())
bankovky = [2000,1000,500,200,100,50,20,10,5,2,1]
x = len(bankovky)
pocet_bankovek = [0] * x
while cislo != 0:
    for i in range(0, x):
        if cislo >= bankovky[i]:
            pocet_bankovek[i] = int(cislo / bankovky[i])
            cislo = cislo % bankovky[i]
            break
for i in range(0,x,1):
    print(f"{bankovky[i]} = {pocet_bankovek[i]}")