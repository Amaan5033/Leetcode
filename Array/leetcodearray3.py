

# def removeElement(nums,val):
#     i=0
#     while i<len(nums):
#         if nums[i]==val:
#             nums.pop(i)
#         else:
#             i+=1
#     return nums


# print(removeElement([0,1,2,2,3,0,4,2],2))



def removeDuplicates(nums):
    i=0
    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            nums.pop(i+1)
        else:
            i+=1
    return len(nums)



nums=[0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))


