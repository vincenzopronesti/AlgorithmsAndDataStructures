import sys
sys.path.append("/home/vi/Desktop/git/AlgorithmsAndDataStructures")
from HeapMin import HeapMin
from __init__ import printSwitch
from math import ceil
from sorting.Sorting import mergeSort, partition

def trivialSelect(l, position):
    if printSwitch.dumpOperations:
        print("trivialSelect of ", str(l), "with position", str(position))
    length = len(l)
    if position <= 0 or position > length:
        return None

    for i in range(0, position):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]
    if printSwitch.dumpOperations:
        print("  returns", l[position - 1])
    return l[position - 1]


# Ordina la sequenza in input, e restituisce il k-esimo elemento. Richiede tempo O(n log n)
def sortSelect(l, position):
    if printSwitch.dumpOperations:
        print("sortSelect")
    if position <= 0 or position > len(l):
        return None
    mergeSort(l)
    if printSwitch.dumpOperations:
        print(l)
    return l[position - 1]

def heapSelect(l, position):
    if printSwitch.dumpOperations:
        print("heapSelect")
    if position <= 0 or position > len(l):
        return None
    
    heap = HeapMin(l)
    heap.heapify()
    if printSwitch.dumpOperations:
        print(heap.heap)
    for i in range(0, position - 1):  # @UnusedVariable i
        heap.deleteMin()
    if printSwitch.dumpOperations:
        print(heap.heap)
    
    return heap.findMin()

# QUICKSELECT RANDOMIZZATO (ricorsivo)
""" Prende un perno random x, ed individua gli elementi A <= di x e quelli B >x.
    Se |A|+1=k, l'elemento cercato e' x. Se |A|<=k, prosegue ricorsivamente la ricerca
    in A.
    Altrimenti prosegue ricorsivamente su B, questa volta cercando k'=k-(|A|+1)
    Richiede tempo atteso O(n)
    Somiglia a quickSort randomizzato, con la differenza che si fa una sola chiamata
    ricorsiva anziche' 2
    (il che suggerisce perche' il tempo d'esecuzione sia migliore)
"""

def quickSelectRand(l, position): #position 1...n
    if position <= 0 or position > len(l):
        return None
    return recursiveQuickSelectRand(l, 0, len(l) - 1, position)
    
def recursiveQuickSelectRand(l, left, right, position):
    if printSwitch.dumpOperations:
        print("recursiveQuickSelectRand({},{},{})".format(left, right, position))
    
    if left > right: #controllo superfluo
        return
    
    if left == right and position - 1 == left:
        return l[position - 1]
        
    mid = partition(l, left, right)
    if printSwitch.dumpOperations:
        print("mid: {}".format(mid))
    
    if position - 1 == mid:
        return l[mid]
    if position - 1 < mid:
        return recursiveQuickSelectRand(l, left, mid - 1, position)
    else:
        return recursiveQuickSelectRand(l, mid + 1, right, position)

# End of quickSelect

if __name__ == '__main__':
    basel = [5, 34, 26, 1, 4, 2, 17, 50, 41]
    k = 4
    l = list(basel)
    print(l)
    #print(trivialSelect(l,k))
    #print(sortSelect(l, k))
    print(heapSelect(l, k))
    #print(quickSelectRand(l, k))

    
