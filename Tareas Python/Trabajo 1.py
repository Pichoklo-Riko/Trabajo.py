# Valor de los medicamentos y su despacho

valor_base_medicamentos = 60000
valor_despacho = 8000

# Datos del usuario

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B. C, D): ").strip().upper()

# Descuentos

if edad <= 30:
    if tramo == 'A' or tramo == 'B':
        descuento_medicina = 0.18
    elif tramo == 'C' or tramo == 'D':
        descuento_medicina = 0.12
elif 31 <= edad <= 60:
    if tramo == 'A' or tramo == 'B':
        descuento_medicina = 0.12
    elif tramo == 'C' or tramo == 'D':
        descuento_medicina = 0.08
else:
    descuento_medicina = 0.0

# Descuento del despacho

if tramo == 'A' or tramo == 'B':
    descuento_despacho = 0.10
    if edad >= 55:
        descuento_despacho += 0.05
else:
    descuento_despacho = 0.0

#Cálculo de los valores

valor_final_medicamentos = int(valor_base_medicamentos * (1 - descuento_medicina))
valor_final_despacho = int(valor_despacho * (1 - descuento_despacho))

print(f"El valor del medicamento es: {valor_final_medicamentos}")
print(f"El valor final del desapcho es: {valor_final_despacho}")
