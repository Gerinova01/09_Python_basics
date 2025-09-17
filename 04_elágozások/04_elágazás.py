"""
Ha a bevitt szám kisebb mint 0, akkor írja ki hogy a szám negatív, ha nagyobb akkor írja ki hogy a szám pozitív.
"""

#szam = int(input("Adj meg egy számot "))

#if szam < 0:
    #print("Ez a szám negatív")
#elif szam > 0:
    #print("Ez a szám pozitív")
#else:
    #print("Nulla")
"""
    Ha a szám ostható 2-vel páros, ha nem páratlan.
 """

szam = int(input("Adj meg egy számot "))

if szam % 2 == 0 and szam != 0:
    print("A megadott szám páros")
elif szam == 0:
    print("Nulla")
else:
    print("A megaditt szám páratlan")
