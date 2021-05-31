

def checkIfExist(arr):
    i=0 
    
    while i<len(arr):
        j=0
        while j<len(arr):
            if i!=j:
                print(f"comparing between {arr[i]} and {arr[j]}")
                if arr[i]==(2*arr[j]):
                    return True
                if arr[j]==(2*arr[i]):
                    return True
            j+=1
        i+=1
    return False



arr=[-20,8,-6,-14,0,-19,14,4]

print(checkIfExist(arr))





