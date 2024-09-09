def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo dado su ancho y alto."""
    return ancho * alto

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    return 0.5 * base * altura

def main():
    try:
        ancho = float(input("Introduce el ancho del rectángulo: "))
        alto = float(input("Introduce el alto del rectángulo: "))
        rect_area = calcular_area_rectangulo(ancho, alto)
        print(f"Área del rectángulo: {rect_area:.2f}")

        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        tri_area = calcular_area_triangulo(base, altura)
        print(f"Área del triángulo: {tri_area:.2f}")

    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()
