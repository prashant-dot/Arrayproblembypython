a=[1, 3, 4, 7, 10]
x=14
i=0
j=len(a)-1
min=float("inf")
mini=i
minj=j
while(i<j):
	if a[i]+a[j]>=x:
		j-=1
	if a[i]+a[j]<x:
		if min>x-a[i]-a[j]:
			min=x-a[i]-a[j]
			mini=i
			minj=j
		i+=1
print("pair is ",a[mini], "and", a[minj] ,"with difference ", min)

==>O(n)
