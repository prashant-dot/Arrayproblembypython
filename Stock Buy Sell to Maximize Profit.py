def StockBuySell(a,n):
	i=0
	if n==1:
		return 
	while(i<n-1):
		while(i<n-1 and a[i+1]<=a[i]):
			i+=1
		if i==n-1:
			break
		buy=i
		i+=1
		while(i<n and a[i-1]<=a[i]):
			i+=1

		sell=i-1
		print("buy on day=",buy ,"and sell on day=",sell)
a=[130,240,333,20,201,600,700]
StockBuySell(a,len(a))
==>O(n)
