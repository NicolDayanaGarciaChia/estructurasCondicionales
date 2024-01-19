caracter = input("ingresa un caracter: ")
if len (caracter) == 0:
    print("No ingresaste nigun caracter")
    
elif caracter.isalpha():
    if caracter.isupper():
        print(f"El caracter '{caracter}' es una letra mayuscula")
    else:
        print(f"El caracter '{caracter}' es una letra minuscula")
elif caracter.isdigit():
    print(f"El caracter '{caracter}' es un numero")
else:
    print(f"El caracter '{caracter}' no es una letra, numero")
    