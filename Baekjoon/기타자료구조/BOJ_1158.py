n,k = map(int,input().split())
list = [i for i in range(1,n+1)]
answer = []   
num = 0

for _ in range(n):
    num += k-1  # k번째 사람을 빼기위하여 인덱스번호 -1
    if num >= len(list):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num % len(list)

    answer.append(str(list.pop(num)))
print("<",", ".join(answer)[:],">", sep='')

# 구분자.join(list )