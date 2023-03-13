# https://www.acmicpc.net/problem/1697

from collections import deque

def fastestPath(subin):
    visited_deq = deque([subin])

    while visited_deq:
        locNow = visited_deq.popleft()

        if locNow == dest:
            return visited[locNow]
        
        for nxtLoc in (locNow-1, locNow+1, locNow*2):
            if 0 <= nxtLoc <= 100000 and visited[nxtLoc] == 0:
                visited[nxtLoc] = visited[locNow] + 1
                visited_deq.append(nxtLoc)

subin, dest = map(int, input().split())
visited = [0] * 100001
time = fastestPath(subin)
print(time)