
#Calculadora de descuento.
def calcular_descuento(monto_total, porcentaje_descuento=10):

    # Calcula el descuento multiplicando el monto total por el porcentaje de descuento /100.
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento
print("Calculadora de descuento.\n")
# Primera llamada a la función con solo el monto total.
monto1 = 800.0
descuento1 = calcular_descuento(monto1)  # Llama a la función con el monto total.
monto_final1 = monto1 - descuento1  # Calcula el monto final a pagar.
print(f"Monto total sin descurento: ${monto1:.2f}")  # Muestra el monto total.
print(f"Monto final a pagar con descuento del 10 %: ${monto_final1:.2f}\n")  # Muestra el monto final a pagar.

# Segunda llamada a la función con monto total y porcentaje de descuento.
monto2 = 1500.0
porcentaje2 = 15  # Se define un porcentaje de descuento específico.
descuento2 = calcular_descuento(monto2, porcentaje2)  # Llama a la función con ambos parámetros.
monto_final2 = monto2 - descuento2  # Calcula el monto final a pagar.
print(f"Monto total sin descuento: ${monto2:.2f}")  # Muestra el monto total.
print(f"Descuento 15%: ${descuento2:.2f} ")  # Muestra el descuento aplicado.
print(f"Monto final a pagar con descuento del 15%: ${monto_final2:.2f}\n")  # Muestra el monto final a pagar.
print("Gracias por su compra.")