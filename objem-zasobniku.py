from math import pi
from math import pow
from time import sleep
print("Zadejte polomer")
while True:
    try:
        polomer = float(input())
    except ValueError:
        print("Chyba: Zadejte prosím platné číslo.")
    else:
        break
if(polomer<0):
    print("Cyba, zadali jste zaporne cislo")
    print("Prevadim na kladne cislo: ")
    sleep(5)
    polomer = polomer * -1
obsah = (pow(polomer,3)/3)*4 * pi
voda_na_den = 5
obsah_v_l=obsah*1000
voda_pro_cloveka = obsah_v_l/voda_na_den
print(f"Jednomu cloveku vyjde tento kulovy zasobnik na {voda_pro_cloveka:.2f} dni, nebo {(voda_pro_cloveka*24):.2f} hodin")
exit(0)