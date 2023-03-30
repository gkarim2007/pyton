a = input([1,0,-3,4])
min=99
max=0
mi=0
ma=0
no=0
for i in a:
    if a[i]<0:
        mi=+1
    if a[i]>0:
        ma=+1
    if a[i]==0:
        no=+1
    if a[i]<min:
        min=a[i]
    if a[i]>max:
        max=a[i]
print(max)
print(min)
print(mi)
print(ma)
print(no)
