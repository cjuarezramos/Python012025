# Ejercicio de uso de Tuplas con datos historicos
def stats(a,b,c):
    prom = (a+b+c)/3
    var=(((a-prom)**2+(b-prom)**2+(c-prom)**2)/3)
    return prom,var # Retorna una tupla con dos valores

estaddisticas = stats(34,67,87) 
print(estaddisticas)
promedio,varianza = stats(34,67,87) # Desempaquetando la tupla
print(promedio,varianza)