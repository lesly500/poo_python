# poo_python

- El paradigma de poo esta basado en una abtraccion del mundo real que nos va a permitir desarrollar programasnde forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y acciones que podemos hacer hacer con ellos.

## Clase

- Una clase es un tipo de dato cuyas variables se llaman objetos o instancia.
- La clase es la difinicion del mundo real y los objetos o instancias son el "propio" objeto del mundo real.
-Las clases estan compuestas por dos elementos: atributos y metodo.

## Atributos
-Informacion que almacena la clase

### Metodos
- Operaciones que pueden realizar las clases

## Definicion de una clase  en Pytho

```Python
class NombreClase:

  def __init__(self, variable1, variable2):
       self.Atributo1 = valor1
       self.Atributo2 = valor2

  def nombreMetodo(self):
    bloqueCodigo
```    
### componentes

```class```: palabra reservada en Python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear.

```def```:palabra reservada en Python que se utiliza para definir tanto el constrctor de la clase (metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodos que tiene.

```__init__```: palabra reservada en Python para definir el metodos constructor de la clase. Es lo primero que se ejecuta cuandp crear un objeto de una clase.

```(self, variableX)```: parametro del construtor de la clase. El parametro self es obligatorio y despues puesdes tener tantos parametros como quieras. La forma de añadir parametro es la misma que en las funciones.

```self.AtributoX```:forma de utilizacion y acceso a los atributos de la clases.

``` nombreMetodo```: nombre del metodo de la calse

```(self)```:parametros del metodo. El parametro self es onligatorio y despues puedes tener tantos parametros cmo quieras. La foma de añdir parametro es la misma que las funciones.

```bloquedoCodigo```: instrucciones que  ejecutara el metodo.

- cuando  defines una clase debes tener en cuenta los siguientes puntos:
   - Puedes definir tanto atributos como necesites.
   - puedes definir tantos metodos como necesites.
   - Puedes definr tntoparametros en el 
   
   ## Composicion
   - Consiste en la creacion de nuevas clases a partir de otras clases ya exisitentes que actuan como elementos compositores de la nueva.
   - Las clases existentes seran atributos de nueva clases.
   - En POO la composicion significa que entre las dos clases existe una relacion del tipo "tiene un".
   - Ejemplo:
     - Una coordenada en dos dimensiones esta compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, esto pdria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que son los cuatros vertices, esto podria ser una clase que esta compuesta por cuatro clases de objeto coordenada.