"""
def prazdna_funkce():
    print("Toto je prazdna funkce")


def funkce_s_navratem() -> int:
    print("Toto je funkce s navratem")
    return 5
"""


def zadani_cisla() -> float:
    while True:
        try:
            return float(input("Zadej číslo: "))
        except ValueError:
            print("Neplatný vstup, zkus to znovu.")


def zadani_znak() -> str:
    while True:
        znak = input("Zadej znak: ")
        if len(znak) == 1:
            return znak
        print("Neplatný vstup, zkus to znovu.")


def matematicka_operace(a: float, b: float, znak: str) -> float:
    if znak == "+":
        return a + b
    elif znak == "-":
        return a - b
    elif znak == "*":
        return a * b
    elif znak == "/":
        if b == 0:
            raise ValueError("Nelze dělit nulou")
        return a / b
    else:
        raise ValueError("Neplatný znak")


a = zadani_cisla()
b = zadani_cisla()
znak = zadani_znak()
print(matematicka_operace(a, b, znak))
