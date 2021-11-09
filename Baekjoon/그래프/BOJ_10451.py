import sys
sys.setrecursionlimit(1000000) 
input = sys.stdin.readline

def dfs(gragh,v,visited):
    visited[v] = True
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i,visited)

TEST_CASE = int(input())
for i in range(TEST_CASE):
    size = int(input())
    graph = [[] for _ in range(size + 1)]
    visited = [False] * (size + 1)

    node_A = list(map(int, input().split()))

    ## node_A 를 [[],[1,a],[2,b] ] 이런 식으로 만들어야함.
    for i in range(1, size):
        graph[i].append(node_A)

    cnt = 0

    for i in range(1, size+1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1
    print(cnt)