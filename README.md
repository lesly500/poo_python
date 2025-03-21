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

     ## Encapsulación
- Se trata de la protección de los datos de usos o accesos no controlados.
- Los datos (atributos) que componen una clase pueden ser de dos tipos:
    - Públicos:  los datos son accesibles sin control, es decir, los datos pueden ser usados sin ningún tipo de mecanismo que proteja ante usos no autorizados o indebidos.
    - Privados: los datos no pueden ser accedidos sin control y para acceder a ellos se deberá implementar un método que acceda a ellos.  De esta forma, los datos serán accedidos única y directamente por la propia clase.
- La encapsulación no solo puede realizarse sobre los atributos de la clase, también es posible realizarla sobre los métodos, es decir, aquellos métodos que indiquemos que son privados no podrán ser utilizados por elementos externos al propio objeto.
- La definición de atributos y metodos privados se realiza incluyendo los caracteres "__" (dos guiones de piso) entre la palabra "self" y el nombre del atributo.

## Herencia
- Permite la reutilización de código.
- Consiste en la definición de una clase utilizando como base una clase ya existente.
- La nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliará el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.
- Significa que entre dos clases existe una relación del tipo "es un".
- La herencia en Python se especifica de la siguiente manera: ``class NombreClase(ClaseBase):``
- Ejemplo:
    - Pensemos en una persona como una clase, la persona tendría una serie de atributos como pueden ser el nombre, los apellidos, la edad, etc.  Esas características de una persona serían compartidas por todas aquellas clases hijas como pueden ser alumno y profesor.  Es decir, alumno y profesor heredarían las propiedades de la clase persona y tendrían sus propias propiedades, diferentes entre ellas, como por ejemplo el curso en el que está el alumno y el horario de tutorias del profesor.

    - Clase base: Persona
        - Atributos:
            - Nombre
            - Apellidos
            - Edad

    - Clase derivada: Alumno
        - Atributos:
            - Curso
            - Asignaturas
    
    - Clase derivada: Profesor
        - Atributos:
            - Antigüedad
            - Tutorias
            - Teléfono

## Actividad:
- Consulte un ejemplo práctico del uso de herencia múltiple en Python

### Bibliografía
Moreno, A. y Córcoles, S.  (2020).  Python práctica.  Herramientas, conceptos y técnicas.  Ediciones de la U.