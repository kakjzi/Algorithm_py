n = int(input())
num = list(map(int, input().split()))
sum = [0] * n 

for i in range(1,n): 
    for j in range(i):                       
        if num[i] > num[j]:
            sum[i] = max(num[i], sum[j]+num[i]) 
print(max(sum))