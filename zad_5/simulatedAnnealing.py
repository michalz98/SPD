from RandomNumberGenerator import RandomNumberGenerator as RNG
import random
import math

seed = int(input("Podaj seed: "))
tasks_num = int(input("Ilosc zadan: "))
machines_num = int(input("Ilosc maszyn: "))

rng = RNG(seedValue=seed)
random.seed()


class Data:

    def __init__(self, tas_num, mach_num):
        self.m_num = mach_num
        self.t_num = tas_num
        self.j = self.gen_j()
        self.p = self.gen_p()
        self.s = self.gen_s()
        self.c = self.gen_c()

        self.cmax = 0
        self.cmax_current = 0
        self.cmax_best = 0
        self.cmax_new = 0

        self.pi = []
        self.pi_current = self.j
        self.pi_best = []

    def gen_j(self):
        j_tmp = []
        for i in range(self.t_num):
            j_tmp.append(i)
        return j_tmp

    def gen_p(self):
        p_tmp = []
        for i in range(self.t_num):
            p_tmp.append([0]*self.m_num)

        for c in p_tmp:
            for r in range(self.m_num):
                c[r] = rng.nextInt(1, 29)
        return p_tmp

    def gen_s(self):
        s_tmp = []
        for i in range(self.t_num):
            s_tmp.append([0]*self.m_num)
        return s_tmp

    def gen_c(self):
        c_tmp = []
        for i in range(self.t_num):
            c_tmp.append([0]*self.m_num)
        return c_tmp

    def calc_cmax(self, array):
        self.c[0][0] = self.p[array[0]][0]
        for i in range(1, self.m_num):
            self.c[0][i] = self.p[array[0]][i] + self.c[0][i - 1]

        for i in range(1, self.t_num):
            self.c[i][0] = self.c[i - 1][0] + self.p[array[i]][0]

        for k in range(1, self.m_num):
            for i in range(1, self.t_num):
                self.c[i][k] = max(self.c[i][k - 1], self.c[i - 1][k]) + self.p[array[i]][k]

        for k in range(self.m_num):
            for i in range(self.t_num):
                self.s[i][k] = self.c[i][k] - self.p[array[i]][k]

        return max(max(self.c))


def swap(arr, i_elem, j_elem):
    arr_tmp = arr.copy()
    i_tmp = arr_tmp[i_elem]
    arr_tmp[i_elem] = arr[j_elem]
    arr_tmp[j_elem] = i_tmp
    return arr_tmp


def symAnnealing(data, t0, tend, l):
    t = t0
    pi = data.j
    while t > tend:
        for k in range(1, l):
            i = random.randrange(data.t_num)
            j = random.randrange(data.t_num)
            pi_new = swap(pi, i, j)

        data.cmax_new = data.calc_cmax(pi_new)
        data.cmax_current = data.calc_cmax(pi)

        if data.cmax_new > data.cmax_current:
            r = random.randrange(0, 100)/100
            dif = data.cmax_current - data.cmax_new
            if r >= math.exp(dif/t):
                pi_new = pi
        pi = pi_new

        if data.calc_cmax(pi) < data.calc_cmax(data.pi_current):
            data.pi_current = pi
            data.cmax = data.calc_cmax(pi)

        t = t - 1


d = Data(tasks_num, machines_num)

l_num = int(math.sqrt(tasks_num * machines_num))
t_end = 0

symAnnealing(d, 50, t_end, l_num)


# print(f'J: {d.j}')
# print(f'P: {d.p}')
# print(f'S: {d.s}')
# print(f'C: {d.c}')
# print(f'C max: {d.cmax_current}')

print(f'PI: {d.pi_current}')
print(f'C: {d.cmax}')
print(f'C: {d.c}')
