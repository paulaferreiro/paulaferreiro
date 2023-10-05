print("Una empresa tiene salas de juegos, segun la edad que tenga cada persona tiene que pagar una cantidad de dinero")
print("Las personas con edad de 4 años pueden entrar gratis,si tienen entre 4 y 18 años debe pagar 5 euros y si tienen más de 18 deben poagar 10 euros ")
edad=int(input("Por favor introduzca su edad"))
if edad== 4:
    print("No tienes que pagar, es gratis")
if edad >4<18:
    print("Tienes que pagar 5 euros")
if edad>18:
    print("Tienes que pagar 10 euros")
