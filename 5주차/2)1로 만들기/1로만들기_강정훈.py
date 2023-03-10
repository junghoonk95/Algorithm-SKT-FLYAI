n = int(input())

dp = [0 for i in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  #먼저 그전꺼에서 1빼준다고 가정하여 그전 에서 +1
    if i % 2 == 0:  # 2나눈거랑 그전꺼 1빼준거 비교
        dp[i] = min(dp[i], dp[i//2]+1) 
    if i % 3 == 0:   # 3나눈거랑 그전꺼 1빼준거 비교
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])

#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#2 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
#3 [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
#4 [0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0] dp[2]+1 vs dp[3]+1
#5 [0, 0, 1, 1, 2, 3, 0, 0, 0, 0, 0]
#6 [0, 0, 1, 1, 2, 3, 2, 0, 0, 0, 0] dp[5]+1 vs dp[3] +1 vs dp[2]+1*
#7 [0, 0, 1, 1, 2, 3, 2, 3, 0, 0, 0]
#8 [0, 0, 1, 1, 2, 3, 2, 3, 3, 0, 0] dp[7]+1 vs dp[4] +1 
#9 [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 0] dp[8]+1 vs dp[3]+1
#10 [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
