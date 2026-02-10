'''x=0;
for i in range(0,101):
    print(f"{i}", end=" ");
    if(i<=10):
        x+=i;
print(f"\nSoucet cisel od 0 do 10 je: {x}");
'''
print("Zadejte vstup: ");
vstup = input();
for i in range(0, len(vstup)):
    print(f"{vstup[i]}", end=" ");