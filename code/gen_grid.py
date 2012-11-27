#!/opt/local/bin/python2

import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

print n * m, n * m * 2

for i in xrange(n):
    for j in xrange(m):
        print i * m + j + 1, ((i + 1) % n) * m + j + 1
        print i * m + j + 1, i * m + (j + 1) % m + 1
