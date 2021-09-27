n = int(input())
for i in range(1, n):
    print('{0}{1}{0}'.format('*' * i ,' ' * 2 * (n-i)))
for i in range(n, 0, -1):
    print('{0}{1}{0}'.format('*' * i ,' ' * 2 * (n-i)))