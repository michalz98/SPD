import itertools


def brute(j_set, p_set, d_set, w_set):
    min = 99999
    per = list(itertools.permutations(j_set))
    Pi = []
    T = []
    Tc = []
    Tt = []
    C = []
    Cc = []
    for pi in per:
        sum = 0
        sum_p = 0
        T.clear()
        C.clear()
        sum_p = 0
        for j in pi: 
            sum_p += p_set[j]
            C.append(sum_p)

        cnt = 0
        for j in pi:

            t = C[cnt] - d_set[j]
            if t <= 0:
                T.append(0)
            else:
                T.append(t)
            cnt += 1

        for j in range(len(pi)):
            sum +=T[j] * w_set[pi[j]]
            

        if sum < min:
            Cc = C.copy()
            Tc = T.copy()
            Pi.clear()
            Tt.clear()
            for i in pi:
                Pi.append(i+1)
            min = sum
            Tt = T.copy()
    print(f'T: {Tc}')
    print(f'C: {Cc}')
    print(f'min: {min}')
    print(f'Tt: {Tt}')
    print(f'Pi: {Pi}')
