def listar_resultado(funcion):
    def wrapper(*args):
        args = [arg - 10 for arg in args]
        print("El resultado después de restar 10 a cada número pasado es:")
        print(funcion(*args))
        return (funcion(*args))
        print("¡Adiós!")
    return wrapper





# def listar_resultado(funcion):
#     def wrapper(*args):
#         arguments = []
#         print("El resultado después de restar 10 a cada número pasado es:")
#         for arg in args:
#             arg -= 10
#             arguments.append(arg)
#         print(funcion(*arguments))
#         print("Adio!")
#         return wrapper




# def listar_resultado(funcion):
#     def wrapper(num1, num2):
#         resultado = num1 - 10 + num2 -10
#         print("El resultado después de restar 10 a cada número pasado es:")
#         print(resultado)
#         print("¡Adiós!")
#     return wrapper


num1 = 10
num2 = 20

@listar_resultado
def suma_nums(*args):
    return sum(args)

if __name__ == "__main__":
    suma_nums(num1, num2)
