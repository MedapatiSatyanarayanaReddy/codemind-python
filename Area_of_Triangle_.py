a,b,c=map(int,input().split())
import math
s=(a+b+c)/2
s=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("%.2f"%s)