from collections import deque
import sys
input = sys.stdin.readline

def bfs(gragh,v,visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        pop = queue.popleft()
        for i in gragh[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    node_A, node_B = map(int, input().split())
    graph[node_B].append(node_A)
    graph[node_A].append(node_B)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
print(cnt)