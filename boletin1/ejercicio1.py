#Ejercicio 1 escribir hola mundo
print("¡Hola mundo!")

#Ejercicio 2 escribir hola mundo con variables
mesage="¡Hola mundo!"
print("¡Hola mundo!")

#Ejercicio 3 
print("¿Hola, cómo te llamas?")
nombre=input("Introduzca su nombre por favor :")
print("¡Hola", nombre, "!" )
#Ejercico 4
print("El resultado de esta operación aritmética es el siguiente")
calculo=(((3+2)/(2*5))**2)
#res=(((3+2)/(2*5))**2)
print(calculo)

#Ejercicio 5
print("¿Cuantas horas llevas trabajadas?¿Cuanto es el coste por hora?")
coste=int(input("Introduzca el coste por favor :"))
horas=int(input("Introduzca las horas por favor :"))
calculo=(horas * coste)
#res=(hora * coste)
print(calculo)

#Ejercicio 6
n=int(input("Por favor introduzca un numero positivo entero "))
suma=(n*(n+1)/2)
#res=(n*(n+1)/2)
print(suma)

#Ejerccio 7
peso=int(input("Por favor introduce tu peso en kg"))
#poñemos float para numeros con decimais
estatura=float(input("Por favor introduzca su estatura en metro"))
#facemos o calculo
imc=peso* estatura
#imprimimos a solucion
print("Calcula el indice de masa corporal :", imc)

#Ejercicio 8
n=int(input("Por favor introduzca el primer numero entero n :"))
m=int(input("Por favor introduzca el segundo numero entero m :"))
calculo=(n/m)
#res=(n/m)
print(calculo)
resto=n%m
print("resto es igual a : ", resto)

#Ejercicio 9
print("¿Cuanto  es la cantidad a invertir, el interés anual y el número de años? ")
inversion=int(input("Cantidad de inversion :"))
interes=float(input("Cantidad de interes anual :"))
anos=int(input(" Numeros de  años :"))
calculo=(inversion*interes)
total=calculo*anos
print("El capital inicial es: ", inversion, "con un interés de: ", interes, "la cantidad final obtenida es: ", total+inversion)
#res=()
#Ejercicio 10
muñecas=int(input("Por favor introduzca el numero de muñecas que cada un apes 75 :"))
payasos=int(input("Por favor introduzca el numero de payasos que cada uno pesa 112 :"))
calculo=(muñecas*75+payasos*112)
print(calculo)

#Ejercicio 11
ahorros=float(input("Por favor introduzca la cantidad de ahorros de tu cuenta"))
calculo1=ahorros*0.04
print(calculo1)
calculo2=calculo1+ ahorros*0.04
print(round(calculo2,2)
calculo3=calculo1+calculo2+ahorros*0.04
print(round(calculo3,2))

#Ejercicio 12
normales=int(input("Por favor introduzaca el numero de barras :"))
vendidas=int(input("Introduzca un numero de barras que no son del dia y no han sido vendidas :"))
barras=3.49*normales
print("El coste de una barra del día es 3.49, con un descuento del 60% al no ser fresca, el precio sería", 3.49*0.6)

print("El coste total de las barras de día es ", barras)
calculo=3.49*vendidas*0.60
print("El coste total de las barras con descuento es ", calculo)