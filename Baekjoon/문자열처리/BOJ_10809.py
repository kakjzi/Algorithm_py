n = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz' 
result = [-1] * len(alphabet)
for i in n:
    result[alphabet.index(i)] = n.index(i)
print(*result)