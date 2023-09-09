import random

sim = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

d = ""

for i in range(500000):
    d += random.choice(sim)
    print(f"\033[32m{d}\033[0m", end='', flush=True)