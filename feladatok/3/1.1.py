"""
1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e!
A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""

kérdés = input("Jó napod van? [igen/nem] ")

if kérdés == "igen":
    print("Az jó")
elif kérdés == "nem":
    print("Remélem jobb lesz")
else:
    print("ÖLD MEG MAGAD")