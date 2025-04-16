"""
Módulo para cálculo de áreas de figuras geométricas.

Implementa una jerarquía de clases con:
- Clase abstracta FiguraGeometrica
- Implementaciones concretas: Rectángulo, Triángulo y Círculo
Cumple con PEP 8 y pasa Pylint con 10/10
"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta base para figuras geométricas."""

    @abstractmethod
    def calcular_area(self):
        """Calcula el área de la figura geométrica.

        Returns:
            float: Valor del área calculada
        """

    @abstractmethod
    def calcular_perimetro(self):
        """Calcula el perímetro de la figura geométrica.

        Returns:
            float: Valor del perímetro calculado
        """


class Rectangulo(FiguraGeometrica):
    """Representa un rectángulo y sus operaciones geométricas."""

    def __init__(self, base: float, altura: float):
        """Inicializa un rectángulo con base y altura.

        Args:
            base (float): Medida de la base
            altura (float): Medida de la altura
        """
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula área como base * altura."""
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """Calcula perímetro como 2*(base + altura)."""
        return 2 * (self.base + self.altura)

    def __str__(self) -> str:
        """Representación en cadena del rectángulo."""
        return f"Rectángulo (base={self.base}, altura={self.altura})"


class Triangulo(FiguraGeometrica):
    """Representa un triángulo rectángulo y sus operaciones."""

    def __init__(self, base: float, altura: float):
        """Inicializa un triángulo con base y altura.

        Args:
            base (float): Medida de la base
            altura (float): Medida de la altura
        """
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula área como (base * altura)/2."""
        return (self.base * self.altura) / 2

    def calcular_perimetro(self) -> float:
        """Calcula perímetro usando teorema de Pitágoras."""
        hipotenusa = (self.base**2 + self.altura**2)**0.5
        return self.base + self.altura + hipotenusa

    def __str__(self) -> str:
        """Representación en cadena del triángulo."""
        return f"Triángulo (base={self.base}, altura={self.altura})"


class Circulo(FiguraGeometrica):
    """Representa un círculo y sus operaciones geométricas."""

    PI = 3.141592653589793  # Constante de clase para π

    def __init__(self, radio: float):
        """Inicializa un círculo con radio.

        Args:
            radio (float): Medida del radio
        """
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula área como π * radio²."""
        return self.PI * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        """Calcula perímetro como 2 * π * radio."""
        return 2 * self.PI * self.radio

    def __str__(self) -> str:
        """Representación en cadena del círculo."""
        return f"Círculo (radio={self.radio})"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear figuras
    figuras = [
        Rectangulo(5, 3),
        Triangulo(4, 3),
        Circulo(2)
    ]

    # Calcular y mostrar propiedades
    for figura in figuras:
        print(f"\n{figura}")
        print(f"Área: {figura.calcular_area():.2f}")
        print(f"Perímetro: {figura.calcular_perimetro():.2f}")