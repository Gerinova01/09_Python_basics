"""
    1. Összegszámítás
Kérj be egy egész számot (pl. 10; 13;  20…),
és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""

szam = int(input("Adj meg egy egész számot számot "))

for x in range(1, szam):
    print(x)
print (sum(range(1,szam)))