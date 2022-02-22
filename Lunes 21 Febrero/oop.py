# Programacion orientada a objetos

# Clase -  Objeto

# Objeto - Coleccion de datos y comportamientos
# Clase  molde para crear objetos

# Empleado  -> Id, Salarym, Departmtamento.  -> Comportamientos -> Metodos,  ingresar , subir, bajar


class Employee:
    ID = None
    salary = None
    deparment = None
    rol = None

Steve = Employee()
print(Steve)

print(Steve.ID)
print(Steve.salary)
print(Steve.deparment)
print(Steve.rol)
print ("----")

Steve.ID = 3438
Steve.salary = 34343
Steve.deparment = "RRHH"
Steve.rol = "Recruiter"
print(Steve.ID)
print(Steve.salary)
print(Steve.deparment)
print(Steve.rol)

# Tiempo de vida -> Creacion -> Inicializacion -> Destruccion

class Person:

    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


#print(Person.ID)
Sabina = Person(
    ID=4242, salary=2242424, department="Tech"
)

print(Sabina.department)
Sabina.department = "Product"
print(Sabina.department)

class PersonDirective:

    def __init__(self, ID, salary, department="directive"):
        self.ID = ID
        self.salary = salary
        self.department = department

diego = PersonDirective(
    42323, 3232
)
print (diego.department)

#johany = PersonDirective()
#print(johany)
#print(johany.ID)
#print(johany.department)

# Variables de clase, Variables de Instancia

class Player:
    team_name = "liverpool"

    def __init__(self, name):
        self.name = name

p1 = Player("Mark")
p2 = Player("Steve")

print ("Name: ", p1.name)
print ("TEam:  ", p1.team_name)

print ("Name: ", p2.name)
print ("TEam:  ", p2.team_name)
p2.team_name = "Manchester"
print ("TEam:  ", p2.team_name)

print ("TEam:  ", p1.team_name)


# Un metodo es un grupo de declaraciones que
# ejecuta algunas instrucciones y puede o no retornar un resultado

class Employee:
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def salary_per_day(self):
        return self.salary/30

    def tax(self):
        return  self.salary * 0.2

print ("ppppppp")
jacobo = Employee(12443434, salary=5400, department="Lead Tech")
print (jacobo.salary)
print (jacobo.salary_per_day())
print (jacobo.tax())