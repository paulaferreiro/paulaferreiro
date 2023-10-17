#Ejercicio de repaso2
num1=int(input("Por favor introduzca el primer numero: "))
num2=int(input("Por favor introduzca el segundo numero: "))
num3=int(input("Por favor introduzca el tercer numero: "))
#Control de entrada
if num1<0 and num2<0 and num3<0:
    print("Error")
else:
    #comienza la lógica de programa
    if num1>=num2>=num3:
      print(num1,">=",num2,">=",num3)
    elif num1>=num3>=num2:
      print(num1,">=",num3,">=",num2)
    elif num2>=num1>=num3:
      print(num2,">=",num1,">=",num3)
    elif num2>=num3>=num1:
      print(num2,">=",num3,">=",num1)
    elif num3>=num2>=num1:
      print(num3,">=",num2,">=",num1)
    elif num3>=num1>=num2:
       print(num3,">=",num1,">=",num2)
    