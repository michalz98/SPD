
def sortFunc(d):
    return d

    
def Greedy(p_set, w_set, d):
    d_copy = d.copy()
    d_copy.sort(key=sortFunc)
    pi = []
    C = []
    T = []
    wT = []
    for i in d_copy:
        cnt = 0
        for j in d:
            if i == j:
                pi.append(cnt+1)
            cnt += 1

    sum_p = 0
    for i in pi:
        sum_p += p_set[i-1]
        C.append(sum_p)

    for i in range(len(pi)):
        dif = C[i] - d_copy[i]
        if dif < 0:
            T.append(0)
        else:
            T.append(dif)

    sumT = 0
    for i in range(len(pi)):
        wT.append(T[i] * w_set[pi[i]-1])
        sumT += T[i] * w_set[pi[i]-1]

    print(f'Pi: {pi}')
    print(f'C: {C}')
    print(f'T: {T}')
    print(f'wT: {wT}')
    print(f'wiTi: {sumT}')

