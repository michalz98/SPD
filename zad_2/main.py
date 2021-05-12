from RandomNumberGenerator import RandomNumberGenerator as rng
# from DynamicProgramming import dP
from Greedy import Greedy
from BruteForce import brute
from DynamicProgramming import dP

seed = int(input("Ziarno: "))
n = int(input("Ilosc zadan: "))
print()

RNG = rng(seedValue=seed)

J = []
P = []
W = []
D = []

memory = []
PI = []
C = []
T = []
wT = []

for i in range(n):
    J.append(i)

for i in range(n):
    P.append(RNG.nextInt(1, 29))

A = sum(P)

for i in range(n):
    W.append(RNG.nextInt(1, 9))

for i in range(n):
    D.append(RNG.nextInt(1, 29))    # 29 zmienic na A po testach


for i in range(n):
    J[i] += 1

print("Permutacja naturalna:")
print(f'Pi:{J}')
print(f'P: {P}')
print(f'W:{W}')
print(f'D:{D}')
print()

for i in range(n):
    J[i] -= 1

# --------------------------BruteForce-----------------------------------

#brute(J.copy(), P.copy(), D.copy(), W.copy())

# --------------------------Greedy---------------------------------------


# PI = Greedy(J.copy(), D)

# print("Algorytm zachłanny:")
# print(f'Pi:{PI}')
# print(f'P: {P}')
# print(f'W:{W}')
# print(f'D:{D}')
# print()


# --------------------------DynamicProgramming-----------------------------------

dP(J, P, D, W)


# d = []
# memory.append(0)
# for i in range(0, pow(2, n)):
#     d.append(i)

# for j in J:
#     dP(j, J.copy, P, W, D, memory)

# print(len(d))
# print(n-1 - bin(1)[2:].zfill(n).find("1"))
