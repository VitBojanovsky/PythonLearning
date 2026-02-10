#vstup na horskou drahu
#>87cm
#<12 let == 50kc
#<18 let == 100kc
#<65 let == 150kc
#foto =+ 40kc

vek = 0;
vyska = 0;
foto = False;
cena = 0;
zakazano = False;
print("Vyej na horske draze");
print("Kolik je ti let: ");
vek = input();
if(int(vek) < 12): 
    cena += 50;
elif(int(vek)<18):
    cena += 100;
elif(int(vek)<65):
    cena += 150;
elif(int(vek)>=65):
    print("jste moc stary na tuto atrakci");
    zakazano = True;
else:
    print("Nezadalijste cislo");
    zakazano = True;
if(not zakazano):
    print("Jaka je vase vyska v cm: ");
    vyska = input();
    if(int(vyska)<87):
        print("Jste moc zakrsli na toto atrakci");
        zakazano = True;
if(not zakazano):
    print("Chcete foto: (ano/ne): ");
    var = input();
    var = var.upper();
    if(var=="ANO"):
        cena+=40;
    elif(var=="NE"):
        print("foto nebude");
    else:
     print("nezadali jste ano/ne");

if(not zakazano):
    print("Vase cena je " + str(cena) + " kc");
