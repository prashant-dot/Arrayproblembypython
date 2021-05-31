a=[4,6]
k=3
p=0
r=len(a)-1
def part(a,p,r):
    k=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=k:
            i += 1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1
def qs(a,p,r):
    if p<r:
        q=part(a,p,r)
        qs(a,p,q-1)
        qs(a,q+1,r)
qs(a,p,r)
print(a)
mid=(a[p]+a[r])//2
if mid>k:
    for i in range(p,r+1):
        if a[i]<=mid:
            a[i]=a[i]+k
        else:
            a[i]-=k
    print(a)
    qs(a,p,r)
    print(a)
    print(a[r]-a[p])
else:
    print(a[r]-a[p])
		
===>O(nlogn)

