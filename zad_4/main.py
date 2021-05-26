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
        self.p_order = self.p_order_gen()

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
        for i in self.operations:
            tp_tab.append(0)

        return tp_tab

    def t_succesors_gen(self):
        ts_tab = []
        for i in self.operations:
            ts_tab.append(0)

        return ts_tab

    def o_succesors_gen(self):
        os_tab = []
        for i in self.operations:
            os_tab.append(0)

        return os_tab

    def o_precursors_gen(self):
        op_tab = []
        for i in self.operations:
            op_tab.append(0)

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

    def p_order_gen(self):
        p_tab = []
        for i in range(len(self.operations)):
            p_tab.append(i)

        return p_tab



def checkPrecAnces(dane):
    t = 0
    for task in dane.tasks:
        if len(task) > 1:
            for op in range(1, len(task)):
                dane.t_precursors[dane.tasks[t][op] - 1] = dane.tasks[t][op - 1]
                dane.prec_num[dane.tasks[t][op - 1]] += 1
                if dane.o_precursors[dane.tasks[t][op] - 1] != 0:
                    dane.prec_num[dane.tasks[t][op - 1]] += 1

            for op in range(len(task) - 1):
                dane.t_succesors[dane.tasks[t][op] - 1] = dane.tasks[t][op + 1]

        t += 1


def addToTopQueue(dane):
    dane.topologic_queue.clear()
    x = dane.prec_num.count(1)
    while x != 0:
        x = dane.prec_num.count(1)
        cnt = 0

        for task in dane.prec_num:
            if task == 0:
                dane.topologic_queue.append(cnt)
                # print(dane.topologic_queue)
                dane.prec_num[cnt] = -1
            cnt += 1

        for t in range(1, len(dane.prec_num)):
            if dane.prec_num[t - 1] == -1 and dane.prec_num[t] >= 1:
                dane.prec_num[t] -= 1


def addQTabel(dane):
    tmp_top = dane.topologic_queue.copy()
    tmp_top.reverse()

    for i in range(len(tmp_top)):
        sum_p = 0

        if dane.t_succesors[tmp_top[i]] != 0:
            sum_p = dane.operations[dane.t_succesors[tmp_top[i]] - 1][1]

        dane.q_tab[tmp_top[i]] = dane.operations[tmp_top[i]][1] + sum_p


def addRTabel(dane):
    tmp_top = dane.topologic_queue.copy()

    for i in range(len(tmp_top)):
        sum_p = 0

        if dane.t_precursors[tmp_top[i]] != 0:
            sum_p = dane.operations[dane.t_precursors[tmp_top[i]] - 1][1]

        dane.r_tab[tmp_top[i]] = dane.operations[tmp_top[i]][1] + sum_p


def sortByP(data):
    tmp_tab = data.p_order.copy()
    data.p_order.clear()
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


def Insa(data):
    while data.p_order:
        task = data.p_order[0]
        m_num = data.operations[task][0] - 1
        data.queue_tab[m_num].append(task)
        t_p_tmp = dane.t_precursors.copy()
        o_p_tmp = dane.o_precursors.copy()
        t_s_tmp = dane.t_succesors.copy()
        o_s_tmp = dane.o_succesors.copy()

        if len(data.queue_tab[m_num]) > 1:
            sum_min = 999999
            for permutation in itertools.permutations(data.queue_tab[m_num]):
                for j in range(len(permutation)):
                    suma = 0
                    max_tmp = []
                    if task == permutation[0]:
                        max_tmp.append(data.r_tab[t_p_tmp[task]-1])

                    else:
                        max_tmp.append(data.r_tab[t_p_tmp[task]-1])
                        max_tmp.append(data.r_tab[o_p_tmp[task]-1])

                    suma += max(max_tmp)

                    max_tmp.clear()

                    suma += data.operations[task][1]

                    if task == permutation[len(permutation) - 1]:
                        # print(f'i: {task},j: {j}, {t_p_tmp[task]-1}')
                        max_tmp.append(data.r_tab[t_s_tmp[task]-1])
                    else:
                        # print(f'i: {task},j: {j}, {t_p_tmp[task]-1}')
                        max_tmp.append(data.r_tab[t_s_tmp[task]-1])
                        max_tmp.append(data.r_tab[o_s_tmp[task]-1])

                    suma += max(max_tmp)

                    if suma < sum_min:
                        sum_min = suma
                        for i in range(len(permutation)):
                            data.q_tab[i] = permutation[i]
                            if i - 1 > -1:
                                data.o_precursors[permutation[i]] = permutation[i - 1]

                            if i + 1 < len(permutation):
                                data.o_succesors[permutation[i]] = permutation[i + 1]

        data.p_order.remove(task)

        checkPrecAnces(data)
        addToTopQueue(data)
        addQTabel(data)
        addRTabel(data)
        sortByP(dane)


dane = Data(tasks_num, machines_num)

print(f'queue: {dane.queue_tab}')
print(f'tasks: {dane.tasks}')
print(f'precursors: {dane.o_precursors}')

checkPrecAnces(dane)
addToTopQueue(dane)
addQTabel(dane)
addRTabel(dane)
sortByP(dane)
Insa(dane)

print()
print(f'tasks: {dane.tasks}')
print(f'operations: {dane.operations}')
print(f'queue:  {dane.queue_tab}')
# print(f't_precursors: {dane.t_precursors}')
# print(f't_succesor: {dane.t_succesors}')
# print(f'o_precursors: {dane.o_precursors}')
# print(f'o_succesor: {dane.o_succesors}')
# print(f'liczba poprzednikow: {dane.prec_num}')
# print(f'topologic: {dane.topologic_queue}')
# print(f'R: {dane.r_tab}')
# print(f'Q: {dane.q_tab}')
# print(f'p_order: {dane.p_order}')
# print(dane.cnt)
print()

