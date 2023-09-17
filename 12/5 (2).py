n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x), c))
    

# 처음에는 오른쪽을 보고 있으므로(동,서,남,북)
dx = []
    

    
