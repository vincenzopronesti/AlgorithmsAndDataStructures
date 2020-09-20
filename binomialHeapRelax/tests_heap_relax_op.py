#!/usr/bin/env python
# encoding: utf-8

from tkinter import *
from tkinter.messagebox import *
from PQBinomialRelax import tests


global tipo
tipo="deleteMin"#tipo di test, default deleteMin
DIM_START = 44   #dimensioni per bottoni
DIM_BUTT = 15

#funzioni collegati a bottoni #########################à
def start():
    """
    valore di default su iterazioni test, in caso di non inserimento cifre
    riabilità tutti bottoni e esegue test"""
    global tipo
    string=num1.get()
    if string.isdigit():
        iterazioni=int(string)  #entry deve prendere cifre e non caratteri
    else:
        iterazioni=10   #valore di default
    print("iterazioni scelte o di default = ",iterazioni)
    tests(tipo,iterazioni)  #esecuzione test scelto
    num4["state"] = "normal"
    num4bis["state"] = "normal"
    num5["state"] = "normal"
    num5bis["state"] = "normal"
def deleteMin():
    """sceglie tipo e disabilita tutti altri bottoni(per evitare scelte
     da click distratti"""
    global tipo
    tipo="deleteMin"
    num4["state"] = "disabled"
    num4bis["state"] = "disabled"
    num5["state"] = "disabled"
    num5bis["state"] = "disabled"

def merge():
    """sceglie tipo e disabilita tutti altri bottoni(per evitare scelte
     da click distratti"""
    global tipo
    tipo="merge"
    num4["state"] = "disabled"
    num4bis["state"] = "disabled"
    num5["state"] = "disabled"
    num5bis["state"] = "disabled"
def decreaseKey():
    """sceglie tipo e disabilita tutti altri bottoni(per evitare scelte
     da click distratti"""
    global  tipo
    tipo="decreaseKey"
    num4["state"] = "disabled"
    num4bis["state"] = "disabled"
    num5["state"] = "disabled"
    num5bis["state"] = "disabled"
def delete():   
    """sceglie tipo e disabilita tutti altri bottoni(per evitare scelte
     da click distratti"""
    global tipo
    tipo="delete"
    num4["state"] = "disabled"
    num4bis["state"] = "disabled"
    num5["state"] = "disabled"
    num5bis["state"] = "disabled"

main = Tk()
#etichette
main.wm_title("ANDREA DI IORIO-VINCENZO PRONESTI-LIVIO TIRABORRELLI")
l1 = Label(main, text="testing su tutte op con verifica tramite riordinamento").grid(row=0, column=0)

l3 = Label(main, text="ITERAZIONI").grid(row=1, column=0)
num1 = Entry(main)  #campo per iterazioni
# bottoni #####

num4 = Button(main, text='deleteMin', command=deleteMin)
num4bis = Button(main, text='merge', command=merge)
num5 = Button(main, text='decreaseKey', command=decreaseKey)
num5bis = Button(main, text='delete', command=delete)

# grid, posizionamento nella finestra
num1.grid(row=1, column=1)

num4.grid(row=3, column=0)
num4bis.grid(row=3, column=1)
num5.grid(row=4, column=0)
num5bis.grid(row=4, column=1)

# dimensionamento
num1.configure(width=DIM_BUTT)

num4.configure(width=DIM_BUTT)
num4bis.configure(width=DIM_BUTT)
num5.configure(width=DIM_BUTT)
num5bis.configure(width=DIM_BUTT)

start = Button(main, text='START!', command=start)
start.grid(row=7, column=1)
start.configure(width=DIM_START, padx=1, pady=1)
start["background"] = "yellow"
mainloop()  #ciclo per modulo grafico

