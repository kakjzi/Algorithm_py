n = int(input())

dp = [0] * 31
dp[0], dp[2] = 1, 3


#dp[n] = dp[n-2]*3 + dp[n-4] * 2 + dp[0] *2

for i in range(4, n + 1):
    dp[i] = dp[i - 2] * 3 # 바로 이전 개수

    for j in range(4, i + 1, 2):  #  i > 4 부터
        dp[i] += dp[i - j] * 2  #   [n-2]블록이 앞뒤로 붙을 경우 , 자기 자신만 만들 수 있는 블록

print(dp[n])