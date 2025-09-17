"""
4 Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""

print("Adj meg három számot")
szam_1 = int(input("Adj meg egy számot! "))
szam_2 = int(input("Adj meg egy számot! "))
szam_3 = int(input("Adj meg egy számot! "))

if szam_1 > szam_2 and szam_1 > szam_3:
     print(f"A legnagyobb szám: {szam_1}")
elif szam_2 > szam_1 and szam_2 > szam_3:
     print(f"A legnagyobb szám: {szam_2}")
else:
     print(f"A legnagyobb szám: {szam_3}")