numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

if numero1 > numero2:
    numero_mayor = numero1
    numero_menor = numero2
else:
    numero_mayor = numero2
    numero_menor = numero1

print(numero_menor , numero_mayor)