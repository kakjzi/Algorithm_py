sentence = ''
for c in input():
    if 'a' <= c <= 'z':
        sentence += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
    elif 'A' <= c <= 'Z':
        sentence += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
    else:
        sentence += c
print(sentence)

# 아스키코드 대문자 시작 65 ~90
# 아스키코드 소문자 97~122