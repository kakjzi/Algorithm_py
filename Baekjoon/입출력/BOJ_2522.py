n = int(input())
for i in range(1, n):
    print('{1}{0}'.format('*' * i ,' ' * (n-i)))
for i in range(n, 0, -1):
    print('{1}{0}'.format('*' * i ,' ' * (n-i)))