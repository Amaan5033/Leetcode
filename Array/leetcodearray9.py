


def findMaxConsecutiveOnes(nums):
    count_list=[]
    i=0
    count=0
    while i<len(nums):
        if nums[i]==1:
            count+=1
        else:
            count_list.append(count)
            count=0
            
        i+=1
    if nums[-1]==1:
        count_list.append(count)

    return max(count_list)


nums=[1,1,0,1,1,1,0,0,1,0]

print(findMaxConsecutiveOnes(nums))

