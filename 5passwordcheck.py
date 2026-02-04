
while True:
    print("zadejte heslo: ")
    heslo1 = input()
    print("zadejte heslo znovu: ")
    heslo2 = input()
    if(heslo1 == heslo2):
        if(len(str(heslo1))>=8):
            print("vase heslo je dostatecne dlouhe")
            break
        else:
            print("Vase heslo je kratke")
            continue
    elif(heslo1 != heslo2):
        print("Hesla nesouhlasi")


