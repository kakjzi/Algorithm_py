n = input()
suffix = []
for i in range(len(n)):
    suffix.append(n[i:])
    suffix.sort()
for i in suffix:
    print(i)
