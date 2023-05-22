n=int(input())
a=list(map(int,input().split()))
k=sum(a)//n
print(k in a)
