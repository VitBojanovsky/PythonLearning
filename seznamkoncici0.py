def zadanicisla(i) -> float:
    print(f"Zadejte {i} cislo: ")
    cislo = float(input())
    return cislo
def vypis_seznam(seznam):
    for i in range(len(seznam)):
        print(seznam[i])

seznam: list[float] = []
i = 0

while True:
    i = i + 1
    seznam.append(zadanicisla(i))
    if(seznam[i-1] == 0):
        i = 0
        seznam.pop()
        break
vypis_seznam(seznam)