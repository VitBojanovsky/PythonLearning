import random


def random_volba():
    return random.choice(["kamen", "nuzky", "papir"])


def vyhodnoceni(volba1, volba2) -> int:
    if volba1 == volba2:
        return 0
    elif (
        (volba1 == "kamen" and volba2 == "nuzky")
        or (volba1 == "nuzky" and volba2 == "papir")
        or (volba1 == "papir" and volba2 == "kamen")
    ):
        return 1
    else:
        return 2


def prirazeni_k_cislu(volba: int) -> str:
    if volba == 1:
        return "kamen"
    elif volba == 2:
        return "nuzky"
    elif volba == 3:
        return "papir"


body1 = 0
body2 = 0
body_vitez = 0
while body_vitez <= 2:
    print("Zadejte volbu")
    volba = int(input())
    volba = prirazeni_k_cislu(volba)
    volba2 = random_volba()
    vysledek = vyhodnoceni(volba, volba2)
    if vysledek == 0:
        print("Remiza")
    elif vysledek == 1:
        print("Vyhral jsi")
        body1 += 1
    else:
        print("Vyhral pocitac")
        body2 += 1
    print(f"Body: {body1} - {body2}")
    if body1 > body2:
        body_vitez = body1
    else:
        body_vitez = body2
