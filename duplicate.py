#First solution for the problem.
def containduplicate(nums):
        seen=set()
        for num in nums:
                if num in seen:
                        return True
                seen.add(num)
        return False
nums=[1,2,3,4,5,1]
results=containduplicate(nums)
if results==True:
        print("The array contains duplicates.")
if results==False:
        print("The array have distinct")
#Second solution for the problem.
def containduplicates(nums):
        nums.sort()
        for i in range(len(nums)-1):
                if nums[i]==nums[i+1]:
                        print(nums,"Contains duplicate.")
        else :
                print(nums,"are distinct.")

nums=[]
n=int(input("Enter the limit for an array :"))
for i in range(n):
        l=int(input())
        nums.append(l)

print(nums)
containduplicates(nums)
#Third solution for the problem.

def containduplicates(nums):
        list(nums)==set(nums)
        if nums==set():
                print(nums,"is distinct.")
        else:
                print(nums," Has a duplicate value.")

nums=[]
n=int(input("Enter the limit for an array :"))
for i in range(n):
        l=int(input())
        nums.append(l)
containdupliates(nums)

#fourth solution for the question.
def duplicate():
    array=[]
    n=int(input("Enter the Limit :"))
    for i in range(n):
        array_input=int(input(f"Enter the {i+1} Input :"))
        array.append(array_input)
    print(array)
    unique_elements=set(array)
    if len(unique_elements)==len(array):
        print("The Array Don't contains Duplicate.")
    else:
        print("The Array Contains Duplicate.")


                
