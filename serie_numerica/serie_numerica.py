# Ejercicio #3 Taller While: La serie fibonacci es una serie numérica en la cual cada elemento es la suma de los dos anteriores tomando como variables los dos numeros iniciales a=0 y b=1. Hacer el Programa en Python y Diagrama de flujo que calcule e imprima a partir del tercero todos los elementos de la serie que sean menores de 1000.



print("-----------------------------------------")
print("-------------Serie Numérica--------------")
print("-----------------------------------------")

# input

a = 0
b = 1
k = a + b

# processing and output

a = a + 1
b = b + 1

while k < 900:
    k = a + b
    a = b 
    b = k
    print("\n Los números menores a 1000 según esta secuencia son los siguientes:")
    print("\n "+ str(k))

    