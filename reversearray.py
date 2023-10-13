#First solution by reverse function
def reversearray(arr):
    arr=[]
    n=int(input("Enter the range :"))
    for i in range(n):
        l=int(input("Enter the {} th element :".format(i)))
        arr.append(l)
    print(arr)
    arr.reverse()
    print(arr)
    

arr=[]
reversearray(arr)
#second solution by slicing
def reversearray(arr):
    arr=[]
    n=int(input("Enter the range :"))
    for i in range(n):
        l=int(input("Enter the {} th element :".format(i)))
        arr.append(l)
    print(arr)
    l=arr[::-1]
    print(l)

arr=[]
reversearray(arr)
    
