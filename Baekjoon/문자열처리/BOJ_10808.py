n = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz' 
result = [0] * len(alphabet)
for i in n :
    result[alphabet.index(i)] += 1
print(*result)

#* 은 unpacking
# .index()는 리스트중에서 특정한 원소가 몇번째 위치하는지 알려준다.
# 중복의 경우 맨 처음의 원소 위치를 알려준다.