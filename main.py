text = "Vitejte v python kalkulátoru!"
print(text)
print("Zadejte 1. cislo:")
a = float(input())
print("Zadejte 2. cislo:")
b = float(input()) 
print("Zadejte operaci (+, -, *, /):")
x = (input())
if(x == '+'):
    print(f"Vysledek je: {x}", (a + b))
elif(x == '-'):
    print(f"Vysledek je: {x}", (a - b))
elif(x == '*'):
    print(f"Vysledek je: {x}", (a * b))
elif(x == '/'):
    print(f"Vysledek je: {x}", (a / b))