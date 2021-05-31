

def heightChecker(heights):
    sorted_heights=sorted(heights)
    i=0
    moved_students=0
    while i<len(heights):
        if heights[i]!=sorted_heights[i]:
            moved_students+=1
        i+=1
    return moved_students


heights=[1,1,4,2,1,3]

print(heightChecker(heights))



