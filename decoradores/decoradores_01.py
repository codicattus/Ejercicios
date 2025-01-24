def decorador(funcion):
    def contenido(*args, **kwargs):
        print(f"función recibida: {funcion.__name__}")
        print(f"argumentos recibidos: {args}, {kwargs}")
        funcion_modificada = funcion(*args)
        return funcion_modificada
    return contenido

def comprobar_numeros(funcion):
    def contenido(*args):
        for arg in args:
            if arg <= 0:
                return "Todos los números han de ser mayores a cero"
        return funcion(*args)
    return contenido

#@decorador
def division(x,y):
    return x/y

division = comprobar_numeros(division)
print(division(8,0))
