def dP(j_set, p_set, d_set, w_set):
    n = len(j_set)
    memory = []
    for i in range(pow(2, n)+1):
        memory.append(0)

    D = []
    for i in range(1, pow(2, len(j_set))):
        D.append(i)
    
    memory[0] = 0
    correct = 1
    ind_p = []
    ind_w = []
    ind_m = []
    for i in D:
        
        if bin(i)[2:].zfill(n).count("1") == 1:
            if p_set[i-correct] - d_set[i-correct] < 0:
                max = 0
            else:
                max = p_set[i-correct] - d_set[i-correct]
            memory[i] = max * w_set[i - correct]
        else:
            correct += 1
            b = 1

            num_ones = bin(i)[2:].zfill(n).count("1")

            for j in range(bin(pow(2,n)-1)[2:].zfill(n).count("1")):
                # print(f'war1: {bin(b)[2:].zfill(n)}')
                if bin(i^b)[2:].zfill(n).count("1") == (num_ones - 1):
                    num = i^b
                    # print(f'bin: {bin(i)[2:].zfill(n)}')
                    # print(f'bin op: {bin(num)[2:].zfill(n)}')
                    ind_m.append(bin(num)[2:].zfill(n).find("1")-1)
                    ind_p.append(bin(b)[2:].zfill(n).find("1")-1)
                    # print(f'ind_m: {n-1-bin(num)[2:].zfill(n).find("1")}, ind_p: {n-1-bin(b)[2:].zfill(n).find("1")}')
                    # print(bin(b)[2:].zfill(n))
                    # print(i^b)

                    for cnt in num_ones:
                        

                    # ind = bin(i^b)[2:].zfill(n).find("1")
                    # sum = 0
                    # bt = 1
                    # for x in range(bin(pow(2,n)-1)[2:].zfill(n).count("1")):
                    #     if bin(x^b)[2:].zfill(n).count("1") == (num_ones - 1):
                    #         if bin(x^b)[2:].zfill(n).count("1") == (num_ones - 1):
                    #             indt = bin(x^b)[2:].zfill(n).find("1")
                    #             # print(f'ind: {indt}')
                    #             sum += p_set[indt]
                    #             bt = bt*pow(2, 1)

                    # if sum - d_set[i] < 0:
                    #     max = 0
                    # else:
                    #     max = sum - d_set[i]

                    # print(f'max: {max}')
                b = b*pow(2, 1)

