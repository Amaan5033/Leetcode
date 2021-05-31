


def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i]=pow(nums[i],2)
    return sorted(nums)



nums=[-4,-1,0,3,10]
print(sortedSquares(nums))