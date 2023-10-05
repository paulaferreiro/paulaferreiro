print("Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas") 
print("Cuando la puntuacion es 0.0 el nivel es inaceptable")
print("Cuando la puntuacion es 0.4 el nivel es aceptable")
print("Cuando la puntuacion es 0.6 o mas el nivel es meritorio")
print("En cada nivel se consigue 2.400 euros por la puntuación")
puntuacion=float(input("Por favor introduzca su puntacion: "))
calculo=2.400*puntuacion
#res(calculo)
if puntuacion==0.0:
    print("inaceptable, tu subida salarial es", calculo)
if puntuacion==0.4:
    print("aceptable, tu subida salarial es ", calculo)
if puntuacion>=0.6:
    print("meritorio, tu subida salarial es", calculo)