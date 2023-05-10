def multiplo(numero):
    if (numero % 3 == 0):
        return True
    else:
        return False
num = int(input("dime un numero"))
print(multiplo(num))
