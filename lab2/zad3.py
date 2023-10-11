def suma_int(tab):
    suma = 0
    for x in tab:
        if type(x)==int:
            suma+=x
    return suma

print(suma_int([1, 5.4, 7, "Ala", 42, True]))