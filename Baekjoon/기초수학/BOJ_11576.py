import math # pow라는 n제곱을 쉽게 해주는 내장함수 이용을 위함

a, b = map(int, input().split())    # a진법의 수를 b진법으로
n = int(input())    # n자리수인 a진법 수
lists = list(map(int, input().split()))
ten = 0	# 10진법으로 만든 수
result = []
fin = ''

for i in range(n):
     # a 진법 to 10진법
    ten += int(lists[i] * math.pow(a, n - i - 1))  # list[0] 일의 자리서 부터 해당진법에 맞게 곱해줌. 그리고 더함.

while ten: # 10진법 to b 진법
    ten,nam = divmod(ten,b)
    result.append(str(nam))

result = result[::-1]
fin = ' '.join(result)
print(fin)

# 진법은 나머지가 0될 떄 까지 계산을하여 나온 나머지들을 역순으로 해줘야 그 해당진법으로 나열됨.