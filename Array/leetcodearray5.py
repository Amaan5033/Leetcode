

# valid Mountain Array

def validMountainArray(arr):
    if len(arr)<3:
        return False
    i=0
    max,min,count=arr[0],float("inf"),0
    while i<len(arr)-1:
        if min==float("inf") and arr[i+1]>max:
            max=arr[i+1]
            count+=1
        elif min==float("inf") and arr[i+1]==max: 
                return False
        elif min==float("inf") and arr[i+1]<max:
                min=arr[i+1]
        elif arr[i+1]<min:
            min=arr[i+1]
        elif arr[i+1]==min:  
                return False
        else:
            if arr[i+1]>min:
                return False
        i+=1
    if max==arr[0]:
        return False
    elif count==len(arr)-1:
        return False
    else:
        return True 

arr=[3,7,6,4,3,0,1,0]

print(validMountainArray(arr))