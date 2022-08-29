dia_mes=int(input("Ingrese un numero correspondiente a un dia del mes "))
mes=int(input(" Ingrese un numero correspondiente a un mes del año "))
ano=int(input(" Ingrese un numero correspondiente a un año "))
if dia_mes<=31 and dia_mes>0 and mes>0 and mes<=12 and ano>0:
    print ("Fecha valida")
else:
    print("Fecha invalida")

