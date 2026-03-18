from math import factorial
'''
def absolutni_hodnota(n):
    return abs(int(n))
def factorial(x):
    x = absolutni_hodnota(x)
    factorial = 1
    if(x == 0):
        return factorial
    for i in range(1,int(x)+1,1):
        factorial = factorial*i
    return factorial
    '''

print("Zadejte cislo: ")
cislo = int(input())
#cislo = factorial(cislo)
cislo = factorial(cislo)
print(f"factorial je {cislo}")
