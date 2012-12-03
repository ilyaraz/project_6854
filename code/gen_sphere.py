#!/opt/local/bin/python2

import sys

def gen(n, k):
    if k == 0:
        return [[]]
    if n == 0:
        return []
    a = gen(n - 1, k)
    b = gen(n - 1, k - 1)
    for l in b:
        l.reverse()
        l.append(n)
        l.reverse()
        a.append(l)
    return a

def get_index(c, b):
    return c.index(b) + 1

n = int(sys.argv[1])
k = int(sys.argv[2])

c = sorted([sorted(x) for x in gen(n, k)])

print len(c), k * (n - k + 1)

for b in c:
    s = set(b)
    for i in xrange(1, n + 1):
        if not (i in s):
            continue
        for j in xrange(1, n + 1):
            if (i == j) or not (j in s):
                s1 = set(s)
                s1.remove(i)
                s1.add(j)
                print get_index(c, sorted(list(s1))),
    print
