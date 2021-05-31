

def thirdMax(nums):
    nums.sort(reverse=True)
    count=0
    i=0
    while i<len(nums):
        if (i==len(nums)-1 and count!=2) or len(nums)<3:
            return max(nums)
        if count==2:
            return nums[i]
        if nums[i]!=nums[i+1]:
            count+=1
        i+=1



if __name__=="__main__":
    testcases=[[3,2,1],
               [1,2],
               [2,2,3,1],
               [1,1,2],
               [4,2,7,4,8,1,0,3],
               [5,4,3,6,4,0]]
    for i in testcases:
        print(thirdMax(i))

