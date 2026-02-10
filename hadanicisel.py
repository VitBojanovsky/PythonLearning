import random;

nahodne=random.randint(1,11);
i=3;
print(f"hadej nahodne cislo mezi 1 a 10: ");
print("Vyber si pocet pokusu: ");
i=int(input());
guess = input();
uhodl = False;
for x in range(0,i):
    if(int(guess) == nahodne):
        print(f"Uhodl jsi cislo na {x+1} pokus!");
        uhodl=True;
        break;
    elif(int(guess) < nahodne):
        print("Hledane cislo je vetsi nez tvoje hadani");
    elif(int(guess) > nahodne):
        print("Hledane cislo je mensi nez tvoje hadani");
if(not uhodl):
    print("Neuhodl jsi cislo, treba priste");