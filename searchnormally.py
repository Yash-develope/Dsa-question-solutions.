arr=[]
Limit=int(input("Enter the Limit of the array :"))
for i in range(Limit):
    Element=int(input(f'Enter the {i+1}st Element of the array :'))
    arr.append(Element)
print(arr)

def search(arr,Element):
    for i in range(len(arr)):
        if arr[i]==Element:
            print(f'The {Element} is at {i} index.')
Element=int(input("Enter the Element which has to be searched :"))
search(arr,Element)
    
