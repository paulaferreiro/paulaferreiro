#calcular numero aleatorio utilizar random
import random
#para xcalcular de 1 a 10
aleatorio=random.randint(1,10)
#print(aleatorio)
#iniciamos el programa
print("Bienvenidos a este juego de adivinar cifra ---------, ¿como te llamas?")
nombreusuario=input("Por favor introduzca su nombre: ")

print("Hola",nombreusuario)
pregunta=input("Quieres jugar al juego? [si/no]")
if pregunta == "no":
    print("Ah vale... hasta luego")
if pregunta == "si":
    print("Estoy pensando en un numero... entre 1 y 10")
    numusuario=int(input("Por favor adivina. "))
if numusuario > aleatorio:
    print("Un poco menos")
if numusuario < aleatorio:
    print("Un poco más")
while numusuario!=aleatorio:
    numusuario=int(input("Intentalo otra vez"))
if numusuario == aleatorio:
    print("Has acertado")
    



