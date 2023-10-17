anho=int(input("Por favor introduzca tu año de nacimiento: ")) #variable normal
zodiaco=anho%12 #variable interna
if zodiaco==0 :
         print("Mono")
elif zodiaco==1:
         print("Gallo")
elif zodiaco==2:
         print("Perro")
elif zodiaco==3:
         print("Cerdo")
elif zodiaco==4:
         print("Rata")
elif zodiaco==5:
         print("Buey")
elif zodiaco==6:
         print("Tigre")
elif zodiaco==7:
         print("Conejo")
elif zodiaco==8:
         print("Dragón")
elif zodiaco==9:
         print("Sepiente")
elif zodiaco==10:
         print("Caballo")
elif zodiaco==11:
         print("Cabra")
#lista
signo_chino=["Mono","Gallo","Perro","Cerdo","Rata","Buey","Tigre","Conejo","Dragón","Serpiente","Caballo","Cabra"]
print("Eres", signo_chino[zodiaco])

        
      




        
        
