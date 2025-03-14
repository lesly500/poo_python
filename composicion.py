# Composicion

"""Una coordenada en dos dimensiones esta compuesta por dos valores, el valor en el eje e las x y valor en el eje de las y, esto podria ser una clase. Un cuadro esta compuesto por cuatro coorenadas que son os cuatos vertices, esto podria ser una clase que esta compuesta por cuatros clases del objetos coordenada."""

# Clase coordenada

class Coordenada:

    # metodoconstructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # metodo para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.X, ",", self.Y, ")")

# clases cuadros

class Cuadrado:

    # metodo constructor
    def __init__(self, v1,v2,v3,v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

     # metodo para mostrar los vertices
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()

# metodo principal
def main():
    # input 
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("Digite el valor de y: "))

    # processign
    c1 = Coordenada(x1,x2) 
    c1.mostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()


if __name__ =="__main__":
    main()    