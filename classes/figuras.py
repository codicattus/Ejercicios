class Constantes:
    PI = 3.14159

def decorador(funcion):
    def contenido(*args):
        instancia = args[0]
        print(instancia.__dict__)
        for valor in instancia.__dict__.values():
            if valor <= 0:
                return "Todos los valores deben ser positivos y mayores que cero. Valor inválido"
            else:
                resultado = funcion(*args)
        return resultado
    return contenido


class Cubo:
    def __init__(self, lado):
        self.lado = lado

    @decorador
    def volumen(self):
            return self.lado**3
    
    @decorador
    def area(self):
        return self.lado**2 * 6
    
class Cuboide:

    def __init__(self, altura, anchura, profundidad):
        self.altura = altura
        self.anchura = anchura
        self.profundidad = profundidad

    @decorador
    def volumen(self):
        return self.altura * self.anchura * self.profundidad
    
    def area(self):
        return 2 * (self.altura * self.anchura + self.altura * self.profundidad + self.anchura * self.profundidad)
    
class Esfera(Constantes):

    def __init__(self, radio):
        self.radio = radio
    @decorador
    def volumen(self):
        return (4/3 * self.PI) * self.radio ** 3
    
    @decorador
    def area(self):
        return 4*self.PI * self.radio ** 2
