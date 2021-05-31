


# def sortedSquares(nums):
#     sorted_array=[]
#     for i in range(len(nums)):
#         nums[i]=pow(nums[i],2)
#     sorted_array.append(nums[0])
#     j=1
#     k=0
#     while j<len(nums):
#         if nums[j]<=sorted_array[k]:
#             sorted_array=[nums[j]]+sorted_array
#             j+=1
#             k=0
#         elif nums[j]>sorted_array[k]:
#             try:
#                 if nums[j]>sorted_array[k+1]:
#                     k+=1
#                 else:
#                     sorted_array=sorted_array[:k+1]+[nums[j]]+sorted_array[k+1:]
#                     j+=1
#                     k=0
#             except:
#                 sorted_array.append(nums[j])
#                 j+=1
#         else:
#             pass
#     return sorted_array


# if __name__=="__main__":
#     testcases=[[-4,-1,0,3,10],
#                [-7,-3,2,3,11],
#                [-8,0,-2,0,-4,3,-3],
#                [2,6,1,0,3,2,5]
#                ]
#     for i in testcases:
#         print(sortedSquares(i))



def SortedSquares(nums):
    sorted_array=[]
    left_index=0
    right_index=len(nums)-1
    i=0
    while i<len(nums):
        if left_index==right_index:
            sorted_array=[pow(nums[left_index],2)]+sorted_array
            break
        if pow(nums[left_index],2)>pow(nums[right_index],2):
            sorted_array=[pow(nums[left_index],2)]+sorted_array
            left_index+=1
        else:
            sorted_array=[pow(nums[right_index],2)]+sorted_array
            right_index-=1
    return sorted_array


nums=[-7,-3,2,3,11]
print(SortedSquares(nums))

# if __name__=="__main__":
#     testcases=[[-4,-1,0,3,10],
#                [-7,-3,2,3,11],
#                [-8,-4,-2,0,3,9],
#                [-9,-2,1,4,8,10]
#                ]
#     for i in testcases:
#         print(SortedSquares(i))