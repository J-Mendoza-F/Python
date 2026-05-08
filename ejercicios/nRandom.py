# ADIVINAR NÚMERO ALEATORIO

import random

x=random.randint(1,10)
n=int(input("Adivina el número (1 - 10): "))

if n==x:
    print("[CORRECTO]")
else:
    print("[NÚMERO INCORRECTO]")