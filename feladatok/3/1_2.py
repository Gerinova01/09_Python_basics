"""
1.2 Feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem)
közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
"""

kérdés = input("Jó napod van? [igen/nem] ")

if kérdés == "igen":
    print("Az jó")
elif kérdés == "nem":
    print("Remélem jobb lesz")
else:
    print("Sajnos nem értem a válaszodat!")