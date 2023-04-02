a = [-1,2,-4,3,1,4,6,7]
size=8
mi=0
ch=0
ne=0
pr=1
for i in range (size):
    if a[i]<0:
        mi=mi+a[i]
    if a[i]%2==0:
        ch=ch+a[i]
    if a[i]%2!=0:
        ne=ne+a[i]
    if i%3==0:
        pr=pr*a[i]
        
    
print(mi)
print(ch)
print(ne)
print(pr)