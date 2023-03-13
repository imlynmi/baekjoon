# https://www.acmicpc.net/problem/1759

import sys, string
from itertools import combinations

l, c = map(int, input().split())
letters = list(sys.stdin.readline().split())

vows = {'a', 'e', 'i', 'o', 'u'}
alpha = set(string.ascii_lowercase)
cons = alpha - vows

letters.sort()
comb = list(combinations(letters, l))

for pwd in comb:
    vow_num = len(set(pwd).intersection(vows))
    con_num = len(set(pwd).intersection(cons))

    if vow_num > 0 and con_num > 1:
        print(*pwd, sep='')