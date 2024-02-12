def choclate_dirstribution(choclate,student):
    if student > len(choclate):
        print("Invalid!!")
    choclate.sort()
    min_diff=choclate[student-1] - choclate[0]
    for i in range(1,len(choclate)-student +1):
        diff=choclate[i+student - 1] - choclate[i]
        if diff<min_diff:
            min_diff = diff
    return min_diff

choclate=[3,4,1,9,56,7,9,12]
student = 5
min_diff=choclate_dirstribution(choclate,student)
print("The Minimum Difference will be :",min_diff)
