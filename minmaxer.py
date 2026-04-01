def zadanicisla(i) -> float:
    print(f"Zadejte {i} cislo: ")
    cislo = float(input())
    return cislo
def vypis_seznam(seznam):
    for i in range(len(seznam)):
        print(seznam[i])

seznam: list[float] = []
i = 0
min = 99999999.9
max = -99999999.9
while True:
    i = i + 1
    seznam.append(zadanicisla(i))
    if(seznam[i-1] == 0):
        i = 0
        seznam.pop()
        break
    if(max<seznam[i-1]):
        max = seznam[i-1]
    if(min>seznam[i-1]):
        min = seznam[i-1]
vypis_seznam(seznam)
print(f"Max = {max}\nMin = {min}\nRozdil = {max-min}")