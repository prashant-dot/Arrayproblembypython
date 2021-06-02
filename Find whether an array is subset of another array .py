from MergeSort import merge_sort
a1=[22,11,32,3,24,4]
a2=[11,3,4]
merge_sort(a1,0,len(a1)-1)
n=len(a2)
c=0
for i in a2:
    if i in a1:
        c+=1
if c==n:
    print("YES")
else:
    print("NO")
==> O(max(nlogn,mlogn))
