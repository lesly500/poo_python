# Crear un sistema de clases para representar vehículos que puedan tener motor y ruedas, y además, algunos vehículos tienen la capacidad de flotar. Usaremos herencia múltiple para combinar estos comportamientos.

class Motor:
    def encender_motor(self):
        print("Motor encendido")

    def apagar_motor(self):
        print("Motor apagado")

class Ruedas:
    def inflar_ruedas(self):
        print("Ruedas infladas")

    def desinflar_ruedas(self):
        print("Ruedas desinfladas")

class Coche(Motor, Ruedas):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
mi_coche.mostrar_informacion()  # Método propio de Coche
mi_coche.encender_motor()       # Método heredado de Motor
mi_coche.inflar_ruedas()        # Método heredado de Ruedas

