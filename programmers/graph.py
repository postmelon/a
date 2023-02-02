
graph = [
         [],
         [2, 3],
         [1, 3, 5],
         [1, 2, 5, 4],
         [3],
         [2, 3],
        ]

# DFS
def dfs():
    s = 1
    # 그래프에서 정점의 개수
    v = 5

    # 1. 목적지
    to_visits = [s]

    # 2. 방문 체
    visited = [False for _ in range(v+1)] # 0을 버림

    while to_visits: # 값이 하나라도 있으면 계속 반복 요소가 있는 리스트는 True 반환
        # 리스트 뒤의 값을 빼서 방문
        now = to_visits.pop()
        if not visited[now]:
            visited[now] = True
            print(now)
            to_visits += graph[now]
dfs()



# BFS
def bfs():
    s = 1
    # 그래프에서 정점의 개수
    v = 5

    # 1. 목적지
    to_visits = [s]

    # 2. 방문 체
    visited = [False for _ in range(v + 1)]  # 0을 버림

    while to_visits:  # 값이 하나라도 있으면 계속 반복 요소가 있는 리스트는 True 반환
        # 리스트 뒤의 값을 빼서 방문
        now = to_visits.pop(0)
        if not visited[now]:
            visited[now] = True
            print(now)
            to_visits += graph[now]
bfs()