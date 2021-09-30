TEST_CASE = int(input())
for i in range(TEST_CASE):
    dp = []
    n = int(input())
    for k in range(2):
        dp.append(list(map(int, input().split())))

    # n = 1 일때 초기값 설정.    
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for j in range(2, n):
        dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
        dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))


## 해당 문제는 스티커 선택시 해당 스티커의 상, 하, 좌, 우 에 위치한 스티커를 고르지 않으면서 얻을 수 있는 최대 점수를 구하는 것이다.

