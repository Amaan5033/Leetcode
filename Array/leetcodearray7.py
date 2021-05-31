

def moveZeroes(nums):
    i=0
    while i<len(nums):
        if max(nums[i:])==0 and min(nums[i:])==0:
            break
        if nums[i]==0:
            a=nums.pop(i)
            nums.append(a)
        else:
            i+=1
        
    return nums

nums=[4,3,0,0,0,2,1,-1,2,-1,4,0,0,-1,0,-2,0]
print(moveZeroes(nums))
