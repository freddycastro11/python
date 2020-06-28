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
