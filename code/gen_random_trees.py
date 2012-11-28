#!/opt/local/bin/python2

import sys
import random
import itertools

n = int(sys.argv[1])
k = int(sys.argv[2])

print n, (n - 1) * k

for i in xrange(k):
    j = 0
    was = list(itertools.repeat(0, n))
    was[0] = 1
    t = 1
    while t < n:
        u = random.randint(0, n - 1)
        if was[u] == 1:
            j = u
            continue
        print j + 1, u + 1
        t += 1
        j = u
        was[j] = 1
         
