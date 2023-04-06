a = [1,2,-4,3,-1,-4,6,-7]
b=[0,0,0,0,0,0,0,0,0]
c=0
d=[0,0,0,0,0,0,0,0,0]
k=0
y=[0,0,0,0,0,0,0,0,0]
x=0
l=[0,0,0,0,0,0,0,0,0]
j=0
for i in range(len(a)):
    if a[i]%2==0:
        b[c]=a[i]
        print (b[c])
        c=+1
for i in range(len(a)):
    if a[i]%2!=0:
        d[k]=a[i]
        print (d[k])
        k=+1
for i in range(len(a)):
    if a[i]>0:
        y[x]=a[i]
        print (y[x])
        x=+1
for i in range(len(a)):
    if a[i]<0:
        l[j]=a[i]
        print (l[j])
        j=+1
