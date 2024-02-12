#start
#Take an empty string arr
arr=[]
#take the range of the array as the input
lim=int(input("Enter the limit :"))
for i in range(lim):
    inp=int(input(f'Enter the {i+1}st Element :'))
    arr.append(inp)

print(arr)
# This is for ascending order let us if the array=[23,1,45,32,67] then the output will be the array=[1,23,32,45,67]
def bbblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(f'{i+1}st pass will be after completion :{arr}')
    print(f'So the sorted array will be :{arr}')

bbblesort(arr)
#This is for descending sort let us if the array will be =[23,1,45,32,67] then the output will be the array=[67,45,32,23,1]

def descendingbbblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(f'{i+1}st pass will be after completion :{arr}')
    print(f'So the sorted array will be :{arr}')

descnedingbbblesort(arr)

