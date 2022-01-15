from FigurasGeometricas.Perimetro import (perimetroTriangulo,
    perimetroCuadrado, perimetroRectangulo, perimetroCirculo)
from FigurasGeometricas.Area import areaTriangulo, areaCuadrado, areaRectangulo, areaCirculo

print("Perimetro:")
print("Triangulo:", perimetroTriangulo(5))
print("Cuadrado:", perimetroCuadrado(9))
print("Rectangulo:", perimetroRectangulo(5,4))
print("Circulo:", perimetroCirculo(8))

print("Area:")
print("Triangulo:", areaTriangulo(5, 3))
print("Cuadrado:", areaCuadrado(9))
print("Rectangulo:", areaRectangulo(5,4))
print("Circulo:", areaCirculo(8))