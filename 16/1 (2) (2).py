array = list(map(int, input().split()))
    

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
dp = []
index = 0
for i in range(3):
    dp.append(array[index:index + 3])
    index += m
    
print(dp)