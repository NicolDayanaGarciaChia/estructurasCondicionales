numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
operador = (input("Ingresa el operador (+, -, *, /): "))

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2
    
else: 
    print("Operador no valido")
    
if operador in "+-*/":
    print(f"El resultado de la operacion {numero1} {operador} {numero2} es: {resultado}")
    