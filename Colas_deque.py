'''
implementacion de colas mediante deque()
Demuestra las difrencuas en la forma de implementacion

'''
SEPARADOR = ("*" * 20) + "/in"
import collections

cola = collections.deque()  #Cola utilizando deque

for cantidad in range(5):
    nuevo = input("Nombre del recien llegado: ")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos:")
for elemento in cola:
    print(elemento)
print(SEPARADOR)
pass #Hacer notar que los elementos permanecen en la cola 

print("Procedemos a retirarlo de la cola")
while cola:
    print(cola.popleft)
pass #Verificar que la estructura se encuentre vacia
