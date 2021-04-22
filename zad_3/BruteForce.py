

def cset_calc(j, c_set, p_set, machines_num, depth):

    if c_set[0][0] == 0:
        c_set[0][0] = p_set[j][0]

        for i in range(1, machines_num):
            c_set[0][i] = p_set[j][i] + c_set[0][i - 1]

    else:

        c_set[depth][0] = c_set[depth - 1][0] + p_set[j][0]

        for k in range(1, machines_num):
            c_set[depth][k] = max(c_set[depth][k - 1], c_set[depth - 1][k]) + p_set[j][k]




def brute(j_val, n_set, p_set, c_set, tasks_num, machines_num, pi, data):

    pi.append(j_val)
    depth = tasks_num - len(n_set)
    cset_calc(j_val, c_set, p_set, machines_num, depth)
    n_set.remove(j_val)

    #print(pi)

    if n_set:
        for i in n_set:
            brute(i, n_set.copy(), p_set, c_set.copy(), tasks_num, machines_num, pi, data)
    else:
        c_max = max(max(c_set))    
        if c_max < data.UB:
            #print(f'Cmax{c_max}')
            data.UB = c_max
            data.PI = pi.copy()

    pi.remove(j_val)
    for i in range(machines_num):
        c_set[depth][i] = 0
