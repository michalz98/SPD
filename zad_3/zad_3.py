from RandomNumberGenerator import RandomNumberGenerator as rng
from Johnson import johnson

seed = int(input("Ziarno: "))
n = int(input("Ilosc zadan: "))
m = int(input("Ilosc maszyn: "))
print()

RNG = rng(seedValue=seed)

J = []
P = []
S = []
C = []
Cmax = 0

for i in range(n):
    J.append(i)

for i in range(n):
    P.append([0]*m)

for i in range(n):
    S.append([0]*m)

for i in range(n):
    C.append([0]*m)

for i in P:
    for j in range(m):
        i[j] = RNG.nextInt(1, 29)

C[0][0] = P[0][0]
for i in range(1, m):
    C[0][i] = P[0][i] + C[0][i-1]

for i in range(1, n):
    C[i][0] = C[i-1][0] + P[i][0]

for k in range(1, m):
    for i in range(1, n):
        C[i][k] = max(C[i][k-1], C[i-1][k]) + P[i][k-1]

for k in range(m):
    for i in range(n):
        S[i][k] = C[i][k] - P[i][k]

Cmax = max(max(C))

for i in J:
    i += 1

print("Permutacja naturalna:")
print(f'Pi:{J}')
print(f'C:{C}')
print(f'Cmax:{Cmax}')
print()

for i in J:
    i -= 1

pi = johnson(J, P, n, m)

C[0][0] = P[0][0]
for i in range(1, m):
    C[0][i] = P[0][i] + C[0][i-1]

for i in range(1, n):
    C[i][0] = C[i-1][0] + P[pi[i]][0]

for k in range(1, m):
    for i in range(1, n):
        C[i][k] = max(C[i][k-1], C[i-1][k]) + P[pi[i]][k]

for k in range(m):
    for i in range(n):
        S[i][k] = C[i][k] - P[pi[i]][k]

Cmax = max(max(C))


print("Algorytm Johnson'a:")
for i in pi:
    i += 1

print(f'Pi:{pi}')
print(f'C:{C}')
print(f'Cmax:{Cmax}')

for i in pi:
    i -= 1
print()