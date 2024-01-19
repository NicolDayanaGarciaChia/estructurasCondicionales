def diferencia_longitud(palabra1, palabra2):

    diferencia = len(palabra1) - len(palabra2)

    if diferencia > 0:
        resultado = f"{palabra1} es {diferencia} letras más larga que {palabra2}."
    elif diferencia < 0:
        resultado = f"{palabra2} es {-diferencia} letras más larga que {palabra1}."
    else:
        resultado = f"{palabra1} y {palabra2} tienen la misma longitud."

    return palabra1 if abs(diferencia) <= len(palabra2) else palabra2, diferencia, resultado

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")


palabra_mas_larga, diferencia, resultado = diferencia_longitud(palabra1, palabra2)

print(resultado)


