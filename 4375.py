# https://www.acmicpc.net/problem/4375

length = []

while True:
    try:
        n = int(input())
    except:
        for l in length:
            print(l)
        break

    ones = '1'

    while int(ones) % n != 0:
            ones += '1'
    
    length.append(len(ones))