class User:

    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return f"{self._nombre}"
    
    @property
    def apellido(self):
        return f"{self._apellido}"
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser un string")
        self._nombre = nuevo_nombre
        print("Nombre cambiado a:", self._nombre)



if __name__ == "__main__":
    new_user = User("Miguel", "Andrés")

    print(new_user.nombre)
    print(new_user.apellido)

    new_user.nombre = "Juanjo"
    print(new_user.nombre)



