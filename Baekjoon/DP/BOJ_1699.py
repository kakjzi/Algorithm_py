n = int(input())
dp = [x for x in range (n+1)] # 초기값 세팅
for i in range(1,n+1): #dp[n]을 구해야하기 때문에 n+1 범위 지정
    for j in range(1,i):
        if j*j > i : 
            break
        if dp[i] > dp[i-j*j] + 1 :  #
            dp[i] = dp[i-j*j] + 1
print(dp[n])