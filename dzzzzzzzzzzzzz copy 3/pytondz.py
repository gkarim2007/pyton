a = [-1,2,-4,3,1,4,6,7]
size=8
mi=0
ch=0
ne=0
pr=1
min=a[0]
max=a[0]
minmax=1
poloj1=0
poloj2=0
poloj=0
for i in range (size):
    if a[i]<0:
        mi=mi+a[i]
    if a[i]%2==0:
        ch=ch+a[i]
    if a[i]%2!=0:
        ne=ne+a[i]
    if i%3==0:
        pr=pr*a[i]
    if a[i]<min:
        min=i
    if a[i]>max:
        max=i
    if a[i]>0 and poloj1==0:
        poloj1=i
    if a[i]>0:
        poloj2=i

print(mi)
print(ch)
print(ne)
print(pr)
for i in range (min - 1,max):
    minmax=minmax*a[i]
print(minmax)
for i in range (poloj1+1,poloj2):
    poloj=poloj+a[i]
print(poloj)
