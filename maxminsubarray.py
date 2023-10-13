def maxSubArray(arr):
        cur_sum=0
        max_so_far=arr[0]
        st=0
        end=0
        poi=0
        for i in range(0,len(arr)):
            cur_sum=cur_sum+arr[i]
            if (max_so_far<cur_sum):
                max_so_far=cur_sum
                st=poi
                end=i
            if cur_sum<0:
                cur_sum=0
                poi=i+1
        print("The maximum of subarray is",max_so_far)
        print("Start Index of window is ",st)
        print("End Index of Window is ",end)
        arr=arr[st:end]
        print("The subarray is :",arr)
L=[]
n=int(input("Enter the Limit :"))
for i in range(0,n):
    l=int(input("Enter the element :"))
    L.append(l)
print(L)
maxSubArray(L)
