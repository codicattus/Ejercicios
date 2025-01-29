import hashlib

class User:

    def __init__(self, nombre, apellido, password):
        self.__password = self.hash_password(password)
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre(self):
        return f"{self.__nombre}"
    
    @property
    def apellido(self):
        return f"{self.__apellido}"
    
    @nombre.setter
    def nombre(self, nuevo__nombre):
        if not isinstance(nuevo__nombre, str):
            raise TypeError("El nombre debe ser un string")
        self._nombre = nuevo__nombre
        print("Nombre cambiado a:", self._nombre)

    def hash_password(self, password):
        self.__encrypted_pass = hashlib.sha512(password.encode('utf-8')).hexdigest()

    @property
    def password(self):
        return self.__encrypted_pass

def main():

    new_user = User("Miguel", "Andrés", "Alondra")

    # print(new_user.nombre)
    # print(new_user.apellido)

    # new_user.nombre = "Juanjo"
    # print(new_user.nombre)
    # print(new_user.apellido)
    # print(new_user.password)
    # print(new_user.name)
    print(new_user.password)
    # new_user.__password = "loquete"
    # print(new_user.__password)


if __name__ == "__main__":
    main()

