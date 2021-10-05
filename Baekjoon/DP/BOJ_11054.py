n = int(input())
num = list(map(int, input().split()))
reverse_num = num[::-1]

d_front = [1]*n
d_rear = [1]*n

for i in range(n):
  for j in range(i):
    if num[j]<num[i]:
      d_front[i]=max(d_front[i], d_front[j]+1) ## 증가
    if reverse_num[j]<reverse_num[i]:
      d_rear[i]=max(d_rear[i], d_rear[j]+1) ## 역배열 증가

result = [0]*n
for i in range(n):
  result[i] = d_front[i]+d_rear[n-1-i]-1

print(max(result))