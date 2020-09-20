from Queue import QueueLinkedList
from Queue import QueueArrayList
from Queue import QueueArrayList_deque

from time import time

#global functions
def enqueueTest(q,n=50000):
    start = time()
    for i in range(n):
        q.enqueue(i)
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")

def dequeueTest(q,n=50000):
    start = time()
    for i in range(n): #@UnusedVariable
        q.dequeue()
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")
    
# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__ == "__main__":
    print("\tEnqueueing elements")
    print("QueueLinkedList")
    ql=QueueLinkedList()
    enqueueTest(ql)
    print("QueueArrayList")
    qal=QueueArrayList()
    enqueueTest(qal)
    print("QueueArrayList_deque")
    qald=QueueArrayList_deque()
    enqueueTest(qald)
    
    print("\tDequeueing elements")
    print("QueueLinkedList")
    dequeueTest(ql)
    print("QueueArrayList")
    dequeueTest(qal)
    print("QueueArrayList_deque")
    dequeueTest(qald)
    