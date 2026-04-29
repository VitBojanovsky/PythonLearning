print("Zadejte pocet kraliku: ")
while True:
    try:
        kralici = int(input())
    except ValueError:
        print("Chyba: Zadejte prosím platné číslo.")
    else:
        break
print("Zadejte pocet slepic:")
while True:
    try:
        slepice = int(input())
    except ValueError:
        print("Chyba: Zadejte prosím platné číslo.")
    else:
        break
hlavy = 0
nohy = 0
while(slepice>0):
    nohy = nohy+2
    hlavy = hlavy + 1
    slepice = slepice - 1 
while(kralici>0):
    nohy = nohy + 4
    hlavy = hlavy + 1
    kralici = kralici - 1

print(f"hlavy = {hlavy}")
print(f"nohy = {nohy}")

#opacne 
kralici_c = nohy / 4
b = nohy - kralici_c *4
slepice_c = b/2
while True:
    if(kralici_c + slepice_c ) < hlavy:
        kralici_c = kralici_c -1
        slepice_c = slepice_c + 2
    if(kralici_c + slepice_c ) > hlavy:
        kralici_c = kralici_c + 1
        slepice_c = slepice_c - 2
    if(kralici_c + slepice_c ) == hlavy:
        break   
print(f"Vypocitani kralici = {kralici_c}")
print(f"vypocitane slepice = {slepice_c}")

