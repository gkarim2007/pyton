a=int(input())
b=int(input())
sum=0
sum2=0
for i in range(a, b + 1):
    if i%2==0:
        sum=sum+i
    else :
        sum2=sum2+i
        
print(sum)
print(sum2)
