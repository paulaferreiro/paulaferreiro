#programa que compruebe si una palabra es un palíndromo
palabra=input("Por favor introduzca la palabara: ")
palabra_inv=""
#solo comillas para indicar que es una cadena
for i in range (len(palabra),0,-1):
    #print(palabra[i-1])
#al imprimir cuenta los espacios
    palabra_inv=palabra_inv+palabra[i-1]
print(palabra_inv)
if palabra==palabra_inv:
    print("Es palíndromo")
else:
    print("No es palíndromo")
    
