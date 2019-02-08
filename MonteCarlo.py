#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
np.set_printoptions(threshold=11000)

def hodmincami(Nkrat):
    '''
    Funkcia vytvorí náhodne hod N mincami (ako rad núl a jednotiek).
    1 - znamená znak
    0 - znamená písmo
    '''
    if Nkrat>10**6:
        print('Algoritmus je naprogramovaný na hod s max. 1 milión mincami naraz.')
        pocethodov = 10**6
    else:
        pocethodov = Nkrat
    radhodov = np.random.randint(0,2, size=pocethodov)
    return radhodov

def statistika(hod):
    '''
    Funkcia spočíta v danom hode viacerými mincami počet znakov (jednotiek) a počet všetkých mincí.
    Dané počty vypíše.
    '''
    h1 = 'počet znakov = '
    h2 = 'počet všetkých mincí = '
    print('Štatistika hodov:')
    print(h1,sum(hod),', ',h2,len(hod))
    print()

def zobraz(hody):
    '''
    Funkcia zobrazí prvých max 10 000 mincí v danom hode mincami.
    '''
    print('Zobrazujem prvých (max. 10 000) mincí z(o) ', len(hody),' mincí:')
    print(hody[:10000])
    print()