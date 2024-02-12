'''#Understand simple 2D array.
student_dt=[ [72, 85, 87, 90, 69], [80, 87, 65, 89, 85], [96, 91, 70, 78, 97], [90, 93, 91, 90, 94], [57, 89, 82, 69, 60] ]
print(student_dt[0][0])
print(student_dt[1])
print(student_dt[2])
print(student_dt[3])

#Traversing the element
for x in student_dt:
    for i in x:
        print(i,end=' ')
    print()'''

#Inserting the Element
arr1=[[454,323,443],[45,12,48]]
print(arr1)
arr2=[54,32,21]
arr1.insert(2,arr2)
print(arr1)
for i in arr1:
    for j in i:
        print(j,end=' ')
    print()



