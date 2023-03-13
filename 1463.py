# https://www.acmicpc.net/problem/1463

x = int(input())
minStep = [0]*(x+1)

for n in range(2, x+1):
    if n % 2 == 0 and n % 3 == 0:
        minStep[n] = min(minStep[n//2], minStep[n//3], minStep[n-1]) + 1
    elif n % 2 == 0:
        minStep[n] = min(minStep[n//2], minStep[n-1]) + 1
    elif n % 3 == 0:
        minStep[n] = min(minStep[n//3], minStep[n-1]) + 1
    else:
        minStep[n] = minStep[n-1] + 1

print(minStep[x])