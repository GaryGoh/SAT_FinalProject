__author__ = 'GaryGoh'
import outputCNF
from numpy import *


def ALO(n):
    outputCNF.write_header(268618, 268618, "out.cnf")
    f = open("out.cnf", "a")

    X = range(1, n, 1)
    Y = range(1, n, 1)
    T = range(1, n * n, 1)

    for x in X:
        for y in Y:
            for t in T:
                print >> f, "%d%d%d" % (x, y, t),
            print >> f, 0
    return


def AMO(n):
    f = open("out.cnf", "a")

    X = range(1, n, 1)
    Y = range(1, n, 1)
    T = range(1, n * n, 1)

    for x in X:
        for y in Y:
            for t in T:
                for t1 in T:
                    print >> f, "-%d%d%d" % (x, y, t),
                    print >> f, "-%d%d%d 0" % (x, y, t1)

    return


def CON(n):
    f = open("out.cnf", "a")

    X = range(1, n, 1)
    Y = range(1, n, 1)
    T = range(1, n * n, 1)

    for x in X:
        for y in Y:
            for x1 in X:
                for y1 in Y:
                    if ((x < x1) or (x == x1 and y < y1)):
                        for t in T:
                            print >> f, "%d%d%d" % (x, y, t),
                            print >> f, "%d%d%d 0" % (x1, y1, t)

    return




def AMO_2(n):
    X = range(1, n, 1)
    Y = range(1, n, 1)
    I = range(1, n + 1, 1)

    f = open(cnfFlieName, "a")

    for x in X:
        for y in Y:
            for x1 in range(x + 1, n + 1, 1):
                for y1 in range(y + 1, n + 1, 1):
                    for i in I:
                        # print >> f, "-%d%d%d -%d%d%d 0" % (x, y, i, x, y, j)
                        print >> f, "-%d -%d 0" % (n * n * (x - 1) + n * (y - 1) + i, n * n * (x - 1) + n * (y - 1) + j)

    return

ALO(8)
AMO(8)
CON(8)


