import Schrage
import SearchFunctions as SF


def carlier(UB, J, R_j, P_j, Q_j, PI, S, C, Cq, n):

    S.clear()
    C.clear()
    Cq.clear()
    PI.clear()

    Schrage.schrage(J, R_j, P_j, Q_j, PI)

    S.append(R_j[PI[0]])
    C.append(S[0] + P_j[PI[0]])
    Cq.append(C[0] + Q_j[PI[0]])
    C_max = C[0] + Q_j[PI[0]]

    for i in range(1, n):
        S.append(max(R_j[PI[i]], C[i - 1]))
        C.append(S[i] + P_j[PI[i]])
        Cq.append(C[i] + Q_j[PI[i]])
        C_max = max(C_max, Cq[i])

    U = C_max
    if U < UB:
        UB = U
        PI_p = PI.copy()

    a = -1
    b = -1
    c = -1
    for j in J:
        if C_max == (C[j] + Q_j[PI[j]]):
            b = j

    p_sum = 0
    a_min = []
    for j in J:
        for k in range(j, b+1):
            p_sum += P_j[PI[k]]

        if C_max == (R_j[PI[j]] + p_sum + Q_j[PI[b]]):
            a_min.append(j)

        if len(a_min):
            a = min(a_min)
        p_sum = 0
    a_min.clear()

    j_max = 0
    for j in range(a, b):
        if j_max < j and Q_j[PI[j]] < Q_j[PI[b]]:
            c = j
            j_max = j

    if c == -1:
        return PI_p

    K = []
    for i in range(c+1, b+1):
        K.append(i)

    r_p = SF.min_arg_special(PI, K, R_j)
    q_p = SF.min_arg_special(PI, K, Q_j)

    p_sum = 0
    for j in K:
        p_sum += P_j[PI[j]]

    p_p = p_sum
    r = R_j[PI[c]]
    zad = PI[c]
    R_j[PI[c]] = max(R_j[PI[c]], r_p + p_p)
    LB = Schrage.schrage_pmtn(J, R_j.copy(), P_j.copy(), Q_j.copy(), PI.copy())
    if LB < UB:
        carlier(UB, J, R_j, P_j, Q_j, PI, S, C, Cq, n)

    for j in PI:
        if j == zad:
            R_j[j] = r

    for j in PI:
        if j == zad:
            q = Q_j[j]
            Q_j[j] = max(Q_j[j], q_p + p_p)

    LB = Schrage.schrage_pmtn(J, R_j.copy(), P_j.copy(), Q_j.copy(), PI.copy())

    if LB < UB:
        carlier(UB, J, R_j, P_j, Q_j, PI, S, C, Cq, n)

    for j in PI:
        if j == zad:
            Q_j[j] = q
