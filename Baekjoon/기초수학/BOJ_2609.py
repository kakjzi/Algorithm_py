a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

## 유클리드 호제법을 사용
## 위 알고리즘은 mod연산을 반복하면 된다.