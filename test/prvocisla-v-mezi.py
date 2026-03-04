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

def SieveOfEratosthenes(n):
	primeNumber = [True for i in range(n+2)]
	i = 2
	while (i * i <= n):
		if (primeNumber[i] == True):
			for j in range(i * i, n+1, i):
				primeNumber[j] = False
		i += 1
	for i in range(2, n):
		if primeNumber[i]:
			print(i)

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
   # print(f"{i} je prvocislo = {jeprvocislo(i)}")
   if(jeprvocislo(i) == True):
       print(f"{i}, ",end="")