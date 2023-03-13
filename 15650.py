# https://www.acmicpc.net/problem/15650

def combination(arr):
    if len(arr) < m:
        for i in range(1, n+1):
            if len(arr) == 0:
                arr.append(i)
                combination(arr)
                arr.pop()
            else:
                if i > arr[len(arr)-1]: 
                    arr.append(i)
                    combination(arr)   
                    arr.pop()
    elif len(arr) == m:
        print(*arr, sep=" ")

n, m = map(int, input().split())
combination([])