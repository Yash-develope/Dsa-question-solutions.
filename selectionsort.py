def selsor(arr):
    n=len(arr)
    for i in range(n-1):
        minindex=i
        for j in range(i+1,n):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr


arr=[]
n=int(input("Enter the length of the array :"))
for i in range(n):
    ele=int(input(f"Enter the {i+1}st Element of the array :"))
    arr.append(ele)

print(arr)
print('The unsorted array will be :',selsor(arr))
