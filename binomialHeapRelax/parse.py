#!/usr/bin/env python
# encoding: utf-8

import argparse
import demo_definitivo as demo
import sys


def parseArgs():
        parser = argparse.ArgumentParser(description = "input per heap binomiali  A INSERIMENTI CASUALI")
        parser.add_argument("numero_nodi_da_creare", type = int, help = \
                "tipo intero, numero dei nodi che verranno creati")

        parser.add_argument("inizio_intervallo", type = int, help = \
                "tipo intero, inizio dell'intervallo in cui verranno generati i numeri")
        parser.add_argument("fine_intervallo", type = int, help = \
                "tipo intero, fine dell'intervallo in cui verranno generati i numeri, IGNORATO IN CASO DI VALORI SEQUENZIALI")
        parser.add_argument("struttura", type = int, choices = [0, 1],\
         help = "0: heap binomaiale\n1: heap rilassato")
        parser.add_argument("operazione", type = str, choices = ["deleteMin", "findMin"], \
        help = "il tipo di operazione da eseguire oltre agli inserimenti, si può scegliere tra deleteMin e findMin")

        parser.add_argument("-s", "--sequenziale", action = "store_true",\
                            help="di default i valori vengono generati casualmente, se si specifica --sequenziale allora verranno generati in modo iterativo")



        args = parser.parse_args()
        if args.numero_nodi_da_creare < 0:
                raise argparse.ArgumentTypeError("il numero di nodi da creare deve essere positivo")
        return args


 

def main(args):
        if args.inizio_intervallo> args.fine_intervallo:
                args.inizio_intervallo, args.fine_intervallo= args.fine_intervallo,args.inizio_intervallo
        s={0:'heap binomiale', 1:'heap binomiale rilassato'}
        print("struttura: ", s[args.struttura])
        if args.sequenziale == False:
                print("i valori sono generati in modo casule\n",\
            "numero nodi da creare: {}\n intervallo inizio: {}\n intervallo fine: {}\n".format(args.numero_nodi_da_creare, \
                                        args.inizio_intervallo, args.fine_intervallo))
                if args.struttura == 0: # binomiale
                        if args.operazione == "deleteMin":
                                demo.albero_bh_ran(args.numero_nodi_da_creare, args.inizio_intervallo, args.fine_intervallo)
                        else: # findMin
                                demo.insert_test(args.numero_nodi_da_creare, "casuale", args.inizio_intervallo, args.fine_intervallo)
                else: # rilassato
                        if args.operazione == "deleteMin":
                                demo.albero_bhr_ran(args.numero_nodi_da_creare, args.inizio_intervallo, args.fine_intervallo)
                        else: # findMin
                                demo.insert_test_relax(args.numero_nodi_da_creare, "casuale", args.inizio_intervallo, args.fine_intervallo)
        else: # sequenziale
                print("i valori sono generati in modo iterativo\n",\
                          "numero nodi da creare:  {}\n".format(args.numero_nodi_da_creare))
                if args.struttura == 0: # binomiale
                        if args.operazione == "deleteMin":
                                demo.albero_bh_seq(args.numero_nodi_da_creare,args.inizio_intervallo)
                        else: # findMin
                                demo.insert_test(args.numero_nodi_da_creare, "sequenziale",args.inizio_intervallo)
                else: # rilassato
                        if args.operazione == "deleteMin":
                                demo.albero_bhr_seq(args.numero_nodi_da_creare,args.inizio_intervallo)
                        else: # findMin
                                demo.insert_test_relax(args.numero_nodi_da_creare, "sequenziale",args.inizio_intervallo)

if __name__ == "__main__":
        
	args = parseArgs()
	main(args)
