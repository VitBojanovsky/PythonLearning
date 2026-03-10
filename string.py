heslo = "ahoj_svete"
delka = len(heslo)
male = False
cisla = False
specialni_znaky = False
bezpecnost = 0
if(delka>8):
    bezpecnost = bezpecnost + 1
if(heslo.islower()):
    male = True
else:
    bezpecnost = bezpecnost + 1
    male = False
if(heslo.isalpha()):
    cisla = False
else:
    cisla = True
    bezpecnost = bezpecnost + 1
if not any(char in "!@#$%^&*()" for char in heslo):
    specialni_znaky = False
else:
    specialni_znaky = True
    bezpecnost = bezpecnost + 1
print(f"bezpecnostni skore = {bezpecnost}")