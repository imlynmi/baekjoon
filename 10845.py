# https://www.acmicpc.net/problem/10845

import sys

n = int(input())
queue = []

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if len(cmd) > 1:
        x = cmd[1]
        queue.append(x)
    else:
        if cmd[0] == 'pop':
            if len(queue) != 0:
                print(queue[0])
                queue.pop(0)
            else:
                print(-1)
        elif cmd[0] == 'size':
            print(len(queue))
        elif cmd[0] == 'empty':
            print(1) if len(queue) == 0 else print(0)
        elif cmd[0] == 'front':
            print(queue[0]) if len(queue) != 0 else print(-1)
        elif cmd[0] == 'back':
            print(queue[len(queue)-1]) if len(queue) != 0 else print(-1)