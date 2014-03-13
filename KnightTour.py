__author__ = 'GaryGoh'
import outputCNF
from math import *


cnfFlieName = "KnightTour.cnf"
n = 4


# Number of clauses
ALO_num = n ** 2
AMO_num = n ** 4 * (n ** 2 - 1) / 2
# CON_num = n ** 3 * (n - 1) + (n * (n - 1) / 2 - n * (int(sqrt(n)) - 1)) * n ** 2
# SUP_num = n ** 3 + (n ** 3 * (n - 1 )) / 2
# MAX_num = n ** 3


def ALO(n):
    # To ensure each square has at least one value.
    f = open(cnfFlieName, "a")

    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n * n + 1, 1)

    for x in X:
        for y in X:
            for i in I:
                print >> f, "%d" % ( (n * n * n ) * (x - 1) + (n * n) * (y - 1) + i),
            print >> f, 0
    return


def AMO(n):
    # To ensure each square has at most one value.

    f = open(cnfFlieName, "a")

    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n * n + 1, 1)

    for x in X:
        for y in Y:
            for i in I:
                for j in range(i + 1, n * n + 1, 1):
                    # print >> f, "-%d -%d 0" % (
                    #     (n * n * n ) * (x - 1) + (n * n) * (y - 1) + i, (n * n * n ) * (x - 1) + (n * n) * (y - 1) + j)
                    print >> f, "-(%d,%d)%d -(%d,%d)%d 0" % (x, y, i, x, y, j)
    return


# To constrain each square is different with each other
def CON_ALL(n):
    # To constrain each square is visited once.
    f = open(cnfFlieName, "a")

    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n * n + 1, 1)

    for i in I:
        for x in X:
            for y in Y:
                for x1 in X:
                    for y1 in Y:
                        if (x != x1 or y != y1):
                            print >> f, "-%d -%d 0" % ((n * n * n ) * (x - 1) + (n * n) * (y - 1) + i,
                                                       (n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + i)
                            # print >> f, "-(%d,%d)%d -(%d,%d)%d" % (x, y, i, x1, y1, i)
    return


# To judge current coordinate is in legal squares set or not.
def In_LegalSquare(legal_square, x_current, y_current):
    if ((x_current, y_current) in legal_square):
        return True
    return False


# To get the legal squares set.
def Legal_Squares(x_origin, y_origin):
    legal_move = [-2, -1, 1, 2]
    legal_square = []

    for a in legal_move:
        for b in legal_move:
            if ((fabs(a) != fabs(b))):
                # At most 16 squares to be searched
                legal_square.insert(len(legal_square), (x_origin + a, y_origin + b))
    # print legal_square
    return legal_square


# To constrain each move is legally.
def CON_IllegalMove(n):
    # Use 2 helper method
    # Legal_Squares()
    # In_LegalSquare

    f = open(cnfFlieName, "a")

    legal_move = [-2, -1, 1, 2]
    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n * n, 1)
    J = range(1, n * n + 1, 1)


    # legal_square = []
    k = 0

    for x in X:
        for y in Y:
            # reduce computing times.
            legal_square = Legal_Squares(x, y)
            for x1 in X:
                for y1 in Y:
                    if ( (x1 > 0) and (x1 <= n) and (y1 > 0) and (y1 <= n) and ((x != x1) or (y != y1))):
                        if not (In_LegalSquare(legal_square, x1, y1)):
                            for i in I:
                                k = k + 1
                                print >> f, "-%d -%d 0" % ((n * n * n ) * (x - 1) + (n * n) * (y - 1) + i,
                                                           (n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + i)
                                # print >> f, "-(%d,%d)%d -(%d,%d)%d" % (x, y, i, x1, y1, i)
                                #
                                k = k + 1
                                print >> f, "-%d -%d 0" % ((n * n * n ) * (x - 1) + (n * n) * (y - 1) + i,
                                                           (n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + i + 1)
                                # print >> f, "-(%d,%d)%d -(%d,%d)%d" % (x, y, i, x1, y1, i + 1)
                        else:
                            for i in I:
                                for j in J:
                                    if (j != i + 1):
                                        k = k + 1
                                        print >> f, "-%d -%d 0" % ((n * n * n ) * (x - 1) + (n * n) * (y - 1) + i,
                                                                   (n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + j)
                                        # print >> f, "-(%d,%d)%d -(%d,%d)%d" % (x, y, i, x1, y1, j)

    return k


def SUP(n):
    f = open(cnfFlieName, "a")

    legal_move = [-2, -1, 1, 2]
    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n * n, 1)

    k = 0

    for x in X:
        for y in Y:
            # reduce computing times.
            legal_square = Legal_Squares(x, y)
            for i in I:
                for x1 in range(x - 2, x + 3, 1):
                    for y1 in range(y - 2, y + 3, 1):
                        if ( (x1 > 0) and (x1 <= n) and (y1 > 0) and (y1 <= n) and ((x != x1) or (y != y1))):
                            if (In_LegalSquare(legal_square, x1, y1)):
                                print >> f, "%d" % ((n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + i + 1),
                                # print >> f, "(%d,%d)%d" % (x1, y1, i + 1),
                k = k + 1
                print >> f, "-%d 0" % ((n * n * n ) * (x - 1) + (n * n) * (y - 1) + i)
                # print >> f, "-(%d,%d)%d 0" % (x, y, i)

    return k


def MAX(n):
    f = open(cnfFlieName, "a")

    legal_move = [-2, -1, 1, 2]
    X = range(1, n, 1)
    Y = range(1, n, 1)
    I = range(1, n * n + 1, 1)
    J = range(1, n * n + 1, 1)

    for x in X:
        for y in Y:
            for j in J:
                for a in legal_move:
                    for b in legal_move:
                        for x1 in range(x - 2, x + 3, 1):
                            for y1 in range(y - 2, y + 3, 1):
                                if ( (x1 > 0) and (x1 <= n) and (y1 > 0) and (y1 <= n)):
                                    if (fabs(a) != fabs(b) and (x + a == x1) and (y + b == y1) and (
                                                x != x1) and (
                                                y != y1)):
                                        # print >> f, "%d" % (
                                        #     (n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + j),
                                        print >> f, "(%d,%d)%d" % (x1, y1, j),
                # print >> f, "%d 0" % ((n * n * n) * (x - 1) + (n * n) * (y - 1) + j)
                print >> f, "(%d,%d)%d" % (x, y, j)
    return


def MAX_new(n):
    f = open(cnfFlieName, "a")

    legal_move = [-2, -1, 1, 2]
    X = range(1, n + 1, 1)
    Y = range(1, n + 1, 1)
    I = range(1, n * n + 1, 1)

    k = 0

    for x in X:
        for y in Y:
            # reduce computing times.
            legal_square = Legal_Squares(x, y)
            for i in I:
                for x1 in X:
                    for y1 in Y:
                        if ( (x1 > 0) and (x1 <= n) and (y1 > 0) and (y1 <= n) and ((x != x1) or (y != y1))):
                            if not (In_LegalSquare(legal_square, x1, y1)):
                                for j in range(i, i + 2, 1):
                                    print >> f, "%d" % ((n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + j),
                                    # print >> f, "(%d,%d)%d" % (x1, y1, j),
                            else:
                                for j in I:
                                    if (j != i + 1):
                                        print >> f, "%d" % ((n * n * n ) * (x1 - 1) + (n * n) * (y1 - 1) + j),
                                        # print >> f, "(%d,%d)%d" % (x1, y1, j),
                print >> f, "%d 0" % ((n * n * n ) * (x - 1) + (n * n) * (y - 1) + i)
                # print >> f, "(%d,%d)%d 0" % (x, y, i)
                k = k + 1
    return k


def direct_encoding(n):
    outputCNF.write_header(n ** 4, ALO_num + AMO_num + CON_IllegalMove(n), cnfFlieName)

    ALO(n)
    AMO(n)
    CON_IllegalMove(n)


def support_encoding(n):
    outputCNF.write_header(n ** 4, ALO_num + AMO_num + SUP(n), cnfFlieName)

    ALO(n)
    AMO(n)
    SUP(n)


def maximal_encoding(n):
    outputCNF.write_header(n ** 4, ALO_num + CON_IllegalMove(n) + MAX_new(n), cnfFlieName)

    ALO(n)
    CON_IllegalMove(n)
    MAX_new(n)


# direct_encoding(n)
# support_encoding(n)
# maximal_encoding(n)
