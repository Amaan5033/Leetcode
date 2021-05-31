

def findNumbers(nums):
    i=0
    evendigits=0
    while i<len(nums):
        if len(str(nums[i]))%2==0:
            evendigits+=1
        i+=1
    return evendigits


nums=[555,901,482,1771]
print(findNumbers(nums))

