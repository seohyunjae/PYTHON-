from collections import deque

# BFS �޼��� 
def bfs(graph, start, visited):
    # ť(Queue) ������ ���� deque ���̺귯�� ���
    queue = deque([start])
    # ���� ��带 �湮 ó��
    visited[start] = True
    # ť�� �� ������ �ݺ�
    while queue:
        # ť���� �ϳ��� ���Ҹ� �̾� ���
        v = queue.popleft()
        print(v)
        # �ش� ���ҿ� �����, ���� �湮���� ���� ���ҵ��� ť�� ����
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
# �� ��尡 ����� ������ ����Ʈ �ڷ������� ǥ��(2���� ����Ʈ)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7] 
]
# �� ��尡 �湮�� ������ ����Ʈ �ڷ������� ǥ��(1���� ����Ʈ)
visited = [False] * 9
# ���ǵ� BFS �Լ� ȣ��
bfs(graph, 1, visited)