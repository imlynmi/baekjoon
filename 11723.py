# https://www.acmicpc.net/problem/11723

import sys

myset = set()

m = int(sys.stdin.readline())

for _ in range(m):
    cmd = sys.stdin.readline().split()

    if len(cmd) == 1:
        if cmd[0] == 'all':
            myset = set([i for i in range(1, 21)])
        else:
            myset.clear()
    else:
        action, num = cmd[0], int(cmd[1])

        if action == 'add':
            myset.add(num)
        elif action == 'remove':
            myset.discard(num)
        elif action == 'check':
            print(1) if num in myset else print(0)
        elif action == 'toggle':
            myset.discard(num) if num in myset else myset.add(num)