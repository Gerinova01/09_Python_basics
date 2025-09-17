"""
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot!
 Azután a program bekér egy számot a felhasználótól,
 majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
"""

import random
gondolt_szam = random.randint(1,5)
adott_szam = int(input("Tippeljen egy számot 1 és 5 között "))
if adott_szam < gondolt_szam:
    print("nagyobb számra gondoltam")
elif adott_szam > gondolt_szam:
    print("kisebb számra gondoltam")
else:
    print ("kitaláltad!")