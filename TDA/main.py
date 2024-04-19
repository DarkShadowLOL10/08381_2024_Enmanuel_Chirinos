import stack
import queue

pila = []
for i in range(20):
    pila = stack.poner(pila, i)
print(pila)

print(stack.largo(pila))
for i in range(stack.largo(pila)):
    print(stack.top(pila))

    pila = stack.quitar(pila)
    print(pila)
