#!/opt/local/bin/python2

import sys
import itertools
import random

n = int(sys.argv[1])
d = int(sys.argv[2])

print n, (n * d) / 2

for i in xrange(d):
    mate = list(itertools.repeat(-1, n))
    for j in xrange(n):
        if mate[j] != -1:
            continue
        while True:
            k = random.randint(0, n - 1)
            if (k != j) and (mate[k] == -1):
                break
        mate[j] = k
        mate[k] = j
    for j in xrange(n):
        if (j < mate[j]):
            print j + 1, mate[j] + 1
