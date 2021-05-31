


def sortArrayByParity(A):
    i=0
    count=0
    while i<len(A):
        count+=1
        if count==len(A):
            break
        if A[i]%2!=0:
            a=A.pop(i)
            A.append(a)
        else:
            i+=1
    return A




A=[1,2,3,4,5,6,7,8,9,10]
print(sortArrayByParity(A))
