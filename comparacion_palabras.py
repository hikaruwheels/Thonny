def comparacion(palabra1, palabra2):
    if (palabra1 == palabra2):
        return "Son palabras iguales"
    else:
        return "No son iguales"
palabra1 = str(input("Dime una palabra "))
palabra2 = str(input("Dime otra palabra "))

print (comparacion(palabra1, palabra2))
