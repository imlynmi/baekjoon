# https://www.acmicpc.net/problem/15649

def combination(result):
    if len(result) == m:
        print(*result)
    else:
        for choice in range(1, n+1):
            if used[choice] == 0:
                result.append(choice)
                used[choice] = 1
                combination(result)
                used[choice] = 0
                result.remove(choice)

n, m = map(int, input().split(' '))
result = []
used = [0] * (n+1)
combination(result)