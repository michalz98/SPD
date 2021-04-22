

def cset_calc(j, c_set, p_set, machines_num, depth):

    if c_set[0][0] == 0:
        c_set[0][0] = p_set[j][0]

        for i in range(1, machines_num):
            c_set[0][i] = p_set[j][i] + c_set[0][i - 1]

    else:

        c_set[depth][0] = c_set[depth - 1][0] + p_set[j][0]

        for k in range(1, machines_num):
            c_set[depth][k] = max(c_set[depth][k - 1], c_set[depth - 1][k]) + p_set[j][k]


def bound(n_set, p_set, c_set, machines_num, x):

    Pmin = []
    sum = []
    for i in range(machines_num):
        sum_pmin = 0
        sum_p = 0
        for j in n_set:
            sum_p += p_set[j][i]

        for k in range(i + 1, machines_num):
            Pmin.clear()
            for j in n_set:
                Pmin.append(p_set[j][k])

            sum_pmin += min(Pmin)

        sum.append(c_set[x][i] + sum_p + sum_pmin)

    lb = max(sum)
    return lb


def bnb(j_val, n_set, p_set, c_set, tasks_num, machines_num, pi, data):

    pi.append(j_val)
    depth = tasks_num - len(n_set)
    cset_calc(j_val, c_set, p_set, machines_num, depth)
    n_set.remove(j_val)

    if n_set:

        lb = bound(n_set.copy(), p_set, c_set.copy(), machines_num, j_val)

        if lb < data.UB:
            for j in n_set:

                bnb(j, n_set.copy(), p_set, c_set.copy(), tasks_num, machines_num, pi, data)

    else:
        c_max = max(max(c_set))
        if c_max < data.UB:
            data.UB = c_max
            data.PI = pi.copy()

    pi.remove(j_val)
    for i in range(machines_num):
        c_set[depth][i] = 0
