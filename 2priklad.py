print("Zadejte delku hriste:");
delka = float(input());
print("Zadejte sirku hriste:");
sirka = float(input());
jedno_kolo = (delka+sirka)*2;
print("kolik kol ubehnes: ");
kola = float(input());
ubehnuta_vzdalenost = jedno_kolo * kola;
print(f"Ubehl jsi celkem: {ubehnuta_vzdalenost} metru");