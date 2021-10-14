while True:
    try:
        lower_case, upper_case, number, blank = 0, 0, 0, 0
        n = input()
        for i in n:
            if i.islower():
                lower_case += 1
            elif i.isupper():
                upper_case += 1
            elif i.isnumeric():
                number += 1
            else:
                blank += 1
        print(lower_case, upper_case, number, blank)
    except EOFError:
        break


#isnumberic >>  isdigit >> isdemical
#제곱근, 특수문자도 포함   

#단일문자가 숫자모양이면 true 

#문자열이 int형으로 변환가능한지 판단