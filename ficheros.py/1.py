entero=int(input("Por favor introduzca un número entero entre el 1 y el 10:"))
#abrimos fichero
f=open("prueba.txt", 'a')
f.write("Esto es una prueba")

#hasta 11 para que incluya el 10
for i in range(1,11):
    print(entero,"x",i,"=",entero*i)

f.close()
