"""
A csoport:
Készítsünk programot, amely labdák csomagolásához végez számításokat.
A labdákat szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni készítéséhez számolunk még 60 cm-t.
A labda körül a szalag egy kör (kerület képlete 2*r*PI)
A program kérje be a labda átmérőjét, a labdák számát, és a rendelkezésre álló szalag hosszát!
Számítsa ki, és írja a képernyőre, hogy a bekért számú labda csomagolásához hány centiméter szalagra van szükség, valamint állapítsa meg,
hogy elegendő szalagunk van-e a művelet elvégzéséhez, és ezt is közölje a felhasználóval!
"""

menyiség = int(input("Írja be a labák számát "))
sugár = int(input("Írja be a labdák átmérőjét cm-ben "))
szalag = int(input("Írja be a szalag hosszát cm-ben "))

szalag_kell = menyiség * sugár * 2 * 3.14 + 60

print(f"A labdák köré {szalag_kell}cm szalag kell.")

if szalag_kell <= szalag:
    print("A szalag elég")
else:
    print("Több szalag kell")