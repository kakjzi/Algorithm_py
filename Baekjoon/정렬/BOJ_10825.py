import sys 
n = int(sys.stdin.readline())
score = [sys.stdin.readline().split() for _ in range(n)]  

score.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) 
print (score)
for student in score: 
    sys.stdout.write(str(student[0]) + "\n")