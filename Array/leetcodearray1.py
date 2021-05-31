

# def findmaxConsecutiveOnes(nums):
#     maxOne=[]
#     count=0
#     i=0
#     flag=True
#     while i<len(nums):
#         if flag and nums[i]==0:
#             i+=1
#             continue
#         elif nums[i]==1:
#            flag=False
#            count+=1
#         else:
#             maxOne.append(count)
#             flag=True
#             count=0
#         i+=1
#     if nums[-1]==1:
#         maxOne.append(count)

#     return maxOne
        

# # nums=[0,0,1,1,0,0,1,1,1,1,1]
# print(findmaxConsecutiveOnes(nums))



def findmaxConsecutiveOnes(nums):
    set_matrix=[]
    max,i,a,flag=0,0,0,False
    while i<len(nums)-1:
        if nums[i]==0 and nums[i+1]==0:
            i+=1
            if flag==True:
                if set_matrix[a][-1]!=0:
                    set_matrix[a].append(nums[i])
            else:
                continue                
        elif nums[i]==0 and nums[i+1]==1:
            set_matrix.append([nums[i],nums[i+1]])
            i+=2
            if flag!=False:
                a+=1
        elif nums[i]==1:
            flag=True
            try:
                set_matrix[a].append(nums[i])
            except:
                set_matrix.append([])
                set_matrix[a].append(nums[i])
            i+=1
        else:
            pass
    if nums[-1]==1 and i!=len(nums):
        set_matrix[a].append(nums[i])
    for i in range(len(set_matrix)-1):
        saved=set_matrix[i+1]
        if set_matrix[i][-1]==0 and set_matrix[i+1][0]==0:
            continue
        else:
            set_matrix[i]=set_matrix[i]+saved
    sum_matrix=0
    for i in range(len(set_matrix)):
        if len(set_matrix[i])>max or sum(set_matrix[i])>sum_matrix:
            max=len(set_matrix[i])
            sum_matrix=sum(set_matrix[i])
    
    return sum_matrix+1

# nums=[0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1]
# print(findmaxConsecutiveOnes(nums))

if __name__=="__main__":
    testcases=[[1,0,1,1,0],
                [1,1,0,0,1,1,0,0,0,1,1,1],
                [0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1],
                [0,0,0,1,1,1,0,1,1,1,1,1],
                [0,0,1,1,1,0,1,1,0,1,1,1,0,1]]
    for i in testcases:
        print(findmaxConsecutiveOnes(i))
