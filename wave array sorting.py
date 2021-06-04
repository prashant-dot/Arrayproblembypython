from MergeSort import merge_sort
a=[2, 4, 6, 8, 10, 20]
print(a)
i=0
while i<len(a)-1:
    if i>0 and a[i]<a[i-1]:
        a[i-1] , a[i] = a[i] , a[i-1]
    if a[i]<a[i+1]:
        a[i + 1], a[i] = a[i], a[i + 1]
    i+=2

print(a)


==>O(n)
