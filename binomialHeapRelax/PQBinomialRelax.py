#!/usr/bin/env python
# encoding: utf-8

import sys
from PQbinomialHeap import *
import random

import time


class PQBinomialRelax():
    INFINITY = float("inf")
    def __init__(self):
        heapMin = BinomialHeap(None, PQBinomialRelax.INFINITY)
        self.heap =[]
        for x in range(32):
            self.heap.append([]) # no riferimenti tra sottoliste
        self.min = heapMin
        self.minIndex = (None, None) # indici del minimo in self.heap


    def __str__(self):
        # noinspection PyRedundantParentheses
        return ("PQ" + "min = " + str(self.min.key) + "in posizione =" + str(self.minIndex))


    def assertAlias(self, node):
        """controlla se c'è aliasing in
           figli di node su node"""
        #assert node != None
        node0 = node.sons.getFirstRecord()
        while node0 is not None:
            if node0.elem is node :
                # noinspection PyUnusedLocal
                node0 = node0.next
                break
            node0 = node0.next


    def swapNode(self, node, othernode):
        """scambia 2 nodi e figli"""
        #assert node != None
        #assert othernode != None
        nodeSons = node.sons
        otherSons = othernode.sons
        c = 0
        if othernode is node.father: # otherNode is father of Node
            tmp = otherSons.getFirstRecord()
            if tmp.elem is node:
                otherSons.first=tmp.next # se riferimento a node è all inizio, faccio partire lista figli da 2nd
            else:
                while tmp.elem is node == False:
                    # noinspection PyUnusedLocal
                    prevTmp = tmp # per cancellare riferimento a node mantengo riferimento a record precedente
                    tmp = tmp.next
                    c += 1
                    if tmp is None:
                        print(c,1212)
                        #assert False # exit id tmp is none
                # noinspection PyUnusedLocal
                prevTmp = tmp.next # cancello riferimento ??#TODO VERIFICA VALIDITA AGGIORNAMENTO LINKD LIST E SE VIENE FATTO ALMENO UNA VOLTA
#                print(prevTmp.next)
        elif node is other.father:  #caso contrario, stesso ragioanmento
            tmp = nodeSons.getFirstRecord()
            #TODO SE FUNZIONA AGGIORNA ANCHE QUI PER SWAP CORRETTO
            while tmp.elem != othernode:
                tmp = tmp.next
                #assert tmp != None
            tmp.elem = node # riferimento temporaneo a
        node.sons, othernode.sons = othernode.sons, node.sons
        node.elem, othernode.elem = othernode.elem, node.elem
        node.key, othernode.key = othernode.key, node.key
        self.assertAlias(node)
        self.assertAlias(othernode)


    def insert(self, e, k):
        """inserisce un nuovo nodo di chiave k
          e elemento e
            dato che rappresenta un heap di altezza
            0 lo inseriamo nel
            prima lista del self.heap"""
        heap = BinomialHeap(e, k)

        self.heap[0].append(heap)
        if heap.root.key < self.min.root.key:
            self.min=heap
            self.minIndex=(0, len(self.heap[0])-1)
        return heap.root #return a node


    def rebuild_old(self):
        """scorrendo tutta la lista
          di alberi self.heap, unendo finche
            c'è al piu un elemento in
            ogni sottolista.
            se si uniscono 2 alberi nella
            sottolista 31 ritorna errore di
            lunghezza """
#        print("inizio rebuild, minIndex prima rebuild", self.minIndex)
        # noinspection PyUnusedLocal
        c = self.debugContaNodi()
        for x in range(32):
            while len(self.heap[x]) > 1: # se c'è piu di un elemento occorre merge
                if x >= 31:
                    raise MemoryError('Errore: e\' stato raggiunto il limite\
                                    massimo di questa priority queue')

                merged = self.heap[x][-1].merge(self.heap[x][-2])
                self.heap[x].pop() # pop degl'uniti
                self.heap[x].pop()
                if merged.root is self.min.root: # aggiornamento indice minimo
                    if len(self.heap[x+1]) > 0:
                        self.minIndex = (x + 1, len(self.heap[x + 1]))
                    else:
                        self.minIndex = (x + 1, len(self.heap[x + 1]))
                self.heap[x + 1].append(merged) # sposto il nuovo albero nella sottolista succesiva
        # noinspection PyUnusedLocal,PyUnusedLocal
        i, j = self.minIndex[0], self.minIndex[1]
        if self.min.root.key < 99999:
            self.findNewMin()
        #assert self.debugContaNodi() == c


    def rebuild(self):
        """scorrendo tutta la
          lista di alberi self.heap, unendo finche
            c'è al piu un elemento in
            ogni sottolista.
            se si uniscono 2 alberi nella
            sottolista 31 ritorna errore di
            lunghezza """
#        print("inizio rebuild, minIndex prima rebuild", self.minIndex)
        # noinspection PyUnusedLocal
        c = self.debugContaNodi()
        notEmpty = False
        for x in range(32):
            while len(self.heap[x]) > 1: # se c'è piu di un elemento occorre merge
                if x >= 31:
                    raise MemoryError('Errore: e\' stato raggiunto il limite\
                                    massimo di questa priority queue')
                notEmpty = True #indica che in foresta ristrutturata ci sara almeno un albero
                merged = self.heap[x][-1].merge(self.heap[x][-2])
                self.heap[x].pop() #pop degl'uniti
                self.heap[x].pop()
                self.heap[x + 1].append(merged)  # sposto il nuovo albero nella sottolista succesiva
                  
        if notEmpty: # aggiornamento indice minimo
            self.findNewMin()  


    def findHeap(self, node):
        """dato in input un
          nodo che è radice del suo heap
         troviamo l heap
         di appartenza
         ritorna tupla con
         posizione in
         self.heap
         O(n)   """
        numFigli = 0 # contatore
        figlio = node.sons.getFirstRecord()
        while figlio is not None:
            figlio = figlio.next
            numFigli += 1
        for x in range(len(self.heap[numFigli ])):
            if self.heap[numFigli][x].root is node: # se la radice degl heap in self.heap ha idendita strutturale con node
                # noinspection PyRedundantParentheses
                return (numFigli, x) # posizione in self.heap
        return None


    def findMin(self):
        """ritorna valore chive elemento minimo"""
        return self.min.root.elem

    def findNewMin(self):
        """trova il nuovo minimo controllando tutte le radici nella foresta
        - se minimo non è a infinito, ergo non da ricalcolare, è sufficente
        cercare minimo tra alberi di dimensione adeguata(numero figli)
        e confrontare con is, piu economico di <= """

        if self.min.root.key < PQBinomialRelax.INFINITY:  #   ricerca nuovo indice e non valore minimo
            # aggiornamento solo indice minimo, is piu economico di <=
            cFig=0
            x=self.min.root.sons.getFirstRecord()
            while x is not None:  #conto figli minimo per valutare solo determinati alberi nella foresta
                x=x.next
                cFig+=1
            x=cFig
            for y in range(len(self.heap[x])):
                if self.heap[x][y] is self.min:
                    self.minIndex = (x, y)  #aggiorno indice minimo
                    return  # possibilità di uscire prima, tempo medio rebuild migliorato

        for x in range(32):  # ricalcolo minimo, costo log ammortizzato, verifica solo su radici
            for y in range(len(self.heap[x])):
                if self.heap[x][
                    y].root.key <= self.min.root.key:  # confronto su tutti alberi in foresta per nunovo minimo
                    self.min = self.heap[x][y]
                    self.minIndex = (x, y)

    def findNewMin_old(self):
        """trova il nuovo minimo controllando tutte le radici nella foresta"""
        #assert not self.isEmpty()
        if self.min.root.key < 9999:  #flag per ricerca nuovo indice e non valore minimo
            # noinspection PyUnusedLocal
            onlyIndex = True
        else:
            # noinspection PyUnusedLocal
            onlyIndex = False
        for x in range(32): #TODO vedi soluzioni piu econimica
            for y in range(len(self.heap[x])):
                if self.heap[x][y].root.key <= self.min.root.key: #confronto su tutti alberi in foresta per nunovo minimo
                    self.min = self.heap[x][y]
                    self.minIndex = (x, y)


    def debugConta(self):
        """ritorna numero di alberi in foresta self.heap"""
        c = 0
        for x in range(32):
            c += len(self.heap[x])
        return c


    def debugContaNodi(self):
        """ritorna numero di alberi in foresta self.heap"""
        c = 0
        for x in range(32):
            c += len(self.heap[x])*(2**x)
        return c


    def deleteMin(self):
        """cancella il minimo e ristruttura
        per ricalcolare minimo
        confronto su tutti alberi
        in forsta"""
#        print("\ninizio deletMin\texminkey=",self.min.root.key,"at pos",self.minIndex)
        cFig = 0
        sons = self.min.getHeapSons()
        i, j = self.minIndex[0], self.minIndex[1]
        exMin = self.heap[i].pop(j) # cancella il minimo e mettilo in exMin

        self.min = BinomialHeap(None, PQBinomialRelax.INFINITY) # minimo tmp a infinito
        heap = sons.getFirstRecord()
        while heap is not None:
            self.heap[cFig].append(heap.elem) # assumendo che i figli di alb cancellato siano ordinato
            heap = heap.next
            cFig += 1

        self.min = BinomialHeap(None, PQBinomialRelax.INFINITY)
        self.rebuild()        #REBUILD AGGIORNA MINIMO  

        if not self.isEmpty():  #TODO VEDI SE ELIMINABILE, REBUID LA CHIAMA GIA FINDMIN! 
             self.findNewMin()
        # noinspection PyRedundantParentheses
        return (exMin.root.key,exMin.root.elem)


    def isEmpty(self):
        """verifica se heap è vuoto"""
        for x in range(len(self.heap)):
            if len(self.heap[x]) > 0:
                return False
        return True 


    def _stampa(self):
        """stampa della foresta di heap rilassati"""
        for x in range(32):
            if len(self.heap[x]) == 0:
                continue
#            print("B_", x, "con ", len(self.heap[x]), "elementi")
#            print("alberi dimensione B_", x)

            for y in range(len(self.heap[x])):
                self.heap[x][y].stampa()


    def stampa(self):
        print()
        """stampa della foresta di heap rilassati"""
        for x in range(32):
            if len(self.heap[x]) == 0:
                continue
            print("B_",x,"con ",len(self.heap[x]),"elementi")
            print("alberi dimensione B_",x)

            for y in range(len(self.heap[x])):

                self.heap[x][y].stampa()  

    def PQMerge(self, PQ2):
        """unisce 2 code con priorità senza rebuild"""

        for x in range(32):
            if len(PQ2.heap[x]) > 0: # data sottolista con dimensione positiva
                self.heap[x] += PQ2.heap[x] # inserisco elementi nella sottolista di PQ1
        if PQ2.min.root.key< self.min.root.key:
            self.min=PQ2.min
            self.findNewMin()

    def decreaseKey(self, node, heap, offset):
        """dato riferimento al
          nodo di cui decrementare la chiave
        swappiamo nel albero di
        apparteneza del nodo, se
        è diventato nuovo minimo
        della foresta, swappiamo
        l'abero di appartenza del nodo al primo posto
        della sua sottolista di
        appartenza e ricerchiamo la posizione del nuovo minimo
        controllando solo le radici
        degl alberi al primo elemento di self.heap[x]
        per trovare l indice di
        appartenza del nodo nella foresta basta contare il numero dei figli
        sul primo livello

        Tn=Log(n)"""
        #TODO NECESSARIO ANCHE HEAP DI APPARTENZA NODO PER AGGIORNARE INDICE EVENTUALE NUOVO MINIMO
        """primo while non swappa un cazzo
           se nodo da decrementare è sul primo livello dei figli della radice pare funzionare
           """
        #valutare costo effettivo trovare heap di appartenza tramite confronto tutta la sottolista B_x

        # noinspection PyUnusedLocal
        tmp0 = node.key
        node.key -= offset # key decrementata



#        print("DECREASE KEY, STAMPA PRIMA DI SWAP \n\n\n\n\n")
        while  node.father is not None and (node.father.key>node.key):
            node.swap(node.father)
            node=node.father
#        print("stampa dopo swaps_0")
#        print("\n\n")
          
        if node.key < self.min.root.key :
            self.min = heap
            self.min.root = node # forzato radice, obsoleto??TODO
            sons = node.sons
            numFigli = 0 # contatore
            nodo = sons.getFirstRecord()
            while nodo is not None:
                nodo = nodo.next
                numFigli += 1
            #if len(self.heap[numFigli]) == 0 or numFigli > 31: # errore in reinserimento
            #    print(numFigli, "aa", self.heap[numFigli])
            #    numFigli += 1
            #    #assert False, "uscita forzata, non ho trovato heap di appartenza"
            for x in range(len(self.heap[numFigli])):
                if self.heap[numFigli][x].root == node:
                    self.minIndex=(numFigli, x)
                    break
                    return   ## warning
            tmp = self.heap[numFigli][0] # primo della sottolista di appartenza di heap
            self.heap[numFigli][0] = heap
            heap.root = tmp.root # swap di radici per evitare ricerca in tempo lineare
#            print("swap effetutato di heap come primo di sua lista")
            self.minIndex = (numFigli, 0)
            #assert self.heap[numFigli][0] is self.min, "idendita dopo swap"
#            print("stampa dopo swap a primo di lista\n\n\n\n\n")


    def delete(self, node, heap):
        #TODO levare heap da input?
        self.decreaseKey(node, heap, 99999)
        self.deleteMin()


   
def reinserimenti(n, PQ):
    """reinserisce n nodi casuali in PQ"""
    for x in range(n):
        e = random.randint(0, 100)
        k = random.randint(0, 100)
        PQ.insert(e, k)


def albero():
    """albero preconfigurato
        ritorna tupla con albero
        con nodi inseriti
        e lista di chiavi nell
        ordine di inserimento"""
    PQ = PQBinomialRelax()
    l = [] # lista di chiavi
    for x in range(10):
        PQ.insert(x, x)
        l.append(x)
    PQ.insert(5, 5)
    PQ.insert(3, 5)
    PQ.insert(3, 5)
    l.append(5)
    PQ.insert(3, 5)
    l.append(5)
    PQ.insert(3, 5)
    l.append(5)
    PQ.insert(3, 5)
    l.append(5)
    l.append(3)
    l.append(3)
    # noinspection PyRedundantParentheses
    return (PQ, l)


def alberoRandom(nInsert, nReinsert, perturbation = False, nodeListFlag = False):
    """ritorna albero casuale e lista di chiavi
        con nInsert iniziali
        e nReinsert numero di volte in cui rensierire num casuale di nodi
        perturbation --> Flag per inserire nell'albero solo nodi casuali
        nodeListFlag --> flag per tornare (PQ,lista di chiavi,lista di nodi)
        per non appensantire tempi, lista di nodi istanziata e estesa solo se c'è flag"""
    PQ = PQBinomialRelax()
    l = []
    nodeList = []
    for x in range(nInsert):
        # noinspection PyUnusedLocal
        e = random.randint(0, 100)
        k = random.randint(0, 509)
        if perturbation:
             k += random.random()
             k += random.random()
        if nodeListFlag:
             nodeList.append(PQ.insert(k, k))
        else:
             PQ.insert(k, k)
        l.append(k)

    PQ.rebuild()

    for y in range(nReinsert):
        node2Reinsert = random.randint(1, 10)
        for x in range(node2Reinsert):
            # noinspection PyUnusedLocal
            e = random.randint(0, 100)
            k = random.randint(0, 509)
            if perturbation:
                 k += random.random()
                 k += random.random()
            l.append(k)
            if nodeListFlag:
                 nodeList.append(PQ.insert(k, k))
            else:
                 PQ.insert(k, k)

    if nodeListFlag:
         # noinspection PyRedundantParentheses
         return (PQ, l, nodeList)
    else:
         # noinspection PyRedundantParentheses
         return (PQ, l)

def mergeTest(x=1000,y=500):
    """testing merge PQ con riordinamento tramite deletMin"""
    # noinspection PyUnusedLocal
    f = random.randint
    alb = alberoRandom(x, y)
    alb1 = alberoRandom(x, y)
    pq0, l0 = alb[0], alb[1]
    pq1, l1 = alb1[0], alb1[1]
    pq0.PQMerge(pq1)
    l0+=l1
    l0.sort()
    q=[]
    for x in range(len(l0)):
        q.append(pq0.deleteMin()[0])
        assert q[x]==l0[x]
    assert q==l0
def testPQDeleteMin(n = 100, m = 5):
    """test per delet min n,m dimensioni albero
          inserimenti e reinserimenti"""
    random.seed()
    alb = alberoRandom(n, m)
    PQ = alb[0]
    l = alb[1]
    l.sort()
    # noinspection PyUnusedLocal
    x = 0
    #print("sorted", l)
    q = [] # per n deletMin
    #PQ.stampa()
    while not PQ.isEmpty():
        q.append(PQ.deleteMin()[0])
        #PQ.stampa()


    assert q == l


def randNode(pq):
     """trova un nodo casuale il piu profondo possibile
        ritorna nodo, heap appartenza nodo"""
     poss = []
     deep = random.randint(1, 10000) % 5 == 0 # random Flag per profondità nodo casuale creato
     for x in range(1, len(pq.heap)): # 0 escluso dato che il decrease è un banale-=
          if len(pq.heap[x]) > 0:
               poss.append(x)
     i = random.choice(poss)
     j = random.choice(list(range(len(pq.heap[i]))))
     heap = pq.heap[i][j]
     #assert not pq.isEmpty()
     if deep: # deep True ==> scelta nodo piu profondo in heap casuale selezionato
          node = heap.root.sons.getLast()
          while node.sons.getLast() is not None:
               node = node.sons.getLast()
     else: # nodo su livelli superficiali
          node = heap.root.sons.getFirstRecord()
          if node is None:
              # noinspection PyRedundantParentheses
              return (heap.root,heap)
          while node.elem.sons.getFirst() is not None:
                 while random.randint(1, 1000) % 7 != 0 or node.next is not None:
                     node = node.next # per scegliere il nodo in modo casuale nella lista dei figli
                 
          node = node.elem # 4 return a node

     #assert node != None
     # noinspection PyRedundantParentheses
     return (node, heap)
          
     

def decreaseKeySort(dim0 = 10, dim1 = 6, m = 1):
     """decrementa m chiavi e verifica il corretto svolgimento
          facendo n deleteMin e verificando sulla lista ordinata se
          decrementando anche quella chiave coincidono i risultati"""
     alb = alberoRandom(dim0, dim1)
     PQ = alb[0]
     l = alb[1]
     q = []
     for x in range(m):
          offset = random.randint(10, 100)
          rNH = randNode(PQ)
          node, heap = rNH[0], rNH[1]
          i = l.index(node.key)
          l[i] -= offset
          PQ.decreaseKey(node, heap, offset)
     
     l.sort()
     for x in range(len(l)):
          q.append(PQ.deleteMin()[0])
          #assert(q[x]==l[x])
     #assert l==q


def decreaseKeySort2(dim0 = 10, dim1 = 6, m = 1):
     """decrementa m chiavi e verifica il corretto svolgimento
          facendo n deleteMin e verificando sulla lista ordinata se
          decrementando anche quella chiave coincidono i risultati"""
     alb = alberoRandom(dim0, dim1, False, True)
     PQ = alb[0]
     l = alb[1]
     lNodi = alb[2]
     q = []
     for x in range(m):
          offset = random.randint(10, 100)
          # noinspection PyUnusedLocal
          randNodeIndex = random.randint(0, len(lNodi))
          node, heap = rNH[0], rNH[1]
          if node.key == superMin:
               continue
          i = l.index(node.key)
          l[i] -= offset
          PQ.decreaseKey(node, heap, offset)
     
     l.sort()
     for x in range(len(l) ):
          PQ.findMin()
          q.append(PQ.deleteMin()[0])
     #assert l == q


def deleteSort(dim0 = 10, dim1 = 6, m = 3):
     """decrementa m chiavi e verifica il corretto svolgimento
          facendo n deleteMin e verificando sulla lista ordinata se
          decrementando anche quella chiave coincidono i risultati"""
     alb = alberoRandom(dim0, dim1)
     PQ = alb[0]
     l = alb[1]
     q = []
     for x in range(m):
          rndNode = randNode(PQ)
          node, heap = rndNode[0], rndNode[1] 
          i = l.index(node.key)
          l.pop(i)
          PQ.delete(node, heap)
     l.sort()
     for x in range(len(l)):
          q.append(PQ.deleteMin()[0])
          #assert q[x] == l[x]
     #assert l == q


def testDecreaseKey():
    """test x decrease key"""

    PQ = PQBinomialRelax()
    print("12 inserimenti")
    for x in range(12):
        e=random.randint(0, 100)
        k=random.randint(0, 50)
        # k += random.random() # perturbazione
        PQ.insert(e, k)

    print("\n\nmin =", PQ.findMin())
    PQ.rebuild()
    print("ristruttura eseguita\n\n")
    print("stampa\n\n")
    PQ.stampa()
    print("rienserimenti\n\n")
    for x in range(6):
        e = random.randint(0, 100)
        k = random.randint(0, 255)
        PQ.insert(e, k)
        print("inserito nodo ", e, k)

    print("min =", PQ.findMin())
    PQ.deleteMin()
    print("\n\ncancellato minimo")
    print("min nuovo  =", PQ.findMin())
    print("\n\nristampa")
    PQ.stampa()

    node = PQ.heap[4][0].root.sons.getLast().sons.getLast().sons.getLast()
    # noinspection PyUnusedLocal
    heap = PQ.heap[4][0]
    print("test decrease key", node.key)
    PQ.decreaseKey (node,heap, 2000) #decrease key con nodo che diventa sicurmente minimo
    PQ.stampa()
    PQ.deleteMin()
    PQ.stampa()
    # noinspection PyUnusedLocal
    node = PQ.heap[4][0].root.sons.getLast().sons.getLast().sons.getLast()
    # noinspection PyUnusedLocal
    heap = PQ.heap[4][0]
     
def tests(tipo, iterazioni = 20):
     """test su principali operazioni deleteMin, decreaseKey, delete
        tipo: stringa, con asserzione che ne controlla la validita
        iterazioni: intero, numero di volte da ripetere il test, default 20"""
     assert tipo in ["deleteMin","decreaseKey","delete","merge"], "inserisci tipo di test adeguato!"
     c=0
     c1=0

     if tipo == "deleteMin":
         print("deleteMin test iniziato")
         start = time.time()
         for x in range(iterazioni):
              random.seed()
              if x % 5 == 0:
                   print(x)
              n, m = random.randint(1000, 5555), random.randint(777, 2222)
              c+=n+m
              testPQDeleteMin(n, m)
         print("elapsed", time.time() - start)
         print("testato su un complesso di ",c,"nodi per ordinare tramite estrazioni minimo")
     elif tipo == "decreaseKey":
          print("decreaseKey test iniziato")
          start = time.time()
          for x in range(iterazioni):
              # noinspection PyUnusedLocal
              f = random.randint
              xx, y, z = random.randint(1996, 10000), random.randint(55, 100), random.randint(555, 1996)
              c+=xx+y
              c1+=z
              decreaseKeySort(xx, y, z)
              if x % 5 == 0:
                   print(x)
          print("elapsed", time.time() - start)
          print("testato su un complesso di ",c,"nodi decrementando",c1,"volte e riordinado  per verificare")
     elif tipo == "delete":
          print("delete test iniziato")

          start = time.time()
          for x in range(iterazioni):
              # noinspection PyUnusedLocal
              f = random.randint
              xx, y, z = random.randint(1000, 10000) ,random.randint(55, 100), random.randint(100, 1000)
              deleteSort(xx, y, z)
              c += xx + y
              c1 += z
              if x % 5 == 0:
                   print(x)
          print("elapsed", time.time() - start) # testSwap()
          print("testato su un complesso di ",c,"nodi eliminando ",c1,"nodi,riordinado  per verificare")
     elif tipo=="merge":
        print("inizio merge test")
        start=time.time()
        c=0
        for z in range(iterazioni):
            if z%5==0:
                print(z)
            x,y=random.randint(500, 1000), random.randint(55, 100),
            mergeTest(x,y)
            c+=x+y
        print("passato",time.time()-start)
        print("testato su un complesso di ",c,"nodi")

 
if __name__ == "__main__":
    tests("merge",10)
    print("testing su principali op, verificando validita utilizzando propieta ordinamento PQ")

    print("ordinamento lista di chiavi (nodi) tramite n deleteMin")
    tests("deleteMin", 10)
    print("decrementazioni chiavi su PQ e lista chiavi dei nodi, verifica con riordinamento ")
    tests("decreaseKey", 10)
    print("cancellazioni su PQ e su lista di nodi, verifica validità op con ordinamento")
    tests("delete", 10)
