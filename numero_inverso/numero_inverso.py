#  Hacer diagrama de flujo y programa que lea un numero n, entero y positivo de cualquier numero de digitos, que calcule su numero inverso y que lo imprima junto con el numero leído.


print("----------------------------------------")
print("-------------Número Inverso-------------")
print("----------------------------------------")


# input

n = int(input("Digite el número entero que quiera evaluar: "))
j = n
k = 0

# processing

while n != 0:
    m = n % 10
    k = k * 10 + m
    n = n // 10

    if n == 0:
        print("Digitaste un número no válido. Por favor vuelve a intentarlo")
    
print("El orden inverso del número que digitaste es "+str(k)+" y el número evaluado fue "+str(j))