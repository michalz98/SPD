import SearchFunctions as sf


def johnson(j_set, p_set, tasks_num, machines_num):
    pi = []
    l = 0
    k = tasks_num
    n = j_set.copy()
    for i in range(k):
        pi.append(0)
    while n:
        tmp = sf.min_ind(n, p_set, machines_num)
        i = tmp[0]
        j = tmp[1]

        if p_set[i][0] < p_set[i][machines_num-1]:
            pi[l] = i
            l += 1
        else:
            pi[k-1] = i
            k -= 1

        n.remove(i)
    return pi
