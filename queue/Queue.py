#Per effettuare l'import from linked_ds.list.LinkedList bisogna specificare il percorso della libreria
#in questo caso si tratta del percorso che contiene la cartella list
#Questo percorso lo dovete specificare all'interno dell'append()

from collections import deque
import sys
sys.path.append("/home/vi/Desktop/git/AlgorithmsAndDataStructures")
from list.LinkedList import LinkedList

class QueueLinkedList(LinkedList):    
    """ Implementation of a FIFO queue using a linked list.
    """
    
    def enqueue(self, elem):
        self.addAsLast(elem)
    
    def dequeue(self):
        return self.popFirst()

class QueueArrayList():
    """ Implementation of a FIFO queue using a Python's list built-in type, i.e., lists based on array implementation.
    """
    
    def __init__(self):
        self.q = []
        
    def enqueue(self, elem):
        self.q.append(elem)
    
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)
    
    def getFirst(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[0]
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def printF(self):
        print("Elements in the collection (ordered):")
        print(self.q)

class QueueArrayList_deque(QueueArrayList):
    """ Faster implementation of a FIFO using the type deque, optimized also for removing elements at the beginning of the collection.
    """
    def __init__(self):
        self.q = deque()
    
    #Override
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.popleft()

#global functions
def testQueue(q):
    for i in range(10):
        q.enqueue(i)
    q.printF()
    
    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())
    
    q.printF()

# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__ == "__main__":
    print("QueueLinkedList")
    q = QueueLinkedList()
    testQueue(q)
    
    print("QueueArrayList")
    q = QueueArrayList()
    testQueue(q)
    
    print("QueueArrayList_deque")
    q = QueueArrayList_deque()
    testQueue(q)
