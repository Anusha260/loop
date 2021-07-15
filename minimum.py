a=[1,3,7,8,5,35]
i=0
min=a[i]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print(min)