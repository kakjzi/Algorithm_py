TEST_CASE = int(input())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(TEST_CASE):
	a = list(map(int,input().split()))
	answer = 0
	for i in range(1,len(a)-1):     
		for j in range(i+1,len(a)):
			answer += (gcd(a[j],a[i]))
	print(answer)

# 해당문제는 문제를 잘 읽어야한다.
# 문제 : 가능한 모든 쌍 GCD의 합 구하기
# 1. 첫째 줄에 테스트케이스 개수
# 2. 각 테스트 케이스는 수의 개수(N)가 먼저 주어지고 그 (N)수 만큼 입력.


#풀이 
# 인덱스 0 번째 = N
# 나머지 list[1:]은 숫자들이고 여기서 가능한 모든 쌍 GCD를 구한 뒤 그 합을 출력하기.