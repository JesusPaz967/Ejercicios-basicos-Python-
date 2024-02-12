"""Escribir una función Reemplazar que tenga como argumentos una pila con tipo de elemento int 
y dos valores int: nuevo y viejo de forma que si el segundo valor aparece en algún lugar de la pila,
sea reemplazado por el segundo. """
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    
def reemplazar(stack,viejo,nuevo):
    modificar=Stack()

    while not stack.is_empty():
        n=stack.pop()
        if n==viejo:
            modificar.push(nuevo)
        else:
            modificar.push(n)

    while not modificar.is_empty():
        stack.push(modificar.pop())

    return stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Original: ",stack.items)
modificar=reemplazar(stack,2,4)
print("Modificado: ",modificar.items)
