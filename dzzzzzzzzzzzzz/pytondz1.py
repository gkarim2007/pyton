a = ([1,2,6,4])
b = ([8,3,6,4])
min=99
max=0
min2=99
max2=0
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
    if a[i]>max:
        max=a[i]
for i in range(len(b)):
    if b[i]<min2:
        min2=b[i]
    if b[i]>max2:
        max2=b[i]
print(max)
print(min)
print(max2)
print(min2)
print()
for i in range(len(a)):
    for i in range(len(b)):
        if b[i]==a[i]:
            print(b[i])
print()
for i in range(len(a)):
    for i in range(len(b)):
        if b[i]!=a[i]:
            print(b[i])
