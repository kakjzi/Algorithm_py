tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
answer = ''
while N != 0:
    answer += str(tmp[N % B]) # 나머지로 진법 변환
    N //= B
    
print(answer[::-1]) # 1의 자리부터 구했으니 뒤집어주자 