def zadanicisla(i) -> int:
    print(f"Zadejte {i} cislo: ")
    cislo = int(input())
    return cislo
def vypis_seznam(seznam):
    for i in range(len(seznam)):
        print(seznam[i])
def odstraneni_nasobku(seznam, delitele):
    to_remove: list[int] = []
    for x in range(len(seznam)):
        for y in range(len(delitele)):
            if seznam[x] % delitele[y] == 0:
                to_remove.append(seznam[x])
    for i in range(len(to_remove)):
        seznam.remove(to_remove[i])
    return seznam
seznam: list[int] = []
delitele: list[int] = []

i = 0
print("Zadejte cisla: ")
while True:
    i = i + 1
    seznam.append(zadanicisla(i))
    if(seznam[i-1] == 0):
        i = 0
        seznam.pop()
        break
print("Zadejte delitele: ")
while True:
    i = i + 1
    delitele.append(zadanicisla(i))
    if(delitele[i-1] == 0):
        i = 0
        delitele.pop()
        break
seznam = odstraneni_nasobku(seznam,delitele)
vypis_seznam(seznam)

