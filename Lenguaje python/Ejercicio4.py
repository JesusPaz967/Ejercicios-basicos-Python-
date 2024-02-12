"""Construir una función imprimeInverso que imprima los elementos de una pila enlazada 
de enteros en orden inverso a partir de una posición p"""
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None


class Pila:
    def __init__(self):
        self.cabeza=None
    
    def is_empty(self):
        return self.cabeza is None
    
    def push(self,dato):
        nuevo=Nodo(dato)
        if self.is_empty():
            self.cabeza=nuevo
        else:
            nuevo.siguiente=self.cabeza
            self.cabeza=nuevo
    
    def pop(self):
        if self.is_empty():
            return None
        dato=self.cabeza.dato
        self.cabeza=self.cabeza.siguiente
        return dato
    

    def imprimirInv(self,p):
       pila_aux=Pila()

       for _ in range(p):
           elemento =self.pop()
           if elemento is not None:
               pila_aux.push(elemento)

           while not pila_aux.is_empty():
             elemento=pila_aux.pop()
           print(elemento)

pila=Pila()

pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)

pila.imprimirInv(2)