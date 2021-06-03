a=[4,5,3,2,1,3,4]
n=len(a)
list=[0]*n
for i in range(n):
    if list[a[i]]==1:
        print(a[i])
    else:
        list[a[i]]+=1

==> TC=O(n) and SC=O(n)
