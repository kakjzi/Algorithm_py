import sys
n,k = list(map(int,sys.stdin.readline().split()))
sort_list=(list(map(int,sys.stdin.readline().split())))
sort_list.sort()
print(sort_list[k - 1])