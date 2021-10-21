n = int(input()) 
answer = ''
if n == 0:
    print('0')
else:
    while n:
    	# 나머지가 1인 경우
        if n % -2:
            answer = '1' + answer
            n = n // -2 + 1
            
        # 나머지가 0인 경우
        else:
            answer = '0' + answer
            n = n // -2
            
print(answer)