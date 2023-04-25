a=[4]
a={1,3,2,5}
cel=4
for i in range(a.__len__):
    for j in range((a.__len__)-1):
        if a[i]+a[j]==cel:
            print(i)
            print(j)

