"""
3 Szó keresése a szövegben  tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra, majd ellenőrizd, hogy szerepel-e benne a „Python” szó.
b) Ha van benne, akkor hányszor?
"""

szoveg = input("Adjon meg egy szöveget! ")

szam = szoveg.count("python")
print(f"A python szó {szam} helyen jelenik meg a szövegében")