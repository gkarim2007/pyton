a="ааа а ааа аа"
a=a.split(" ")
b=0
c=0
d=0
b1=''
c1=''
d1=''
b=a[0]

for i in range(len(a)):
    if a[i]==b1:
        b+=1
    elif a[i]==c1:
        c+=1
    else:
        c1=a[i]
    if a[i]==d1:
        d+=1
    else:
        c1=a[i]
if b >= c or d:
    print(b1)
if c>=b or d:
    print(c1)
if d>=c or b:
    print(d1)