def dP(j_set, p_set, d_set, w_set):
    n = len(j_set)
    memory = []
    ind_table = []
    for i in range(pow(2, n)+1):
        memory.append(0)
        if i > 0:
            ind_table.append(0)

    D = []
    for i in range(1, pow(2, len(j_set))):
        D.append(i)

    C = []
    Tt = []
    wT = []
    T = []
    pi_p = []
    memory[0] = 0
    correct = 0
    ind_p = []
    for i in D:
        
        if bin(i)[2:].zfill(n).count("1") == 1:
            if p_set[i-1-correct] - d_set[i-1-correct] < 0:
                maxp = 0
            else:
                maxp = p_set[i-1-correct] - d_set[i-1-correct]

            memory[i] = maxp * w_set[i - 1 - correct]
            T.append(maxp)
            ind_table[i] = i - correct
        else:
            correct += 1
            tm = i
            ind_p.clear()
            num_ones = bin(i)[2:].zfill(n).count("1")
            max_ones = bin(pow(2, n)-1)[2:].zfill(n).count("1")
            for j in range(num_ones):
                b = pow(2, n-1)
                b = b >> bin(tm)[2:].zfill(n).find("1")
                tm = tm ^ b
                ind_p.append(n-1-bin(b)[2:].zfill(n).find("1"))

            b = 1
            Fmin = []
            fi = []
            for j in range(max_ones):
                if bin(i ^ b)[2:].zfill(n).count("1") == (num_ones - 1):
                    num = i ^ b
                    indp = n-1-bin(b)[2:].zfill(n).find("1")

                    sump = 0
                    for cnt in range(num_ones):
                        sump += p_set[ind_p[cnt]]

                    if sump - d_set[indp] < 0:
                        maxp = 0
                    else:
                        maxp = sump - d_set[indp]

                    Fmin.append(maxp*w_set[indp] + memory[num])
                    fi.append(indp + 1)
                b = b*pow(2, 1)

            memory[i] = min(Fmin)
            index = Fmin.index(min(Fmin))
            ind_table[i] = fi[index]
            Fmin.clear()

    ite = pow(2, n) - 1
    for i in range(n):
        b = pow(2, n-1)
        b = b >> n - ind_table[ite]
        pi_p.append(ind_table[ite])
        ite = ite ^ b

    pi_p.reverse()
    pi = pi_p.copy()

    sump = 0
    wiTi = 0
    for i in range(len(pi)):
        sump += p_set[pi[i]-1]
        C.append(sump)
        dif = sump - d_set[pi[i]-1]
        if dif < 0:
            Tt.append(0)
        else:
            Tt.append(dif)

        wT.append(Tt[i] * w_set[pi[i]-1])
        wiTi += wT[i]

    print(f'pi:{pi}')
    print(f'C: {C}')
    print(f'T: {Tt}')
    print(f'wT: {wT}')
    print(f'wiTi:{wiTi}')
