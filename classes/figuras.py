class Constantes:
    PI = 3.14159

def validar_valor_positivo(metodo):
    def envoltura(self, *args, **kwargs):
        if hasattr(self, 'lado') and self.lado <= 0:
            return 0
        return metodo(self, *args, **kwargs)
    return envoltura


class Cubo:
    def __init__(self, lado):
        self.lado = lado

    @validar_valor_positivo
    def volumen(self):
            return self.lado**3

    
    def area(self):
        if self.lado > 0:
            return self.lado**2 * 6
        else:
            return 0
    
class Cuboide:
    def __init__(self, altura, anchura, profundidad):
        self.altura = altura
        self.anchura = anchura
        self.profundidad = profundidad

    def volumen(self):
        return self.altura * self.anchura * self.profundidad
    
    def area(self):
        return 2 * (self.altura * self.anchura + self.altura * self.profundidad + self.anchura * self.profundidad)
    
class Esfera(Constantes):
    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        if self.radio > 0:
            return (4/3 * self.PI) * self.radio ** 3
        else:
            return 0
    
    def area(self):
        if self.radio > 0:
            return 4*self.PI * self.radio ** 2
        else:
            return 0