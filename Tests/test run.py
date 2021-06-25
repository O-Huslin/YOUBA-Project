def front(q):
    return q[0]

def enqueue(q, lst):
    lst.append(q)

def dequeue(lst):
    lst.remove(front[lst])

def cycles(lst, c, t):
    c = int(c)
    t = int(t)
    for i in lst:
        while front(i) > c:
            if front(i) <= c:
                return front(i) + t
            else:
                i[0] -= c
                t += 10
    return t - front(min(lst))


def check(lst1, lst2):
    if lst1 == []:
        return []
    else:
        return [[lst1[0], lst2[0]]] + check(lst1[1:], lst2[1:])
