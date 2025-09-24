"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot,
 majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
 Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random
gondolt_szam = random.randint(1,3)
adott_szam = int(input("Tippeljen egy számot 1 és 3 között "))
if adott_szam < gondolt_szam:
    print("nagyobb számra gondoltam")
elif adott_szam > gondolt_szam:
    print("kisebb számra gondoltam")
else:
    print ("kitaláltad!")