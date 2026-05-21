from random import randint

while True:
    num1 = int(input("Ingrese límite inferior: "))
    num2 = int(input("Ingrese límite superior: "))
    if num1 < num2:
        break
    print("Error: El primer valor debe ser menor que el segundo. Intente de nuevo.\n")

numero = randint(num1, num2)

if numero % 2 != 0:  
    if (numero + 1) <= num2:
        numero = numero + 1
    else:
        numero = numero - 1

adivino = False

intento1 = int(input("Intente adivinar: "))

if intento1 == numero:
    print("Congratulations, lo has adivinado.")
    adivino = True
else:
    if intento1 < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

if not adivino:
    intento2 = int(input("Intente de nuevo: "))
    
    if intento2 == numero:
        print("Congratulations, lo has adivinado..")
        adivino = True
    else:
        if intento2 < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")
            
        distancia1 = abs(numero - intento1)
        distancia2 = abs(numero - intento2)
        
        print("Te daré una pista:")
        if distancia2 < distancia1:
            print(f"El número que buscas está más cerca de {intento2} que de {intento1}")
        elif distancia1 < distancia2:
            print(f"El número que buscas está más cerca de {intento1} que de {intento2}")
        else:
            print(f"Ambos intentos ({intento1} y {intento2}) están a la misma distancia.")


if not adivino:
    intento3 = int(input("Intente la última vez: "))
    
    if intento3 == numero:
        print("Congratulations, lo has adivinado.")
    else:
        print("Game Over.")
        print(f"El número era: {numero}")