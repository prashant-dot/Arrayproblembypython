a=[4,3,5,2,1,5,8,7]
b=[0]*(len(a)+1)
for i in range(len(a)):
	if b[a[i]]==0:
		b[a[i]]=1
	else:
		print("Repeating element : ",a[i])
for ind,val in enumerate(b):
	if val==0:
		if ind==0:
			pass
		else:
			print("Missing element : ",ind)
			break
==> TS=O(n) and SC=O(n)
