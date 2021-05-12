# Algorytm zachłanny
#def Greedy(tasks)

def sortFunc(d):
    return d

    
def Greedy(j_copy, d):
    d_copy = d.copy()
    d_copy.sort(key = sortFunc)
    pi = []
    for i in d_copy:
        cnt = 0
        for j in d:
            if i == j:
                pi.append(cnt+1)
            cnt += 1

    return pi

