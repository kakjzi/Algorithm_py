#DFS 깊이
#BFS 넓이
## DFS & BFS 두가지 방식 모두 구하여라

from collections import  deque
#재귀
# 1. 시작노드에서 인접한 노드 중 숫자가 작은 노드를 선택하여 탐색
# 2. 탐색 할 점이 없으면 
# 이전노드에 연결되어있는 점 중 
# 다음으로 크고 방문하지않은 노드 탐색
def dfs(gragh,v,visited):
    visited[v] = True
    print(v, end=' ')

    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)

# 방문하고자하는 노드, 방문한 노드
# 1. 시작노드를 방문한 노드에 삽입
# 2. 방문하고자하는 노드에 시작노드의 Child Node 를 삽입 
# 3. child Node 중심으로 다시 위의 단계 수행
def bfs(gragh,v,visited):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs(graph, v, visited)
print()
bfs(graph, v, visited)