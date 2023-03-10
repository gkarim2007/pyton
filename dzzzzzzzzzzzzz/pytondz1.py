a=int(input())
c=int(input())
b=int(input())


if b==1:
    if a>c:
        print(a)
    if a<c:
        print(c)
        
if b==2:
    if a<c:
        print(a)
    if a>c:
        print(c)
if b==3:
    print((a+c)/2)
