"""
5 Szó elejének/végének ellenőrzése  email ellenőrzés
Feladat: Kérj be egy email címet a regisztrációhoz, majd ellenőrizd, hogy Gmail-es-e.
"""

cim = input("Adj meg egy gmail címet! ")
if "@gmail.com" in cim:
    print("Cím elfogadva")
else:
    print("Nem valós gmail cím")