import math as m

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    def area(self):
        pass
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = int(base)
        self.altura = int(altura)

    def area(self):
        return "Área: ", self.base * self.altura

    def perimetro(self):
        return "Perímetro: ", ((2*self.base) + (2*self.altura))

    def __str__(self):
        return f'{self.nombre}[Base: {self.base} \nAltura: {self.altura} ]'


class Circulo(Figura):
   def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = int(radio)
       
   def area(self):
        return (m.pi*(self.radio)**2)

   def perimetro(self):
        return ((2*m.pi) * self.radio)

   def __str__(self):
        return f'{self.nombre}[Radio: {self.radio}] '

def probar_figura(figura):
    print(figura)
    print("Area: ", figura.area())
    print("Perímetro: ",figura.perimetro())
