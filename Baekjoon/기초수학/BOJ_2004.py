# 팩토리얼을 기본적으로 사용하게되면 범위가 2,000,000,000 인데 당연 시간초과가 뜰것이다.
# 조합의 식은 n!/(n-r)!*r! 
# 순열의 식은 n!/(n-r)!

# 접근
# 끝자리 0의 개수는 10의 배수, 즉 2, 5의 쌍
# 2 와 5중 개수가 낮은거 하나 골라 출력.

# 5가 몇번 나누어지는지를 구한다.
def fiveCount(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

# 2가 몇번 나누어지는지를 구한다.
def twoCount(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer


n, m = map(int, input().split())

if m == 0:
    print(0)

else:
    # 2와 5의 개수를 nCm을 구할 때처럼 구해서 더 작은 개수를 선택한다.
    # n! - m! - (n-m)!
    print(min(twoCount(n) - twoCount(m) - twoCount(n - m), fiveCount(n) - fiveCount(m) - fiveCount(n - m)))

