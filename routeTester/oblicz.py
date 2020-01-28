#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
import string
from math import sqrt
 # Wywołania: " python zmieniacz.py nazwa_pliku_we" (np.: "python zmieniacz.py berlin52.txt wyniki.txt")
def zbudujMacierz(wiersze):
    macierz = [[0 for col in range(int(wiersze[0]))] for row in range(int(wiersze[0]))]
    i = 0
    for w in wiersze[1:]:
        w = w.strip().split(' ')
        j = 0
        for odl in w:
            macierz[i][j] = int(odl)
            macierz[j][i] = int(odl)
            j+=1
        i+=1
    return macierz

def obliczOdleglosc(trasa, macierz):
    odleglosc = 0
    trasa = trasa.strip().split('-')
    try:
        trasa = list(map(int, trasa))
    except ValueError:
        pass
    for i in range(len(trasa)-1):
        odleglosc+=macierz[trasa[i]][trasa[i+1]]
    odleglosc+=macierz[trasa[len(trasa)-1]][trasa[0]]
    return odleglosc, trasa

nPliku = sys.argv[1]
nPlikuWynikow = sys.argv[2]

plikWe = open(nPliku, 'r') # Otwarcie pliku wejściowego
plikWe2 = open(nPlikuWynikow, 'r') # Otwarcie pliku wejściowego wyników

plikWy = open('spr_'+nPliku.split('.')[0]+'.txt', 'w') # Stworzenie nowego pliku (wyjściowego) o tej samej nazwie, co wejściowy, ale z rozszerzeniem .txt

wiersze = plikWe.readlines() # linie pliku do listy
plikWe.close()

macierz = zbudujMacierz(wiersze)

wyniki = plikWe2.readlines() # linie pliku do listy
plikWe2.close()

#minimum = sys.maxint
for w in wyniki:
    odleglosc = 0
    w = w.strip().split(' ') # Podział linii według spacji, a przed tym wycięcie zbędnych białych znaków
    if len(w)==2:
        odleglosc, trasa = obliczOdleglosc(w[0], macierz)

        flaga = True
        if len(trasa) != int(wiersze[0]):
            flaga = False

        i=0
        trasa.sort()
        for el in trasa:
            if el!=i:
                flaga = False
            i+=1

#        if odleglosc<minimum:
#            minimum=odleglosc
        wynik = "%i %i %s %s" % (odleglosc, int(w[1]), "Odległość: "+str(odleglosc==int(w[1])), "Trasa: "+str(flaga))
    else:
        wynik = "Pominięto: %s" % w
    print(wynik)
    plikWy.write(wynik+'\n') # Zapisanie do pliku
       
plikWy.close()
#print(minimum)
