# Desafío 4. Determinar años bisiestos 12
# Crear el código necesario para determinar si un año es bisiesto o no, para lo cual puede guiarse de la
# imagen siguiente (obtenidad de: https://docs.microsoft.com/es-es/office/troubleshoot/excel/determinea-leap-year)

 
año = int(input("Ingrese el año para veriricar si es o no bisiesto"))

if (año % 4 == 0 and año % 100 == 0) or año % 400 == 0:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} es no bisiesto") 

