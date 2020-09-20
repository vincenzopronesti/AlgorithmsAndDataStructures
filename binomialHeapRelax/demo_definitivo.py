#!/usr/bin/env python
# encoding: utf-8

#import sys
from PQbinomialHeap import PQbinomialHeap
from PQBinomialRelax import *

FATTORE_FIND_MIN=5
FATTORE_DEL = 3
#FATTORE_REBUILD=111  #FATTORE RISTRUTTURA IN HEAP RILASSATO PER EVITARE N INSERIMENTI SENZA ALCUNA RISTRUTTURA
 
def insert_test(num_nodi, tipoInserimento, inizio_int = 0, fine_int = 10):
    """testa inserimenti e findMin
        su heap binomiale standard
        tipo inserimento: stringa, casuale o sequenziale
        valori sequenziali tra inizio_int e inizio_int+numNodi
        findMin inseriti in percentuale 1/fattore find_min
        al fine di dare consistenza a ricerca minimo
        (se ricercato solo dopo tutti inserimenti si troverebbe sempre
        stesso minimo!)"""
    ##
    print("test su varie insert e findMin su heap binomiale \ninserimento",tipoInserimento)

    PQ = PQbinomialHeap()
    inizio=time.time()  ##
    assert tipoInserimento in ["sequenziale","casuale"],"scegli tra inserimento sequenziale o casuale"
    if tipoInserimento=="sequenziale": #TODO AGGIORNARE SE PROF RISPONDE CHE SEQ È CON INPUT
        for x in range(inizio_int,inizio_int+num_nodi):
            PQ.insert(x,x)
            if x%FATTORE_FIND_MIN==0:
                PQ.findMin()
    else:   #random inserimento
        for z in range(num_nodi):
            x=random.randint(inizio_int,fine_int)
            PQ.insert(x,x)
            if z%FATTORE_FIND_MIN==0:
                PQ.findMin()
    print("test concluso\n passati ",time.time()-inizio,"secondi")   ##
    return PQ


def insert_test_relax(num_nodi, tipoInserimento, inizio_int = 0, fine_int = 10):
    """testa inserimenti e findMin
        su heap RELAX  
        tipo inserimento: stringa, casuale o sequenziale
        valori sequenziali tra inizio_int e inizio_int+numNodi
        findMin inseriti in percentuale 1/fattore find_min
        al fine di dare consistenza a ricerca minimo
        (se ricercato solo dopo tutti inserimenti si troverebbe sempre
        stesso minimo!)"""
    PQ = PQBinomialRelax()
    assert tipoInserimento in ["sequenziale", "casuale"],"scegli tra inserimento sequenziale o casuale"
    print("test su varie insert e findMin su heap binomiale \ninserimento",tipoInserimento)
    ##
    inizio=time.time()  ##
    if tipoInserimento == "sequenziale":
        for x in range(inizio_int,inizio_int+num_nodi ):
            PQ.insert(x, x)
            if x % FATTORE_FIND_MIN == 0:
                PQ.findMin()
    else:  # random inserimento
        for z in range(num_nodi):
            x = random.randint(inizio_int, fine_int)
            PQ.insert(x, x)
            if z % FATTORE_FIND_MIN == 0:
                PQ.findMin()
    print("test concluso\n passati ",time.time()-inizio,"secondi")

    return PQ
def albero_bh_seq(num_nodi,inizio_int=0):
    """ crea albero binomiale  con nodi a chiavi sequenziali
       tra inizio_int e inizio_int+num_nodi
        dopo  un ciclo di num_nodi inserimenti
        
        testa su n/Fattore_Del deleteMin 
        """
    inizio=time.time()  ##
    ##
    print("testing su n insert e n/Fattore_Del deleteMin","su heap binomiali, inserimenti sequenziali")
    PQ = PQbinomialHeap()
    i = 0
    
    for x in range(inizio_int,inizio_int+num_nodi ):
        PQ.insert(i, i)
         
        
    for x in range(int(num_nodi/FATTORE_DEL)):
        PQ.deleteMin()
    print("test Concluso passato",time.time()-inizio,"secondi")
    return PQ


def albero_bh_ran(num_nodi, inizio_int, fine_int):
    """ crea albero binomiale  con nodi a chiavi casuale
       tra inizio_int e fine_int
        dopo  un ciclo di num_nodi inserimenti
        
        testa su n/Fattore_Del deleteMin """
    inizio=time.time()  ##
    ##
    print("testing su n insert e n/Fattore_Del deleteMin","su heap binomiali, inserimenti casuali")
    PQ = PQbinomialHeap()
    i = 0
    while i < num_nodi:
        n = random.randint(inizio_int, fine_int)
        PQ.insert(n, n)
        ##if i % FATTORE_DEL == 0:
        ##    PQ.deleteMin()

        i += 1
    for x in range(int(num_nodi/FATTORE_DEL)):
        PQ.deleteMin()
    print("test Concluso passato",time.time()-inizio,"secondi")##
    return PQ


def albero_bhr_seq(num_nodi,inizio_int=0):
    """ crea albero binomiale rilassato
     con nodi a chiavi sequenziali
       tra inizio_int e inizio_int+num_nodi
        dopo  un ciclo di num_nodi inserimenti
        
        testa su n/Fattore_Del deleteMin 
         """
    PQ = PQBinomialRelax()
    i = 0
    ##
    print("testing su n insert e n/Fattore_Del deleteMin","su heap relax, inserimenti sequenziali")
    inizio=time.time()##
    for x in range(inizio_int,inizio_int+num_nodi ):
        PQ.insert(i, i)
        #if i % FATTORE_REBUILD == 0:
        #    PQ.rebuild()
        i += 1
    for x in range(int(num_nodi/FATTORE_DEL)):
        PQ.deleteMin()
    print("test Concluso passato",time.time()-inizio,"secondi")##

    return PQ


def albero_bhr_ran(num_nodi, inizio_int, fine_int):
    """crea albero binomiale RILASSATO
       con nodi a chiavi sequenziali
       tra inizio_int e fine_int
        dopo  un ciclo di num_nodi inserimenti
        
        testa su n/Fattore_Del deleteMin """
    PQ = PQBinomialRelax()
    i = 0
    ##
    print("testing su N insert e N/Fattore_Del deleteMin","su heap relax, inserimenti casuali")
    inizio=time.time()##
    
    while i < num_nodi:
        n = random.randint(inizio_int, fine_int)
        PQ.insert(n, n)
        ##if i % FATTORE_REBUILD == 0:
        ##    PQ.rebuild()
        i += 1
    for x in range(int(num_nodi/FATTORE_DEL)):
        PQ.deleteMin()

    print("test Concluso passato",time.time()-inizio,"secondi")##

    return PQ


 

def testVari(tipo,iterazioni=20):
    print("tests su varie op, verifica validità tramite ordinamento")
    tests(tipo, iterazioni)
if __name__ == "__main__":
    num_nodi = 150000
    inizio_int = 30
    fine_int = 33000

    print("confronti su insert e deleteMin su heaps rilassati con inserimenti casuali o sequenziali")
    
    print("\ninizio heap RELAX sequenziale")
    albero_bhr_seq(num_nodi,inizio_int)
    print("fine heap RELAX sequenziale\n")
 
    print("\ninizio heap RELAX casuale")
    albero_bhr_ran(num_nodi, inizio_int, fine_int)
    print("fine heap RELAX casuale\n")
  
    print("inizio heap BINOMIALE sequenziale")
    albero_bh_seq(num_nodi,inizio_int)
    print("fine heap BINOMIALE sequenziale\n")
     
    print("\ninizio heap BINOMIALE  casuale\n")
    albero_bh_ran(num_nodi, inizio_int, fine_int)
    print("fine heap  BINOMIALE casuale\n")
    
    print("\n\n\n test su inserimenti e findMin su heaps binomiali e rilassati")
    print("\ntest su inserimenti casuali heap RELAX ")
     
    insert_test_relax(num_nodi, "casuale", inizio_int, fine_int)
    print("fine Test \n\n") 
    print("test su inserimenti sequenziali heap RELAX ")
     
    insert_test_relax(num_nodi, "sequenziale", inizio_int, fine_int)
    print("fine Test \n\n")



    print("test su inserimenti sequenziali heap BINOMIALE ")
     
    insert_test(num_nodi, "sequenziale", inizio_int, fine_int)
    print("fine Test \n\n")
    print("test su inserimenti casuali heap BINOMIALE ")
      
    insert_test(num_nodi, "casuale", inizio_int, fine_int)
    print("fine Test \n\n") 
    
