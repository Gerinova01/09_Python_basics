"""
2 Szóhossz meghatározása tweet vagy SMS ellenőrzés
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll.
 Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez.
"""

uzenet  = input("Adj meg egy üzenetet! ")
hossz = len(uzenet)

print(f"Az üzeneted {hossz}karakter hosszú")