from Stack import StackLinkedList
from Stack import StackArrayList_dummy
from Stack import StackArrayList

from time import time

#global functions
def pushTest(s,n=50000):
    start = time()
    for i in range(n):
        s.push(i)
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")

def popTest(s,n=50000):
    start = time()
    for i in range(n): #@UnusedVariable
        s.pop()
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")
    
# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__ == "__main__":
    print("\tPushing elements")
    print("StackLinkedList")
    sl=StackLinkedList()
    pushTest(sl)
    print("StackArrayList_dummy")
    sald=StackArrayList_dummy()
    pushTest(sald)
    print("StackArrayList")
    sal=StackArrayList()
    pushTest(sal)
    
    print("\tPopping elements")
    print("StackLinkedList")
    popTest(sl)
    print("StackArrayList_dummy")
    popTest(sald)
    print("StackArrayList")
    popTest(sal)
    