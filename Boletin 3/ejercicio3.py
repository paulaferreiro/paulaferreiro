#pedimos un numero entero positivo
n=int(input("Por favor introduzca un numero entero positivo: "))

#control de errores
if n <= 0:
     print("Error.El numero introducido no es entero")
else:
    for i in range(1, n+1, 2):
        print(i)
#donde empiezas,donde acabas y que saltos das