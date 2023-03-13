# https://www.acmicpc.net/problem/10430

a, b, c = map(int, input().split(' '))

cal1 = (a + b) % c
cal2 = ((a % c) + (b % c)) % c
cal3 = (a * b) % c
cal4 = ((a % c) * (b % c)) % c

print(cal1, cal2, cal3, cal4, sep = '\n')