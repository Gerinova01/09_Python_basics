"""
1 Kis- és nagybetűssé alakítás - névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),


kisbetűs (pl. email összehasonlításhoz),


csak az első betű nagy (személyes üdvözlésnél).

"""

felhasznalo = input("Adj meg egy felhasználónevet! ")
nagy = felhasznalo.capitalize()

print(f"Nagybetűs szó {nagy}")

kis = felhasznalo.lower()

print(f"kisbetűs szó {kis}")