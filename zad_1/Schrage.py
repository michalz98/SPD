import SearchFunctions as Sf


# Standardowy algorytm Schrage
def schrage(j, r_j, p_j, q_j, pi):
    g = []
    n = j.copy()
    t = Sf.min_arg(n, r_j)
    while len(g) != 0 or len(n) != 0:
        while len(n) != 0 and Sf.min_arg(n, r_j) <= t:
            e = Sf.min_ind(n, r_j)
            g.append(e)
            n.remove(e)

        if len(g):
            e = Sf.max_ind(g, q_j)
            pi.append(e)
            g.remove(e)
            t += p_j[e]
        else:
            t = Sf.min_arg(n, r_j)


# Algorytm Schrage z "kolejka"
def schrage_k(j, r_j, p_j, q_j, pi):
    g = []
    n = []
    tmp = j.copy()
    done = 0
    while len(tmp) != 0:
        m = Sf.min_ind(tmp, r_j)
        n.append(m)
        tmp.remove(m)

    t = Sf.min_arg(n, r_j)

    while len(g) != 0 or len(n) != 0:
        while len(n) != 0 and Sf.min_arg(n, r_j) <= t:
            e = n[0]
            g.append(e)
            n.pop(0)

        tmp = g.copy()
        g.clear()
        while len(tmp) != 0 and done == 0:
            m = Sf.max_ind(tmp, q_j)
            g.append(m)
            tmp.remove(m)

        done = 1
        if len(g):
            e = g[0]
            pi.append(e)
            g.pop(0)
            t += p_j[e]
        else:
            t = Sf.min_arg(n, r_j)
        done = 0


def schrage_pmtn(j, r_j, p_j, q_j, pi):
    pi.clear()
    c_max = 0
    g = []
    n = j.copy()
    t = 0
    l = 0
    while len(g) != 0 or len(n) != 0:
        while len(n) != 0 and Sf.min_arg(n, r_j) <= t:
            e = Sf.min_ind(n, r_j)
            g.append(e)
            n.remove(e)
            if q_j[e] > q_j[l]:
                p_j[l] = t - r_j[e]
                t = r_j[e]
                if p_j[l] > 0:
                    g.append(l)
        if len(g):
            e = Sf.max_ind(g, q_j)
            g.remove(e)
            pi.append(e)
            t += p_j[e]
            c_max = max(c_max, t + q_j[e])
            l = e
        else:
            t = Sf.min_arg(n, r_j)
    return c_max
