# Tarea 01 realizada con un for
while True:
    numero = int(input('Ingrese un número entero: '))
    if 1000 <= numero and numero <= 50000:
        cont = 0
        for divisor in range(2,numero):
            if numero % divisor == 0:
                cont = cont + 1
        if cont == 0:
            print(str(numero) + ' es primo')
            break # rompe el lazo while
        else: 
            print('No es primo')
    else:
        print('Debe ingresar un número entre 1000 y 5000')
