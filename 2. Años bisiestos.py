año = int(input("Ingrese su año:\n"))
if año <= 1599:
    if(año % 4 == 0):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")
else:
    if(año%100 == 0 and año%400 == 0):
        print(f"{año} es bisiesto")
    else:
        if(año%4 == 0):
            if(año%100 != 0 and año%400 == 0):
                print(f"{año} es bisiesto")
            else:
                print(f"{año} no es bisiesto")
        else:
            print(f"{año} no es bisiesto")
            