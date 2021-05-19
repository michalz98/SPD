from RandomNumberGenerator import RandomNumberGenerator

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

    # generowanie tabeli zadań
    def task_gen(self, t, m):
        tasks_arr = []

        for i in range(t):
            tasks_arr.append([0] * rng.nextInt(1, m * 2))

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
        m_op_tab = []   # pomocnicza tabela przechowująca ilość zadań dla danej maszyny
        q_tab = []      # tabela kolejki
        for i in range(m):
            m_op_tab.append(0)

        for i in self.operations:
            m_op_tab[i[0]-1] += 1

        for i in range(m):
            q_tab.append([-1] * m_op_tab[i])

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
        if len(task) > 1:
            for op in range(len(task) - 1):
                dane.t_succesors[t][op] = dane.tasks[t][op + 1]
        t += 1


def addToTopQueue(Dane):
    x = dane.prec_num.count(1)
    flag = 0
    while flag < x:
        cnt = 0
        for t in range(1, len(dane.prec_num)):
            if dane.prec_num[t - 1] == -1 and dane.prec_num[t] == 1:
                dane.prec_num[t] = 0

        for task in dane.prec_num:
            if task == 0:
                dane.topologic_queue.append(cnt)
                dane.prec_num[cnt] = -1
            cnt += 1
        flag += 1


#testowane nie dziala xd
def R(dane):
    for topnum in dane.topologic_queue:
        if dane.t_precursors[topnum][0] == 0 :
            dane.r_tab[topnum] = dane.operations[topnum]
        else :
            dane.r_tab[topnum] = dane.operations[topnum] + dane.r_tab[topnum - 1]

dane = Data(tasks_num, machines_num)

checkPrecAnces(dane)
addToTopQueue(dane)
#R(dane)

print(f'tasks: {dane.tasks}')
print(f'operations: {dane.operations}')
print(f'queue:  {dane.queue_tab}')
print(f't_precursors: {dane.t_precursors}')
print(f't_succesor: {dane.t_succesors}')
print(f'liczba poprzednikow: {dane.prec_num}')
print(f'topologic: {dane.topologic_queue}')
print(f'R: {dane.r_tab}')
# print(dane.cnt)
