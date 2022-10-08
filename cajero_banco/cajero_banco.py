# Ejercicio # 4 Taller While: El cajero de un banco solo dispone de billetes de $10000, $2000 y monedas de $100. Su función es cambiar los cheques a los clientes, dándoles el menor número posible de billetes. Asumiendo que todos los cheques son múltiples de $100, hacer el diagrama de flujo y el programa en Python que reciba el valor del cheque a cambiar y que le informe al cajero cuántos billetes de cada denominación debe entregar. Como no se sabe cuántos clientes vienen en un día, el programa debe terminar cuando reciba cero como valor del cheque, y al final del día debe informar cuántos billetes de cada denominación se gastaron.


print("-----------------------------")
print("---------Cajero Banco--------")
print("-----------------------------")

# input 

k = int(input("\nDame el valor en $$ del cheque que quieres cambiar: "))

TB1 = 0
TB2 = 0
TB3 = 0

# processing

while k != 0:
    B1 = k/10000
    r = k - B1*10000
    B2 = r/2000
    r = r- B2*2000
    B3 = r/100
    TB1 += B1
    TB2 += B2
    TB3 += B3
    print("Es "+str(k)+str(B1)+str(B2)+str(B3))

    print("Es " +str(TB1)+str(TB2)+str(TB3))
