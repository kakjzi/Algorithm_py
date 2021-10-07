TestCase = int(input())
dp = [0] * 101
dp[1]=dp[2]=dp[3] = 1
dp[4]=dp[5]=2

for k in range(TestCase):
    n = int(input())
    for i in range(5,n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])