# Information Hiding
# Encasuplation - Abstraction (Polimorfismot)

# PAciente -> visita un hospital -> Doctor ->Diagnostica -> Una medicina

# Encapsulacion - Se refiere a linkead data y metodos para manipulara esa data
# getter setter
# getter - > Metordo que nos permite leer el valor de una propiedad
# setter -> Modificar el valor de una propiedad

class User:
    def __init__(self, username=None):
        self.__username = username

    def set_user_name(self, x):
        self.__username = x

    def get_user_name(self):
        return  self.__username

steve = User("Steve 1")
print(steve.get_user_name())

steve.set_user_name("Steve 2")
print(steve.get_user_name())


class User:
    def __init__(self, username=None):
        self.__username = username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username


mark = User(
    "Mark1"
)
print(mark.username)
mark.username = 4
print(mark.username)

class User:
    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.password = password

    def login(self, user_name, password):
        if self.user_name.lower() == user_name.lower() and self.password == password:
            print("Tienes acceso")
        else:
            print("Credenciales invalidas")


steve = User("Steve", "12345")
steve.login("steve", "12345")
steve.login("steve", "6789")
steve.password= "6789"
steve.login("steve", "6789")



class User:
    def __init__(self, user_name=None, password=None):
        self.__user_name = user_name
        self.__password = password


    def login(self, user_name, password):
        if self.__user_name.lower() == user_name.lower() and self.__password == password:
            print("Tienes acceso")
        else:
            print("Credenciales inválidas")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, values):
        old_password, new_password = values
        if old_password == self.__password:
            self.__password = new_password


steve = User("Steve", "12345")

steve.login("steve", "12345")
steve.login("Steve", "6789")
steve.password= ("12345", "6789")
steve.login("Steve", "6789")