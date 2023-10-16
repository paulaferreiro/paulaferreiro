#Ejercicio de repaso1
num1=int(input("Por favor introduzca el primer numero: "))
num2=int(input("Por favor introduzca el segundo numero: "))
#Control de entrada
if num1<0 or num2<0:
    print("Error")
else:
    #comienza la lógica de programa
    if num1>num2:
      print(num1,">",num2)
    elif num2>num1:
      print(num2,">",num1)
    else: 
      print(num1,"=",num2)

