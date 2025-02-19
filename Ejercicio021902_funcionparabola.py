# Ejericio de función f(x ) = x**2  + 2

# Definición de función con retorno
def f(x):
    respuesta = x**2 + 2
    return respuesta

# Definición de función que no produce retorno
def poner_nombre(nombre):
    print(nombre)

# Llamado de una función que posee retorno 
n = f(5)
m = f(34)

# Uso de Tupla en print
print(n,m)

# Llamando una función que no produce retorno.
poner_nombre("Nombre propio")