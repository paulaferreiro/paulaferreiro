#ordena el armario
print("Hola!,bienvenido a tu armario desordenado")
armario=input("Por favor introduzca el cotenido de tu armario: ")
#print("string ->",armario)

#como convertir un string en una lista,split(para cortar) 
armario_lista= armario.split()
#print("lista ->",armario_lista)
v=0
i=0
a=0

for ropa in armario_lista:
    if ropa == "V":
        v=v+1
    elif ropa =="I":
        i=i+1
    elif ropa == "A":
        a=a+1
    else:("Control incorrecto")
print("valor",v,i,a)
    
if v > i and v > a :
    print("Es de verano")
elif i > v and i > a:
    print("Es de invierno")
elif (a > v and a > i) or a==i==v :
    print("Son ambas")
else:
    print("opcion no contemplada")