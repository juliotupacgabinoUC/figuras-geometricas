"""
Script para calcular áreas de figuras geométricas.

Contiene implementaciones de Rectángulo, Triángulo y Círculo,
siguiendo los principios de POO y las convenciones PEP 8.
"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""
        pass


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo y proporciona su cálculo de área."""

    def __init__(self, base, altura):
        """Inicializa el rectángulo con base y altura.

        Args:
            base (float): Longitud de la base del rectángulo.
            altura (float): Altura del rectángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo.

        Returns:
            float: Área calculada (base * altura).
        """
        area = self.base * self.altura
        return area


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo y proporciona su cálculo de área."""

    def __init__(self, base, altura):
        """Inicializa el triángulo con base y altura.

        Args:
            base (float): Longitud de la base del triángulo.
            altura (float): Altura del triángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo.

        Returns:
            float: Área calculada (base * altura / 2).
        """
        area = (self.base * self.altura) / 2
        return area


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo y proporciona su cálculo de área."""

    PI = 3.14159  # Constante de clase para el valor de Pi

    def __init__(self, radio):
        """Inicializa el círculo con su radio.

        Args:
            radio (float): Radio del círculo.
        """
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo.

        Returns:
            float: Área calculada (PI * radio^2).
        """
        area = self.PI * (self.radio ** 2)
        return area


# Constantes para configuración
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

if __name__ == "__main__":
    # Crear instancias de figuras geométricas
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular y mostrar áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")