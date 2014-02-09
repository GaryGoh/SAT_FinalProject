####
#
#   ALO_ALL(int)
#   AMO_ALL(int)
#   CON_COLUMN(int)
#   CON_ROW(int)
#   CON_SUBGRIDS(int)
#   SUP_ROW(int)
#   SUP_COLUMN(int)
#   SUP_SUBGRIDS(int)
#   SUP(int)
#   MAX(int)
#
####

__author__ = 'GaryGoh'
import outputCNF
from math import *

cnfFlieName = "sudoku.cnf"
num = 9


def ALO_ALL(n):
    X = range(1, n + 1, 1)
    Y = X
    I = X
    outputCNF.write_header(999, 11745, cnfFlieName)
    f = open(cnfFlieName, "a")

    for x in X:
        for y in Y:
            for i in I:
                # print >> f, "%d%d%d" % (x, y, i),
                print >> f, "%d" % (n * n * (x - 1) + n * (y - 1) + i),
            print >> f, 0
    return


def AMO_ALL(n):
    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n, 1)

    f = open(cnfFlieName, "a")

    for x in X:
        for y in Y:
            for i in I:
                for j in range(i + 1, n + 1, 1):
                    # print >> f, "-%d%d%d -%d%d%d 0" % (x, y, i, x, y, j)
                    print >> f, "-%d -%d 0" % (n * n * (x - 1) + n * (y - 1) + i, n * n * (x - 1) + n * (y - 1) + j)

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
                        print >> f, "-%d -%d 0" % (n * n * (x - 1) + n * (y - 1) + i, n * n * (x1) + n * (y1) + i)

    return


def CON_COLUMN(n):
    X = range(1, n, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n + 1, 1)
    f = open(cnfFlieName, "a")

    for y in Y:
        for i in I:
            for x in X:
                for m in range(x + 1, n + 1, 1):
                    # print >> f, "-%d%d%d -%d%d%d 0" % (x, y, i, m, y, i)
                    print >> f, "-%d -%d 0" % (n * n * (x - 1) + n * (y - 1) + i, n * n * (m - 1) + n * (y - 1) + i)

    return


def CON_ROW(n):
    X = range(1, n + 1, 1)
    Y = range(1, n, 1)
    # N = range(y + 1, 9, 1)
    I = range(1, n + 1, 1)
    f = open(cnfFlieName, "a")

    for x in X:
        for i in I:
            for y in Y:
                for n in range(y + 1, n + 1, 1):
                    # print >> f, "-%d%d%d -%d%d%d 0" % (x, y, i, x, n, i)
                    print >> f, "-%d -%d 0" % (n * n * (x - 1) + n * (y - 1) + i, n * n * (x - 1) + n * (n - 1) + i)

    return


def CON_SUBGRIDS(n):
    I = range(1, n + 1, 1)
    Z = range(int(sqrt(n)))
    J = range(int(sqrt(n)))
    X = range(1, int(sqrt(n)) + 1, 1)
    Y = range(1, int(sqrt(n)) + 1, 1)
    L = range(1, int(sqrt(n)) + 1, 1)

    f = open(cnfFlieName, "a")

    for i in I:
        for z in Z:
            for j in J:
                for x in X:
                    for y in Y:
                        for k in range(y + 1, int(sqrt(n)) + 1, 1):
                            # print >> f, "(%d,%d)-%d (%d,%d)-%d 0" % (
                            #     int(sqrt(n)) * z + x, int(sqrt(n)) * j + y, i, int(sqrt(n)) * z + x,
                            #     int(sqrt(n)) * j + k,
                            #     i)
                            print >> f, "-%d -%d 0" % (
                                n * n * ((int(sqrt(n)) * z + x) - 1) + n * ((int(sqrt(n)) * j + y) - 1) + i,
                                n * n * ((int(sqrt(n)) * z + x) - 1) + n * ((int(sqrt(n)) * j + k) - 1) + i)

                        for m in range(x + 1, int(sqrt(n)) + 1, 1):
                            for l in L:
                                # print >> f, "(%d,%d)-%d (%d,%d)-%d 0" % (
                                #     int(sqrt(n)) * z + x, int(sqrt(n)) * j + y, i, int(sqrt(n)) * z + k,
                                #     int(sqrt(n)) * j + l, i)
                                print >> f, "-%d -%d 0" % (
                                    n * n * ((int(sqrt(n)) * z + x) - 1) + n * ((int(sqrt(n)) * j + y) - 1) + i,
                                    n * n * ((int(sqrt(n)) * z + k) - 1) + n * ((int(sqrt(n)) * j + l) - 1) + i)

    return


def SUP_ROW(n):
    X = range(1, n, 1)
    I = range(1, n + 1, 1)

    f = open(cnfFlieName, "a")

    for x in I:
        for y in X:
            for z in range(y + 1, n + 1, 1):
                for i in I:
                    for j in I:
                        if (i != j):
                            # print >> f, "(%d,%d)%d" % (x, y, j),
                            print >> f, "%d" % (n * n * (x - 1) + n * (y - 1) + j),
                    # print >> f, "(%d,%d)-%d 0" % (x, z, i)
                    print >> f, "-%d 0" % (n * n * (x - 1) + n * (z - 1) + i)

    return


def SUP_COLUMN(n):
    X = range(1, n, 1)
    I = range(1, n + 1, 1)

    f = open(cnfFlieName, "a")

    for x in I:
        for y in X:
            for z in range(y + 1, n + 1, 1):
                for i in I:
                    for j in I:
                        if (i != j):
                            # print >> f, "(%d,%d)%d" % (y, x, j),
                            print >> f, "%d" % (n * n * (y - 1) + n * (x - 1) + j),
                    # print >> f, "(%d,%d)-%d 0" % (z, x, i)
                    print >> f, "-%d 0" % (n * n * (z - 1) + n * (x - 1) + i)

    return


def SUP_SUBGRIDS(n):
    X = range(1, n + 1, int(sqrt(n)))
    Y = range(1, n + 1, int(sqrt(n)))
    K = range(int(sqrt(n)))
    L = range(int(sqrt(n)))
    I = range(1, n + 1, 1)
    I1 = range(1, n + 1, 1)

    f = open(cnfFlieName, "a")

    for x in X:
        for y in Y:
            for k in K:
                for l in L:
                    for i in I:
                        for k1 in K:
                            for l1 in L:
                                if (k != k1 or l != l1):
                                    for i1 in I:
                                        if (i != i1):
                                            # print >> f, "(%d,%d)%d" % (x + k1, y + l1, i1),
                                            print >> f, "%d" % (n * n * ((x + k1) - 1) + n * ((y + l1) - 1) + i1),
                        # print >> f, "(%d,%d)-%d 0" % (x + k, y + l, i)
                        print >> f, "-%d 0" % (n * n * ((x + k) - 1) + n * ((y + l) - 1) + i)
    return


# For all squares
def SUP(n):
    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n + 1, 1)

    f = open(cnfFlieName, "a")

    for x in X:
        for y in Y:
            for i in I:
                for x1 in X:
                    for y1 in X:
                        if (x1 != x or y1 != y):
                            for j in I:
                                if (i != j):
                                    # print >> f, "(%d,%d)%d" % (x1, y1, j),
                                    print >> f, "%d" % (n * n * (x - 1) + n * (y - 1) + j),
                            # print >> f, "(%d,%d)-%d 0" % (x, y, i)
                            print >> f, "-%d 0" % (n * n * (x1 - 1) + n * (y1 - 1) + i)

    return


def Arithmetic_formula(upper, n, d):
    x = range(1, upper + 1, d)
    return x[n - 1]


def MAX(n):
    # rows and columns
    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n + 1, 1)

    # sub-grids
    K = range(int(sqrt(n)))
    L = range(int(sqrt(n)))

    f = open(cnfFlieName, "a")

    for x in X:
        for y in Y:
            for i in I:
                # To print out row-relevant maximal value
                for y1 in Y:
                    if (y1 != y):
                        # print >> f, "(%d,%d)%d" % (x, y1, i),
                        print >> f, "%d" % (n * n * (x - 1) + n * (y1 - 1) + i),

                # To print out column-relevant maximal value
                for x1 in X:
                    if (x1 != x):
                        # print >> f, "(%d,%d)%d" % (x1, y, i),
                        print >> f, "%d" % (n * n * (x1 - 1) + n * (y - 1) + i),

                # To print out sub-grids-relevant maximal value
                n2 = int((x + sqrt(n) - 1) / sqrt(n))
                m2 = int((y + sqrt(n) - 1) / sqrt(n))
                x2 = Arithmetic_formula(n, n2, int(sqrt(n)))
                y2 = Arithmetic_formula(n, m2, int(sqrt(n)))
                for k in K:
                    if (x2 + k != x):
                        for l in L:
                            if (y2 + l != y):
                                # print >> f, "(%d,%d)%d" % (x2 + k, y2 + l, i),
                                print >> f, "%d" % (n * n * ((x2 + k) - 1) + n * ((y2 + l) - 1) + i),

                # To print out the end of each clause and the corresponding CSP variable
                # print >> f, "(%d,%d)%d 0" % (x, y, i)
                print >> f, "-%d 0" % (n * n * (x1 - 1) + n * (y1 - 1) + i)

    return


ALO_ALL(num)
# AMO_ALL(num)
CON_COLUMN(num)
CON_ROW(num)
CON_SUBGRIDS(num)
# SUP_ROW(num)
# SUP_COLUMN(num)
# SUP_SUBGRIDS(num)
# SUP(num)
MAX(num)
