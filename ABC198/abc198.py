# import re
# import sys
# import math
# import itertools
# import bisect
# import heapq#.heapify:Priority Queueに変換 
# #.heappop:最小値取得, .heappush:要素挿入
# from copy import copy,deepcopy
# from collections import deque,Counter,defaultdict
# from decimal import Decimal
# import functools
# from functools import reduce
# from operator import itemgetter
# def v(): return input()
# def k(): return int(input())
# def S(): return input().split()
# def I(): return map(int,input().split())
# def X(): return list(input())
# def L(): return list(input().split())
# def l(): return list(map(int,input().split()))
# def Z(): return tuple(map(int,input().split()))
# def lcm(a,b): return a*b//math.gcd(a,b)
# def gcd(*numbers):
#     return reduce(math.gcd, numbers)
# sys.setrecursionlimit(10 ** 6)
# mod = 10**9+7
# INF = float("inf")
# cnt = 0
# ans = 0
# move = [(-1,0),(1,0),(0,1),(0,-1)]

# s1 = v()
# s2 = v()
# s3 = v()
# l1, l2, l3 = len(s1), len(s2), len(s3)

# alpha = {}
# for i in s1:
#     alpha[i] = 0
# for i in s2:
#     alpha[i] = 0
# for i in s3:
#     alpha[i] = 0

# if len(alpha) >= 11 or (s1==s3) or (s2==s3) or (l1>l3) or (l2>l3):
#     print("UNSOLVABLE")
#     exit()

# number = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(alpha)))
# print(len(number))

# for i in range(len(number)):
#     for index, key in enumerate(alpha):
#         alpha[key] = number[i][index]
#     num1,num2,num3="","",""
#     for a in s1:
#         num1 += str(alpha[a])
#     for a in s2:
#         num2 += str(alpha[a])
#     for a in s3:
#         num3 += str(alpha[a])
#     if l1 != len(str(int(num1))) or l2 != len(str(int(num2))) or l3 != len(str(int(num3))):
#         continue
#     if int(num1)+int(num2)==int(num3):
#         print(num1)
#         print(num2)
#         print(num3)
#         exit()

# print("UNSOLVABLE")
import sys
N = 128
s = "0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ"
word = [['' for i in range(N)] for j in range(128)]
digit = [0 for i in range(len(s))]
l = [0 for i in range(len(s))]
ok = [False for i in range(10)]
ii = 0
jj = 0
carry = 0
solution = 0


def found():
    global solution
    solution += 1
    for i in range(imax):
        for j in range(jmax):
            k = jmax-1-j
            c = word[i][k]
            if (c == ''):
                print("", end="")
            else:
                print("%d" % digit[s.index(c)], end='')
        print("")
    exit()


def tr(sum):
    global ii, jj
    w = word[ii][jj]
    c = 0 if w == '' else s.index(w)
    if (ii < imax-1):
        ii += 1
        d = digit[c]
        if (d < 0):
            d = l[c]
            while(d <= 9):
                if (ok[d]):
                    digit[c] = d
                    ok[d] = False
                    tr(sum+d)
                    ok[d] = True
                d += 1
            digit[c] = -1
        else:
            tr(sum+d)
        ii -= 1
    else:
        jj += 1
        ii = 0
        carry, d = divmod(sum, 10)
        if (digit[c] == d):
            if (jj < jmax):
                tr(carry)
            elif (carry == 0):
                found()
        else:
            if (digit[c] < 0 and ok[d] and d >= l[c]):
                digit[c] = d
                ok[d] = False
                if (jj < jmax):
                    tr(carry)
                elif (carry == 0):
                    found()
                digit[c] = -1
                ok[d] = True
        jj -= 1
        ii = imax-1

s1 = input()
s2 = input()
s3 = input()
argv = [s1,s2,s3]
imax = len(argv)
jmax = max(map(len, argv))

for i in range(imax):
    argv[i] = argv[i].upper()
    l[s.index(argv[i][0])] = 1
    a = argv[i][-1::-1]
    for j in range(len(a)):
        word[i][j] = a[j]
        c = word[i][j]
        if (c.isalpha()):
            digit[s.index(c)] = -1
        elif (c.isdigit()):
            digit[s.index(c)] = int(c)
        else:
            print("UNSOLVABLE")
            exit(1)

for i in range(10):
    ok[i] = True
tr(0)
if (solution == 0):
    print("UNSOLVABLE")
exit(0)