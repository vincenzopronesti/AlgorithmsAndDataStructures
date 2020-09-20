#!/usr/bin/env python
# encoding: utf-8

from tkinter import *

from demo_definitivo import *

global a
a=[11,0, 111, 'binomial', 'casuale','deleteMin',False]  #valori di default
#a= lista con valori presi da interfaccia grafica 
DIM_START=44
DIM_BUTT=15
def start(): #collegamento a bottone start
    """ inserisce in a valori all'interno delle entries
        SOSTITUENDOLI CON VALORI DI DEFAULT SE INSERITI CARATTERI
        distrugge l interfaccia"""
    global a
    c=0
    entrys=[num1,num2,num3]
    for x in range(3):
        string=entrys[x].get()
        if string.isdigit() or string[1:].isdigit() and string[0]=="-":    #primo carattere puo essere-
            a[x]=int(string) #inserimento in a valore di entry solo se è composto da cifre
        c+=1

    main.destroy()  #distrugge interfaccia 
     

def binomial(): #collegamento bottone
    """ inserisce in a, valore scelto da interfaccia
       disabilità scelte alternative a bottone premuto
       per evitare input dovuti un click distratto"""
    global a
    a[3]="binomial"
    num4["state"]="disabled"
    num4bis["state"] = "disabled"
def deletMin(): #collegamento bottone
    """ inserisce in a, valore scelto da interfaccia
       disabilità scelte alternative a bottone premuto
       per evitare input dovuti un click distratto"""
    global a
    a[5]="deleteMin"
    num6["state"]="disabled"
    num6bis["state"] = "disabled"
def insertFind(): #collegamento bottone
    """ inserisce in a, valore scelto da interfaccia
       disabilità scelte alternative a bottone premuto
       per evitare input dovuti un click distratto"""
    global a
    a[5]="insertFind"
    num6["state"]="disabled"
    num6bis["state"] = "disabled"
def relax(): #collegamento bottone
    """ inserisce in a, valore scelto da interfaccia
       disabilità scelte alternative a bottone premuto
       per evitare input dovuti un click distratto"""
    global a
    a[3]="relax"
    num4["state"] = "disabled"
    num4bis["state"]="disabled"
def randominput(): #collegamento bottone
    """ inserisce in a, valore scelto da interfaccia
       disabilità scelte alternative a bottone premuto
       per evitare input dovuti un click distratto"""
    global a
    a[4]="casuale"
    num5["state"] = "disabled"
    num5bis["state"] = "disabled"
def seqinput(): #collegamento bottone
    """ inserisce in a, valore scelto da interfaccia
       disabilità scelte alternative a bottone premuto
       per evitare input dovuti un click distratto"""
    global a
    a[4]="sequenziale"
    num5["state"] = "disabled"
    num5bis["state"] = "disabled"
def stampa(): #collegamento bottone
    """ inserisce in a, valore scelto da interfaccia
        in base a testo bottone cambio valore booleano in a"""
    global a

    if num7["text"]=="stampa_OFF":  #Scambia testo e booleno per stampa albero dopo testing
        a[-1] = True
        num7["text"] = "stampa_ON"
    else:
        a[-1] = False
        num7["text"] = "stampa_OFF"
main = Tk()
#etichette con testo :
main.wm_title("ANDREA DI IORIO-VINCENZO PRONESTI-LIVIO TIRABORRELLI")
l1=Label(main, text = "Numero nodi").grid(row=0,column=0)
l2=Label(main, text = "Inizio intervallo").grid(row=1,column=0)
l3=Label(main, text = "Fine intervallo").grid(row=2,column=0)
l4=Label(main, text = "Metodo inserimento").grid(row=4,column=0)
l5=Label(main, text = "Struttura dati").grid(row=3,column=0)
l6=Label(main, text = "Testing").grid(row=5,column=0)
# entry, campi in cui inserire valori 
num1 = Entry(main)
num2 = Entry(main)
num3 = Entry(main)
#bottoni per scelte
num4 = Button(main,text='Binomiale',command=binomial)
num4bis = Button(main,text='Rilassato',command=relax)

num5 = Button(main,text='Random',command=randominput)
num5bis = Button(main,text='Seqenziale',command=seqinput)
num6 = Button(main,text='deleteMin',command=deletMin)
num6bis = Button(main,text='insert&findMin',command=insertFind)
num7 = Button(main,text='stampa_OFF',command=stampa)
#grid, posizionamento nella finestra
num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
num3.grid(row=2, column=1)
num4.grid(row=3, column=1)
num4bis.grid(row=3, column=2)
num5.grid(row=4, column=1)
num5bis.grid(row=4, column=2)
num6.grid(row=5, column=1)
num6bis.grid(row=5, column=2)
num7.grid(row=0, column=2)
#dimensionamento
num1.configure(width=DIM_BUTT)
num2.configure(width=DIM_BUTT)
num3.configure(width=DIM_BUTT)
num4.configure(width=DIM_BUTT)
num4bis.configure(width=DIM_BUTT)
num5.configure(width=DIM_BUTT)
num5bis.configure(width=DIM_BUTT)
num6.configure(width=DIM_BUTT)
num6bis.configure(width=DIM_BUTT)
num7.configure(width=DIM_BUTT)

start=Button(main, text='START!', command=start)
start.grid(row=7, column=1 )
start.configure(width=DIM_START,padx=1,pady=1)
start["background"]="yellow"
mainloop()  #ciclo di funzionamento interfaccia tkinter
print(a)
print("inseriti","numero nodi    inizio intervallo    fine intervallo    struttura dati tinserimenti tipologia")
#print("\t\t"*15,"op in testing \t          STAMPA BOOL")
if a[1]>a[2]:
    a[1],a[2]=a[2],a[1] #swap su intervallo errato
    
for x in range(len(a)): # controlli validità inserimenti
    #print(2*x*"\t\t\t",a[x])
    if x==0:
        assert a[x]>0,"testing accettabile se quantita di nodi positive"
    elif x <3:
        assert type(a[x])==int,"controllo errato su dimensioni coda con priorita"
    elif x==3:
        assert a[x] in ["binomial","relax"]
    elif x==4:   #x=4 ultimo
        assert a[x] in ["sequenziale","casuale"]
    elif x==5:
        assert a[x] in ["deleteMin","insertFind"]

    else:
        a[x] in [True,False]

##################
if __name__ == "__main__":
    #testing in demo con valori presi da interfaccia grafica e messi in a
    c = 0
    n_nodi = a[0]
    inizio_int = a[1]
    fine_int = a[2]
    if fine_int < inizio_int:
        inizio_int,fine_int=fine_int,inizio_int
    
    if a[5]=="deleteMin":
        if a[4] == "sequenziale":
            if a[3] == "binomial":

                tr = albero_bh_seq(n_nodi,inizio_int)
            else: #relax
                tr = albero_bhr_seq(n_nodi,inizio_int)
        else: #random
            if a[3] == "binomial":

                
                tr = albero_bh_ran(n_nodi, inizio_int, fine_int)
            else: #relax
                 
                tr = albero_bhr_ran(n_nodi, inizio_int, fine_int)
    else: #testing su findMin e insert
        if a[4] == "sequenziale":
            if a[3] == "binomial":

                tr = insert_test(n_nodi,"sequenziale", inizio_int, fine_int)
            else:
                tr = insert_test_relax(n_nodi,"sequenziale", inizio_int, fine_int)
        else:
            if a[3] == "binomial":

                inizio_int = a[1]
                fine_int = a[2]
                tr = insert_test(n_nodi,"casuale",inizio_int, fine_int,)
            else:
                inizio_int = a[1]
                fine_int = a[2]
                tr = insert_test_relax(n_nodi, "casuale", inizio_int, fine_int)

    if a[-1]:   #ultimo valore di a flag per stampa heap
        tr.stampa()
    
        
    
        
        
        

        
        
            
    
                       
    
    
    
    
