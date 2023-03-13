# https://www.acmicpc.net/problem/9095

def summation(n):
    if n < len(sumChart):
        return sumChart[n]
    else:
        total = summation(n - 1) + summation(n - 2) + summation(n - 3)
        sumChart.append(total)
        return total

t = int(input())
n = []
sumChart = [0, 1, 2, 4]

for i in range(t):
    n.append(int(input()))

for target in n:
    print(summation(target))