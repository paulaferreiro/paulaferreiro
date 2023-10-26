inversion=int(input("Por favor introduzca su cantiadad a invertir: "))
interes=int(input("Por favor introduzca su interes anual: "))
años=int(input("Por favor introduzca los años: "))

for i in range(1,años+1,1):
    calculo=interes*inversion
    inversion=+calculo
    print("año",i,"->", calculo)

#el interés también puede ser float