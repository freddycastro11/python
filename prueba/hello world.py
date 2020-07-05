print("Hello", "Freddy")

if 5 > 2:
    print("Cinco es mayor a Dos")

#Esto es un comentario

if 5 > 2:
    print("Five is greater than two!")#Tienes que poner los bloques de espacio bien
if 5 > 2:
        print("Five is greater than two!")

x = 5 #esto es una variable
y = "Hello, Freddy!"

print(x)
print(y)

#Nombres para variables
myvar = "John1"
my_var = "John2"
_my_var = "John3"
myVar = "John4"
MYVAR = "John5"
myvar2 = "John6"

print(MYVAR)

x, y, z = "Naranja", "Banana", "Cereza"
print(x)
print(y)
print(z)
####  Mismo valor a multiples variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Para combinar texto y una variable, Python usa el carácter +:
x = "Asombroso!!!!"
print("Python is " +x)

x = "Python es "
y = "asombroso"
z = x + y 
print(z)
#NO COMBINAR NUMEROS CON LETRAS
x = 50
y = 25
print(x + y)
#CREAR VARIBLE FUERA DE UNA FUNCION Y USARLA DENTRO DE ELLA

x = 'Asombroso afuera de la funcion'

def mifuncion():
    print("Pyton es " + x)
mifuncion()
#   USANDO 2 VARIBALES UNA AFUERA Y OTRA ADENTRO


x = "asombroso "

def myfunc():
    x = "fantastico"
    print("Python es " + x)

myfunc()

print("Python1 es " + x)

#Variables golbales


def myfunc1():
    global x
    x = "fantastic"


myfunc1()

print("Python is " + x)

x = 5
print(type(x))#se obtiene el tipo de dato que es
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#posiciones en los texto H es 0, e es 1
a = "Hello, World!"
print(a[1])

#posciones entre el 2 y el 5
b = "Hello, World!"
print(b[2:5])

#lower-> devuelve la cadena en minuscula
#upper-> devuelve la cadena en mayuscula

# numeros y textos
age = 36
txt = "My name is John, and I am {}"#{} se usa para numeros
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Operaciones booleanas
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


def myFunction():#Imprimir YES si ña funcion es true
    return  True

if myFunction():
    print("YES!")
else:
    print("NO!")


#comprobar si un articulo existe
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#agregar un elemento
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#eliminar un  articulo
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#copia de listas
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#UNIR LAS 2 LISTAS
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#cambio de valores
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#para ordenarlos
thisset = {"Manzana", "banana", "Cereza", "Sandia"}

for x in thisset:
    print(x)

x = 2
y = 2
res = 8
res = x*y
x = 6
res = x*y
res = res+2
print(res)

z= "son las "
x= str(3+12)
print(z + x)

z = str(5)
x = str(2)
print(z + x)
