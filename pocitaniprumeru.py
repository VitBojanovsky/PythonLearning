print("Zadejte zacatek: ");
zacatek = int(input());
print("Zadejte konec: ");
konec = int(input());
print("Zadejte krok: ");
krok = int(input());

soucet = 0;
pocet = 0;
prumer = 0.0;


for i in range(zacatek,konec,krok):
    print(i);
    soucet += i;
    pocet = pocet +1;
prumer = soucet / pocet
print(f"Prumer = {prumer}");
print(f"Soucet = {soucet}");
print(f"Pocet = {pocet}");
