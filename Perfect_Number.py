num=int(input())  
sum_v=0  
for i in range(1,num):  
    if (num%i==0):  
        sum_v=sum_v+i  
if(sum_v==num):  
    print("True")  
else:  
    print("False")  