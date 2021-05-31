

# def merge(nums1,m,nums2,n):
#     i=0  
#     while i<n:
#         j=0
#         while j<=m:
#             if nums2[i]<=nums1[j]:
#                 nums1.insert(j,nums2[i])
#                 i+=1
#                 j+=2
#             else:
#                 j+=1
#         if nums2[i]>nums1[j-1]:
#             nums1.append(nums2[i])
#             i+=1
            
#     return nums1

# print(merge([4,5,6],3,[1,2,8],3))




# def merge(nums1,m,nums2,n):
#     nums1=nums1[:m]
#     nums2=nums2[:n]
#     if len(nums1)==0:
#         return nums2
#     if len(nums2)==0:
#         return nums1
#     else:
#         i=0
#         j=0
#         while i<len(nums1) and j<n:     
#             if nums1[i]>=nums2[j]:
#                 nums1.insert(i,nums2[j])
#                 i+=1
#                 j+=1
#             else:
#                 i+=1
#         if j!=n and nums1[i-1]<nums2[j]:
#             nums1=nums1+nums2[j:]
            
#         return nums1

# print(merge([1,2,3,0,0,0],3,[2,5,6],3))
# if __name__=="__main__":
#     testcases=[[1,2,3],[2,5,6],
#                 [2,3,8],[4,7,9],
#                 [1,2,5,6,8],[1,3,4,7,9],
#                 [1,2,5,6,8],[1,4,7],
#                 [1,2,5,6,8,10,13,16,17,19,21,23],[1,3,4,7,9,10,13,16,17,90,98,205],
#                 [1,2],[],
#                 [1,3,4,6,8]]
#     for i in range(len(testcases)-1):
#         print(merge(testcases[i],len(testcases[i]),testcases[i+1],len(testcases[i+1])))




def merge(nums1,m,nums2,n):

    last =m+n-1
    while m>0 and n>0:
        if nums1[m-1]>nums2[n-1]:
            nums1[last]=nums1[m-1]
            m-=1
        else:
            nums1[last]=nums2[n-1]
            n-=1
        last-=1
    while n>0:
        nums1[last]=nums2[n-1]
        n,last=n-1,last-1

    return nums1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))

