a=input()
b=input()
b.split(" ")
a.split(" ")
otvet=""

for i in a:
    for j in b:
        if a[i]==b[j]:
            otvet="верхний регистр"
        else:
            otvet=a[i]