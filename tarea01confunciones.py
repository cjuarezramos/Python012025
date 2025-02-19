# Tarea 01: Realizar un programa que solicite un número entero entre 1000 y 5000 y que verifique si es un número primo.
# Un número primo es aquel que solo es divisible por 1 y por sí mismo.
# Utilizando funcion.

def es_primo(numero):
    for divisor in range(2,numero):
        if numero % divisor == 0:
            return False
    return True

# Tarea 01 realizada con un for
while True:
    numero = int(input('Ingrese un número entero: '))
    if 1000 <= numero and numero <= 50000:
        if es_primo(numero):
            print(str(numero) + ' es primo')
            break
        else: 
            print('No es primo')
    else:
        print('Debe ingresar un número entre 1000 y 5000')
