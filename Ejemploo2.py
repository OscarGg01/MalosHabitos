def calcular(a, b, c):
    """Realiza la operación a * b + c y devuelve el resultado."""
    return a * b + c
def principal():
    try:
        # Solicitamos al usuario que ingrese los valores
        Numero01 = float(input("Introduce el valor de x: "))
        Numero02 = float(input("Introduce el valor de y: "))
        Numero03 = float(input("Introduce el valor de z: "))

        resultado = calcular(Numero01, Numero02, Numero03)

        print(f"El resultado de {Numero01} * {Numero02} + {Numero03} es: {resultado}")

    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")


# Ejecutamos la función principal
if __name__ == "__main__":
    principal()
