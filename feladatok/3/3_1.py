"""
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
"""
#ez a kód a kiszámolja és kiírja egy kör kerületét és területét
PI = 3.14159
sugar = 5 #cm

kerület = 2 * PI * sugar
terület = PI * sugar*sugar

print(f"A kör kerülete: {kerület} cm")
print(f"A kör területe: {terület} cm²")