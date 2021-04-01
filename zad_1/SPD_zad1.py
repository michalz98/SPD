import Schrage
import Carlier
from RandomNumberGenerator import RandomNumberGenerator as Rng


seed = int(input("Ziarno: "))
n = int(input("Ilosc elementow: "))

rng = Rng(seedVaule=seed)

Cq = []
J = []
P_j = []    # czasy wykonania
R_j = []    # czasy przygotowania/termin dostepnosci
S = []      # czasy rozpoczecia
C = []      # czasy zakonczenia
Q_j = []    # czas dostarczenia/stygniecia
PI = []
A = 0

for i in range(n):
    J.append(i)

for i in range(n):
    p_j = rng.nextInt(1, 29)
    P_j.append(p_j)
    A = A + p_j

for i in range(n):
    r_j = rng.nextInt(1, A)
    R_j.append(r_j)

X = A
for i in range(n):
    q_j = rng.nextInt(1, X)
    Q_j.append(q_j)

S.append(R_j[0])
C.append(S[0] + P_j[0])
Cq.append(C[0] + Q_j[0])
C_max = C[0] + Q_j[0]

for i in range(1, n):
    S.append(max(R_j[i], C[i-1]))
    C.append(S[i] + P_j[i])
    Cq.append(C[i] + Q_j[i])
    C_max = max(C_max, Cq[i])


for i in range(n):
    J[i] += 1

print(f'nr:{J}')
print(f'r:{R_j}')
print(f'p:{P_j}')
print(f'q:{Q_j}')
print()
print(f'S: {S}')
print(f'C: {C}')
print(f'Cq: {Cq}')
print()

for i in range(n):
    J[i] -= 1

S.clear()
C.clear()
Cq.clear()
PI.clear()

# ____________________ Algorytm standardowy _______________________

Schrage.schrage(J, R_j, P_j, Q_j, PI)

S.append(R_j[PI[0]])
C.append(S[0] + P_j[PI[0]])
Cq.append(C[0] + Q_j[PI[0]])
C_max = C[0] + Q_j[PI[0]]

for i in range(1, n):
    S.append(max(R_j[PI[i]], C[i-1]))
    C.append(S[i] + P_j[PI[i]])
    Cq.append(C[i] + Q_j[PI[i]])
    C_max = max(C_max, Cq[i])


print('Po zastosowaniu algorytmu bez przerwan:')
for i in range(n):
    PI[i] += 1

print(f'PI:{PI}')
print(f'S:{S}')
print(f'C:{C}')
print(f'Cq:{Cq}')
print(f'Cmax: {C_max}')
print()

for i in range(n):
    PI[i] -= 1

S.clear()
C.clear()
Cq.clear()
PI.clear()

# ____________________ Algorytm z kolejka _______________________


Schrage.schrage_k(J, R_j, P_j, Q_j, PI)

S.append(R_j[PI[0]])
C.append(S[0] + P_j[PI[0]])
Cq.append(C[0] + Q_j[PI[0]])
C_max = C[0] + Q_j[PI[0]]

for i in range(1, n):
    S.append(max(R_j[PI[i]], C[i-1]))
    C.append(S[i] + P_j[PI[i]])
    Cq.append(C[i] + Q_j[PI[i]])
    C_max = max(C_max, Cq[i])


print('Po zastosowaniu algorytmu z kolejka:')
for i in range(n):
    PI[i] += 1

print(f'PI:{PI}')
print(f'S:{S}')
print(f'C:{C}')
print(f'Cq:{Cq}')
print(f'Cmax: {C_max}')
print()

for i in range(n):
    PI[i] -= 1

S.clear()
C.clear()
Cq.clear()
PI.clear()

# ____________________ Algorytm z przerwaniami _______________________

C_max = Schrage.schrage_pmtn(J, R_j.copy(), P_j.copy(), Q_j.copy(), PI)

print('Po zastosowaniu algorytmu z przerwaniami:')
for i in range(len(PI)):
    PI[i] += 1

print(f'PI: {PI}')
print(f'Cmax: {C_max}')
print()

for i in range(len(PI)):
    PI[i] -= 1

C_max = 0
S.clear()
C.clear()
Cq.clear()
PI.clear()


# ____________________ Carlier _______________________

UB = 999999999999
print(R_j)
print(P_j)
print()
Carlier.carlier(UB, J, R_j, P_j, Q_j, PI, S, C, Cq, n)

print(f'p: {P_j}')
print(f'r: {R_j}')
print(f'q: {Q_j}')

C_max = 0
S.clear()
C.clear()
Cq.clear()

S.append(R_j[PI[0]])
C.append(S[0] + P_j[PI[0]])
Cq.append(C[0] + Q_j[PI[0]])
C_max = C[0] + Q_j[PI[0]]

for i in range(1, len(PI)):
    S.append(max(R_j[PI[i]], C[i-1]))
    C.append(S[i] + P_j[PI[i]])
    Cq.append(C[i] + Q_j[PI[i]])
    C_max = max(C_max, Cq[i])


print('Algorytm Carliera: ')
for i in range(len(PI)):
    PI[i] += 1

print(f'PI:{PI}')
print(f'S:{S}')
print(f'C:{C}')
print(f'Cq:{Cq}')
print(f'Cmax: {C_max}')
print()

for i in range(len(PI)):
    PI[i] -= 1
