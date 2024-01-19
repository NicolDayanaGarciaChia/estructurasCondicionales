def numero(numero1, numero2, numero3, numero4):
    if numero1 > numero2:
       numero1, numero2 = numero2, numero1
    if numero1 > numero3:
        numero1, numero3 = numero3, numero1
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1
    if numero2 > numero3:
        numero2, numero3= numero3, numero2
    if numero2 > numero4:
        numero2, numero4 = numero4, numero2
    if numero3 > numero4:
        numero3, numero4 = numero4, numero3
        return numero1, numero2, numero3, numero4

numero1 = int(input("ingrese un numero\n"))
numero2 = int(input("ingrese un numero\n"))
numero3 = int(input("ingrese un numero\n"))
numero4 = int(input("ingrese un numero\n"))

numero = numero(numero1, numero2, numero3, numero4)
print("los numeros ordenados de menor a mayor son: \n",numero)
