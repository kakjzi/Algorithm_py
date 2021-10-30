import sys
sys.setrecursionlimit(1000000) 
input = sys.stdin.readline

def dfs(gragh,v,visited):
    visited[v] = True
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i,visited)

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
        dfs(graph, i, visited)
        cnt += 1
print(cnt)


# sys.setrecursionlimit(10**6) 란???
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편
# 재귀와 관련된 에러로써, 파이썬이 정한 재귀의 깊이보다 더 깊어질때 발생

# 에러를 방지하는 방법은 다음 2가지가 있다.
# 1. DFS -> BFS 로 변경
# 2. sys.setrecursionlimit(1000000) 이런식으로 재귀의 깊이를 정의해준다.