M,N=map(int,input().split()) 
prime=[True]*(N+1)
prime[1]=False 
for i in range(2,int(N**0.5)+1): 
    if prime[i]==True: 
        for j in range(i+i,N+1,i): 
            prime[j]=False 
for i in range(N+1): 
    if prime[i]==True and M<=i: 
        print(i)
