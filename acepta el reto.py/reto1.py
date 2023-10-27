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
        I=i+1
    elif ropa == "a":
        a=a+1
    else:("Control incorrecto")
print("valor",v,i,a)
    
if a< v > i :
    print("Es de verano")
if i > v < a :
    print("Es de invierno")
if i == a == v or :
    print("Son ambas")