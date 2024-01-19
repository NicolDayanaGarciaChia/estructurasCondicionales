def calcular_division(a, b):
    cociente = a / b
    resto = a % b
    exacto = cociente.is_integer()
    return cociente, exacto, resto
a = int(input("diviendo: "))
b = int(int(input("divisor: ")))

cociente, exacto, resto = calcular_division(a , b)

if exacto:
    print("La division es exacta")
    print("cociente:", cociente)
    print("Resto: " , resto)
    
else: 
    print("la division no es exacta")
    print("cociente:", cociente)
    print("Resto", resto)