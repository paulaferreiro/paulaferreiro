dia=int(input("Por favor introduzca el día del año:"))
mes=int(input("Por favor introduzca el número de mes:"))

anho=[31, 28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
#calculamos cuantos meses faltan del año desde la fecha que nos da el usuario
temporal_anho=anho[mes:12]
res=anho[mes-1]-dia

for i in temporal_anho:
    res=res+i
print(res)

