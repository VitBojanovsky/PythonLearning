print("Zadejte cisla do cyklu: ");
print("Zadejte cislo 1: ");
input1 = int(input());
print("Zadejte cislo 2: ");
input2 = int(input());
print("Zadejte skok: ");
jump = int(input());

if(input2 < input1):
    var = input1;
    input1 = input2;
    input2 = var;

if(jump < 0):
    jump = jump * -1;
for i in range(input1,input2+1,jump):
    print(i);
