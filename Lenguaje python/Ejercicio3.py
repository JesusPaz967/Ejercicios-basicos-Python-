#Construir una función que sume los elementos de una cola de enteros recursivamente. 
from collections import deque

def suma(operacion):
    if not operacion:
        return 0
    else:
        elemento = operacion.popleft()
        return elemento + suma(operacion)

lista = deque([1, 2, 3, 4, 5])

resultado = suma(lista.copy())  
print("La suma de los elementos de la lista es:", resultado)
