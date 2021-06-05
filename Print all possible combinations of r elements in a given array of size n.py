a=[1, 3, 4, 7, 10]
r=3
n=len(a)
def ppair(a,n,r):
	data=[0]*r

	combination(a,data,0,n-1,0,r)
def	combination(a,data,start,end,index,r):
	if index==r:
		for i in range(r):
			print(data[i],end=" ")
		print()
		return
	i=start
	while(i <= end and end - i + 1 >= r - index):
		data[index]=a[i]
		combination(a,data,i+1,end,index+1,r)
		i+=1

ppair(a,n,r)
