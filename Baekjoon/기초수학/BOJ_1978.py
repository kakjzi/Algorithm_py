# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 주어진 수들 중 소수의 개수를 출력한다.

# 소수란 1과 자기자신이다.

n = int(input())
num_list = list(map(int, input().split()))

answer = 0

for i in num_list:
    cnt = 0
    if(i == 1):
        continue
    for j in range(2, i + 1): # 1 제외하고 cnt = 1 일때 소수라고 볼 수 있음.
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        answer += 1
print(answer)