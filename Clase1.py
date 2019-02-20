#! /usr/bin/env python3

print("1.- ¿Cuales son los dos valores de tipo datos booleanos? ¿Cómo se escriben?")

print('\v') # Este comando imprime un espacio

print("True y False")

print('\v')

print("2.- ¿Cuáles son los tres operadores booleanos?")

print('\v')

print("AND, OR y NOT")

print('\v')

print("3.- Tablas de verdad") 
print('\v')

booleanos = [False, True]

# Tabla de verdad and
print("AND")
print("x\ty\tx and y") # El comando \t es para tabular
for x in booleanos:
	for y in booleanos:
		print(x, y, x and y, sep = "\t")
print()

# Tabla de verdad de or
print("OR")
print("x\ty\tx or y")
for x in booleanos:
	for y in booleanos:
		print(x, y, x or y, sep = "\t")
print()

# Tabla de verdad de not
print("NOT")
print("x\tnot x")
for x in booleanos:
	print(x, not x, sep = "\t")
print()

print('\v')

print("4.- ¿Cuáles son los seis operadores de comparación?")

print('\v')

print("== (verdadero cuando dos variables son iguales), != (verdadero si dos variables son diferentes), > (verdadero si la variable de la izquierda es mayor que la de la derecha), < (verdadero si la variable de la izquierda es menor que la de la derecha), >= (verdadero si la variable de la izquierda es mayor o igual a la de la derecha), <= (verdadero si la variable de la izquierda es menor o igual a la de la derecha)")

print('\v')

print("5.- ¿Cuál es la diferencia entre el operador igual y el operador de asignación?")
print('\v')
print("El operador asignación se utiliza para asignar un valor determinado a una variable, mientras que el operador igual evalúa si una variable es igual a otra")
print('\v')
print('\v')
print("6.- Explique qué es una condición y dónde la usaría")
print('\v')
print('\v')
print("Una condición permite que el programa ejecute cierta instrucción cuando se presente o se cumpla alguna situación que nosotros podemos determinar y que se comporte de otra manera cuando esta situación esté ausente. La usamos cuando queremos que se evalúe una situación antes de que el programa tome una acción o cuando la variable puede tomar varios valores que cambian la manera en que se debe comportar el programa.")
print('\v')
print("7.- ¿Qué puede hacer si su programa está atascado en un bucle infinito?")
print('\v')
print("Existen comandos que detienen el programa y evitan que este quede atascado en bucles infinitos, por ejemplo el comando break o el comando continue.")
print('\v')
print("8.- ¿Cuál es la diferencia entre romper y continuar?")
print('\v')
print("Break termian el bucle que lo contiene y el programa pasa directamente al enunciado que procede al cuerpo del bucle. Continue se salta el codigo dentro del bucle por una iteración, de esta manera el bucle no termina si no que comienza con la siguiente iteración.")
print('\v')
print("9.- ¿Cuál es la diferencia entre rango (10), rango (0,10) y rango (0,10,1) en un bucle for?")
print('\v')
print("range(10) enlista los numeros del 0 al 9, pues no incluye al número dentro del paréntesis, range(0,10) enlista los numeros del 0 al 10, en este caso el primer argumento es 0 pero podria ser cualquier número que le indica al programa en dónde comenzar a contar, range(0,10,1) enlista los números del 0 al 9 tomando pasos iguales a 1; en este caso el ultimo argumento le indica al programa cómo debe ir aumentando los valores, es decir el tamaño de los saltos que debe tomar entre los valores.")
print('\v')
print("10.- Escribe un programa que imprima los primeros N números y su suma usando un bucle for y luego un programa que imprima los números del 1 al 10 usando un bucle while")
print('\v')
#para bucle for
print("Bucle for")
print('\v')
n = int(input( "Introduce un número natural: " ))
i = 1
suma = 0

for i in range(0,n+1):
	print(i)
	suma += i
	print("La suma es",suma)
print('\v')
#para bucle while. Utilizo las mismas variables con la condición de que sólo se imprime y se calcula la suma de los primeros 10 números.
print("Bucle while")

i = 1
sum = 0
while i <= 10:
        print(i)
        sum = sum + i
        i = i + 1
        print("La suma es",sum)
print('\v')
print("11.- Escriba un programa que imprima los primeros M numeros impares")
print('\v')
m = int(input("Introduce un número: "))
for i in range(1,m + 1,2):
        print(i)
print('\v')
print("12.- Escriba un programa que calcule los primeros N términos de la serie de fibonacci")
print('\v')

term = int(input("Introduce el número de términos que deseas calcular: "))
n1 = 0
n2 = 1
cuenta = 0

if term <= 0:
	print("Introduce un entero positivo")
elif term == 1:
	print("La secuencia de Fibonacci hasta el número",term,"es:")
	print(n1)
else:
	print("La secuencia de Fibonacci hasta el número",term,"es:")
	while cuenta < term:
		print(n1,end=' , ')
		nth = n1 + n2
		n1= n2
		n2= nth
		cuenta += 1
print('\v')
print("13.- Escriba un programa que calcule el factorial de un número N")

num = int(input("Introduce un número: "))
factorial = 1

if num < 0:
	print("Introduce un número positivo")
elif num == 0:
	print("El factorial de 0 es 1")
else:
	for i in range(1,num + 1):
		factorial = factorial*i
	print("El factorial de",num,"es",factorial)

