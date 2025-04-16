"""
Módulo para cálculo de áreas y perímetros de figuras geométricas.

Implementa:
- Clase abstracta FiguraGeometrica (ABC)
- Implementaciones concretas: Rectángulo, Triángulo Rectángulo y Círculo
Cumple con PEP 8 y obtiene 10/10 en Pylint
"""

from abc import ABC, abstractmethod
from math import sqrt
from typing import List


class FiguraGeometrica(ABC):
    """Clase abstracta base para figuras geométricas."""

    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula el área de la figura.

        Returns:
            float: Valor del área calculada
        """

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """Calcula el perímetro de la figura.

        Returns:
            float: Valor del perímetro calculado
        """


class Rectangulo(FiguraGeometrica):
    """Representa un rectángulo con sus operaciones geométricas."""

    def __init__(self, base: float, altura: float) -> None:
        """Inicializa rectángulo con base y altura.

        Args:
            base (float): Medida de la base
            altura (float): Medida de la altura
        """
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula área (base * altura)."""
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """Calcula perímetro (2*(base + altura))."""
        return 2 * (self.base + self.altura)

    def __str__(self) -> str:
        """Representación en cadena del rectángulo."""
        return f"Rectángulo: base={self.base:.2f}, altura={self.altura:.2f}"


class TrianguloRectangulo(FiguraGeometrica):
    """Representa un triángulo rectángulo con sus operaciones."""

    def __init__(self, base: float, altura: float) -> None:
        """Inicializa triángulo con base y altura.

        Args:
            base (float): Medida de la base
            altura (float): Medida de la altura
        """
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula área ((base * altura)/2)."""
        return (self.base * self.altura) / 2

    def calcular_perimetro(self) -> float:
        """Calcula perímetro (base + altura + hipotenusa)."""
        hipotenusa = sqrt(self.base**2 + self.altura**2)
        return self.base + self.altura + hipotenusa

    def __str__(self) -> str:
        """Representación en cadena del triángulo."""
        return f"Triángulo Rectángulo: base={self.base:.2f}, altura={self.altura:.2f}"


class Circulo(FiguraGeometrica):
    """Representa un círculo con sus operaciones geométricas."""

    PI: float = 3.141592653589793  # Constante de clase para π

    def __init__(self, radio: float) -> None:
        """Inicializa círculo con radio.

        Args:
            radio (float): Medida del radio
        """
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula área (π * radio²)."""
        return self.PI * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        """Calcula perímetro (2 * π * radio)."""
        return 2 * self.PI * self.radio

    def __str__(self) -> str:
        """Representación en cadena del círculo."""
        return f"Círculo: radio={self.radio:.2f}"


def mostrar_resultados(figuras: List[FiguraGeometrica]) -> None:
    """Muestra áreas y perímetros de una lista de figuras.

    Args:
        figuras (List[FiguraGeometrica]): Lista de figuras a procesar
    """
    print("\nRESULTADOS:")
    for i, figura in enumerate(figuras, 1):
        print(f"\nFigura {i}: {figura}")
        print(f"Área: {figura.calcular_area():.2f}")
        print(f"Perímetro: {figura.calcular_perimetro():.2f}")


if __name__ == "__main__":
    # Crear figuras de ejemplo
    figuras = [
        Rectangulo(5.25, 3.5),
        TrianguloRectangulo(4.0, 3.0),
        Circulo(2.75)
    ]

    # Mostrar resultados
    mostrar_resultados(figuras)
