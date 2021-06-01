a=[1, 2, 3, 4, 5]
j=len(a)-1
i=0
x=9
a.sort()
while(i<j-1):
    k=i+1
    j = len(a) - 1
    while(k<j):
        if a[i]+a[k]+a[j]<x:
            k+=1
        elif a[i]+a[k]+a[j]>x:
            j-=1
        else:
            print(a[i],a[k],a[j])
            break
    i+=1
==>O(nlogn+n^2)=O(n^2)
