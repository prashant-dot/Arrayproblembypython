def spiral(a,r,c):
    k=0
    l=0
    while(k<r and l<c):
        for i in range(l,c):
            print(a[k][i], end=" ")
        k+=1

        for i in range(k,r):
            print(a[i][c-1], end=" ")
        c-=1

        if k<r:
            for i in range(c-1,l-1,-1):
                print(a[r-1][i], end=" ")
            r-=1

        if l<c:
            for i in range(r-1,k-1,-1):
                print(a[i][l], end=" ")
            l+=1

a=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
r=4
c=4
spiral(a,r,c)

==>O(rows*cols)
