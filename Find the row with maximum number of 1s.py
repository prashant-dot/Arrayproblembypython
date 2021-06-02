a=[[0,0,1,1],[0,1,1,1],[0,1,1,1],[0,0,0,1]]
R=len(a)
C=len(a[0])
max=-1
max_row=0
def first(mat,l,h):
    if l<=h:
        mid=(h+l)//2
        if (mid==0 or mat[mid-1]==0) and mat[mid]==1:
            return mid
        elif mat[mid]==0:
            return first(mat,mid+1,h)
        else:
            return first(mat,l,mid-1)
    return -1
for i in range(R):
    index=first(a[i],0,C-1)
    if index!=-1 and C-index>max:
        max=C-index
        max_row=i
print("index is ", max_row , "with max 1s ", max)

==>O(M*logN) where M==rows and N==cols
