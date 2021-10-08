n = int(input())
price = [0]+ list(map(int, input().split()))   

dp = [0] * (n+1)  # n 번째 배열의 최대 합

for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = max(dp[i], price[j] + dp[i - j])

print(dp[n])