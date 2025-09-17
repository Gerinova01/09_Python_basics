"""
7 Hőmérséklet tanács
Kérj be egy hőmérsékletet Celsiusban, és adj tanácsot:
0 alatt: „Nagyon hideg, öltözz melegen!”
0-20: „Hűvös, kabát ajánlott.”
21-30: „Kellemes idő.”
30 felett: „Forróság, igyál sok vizet!”
"""

hőfok =  int(input("Írjon be egy hőmérsékletet celsiusban. "))

if hőfok < 0:
    print("Nagyon hideg, öltözz melegen!")
elif hőfok <=20:
    print("Hűvös, kabát ajánlott.")
elif hőfok <=30:
    print("Kellemes idő")
elif hőfok > 30:
    print("Forróság, igyál sok vizet!")