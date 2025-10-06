"""
2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket
"""

szamA = int(input("Adj meg egy egész számot számot "))
szamB = int(input("Adj meg egy másik egész számot számot "))

if szamA < szamB:
    for x in range(szamB, szamA -1):
        print(x)