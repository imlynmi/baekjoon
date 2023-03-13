# https://www.acmicpc.net/problem/2309

total_height = 0
nineH = []

for i in range(9):
    h = input()
    total_height += int(h)
    nineH.append(int(h))

answer = list(nineH)

for j in range(len(nineH)-1):
    for k in range(1, len(nineH)):
        if total_height - (nineH[j] + nineH[k]) == 100:
            answer.remove(nineH[j])
            answer.remove(nineH[k])
            break
    if len(answer) < len(nineH):
        break

answer.sort()
for a in answer: print(a)