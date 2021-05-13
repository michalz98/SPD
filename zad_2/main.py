from RandomNumberGenerator import RandomNumberGenerator as rng
from Greedy import Greedy
from BruteForce import brute
from DynamicProgramming import dP
import time

acc = 6

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


sump = 0
wiTi = 0
for i in range(len(J)):
    sump += P[i]
    C.append(sump)
    dif = sump - D[i]
    if dif < 0:
        T.append(0)
    else:
        T.append(dif)

    wT.append(T[i] * W[i])
    wiTi += wT[i]

for i in range(n):
    J[i] += 1

print("Permutacja naturalna:")
print(f'Pi:{J}')
print(f'P: {P}')
print(f'W:{W}')
print(f'D:{D}')
print()
print(f'C: {C}')
print(f'T: {T}')
print(f'wT: {wT}')
print(f'wiTi:{wiTi}')
print()

for i in range(n):
    J[i] -= 1

# --------------------------Greedy---------------------------------------

print("Greedy")
start = time.time()
Greedy(P.copy(), W.copy(), D.copy())
end = time.time()
print(f'czas wykonywania: {round(end - start, acc)}')
print()

# --------------------------BruteForce-----------------------------------

print("Brute Force")
start = time.time()
brute(J.copy(), P.copy(), D.copy(), W.copy())
end = time.time()
print(f'czas wykonywania: {round(end - start, acc)}')
print()

# --------------------------DynamicProgramming-----------------------------------

print("Dynamic Programming")
start = time.time()
dP(J, P, D, W)
end = time.time()
print(f'czas wykonywania: {round(end - start, acc)}')
