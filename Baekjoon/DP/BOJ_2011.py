n = list(map(int,input()))  # 한 글자 씩 나누어 리스트 
l = len(n)  

dp = [0 for _ in range(l+1)] # i 번째 경우의 수

if n[0] == 0 : # 사용자가 입력한 리스트[0]가 0이면 0출력.
    print(0)
else:
                    # 1 <= n <= 26   -> 알파벳으로 변환 가능 .
    n.insert(0,0)    #인덱스 1부터 시작하기 위해 0을 추가.
    dp[0]=dp[1]=1    # 점화식을 위하여 1로 정의

    for i in range(2,l+1):    # 2부터 l번쨰 인덱스 까지 for 문
        if 0 < n[i] < 10:     # i번째를 한자리로 묶을 때
            dp[i] += dp[i-1]  # i-1 번째 까지 경우의 수 + i 번쨰 경우의 수 더한 값 

        temp = n[i-1] * 10 + n[i]  # i번째를 i-1번쨰와 묶어 십의 자리로 만듬     
        if 10 <= temp and temp <=26: # i번째를 십의 자리로 묶을 때 
            dp[i] += dp[i-2]    # i-2 번째 까지 경우의 수 + i 번쨰 경우의 수 더한 값 
    print(dp[l]%1000000)  