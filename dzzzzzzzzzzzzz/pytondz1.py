a=int(input())
b=int(input())
d=int(input())
aa=str(input())
aaa=''
aa=aa.split(' ')
for i in range(len(aa)):
    if aa[i]=='!'and a!=0:
        aaa=aaa+'a'
    if aa[i]=='?'and b!=0:
        aaa=aaa+'b'
    if aa[i]=='*'and d!=0:
        aaa=aaa+'d'
print(aaa)
