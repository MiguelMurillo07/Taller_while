# Dado un numero n, entero y positivo de cualquier numero de digitos, que calcule la suma de sus digitos y que la imprima junto con el número leído


print("----------------------------------")
print("----------Suma Dígitos------------")
print("----------------------------------")


# input

n = int(input("\nDigite el número que quiera evaluar: "))

k = n
# processing

suma_numero = 0 
ext_numero = 0

while n !=0:
    ext_numero = n % 10
    n = n // 10
    suma_numero = suma_numero + ext_numero

# output

print("La suma de los dígitos es de "+str(suma_numero)+ " del número dado que fue "+str(k))