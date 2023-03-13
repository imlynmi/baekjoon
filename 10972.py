# https://www.acmicpc.net/problem/10972

n = int(input())
array = list(map(int, input().split()))

for i in range(n-2, -1, -1):
    if array[i+1] > array[i]:
        for j in range(i+1, n):
            if array[j] > array[i]:
                pv = j
        array[i], array[pv] = array[pv], array[i]
        array[i+1:] = array[n-1:i:-1]
        print(*array, sep=' ')
        break
else: print('-1')