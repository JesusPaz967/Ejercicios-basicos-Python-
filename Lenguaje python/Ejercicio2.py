"""Supongamos que TEST es alguna función Booleana que toma cualquier entero dado y
devuelve un valor igual o distinto a cero.Consideremos el siguiente segmento de código:

N=3;
p <- CrearPila(capacidad(int));
for (i=1;i<=N;i++)
  si (TEST(i))
    imprimir(i);
  sino extraer(p);
siempre que (PilaNoVacia(p)){
  Tope(p);
  Insertar(p);
  imprimir(i);
}

¿Cuáles de las siguientes son posibles salidas del código anterior?.
a)1 2 3
b)1 3 2
c)2 1 3
d)3 1 2
e)2 3 1 -es esta-
f)3 2 1
"""

class Pila:
    def __init__(self):
      self.items=[]

    def insertar(self,item):
        self.items.append(item)
    
    def extraer(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items)==0
    
def TEST(num):
    if num % 2==0:
        return True
    else:
        return False

N=3
p=Pila()


for i in range (1,N+1):
    if TEST(i):
        print(i)
    else:
        p.insertar(i)

while not p.is_empty():
    i=p.extraer()
    print(i)