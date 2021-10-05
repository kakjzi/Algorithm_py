n = int(input())
#계단수는 300까지
score=[0]*300
dp=[0]*300

for i in range(n):
    score[i]=int(input())

# 연속하여 3개 x 미리 정의.
# 마지막 도착계단 반드시 포함
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[2]+score[1],score[2]+score[0])

for i in range(3,n):
    dp[i] = max(score[i]+score[i-1]+dp[i-3],score[i]+dp[i-2])

#       i-3   i-2   i-1   i
#case 1  O     X     O    O -> score[i] + score[i-1] + dp[i-3]
#case 2  O     O     X    O -> score[i] + dp[i-2]
# dp 의미는 계단을 밟은 거 까지의 최대 합~
print(dp[n-1])