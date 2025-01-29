import os

os.system("clear")

class MiClase:
    def __init__(self, valor):
        self.valor = valor


    # def __str__(self):
    #     return f"Objeto de la clase Miclase con valor {self.valor}"
    
    # def __repr__(self):
    #     return f"Clase Miclase con valor {self.valor}"

    # def __len__(self): 
    #     return len(self.valor)

    # def __getitem__(self, index):
    #     return self.valor[index]

    # def __setitem__(self, index, nuevo_valor):
    #     self.valor[index] = nuevo_valor

    # def __delitem__(self, index):
    #     del self.valor[index]

    # def __call__(self, incremento):
    #     self.valor += incremento
    #     return self.valor



objeto = MiClase([10, 12])

print(objeto)
# print(objeto.__dict__)
# print(objeto.__dict__['valor'][0])
# objeto[1] = 35
# del objeto[0]
# print(objeto.valor)

# objeto_incrementado = MiClase(5)
# print(objeto_incrementado(2))

# print(objeto._MiClase__valor)
