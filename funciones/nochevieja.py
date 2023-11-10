#las funciones empiezan por def y terminan en retun
def falta (dia, mes):
    anho=[31, 28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
    res=anho[mes-1]-dia
    temporal_anho=anho[mes:12]
    for i in temporal_anho:
        res=res+i
    return(res)

dia=int(input("Dia:"))


   

