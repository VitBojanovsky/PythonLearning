def je_palindrom(slovo):
    palindrom = False
    prvni_pulka = ""
    druha_pulka = ""
    if(len(slovo)%2 == 0):
        for i in range(len(slovo)//2):
            prvni_pulka = prvni_pulka + slovo[i]
        for i in range(len(slovo)//2, len(slovo)):
            druha_pulka = druha_pulka + slovo[i]
        if prvni_pulka == druha_pulka[::-1]:
            palindrom = True
        else:
            palindrom = False
    if(len(slovo)%2!=0):
        for i in range(int((len(slovo)-1)//2)):
           prvni_pulka = prvni_pulka + slovo[i]
        for i in range(int((len(slovo)-1)//2)+1, len(slovo)):
            druha_pulka = druha_pulka + slovo[i]
        if prvni_pulka == druha_pulka[::-1]:
            palindrom = True
        else:
            palindrom = False
    return palindrom
            



print("Zadejte slovo: ")
slovo = input()
palindrom = je_palindrom(slovo)
print(f"Je palindrom = {palindrom}")