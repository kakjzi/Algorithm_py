n = int(input())
for i in range(n, 0, -1):
    print('{1}{0}'.format('*' *(2*i-1), ' '*(n-i)))
for i in range(2, n+1):
    print('{1}{0}'.format('*' *(2*i-1), ' '*(n-i)))