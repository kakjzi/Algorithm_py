import sys
dic = {}
N = int(sys.stdin.readline())
for _ in range(N):
    a = int(sys.stdin.readline())
    if a in dic.keys():
        dic[a] += 1
    else:
        dic[a] = 1


dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))  ## 개수로 내림차순 , 숫자로 오름차순
print(dic[0][0])

#x[0] = key ( 카드의 숫자 )
#x[1] = value ( 카드의 개수 )