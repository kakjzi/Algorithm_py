oldPipe= list(input())
newPipe=[]
newPipeCount = 0

for i in range(len(oldPipe)):
    if oldPipe[i] == "(":
        newPipe.append("(")
    elif oldPipe[i] == ")":
        if oldPipe[i-1] == "(":
            newPipe.pop()
            newPipeCount += len(newPipe)
        elif oldPipe[i-1] ==")":
            newPipe.pop()
            newPipeCount += 1
print(newPipeCount)
    

