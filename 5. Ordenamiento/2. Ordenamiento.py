def numeros(numero1, numero2, numero3):
    if numero1 > numero2:
        numero1,numero2 = numero2,numero1
    if numero1 > numero3:
        numero1,numero3 = numero3,numero1
    if numero2 > numero3:
        numero2,numero3 = numero3,numero2
    return(numero1, numero2, numero3)

numero1 = int(input("Ingrese un numero\n"))
numero2 = int(input("Ingrese un numero\n"))
numero3 = int(input("Ingrese un numero\n"))

numeros = numeros(numero1 , numero2 , numero3)
print("los numeros ordenados de menor a mayor son:\n", numeros)