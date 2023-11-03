n=int(input("Por favor introduce tu posición en la fila: "))
#calculamos la cadena del medio
semilla="BUH"
subcadena2="BUUH"
u="U"
subcadena="B"+n*u+"H"
print(subcadena)    
for i in range(n):
    print(i)
    semilla2=(semilla+subcadena+semilla, semilla+subcadena+semilla ,semilla+subcadena+semilla)
     print(semilla2)
    semilla3=(semilla2+subcadena+semilla)
     print(semilla3)
    semilla4=(semilla3+subcadena+semilla)
     print(semilla4)
