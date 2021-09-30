n = int(input())

podoju = [0] * (n+1)

podoju[1] += podoju[0]
podoju[2] += podoju[1]
for i in range(3,1+n):
    podoju[i] += podoju[i-1] + podoju[i-3]

    