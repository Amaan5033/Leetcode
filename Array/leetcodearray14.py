
# def findDisappeardNumbers(nums):
#     nums.sort()
#     i=0
#     a=1
#     while i<len(nums): 
#         if len(nums)==2 and nums[i+1]==1:
#             nums.append(2)
#             nums.pop(i)
#             nums.pop(i)
#             break
#         if a==nums[i] and a>nums[i+1]:
#             nums.pop(i)
#             break
#         if a==nums[i] and a+1==nums[i+1]:
#             nums.pop(i)
#             a+=1
#         elif a==nums[i] and a==nums[i+1]:
#             nums.pop(i)
#             nums.pop(i)
#             a+=1
#         elif a==nums[i] and a+1!=nums[i+1]:
#             for j in range(a+1,nums[i+1]):
#                 nums.append(j)
#             nums.pop(i)
#             a=nums[i]
#         else:
#             nums.append(nums[i])
#     return nums

# if __name__=="__main__":
#     testcases=[[4,3,2,7,8,2,3,1],
#                 [1,7],
#                 [1,1],
#                 [3,9],
#                 [7,1,4,3],
#                 [6,2,1,7,4,9]]
#     for i in testcases:
#         print(findDisappeardNumbers(i))



# def findDisappeardNumbers(nums):
#     maximum_num=max(nums)
#     nums.sort()
#     i=0
#     a=1
#     n=len(nums)
#     count=0
#     while i<n:
#         if a==n+1:
#             break 
#         if nums[i]!=a:
#             count+=1
#             nums.append(a)
#             a+=1
#         else:
#             if nums[i+1]==a:
#                 nums.pop(i)
#             else:
#                 nums.pop(i)
#                 a+=1
#     if maximum_num==n:
#         return nums
#     else:
#         return nums[count:]

# if __name__=="__main__":
#     testcases=[[4,3,2,7,8,2,3,1],
#                 [1,7],
#                 [3,9],
#                 [7,1,4,3],
#                 [6,2,1,7,4,9],
#                 []]
#     for i in testcases:
#         print(findDisappeardNumbers(i))



def findDisappeardNumbers(nums):
    de=[]
    i=0
    while i<len(nums):
            if abs(nums[i])>len(nums):
                pass
            elif nums[abs(nums[i])-1]>=0:
                nums[abs(nums[i])-1]=nums[abs(nums[i])-1]*-1
            i+=1
    for i in range(len(nums)):
        if nums[i]>0:
            de.append(i+1)

    return de    



if __name__=="__main__":
    testcases=[[4,3,2,7,8,2,3,1],
                [1,7],
                [3,9],
                [7,1,4,3],
                [6,2,1,7,4,9],
                []]
    for i in testcases:
        print(findDisappeardNumbers(i))



# nums=[4,3,2,7,8,2,3,1]
# print(findDisappeardNumbers(nums))





