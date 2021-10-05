n = int(input())   # 잔의 개수 

dp = [0] * (n)     # 각 배열 인덱스 n의 최대 합 저장소    1 <= n

podoju = [int(input()) for _ in range(n)]   # 마시는 와인의 양 배열 


# 초기값 설정.
dp[0] = podoju[0]   # 맨 처음 n= 1 일때  최대로 마실수잇는 와인 합은  podoju[0] 하나임.
if n>1:             # 잔의 개수(n)가 1보다 더 클때  
                    # case 로는 둘다 마시는것이 최대 합이다.
    dp[1] = podoju[0] + podoju[1]

if n>2:             # 잔의 개수(n)가 2보다 더 클때 
                    # case로는 최대로 2번 마시는 경우이며 연속해서 마실수 없으니 경우의수를 나눠 max를 구한다.
                    # 경우의 수 는 아래와 같다.
                    #          1     2      3
                    # case 1   o     x      o   => podoju[0] + podoju[2]
                    # case 2   o     o      x   => dp[1]
                    # case 3   x     o      o   => podoju[1] + podoju[2]
    dp[2] = max(dp[1],podoju[0]+podoju[2],podoju[1]+podoju[2])

for i in range(3,n):
    #          i-3   i-2   i-1     i
    # case 1    O     X     O      O
    # case 2    O     O     X      O
    # case 3    X     O     O      X    ...
    dp[i] = max(dp[i-1], dp[i-2]+podoju[i] ,dp[i-3]+podoju[i]+podoju[i-1])
print(dp[n-1])
    

