#First solution by sorting
def maxminarray(arr): #Declared function
    arr=[]
    n=int(input("Enter the limit for an array :"))   #Taking input
    for i in range(n):
        l=int(input("Enter the {} Element of an array :".format(i))) #accessing the elements
        arr.append(l) #Adding elements into the array
    print(arr) #printing the array
    arr.sort() #sorting the array in ascending order
    minimum=arr[0] #first element will be the smallest element
    maximum=arr[-1]# last element will be the largest element
    print("For the given array ",arr," The minimum Element is :",minimum)
    print("For the given array ",arr," The maximum Element is :",maximum)
L=[]
maxminarray(L)


#Second solution by using max min function
def maxminarray(arr):
    arr=[]
    n=int(input("Enter the limit for an array :"))   #Taking input
    for i in range(n):
        l=int(input("Enter the {} Element of an array :".format(i))) #accessing the elements
        arr.append(l) #Adding elements into the array
    print(arr) #printing the array
    maximum=max(arr)
    minimum=min(arr)
    print("Maximum is",maximum)
    print("Minimum is",minimum)
L=[]
maxminarray(L)
#third solution by using linear search algorithm
def maxminarray(arr):
    min_value=arr[0]
    max_value=arr[0]
    for i in arr:
        if i>max_value:
            max_value=i
        if i<min_value:
            min_value=i
    return min_value,max_value
    
arr=[]
n=int(input("Enter the limit for an array :"))   #Taking input
for i in range(n):
    l=int(input("Enter the {} Element of an array :".format(i))) #accessing the elements
    arr.append(l) #Adding elements into the array
print(arr) #printing the array
min_value,max_value=maxminarray(arr)
print("Maximum is :",max_value)
print("Minimum is :",min_value)






        
