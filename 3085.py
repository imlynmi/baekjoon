# https://www.acmicpc.net/problem/3085

import sys

def horizontal(canEat):
    count = 1

    for row in range(n):
        for col in range(n-1):
            if board[row][col] == board[row][col+1]:
                count += 1
            else:
                canEat = max(canEat, count)
                count = 1 
        canEat = max(canEat, count)
        count = 1 
    
    return canEat

def vertical(canEat):
    count = 1

    for col in range(n):
        for row in range(n-1):
            if board[row][col] == board[row+1][col]:
                count += 1
            else:
                canEat = max(canEat, count)
                count = 1  
        canEat = max(canEat, count)
        count = 1
    
    return canEat

n = int(input())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
canEat = 1

for row in range(n):
    for col in range(n-1):
        board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
        canEat = max(horizontal(canEat), vertical(canEat))
        board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
            
for row in range(n-1):
    for col in range(n):            
        board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
        canEat = max(horizontal(canEat), vertical(canEat))
        board[row][col], board[row+1][col] = board[row+1][col], board[row][col]

print(canEat)