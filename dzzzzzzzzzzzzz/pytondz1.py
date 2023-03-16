a=int(input())
b=int(input())
k=0
for i in range(a, b + 1):
    print(i)
for i in range(a, b + 1):
    if i%7==0:
        print(i)
for i in range(a, b + 1):
    if i%5==0:
        k=+1
print(k)
