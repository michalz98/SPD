from RandomNumberGenerator import RandomNumberGenerator
import itertools
import math

seed = int(input("Podaj seed: "))
tasks_num = int(input("Ilosc zadan: "))
machines_num = int(input("Ilosc maszyn: "))

rng = RandomNumberGenerator(seedValue=seed)


class Data:
    cnt = 1

    def __init__(self, t_num, m_num):
        self.tasks = self.task_gen(t_num, m_num)
        self.operations = self.op_gen(m_num)
        self.queue_tab = self.queue_tab_gen(m_num)
        self.t_precursors = self.t_precursors_gen()
        self.t_succesors = self.t_succesors_gen()
        self.o_precursors = self.o_precursors_gen()
        self.o_succesors = self.o_succesors_gen()
        self.prec_num = self.prec_num_gen()
        self.r_tab = self.r_tab_gen()
        self.q_tab = self.q_tab_gen()
        self.topologic_queue = []
        self.p_order = []

    # generowanie tabeli zadań
    def task_gen(self, t, m):
        tasks_arr = []

        for i in range(t):
            tasks_arr.append([0] * math.floor(rng.nextInt(1, m * 1.2) + 1))

        tasks_arr[0][0] = 1

        # numerowanie zadań
        for task in tasks_arr:
            for i in range(len(task)):
                task[i] = self.cnt
                self.cnt += 1

        return tasks_arr

    # generowanie operacji dla zadań
    def op_gen(self, m):
        op = []
        for i in range(self.cnt - 1):
            # 1. wartość - numer maszyny, 2. wartość - czas wykonywania
            op.append([rng.nextInt(1, m), rng.nextInt(1, 29)])
        return op

    # generowanie kolejki wykonywania zadań dla poszczególnych maszyn
    def queue_tab_gen(self, m):
        # m_op_tab = []   # pomocnicza tabela przechowująca ilość zadań dla danej maszyny
        q_tab = []  # tabela kolejki

        for i in range(m):
            q_tab.append([])

        return q_tab

    def t_precursors_gen(self):
        tp_tab = []
        for i in self.tasks:
            tp_tab.append([0] * len(i))

        return tp_tab

    def t_succesors_gen(self):
        ts_tab = []
        for i in self.tasks:
            ts_tab.append([0] * len(i))

        return ts_tab

    def o_succesors_gen(self):
        os_tab = []
        for i in self.tasks:
            os_tab.append([0] * len(i))

        return os_tab

    def o_precursors_gen(self):
        op_tab = []
        for i in self.tasks:
            op_tab.append([0] * len(i))

        return op_tab

    def prec_num_gen(self):
        prec_tab = []
        for i in self.operations:
            prec_tab.append(0)

        return prec_tab

    def r_tab_gen(self):
        r_tab = []
        for i in self.operations:
            r_tab.append(0)

        return r_tab

    def q_tab_gen(self):
        q_tab = []
        for i in self.operations:
            q_tab.append(0)

        return q_tab


def checkPrecAnces(dane):
    t = 0
    for task in dane.tasks:
        if len(task) > 1:
            for op in range(1, len(task)):
                dane.t_precursors[t][op] = dane.tasks[t][op - 1]
                dane.prec_num[dane.tasks[t][op - 1]] += 1
                if dane.o_precursors[t][op] != 0:
                    dane.prec_num[dane.tasks[t][op - 1]] += 1
        if len(task) > 1:
            for op in range(len(task) - 1):
                dane.t_succesors[t][op] = dane.tasks[t][op + 1]

        t += 1


def addToTopQueue(dane):
    x = dane.prec_num.count(1)
    flag = 0
    while flag < x:
        cnt = 0
        for t in range(1, len(dane.prec_num)):
            if dane.prec_num[t - 1] == -1 and dane.prec_num[t] >= 1:
                dane.prec_num[t] -= 1

        for task in dane.prec_num:
            if task == 0:
                dane.topologic_queue.append(cnt)
                dane.prec_num[cnt] = -1
            cnt += 1
        flag += 1


def addQTabel(dane):
    tmp_succesor = []
    tmp_top = dane.topologic_queue.copy()
    tmp_top.reverse()
    for i in dane.t_succesors:
        for j in i:
            tmp_succesor.append(j)

    for i in range(len(tmp_top)):
        sum_p = 0

        if tmp_succesor[tmp_top[i]] != 0:
            sum_p = dane.operations[tmp_succesor[tmp_top[i]] - 1][1]
        dane.q_tab[tmp_top[i]] = dane.operations[tmp_top[i]][1] + sum_p


def addRTabel(dane):
    tmp_prec = []
    tmp_top = dane.topologic_queue.copy()
    for i in dane.t_precursors:
        for j in i:
            tmp_prec.append(j)

    for i in range(len(tmp_top)):
        sum_p = 0

        if tmp_prec[tmp_top[i]] != 0:
            sum_p = dane.operations[tmp_prec[tmp_top[i]] - 1][1]
        dane.r_tab[tmp_top[i]] = dane.operations[tmp_top[i]][1] + sum_p


def sortByP(data):
    tmp_tab = data.topologic_queue.copy()
    while tmp_tab:
        max_p = 0
        it = 0
        index = tmp_tab[0]
        for i in range(len(tmp_tab)):
            actual_p = data.operations[tmp_tab[i]][1]
            if max_p < actual_p:
                max_p = actual_p
                index = tmp_tab[i]
                it = i
        tmp_tab.pop(it)
        data.p_order.append(index)

# =============================================

def INSA(data):
    while data.p_order:
        checkPrecAnces(dane)
        addToTopQueue(dane)
        addQTabel(dane)
        addRTabel(dane)
        for i in data.p_order:
            m_num = data.operations[i][0] - 1
            data.queue_tab[m_num].append(i)
            t_p_tmp = []
            o_p_tmp = []
            t_s_tmp = []
            o_s_tmp = []

            for k in dane.t_precursors:
                for j in k:
                    t_p_tmp.append(j)

            for k in dane.o_precursors:
                for j in k:
                    o_p_tmp.append(j)

            for k in dane.t_succesors:
                for j in k:
                    t_s_tmp.append(j)

            for k in dane.o_succesors:
                for j in k:
                    o_s_tmp.append(j)

            if len(data.queue_tab[m_num]) > 1:
                sum_min = 999999
                pi_m = []
                for permutation in itertools.permutations(data.queue_tab[m_num]):
                    for j in range(len(permutation)):
                        suma = 0
                        max_tmp = []
                        if i == 0:
                            max_tmp.append(data.r_tab[t_p_tmp[i]-1])

                        else:
                            max_tmp.append(data.r_tab[t_p_tmp[i]-1])
                            max_tmp.append(data.r_tab[o_p_tmp[i]-1])

                        suma += max(max_tmp)

                        max_tmp.clear()

                        suma += data.operations[i][1]

                        if i == len(permutation) - 1:
                            max_tmp.append(data.r_tab[t_s_tmp[i]-1])
                        else:
                            max_tmp.append(data.r_tab[t_s_tmp[i]-1])
                            max_tmp.append(data.r_tab[o_s_tmp[i]-1])

                        suma += max(max_tmp)
                        if suma < sum_min: 
                            pi_m = permutation
                            sum_min = suma

                    for c in range(len(data.queue_tab[m_num])):
                        data.queue_tab[m_num][c] = pi_m[c]
                        # print(f'queue: {data.queue_tab}')

                    for c in range(len(data.tasks[m_num])):
                        if c >= 1:
                            # print(f'm: {m_num}, c:{c-1}, {data.o_precursors}')
                            # print(data.o_precursors[m_num][c-1])
                            print(pi_m)
                            data.o_precursors[m_num][c] = pi_m[c-1]
                        if c < len(data.queue_tab[m_num]) -1:
                            # print(f'm: {m_num} , c:{c-1}, {data.o_precursors}')
                            # print(data.o_precursors[m_num][c-1])
                            # print(pi_m[c])
                            data.o_succesors[m_num][c] = pi_m[c+1]


            data.p_order.remove(i)

dane = Data(tasks_num, machines_num)

print(f'queue: {dane.queue_tab}')
print(f'tasks: {dane.tasks}')
print(f'precursors: {dane.o_precursors}')

checkPrecAnces(dane)
addToTopQueue(dane)
addQTabel(dane)
addRTabel(dane)
sortByP(dane)
INSA(dane)

print(f'tasks: {dane.tasks}')
print(f'operations: {dane.operations}')
print(f'p_order: {dane.p_order}')


