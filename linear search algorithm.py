def linearsea(ar,lim,fin):
    for i in range(len(ar)):
        if fin==ar[i]:
            return i
    return -1
ar=[]
lim=int(input("Enter the Limit of the array :"))
for i in range(lim):
    inp=int(input(f'Enter the {i+1}st element of the array :'))
    ar.append(inp)

print(ar)
fin=int(input("Which Element you want to find :"))


res=linearsea(ar,lim,fin)
if(res != -1):
    print(f'Element found at {res} Index')
else:
    print(f'Element not Found in the array')
