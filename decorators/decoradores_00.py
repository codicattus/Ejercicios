# def funcion_decoradora(funcion):
#     def funcion_que_decora():
#         print("El resultado de la operación es: ")
#         resultado = funcion()  # Guardamos el resultado de la función original.
#         print(resultado)  # Mostramos el resultado de la operación.
#         print("Ciao!")
#         return resultado  # Devolvemos el resultado de la función original.
#     return funcion_que_decora

def listar_resultado(funcion):
    def wrapper(*args):
        print("El resultado es:")
        print(funcion(*args))
        print("Adio!")
    return wrapper





# @funcion_decoradora
# def suma():
#     return 3 + 2

# @funcion_decoradora
# def resta():
#     return 3 - 2

num1 = 10
num2 = 20
num3 = 30

@listar_resultado
def suma_nums(num1, num2, num3):
    return num1 + num2 + num3

if __name__ == "__main__":
    # suma()
    # resta()
    suma_nums(num1,num2)