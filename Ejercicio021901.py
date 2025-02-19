# Dado un nùmero positivo x, queremos determinar n tal que el n-èsimo
# número armónico esté justo por encima de x

x = float(input('Ingrese un número positivo mayor que 1: '))
tolerancia = float(input('Error permitido: '))
acum = 0
v = 1
while True:
    acum = acum + 1/v
    v = v + 1

    error = acum-x
    if error>tolerancia:
        break

print('El número armónico de %5.2f  es %5.2f  con %i terminos' % (x,acum,v)) # formateo de una cadena de caracteres.


