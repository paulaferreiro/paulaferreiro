print("El grupo A etsa formado or las mujeres con nombre anteiror  a la M y los hombres con un nombre posterior a la N ")
print ("El grupo B esta formado por el resto")
nombre=input("Por favor introduzca su nombre: ")
sexo=input("Por favor introduzca su sexo: ")
M=nombre
N=nombre
if nombre < M and sexo=="mujer" or nombre >N and sexo=="hombre":
    print("Perteneces al grupo A")
else:
  print("Perteneces al grupo B")