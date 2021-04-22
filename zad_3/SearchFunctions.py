

# Zwraca indeks najmniejszego elementu w zbiorze data_set, szukając po indeksach ze zbioru index_set dla wielu maszyn
def min_ind(index_set, data_set, machine_num):
    if type(data_set) is list and type(machine_num) is int and type(index_set) is list:
        ind_min = [0, 0]
        v_min = 99999
        for j in range(machine_num):
            for i in index_set:
                if data_set[i][j] < v_min:
                    v_min = data_set[i][j]
                    ind_min[0] = i
                    ind_min[1] = j

    else:
        print('Invalid arguments')
    return ind_min


# ------------------------NIE UZYWANE-----------------------------

# Sprawdza czy lista lst zawiera dany element. Zwraca True lub False
def find(lst, element):
    ctr_val = 0
    for i in lst:
        if i == element:
            ctr_val = 1

    if ctr_val == 1:
        return True
    else:
        return False


# Zwraca argument z listy arg, sposrod indeksow z listy arr
def min_arg(ind, arg):
    if type(ind) is list and type(arg) is list:
        v_min = 99999
        for id in ind:
            if arg[id] < v_min:
                v_min = arg[id]
                i_val = id
    else:
        print('Invalid arguments')
    return v_min


# Zwraca indeks elementu listy arr, ktoremu odpowieada najwiekszy parametr z listy arg
def max_ind(ind, arg):
    if type(ind) is list and type(arg) is list:
        i_val = 0
        v_max = 0
        for id in ind:
            if arg[id] > v_max:
                v_max = arg[id]
                i_val = id
    else:
        print('Invalid arguments')
    return i_val


def min_arg_special(ind, indl, arg):
    if type(ind) is list and type(arg) is list and type(indl) is list:
        v_min = 99999
        for id in indl:
            if arg[ind[id]] < v_min:
                v_min = arg[ind[id]]
                i_val = id
    else:
        print('Invalid arguments')
    return v_min