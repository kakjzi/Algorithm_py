import sys 
N = int(sys.stdin.readline().rstrip()) 
que = [] 
for _ in range(N): 
    command = list(sys.stdin.readline().rstrip().split()) 
    if command[0] == "push": 
        que.append(command[1]) 
    elif command[0] == "pop": 
        print(que.pop(0) if len(que) else -1) 
    elif command[0] == "size": 
        print(len(que)) 
    elif command[0] == "empty": 
        print(0 if len(que) else 1)
    elif command[0] == "front": 
        print(que[0] if len(que) else -1) 
    elif command[0] == "back": 
        print(que[-1] if len(que) else -1)

