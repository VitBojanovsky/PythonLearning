print("Zadejte cislo 1: ")
prvni = float(input())
print("Zadejte 2. cislo: ")
druhy = float(input())
print("Zadejte operatora: ")
operator = input()
vysledek = 0.0
variable = 0.0

def mocnina(prvni,druhy):
    vysledek = 0.0
    if(druhy > 0):
        variable = prvni
        for i in range(0,int(druhy-1)):
            variable = variable * prvni
        vysledek = variable
    if(druhy < 0):
        druhy = druhy * -1
        variable = prvni
        for i in range(0,int(druhy)):
            variable = 1/variable
        vysledek = variable
    return vysledek
match operator: 
    case '+':
        vysledek = prvni + druhy
    case '-':
        vysledek = prvni - druhy
    case '*':
        vysledek = prvni * druhy
    case '/':
        if(druhy == 0):
            print("Nelze delit druhou")
        else:
            vysledek = prvni / druhy
    case '^':
        vysledek = mocnina(prvni,druhy)
    case _:
        print("error")
print(vysledek)

