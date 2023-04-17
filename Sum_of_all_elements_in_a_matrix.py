r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
s=sum((sum(i) for i in mat))
print(s)