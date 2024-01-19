def tipo_triangulo(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return "No es un triangulo valido"
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triangulo valido"
    if a == b == c:
        return "Es un triángulo equilátero"
    if a == b or a == c or b == c:
        return "Es un triángulo isósceles"
    return "Es un triángulo escaleno"

a = float(input("Ingrese el primer lado del triángulo: "))
b = float(input("Ingrese el segundo lado del triángulo: "))
c = float(input("Ingrese el tercer lado del triángulo: "))

print(tipo_triangulo(a, b, c))
