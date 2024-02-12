def rotation(arr,key):
    n=len(arr)
    key=key % n
    arr=arr[-key:] + arr[:-key]
    print(arr)

arr=[1,2,3,4,5,6,7]
key=2
rotation(arr,key)
