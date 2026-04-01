def zadanicisla(i) -> float:
    print(f"Zadejte {i+1} cislo: ")
    cislo = float(input())
    return cislo

def vypis_seznam(seznam):
    for i in range(7):
        print(seznam[i])

seznam: list[float] = []
for i in range(7):
    seznam.append(zadanicisla(i))
vypis_seznam(seznam)