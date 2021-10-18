TEST_CASE = int(input())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
    
for _ in range(TEST_CASE):
    a, b = map(int, input().split())
    print(lcm(a, b))