"""
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""

import random

pénz = random.randint(1,2)
válasz = int(input("Válasszon 1 [Fej] és 2 [írás] között"))

if válasz == pénz:
    print("jó válasz")
else:
    print("rosz válasz")