"""
5 Szökőév ellenőrző
Kérj be egy évet, és írd ki, hogy szökőév-e.
 (Szökőév, ha osztható 4-gyel, de nem 100-zal, kivéve ha 400-zal is osztható.)
"""

évszám = int(input("Adj meg egy évszámot! "))
if évszám % 4 == 0 and  évszám % 100 or évszám % 400 == 0:
    print("Ez az év egy szokőév")
else:
    print("Ez az év nem szökőev")