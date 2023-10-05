#Ejercicio1
print("¿Cuantos años tienes?")
edad=int(input("Por favor introduzca su edad"))
if edad < 18 :
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
print(edad)

#Ejercicio 2
contraseña=input("contraseña").lower()
print("¿Cual es tu contraseña?")
print(contraseña)

#Ejercicio 3
numero1=float(input("Por favor introduzca numero1"))
numero2=float(input("Por favor introduzca numero2"))
if numero2 ==0:
    print("Error")
else:
    print("Esta correcto")
    calculo=(numero1/numero2)
    print(calculo)

#Ejercicio 4
numero=int(input("Por favor introduzca un numero enetero"))
if numero%2==0 :
    print("Es par")
else:
    print("Es impar")
    
#Ejercicio 5
print("Para que puedas tributar tienes que ser mayor de 16 añoss y tener unos ingresos iguales o superiores a 1000 € mensuales")
print("¿Cuantos años tienes y cuales son tus ingresos mensuales?")
edad=int(input("Por favor introduzca su edad"))
ingresos=float(input("Por favor introduzca sus ingresos mensuales"))
if edad<16 and ingresos <1000:
    print(" No puedes tributar")
else:
    print("Puedes tributar")
    
#Ejercicio6