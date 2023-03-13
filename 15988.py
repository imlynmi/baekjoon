# https://www.acmicpc.net/problem/15988

import sys

t = int(input())
ways = [0, 1, 2, 4]

for _ in range(t):
    n = int(sys.stdin.readline())
    total = 0

    if n >= len(ways):
        for i in range(len(ways), n+1):
            total = (ways[i-1] + ways[i-2] + ways[i-3])%1000000009
            ways.append(total)

    print(ways[n])