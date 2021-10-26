import math 

def isPrime(num): 
    if num == 1: 
        return False 
    n = int(math.sqrt(num))  #제곱근 

    for k in range(2, n+1): # 소수는 1과 자기자신 따라서 나누어 떨어지면안됨.
        if num % k == 0:
            return False 
    return True 

    
m, n = map(int, input().split()) 
for k in range(m, n+1): # 범위는 m <= k <= n 이므로 , 하나씩 함수에 넣어서 true/false 확인하면 될듯.
    if isPrime(k) : print(k)