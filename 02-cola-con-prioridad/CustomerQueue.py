from typing import Optional
class CustomerQueue:
    def __init__(self):
        #Usaremos un diccionario para organizar los clientes por sus prioridades correspondientes, por lo cual, iniciamos en el constructor con la definicion de este diccionario de prioridades 1,2,3.
        self.priorities = {1: [], 2: [], 3: []}
   
    def enqueue(self, name: str, priority: int) -> None:
        #Encolamos el nombre del cliente en su nivel de prioidad.
        self.priorities[priority].append(name)
   
    def dequeue(self) -> Optional[str]:
        currentCustomer = ""
        #Iteramos en los ordenes de prioridades, 1-VIP 2-PREFERENCIAL 3-REGULAR
        for p in [1,2,3]:
            #Recorremos de mas prioridad a menor, si se encuentra alguien en el nivel, se continua, de lo contrario, exploramos los otros niveles.
            if self.priorities[p]:
                #En el nivel de prioridad actual en el cual estamos, se desaloja el primero que llego.
                currentCustomer = self.priorities[p].pop(0)
                #Retornamos ese nombre como el siguiente Customer a ser atendido.
                return currentCustomer 
        #Se retorna None si no hay ningun cliente en ningun nivel de prioidad.
        return None

# PRUEBAS LOCALES

cq = CustomerQueue()
cq.enqueue("Alice", 3)
cq.enqueue("Bob", 2)
cq.enqueue("Charlie", 1)
cq.enqueue("Dave", 2)

print(cq.dequeue()) 
print(cq.dequeue())  
print(cq.dequeue())  
print(cq.dequeue())  
print(cq.dequeue())  