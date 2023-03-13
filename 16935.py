# https://www.acmicpc.net/problem/16935

import sys

def operation(op, n, m):
    if op == 1:
        newarr = [[0]*m for _ in range(n)]
        for row in range(n//2):
            newarr[row], newarr[n-1-row] = arr[n-1-row], arr[row]
    elif op == 2:
        newarr = [[0]*m for _ in range(n)]
        for col in range(m//2):
            for row in range(n):
                newarr[row][col], newarr[row][m-1-col] = arr[row][m-1-col], arr[row][col]
    elif op == 3:
        newarr = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                newarr[j][n-1-i] = arr[i][j]
    elif op == 4:
        newarr = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                newarr[j][i] = arr[i][m-1-j]
    elif op == 5:
        newarr = [[0]*m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if row < n//2 and col < m//2:
                    newarr[row][col] = arr[row+(n//2)][col]
                elif row < n//2 and col >= m//2:
                    newarr[row][col] = arr[row][col-(m//2)]
                elif row >= n//2 and col < m//2:
                    newarr[row][col] = arr[row][col+(m//2)]
                elif row >= n//2 and col >= m//2:
                    newarr[row][col] = arr[row-(n//2)][col]
    elif op == 6:
        newarr = [[0]*m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if row < n//2 and col < m//2:
                    newarr[row][col] = arr[row][col+(m//2)]
                elif row < n//2 and col >= m//2:
                    newarr[row][col] = arr[row+(n//2)][col]
                elif row >= n//2 and col < m//2:
                    newarr[row][col] = arr[row-(n//2)][col]
                elif row >= n//2 and col >= m//2:
                    newarr[row][col] = arr[row][col-(m//2)]

    return newarr


n, m, r = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

op = list(map(int, input().split()))

for action in op:
    arr = operation(action, n, m)
    n = len(arr)
    m = len(arr[0])

for row in arr:
    print(*row, sep=' ')