#!/usr/bin/env python
# coding: utf-8

# In[7]:


n=int(input("Enter the Number of Rows and Coloumns :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()


# In[6]:


n=int(input("Enter the Number of Rows and Coloumns :"))
rows=1
while rows < n+1:
    col=1
    rows+=1
    while col < n+1:
        print(col,end=' ')
        col+=1
    print()


# In[8]:


n=int(input("Enter the Number of Rows and Coloumns :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n-j+1,end=' ')
    print()


# In[12]:


n=int(input("Enter the Number of Rows and Coloumns :"))
rows=1
while rows < n+1:
    col=1
    rows+=1
    while col < n+1:
        print(n-col+1,end=' ')
        col+=1
    print()


# In[19]:


n=int(input("Enter the Number of Rows and Coloumns :"))
nums=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(nums,end=' ')
        nums+=1
    print()


# In[35]:


n=int(input("Enter the Number of Rows and Coloumns"))
nums=n*n
rows=1
while rows < n+1:
    col=1
    rows+=1
    while col < n+1:
        print(nums,end=' ')
        col+=1
        nums-=1
    print()


# In[36]:


n=int(input("Enter the Number for Rows and Coloumns :"))
for rows in range(1,n+1):
    for col in range(rows):
        print('*',end=' ')
    print()


# In[42]:


n=int(input("Enter the Number for Rows and Coloumns :"))
rows=1
while rows < n+1:
    col=1
    rows+=1
    while col < rows:
        print('*',end=' ')
        col+=1
    print()
    
    


# In[48]:


n=int(input("Enter the Number for rows and Coloumns :"))
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(rows,end=' ')
    print()
        


# In[52]:


n=int(input("Enter the Number for Rows and Coloumns :"))
rows=1
while rows < n+1:
    col=1
    while col < rows+1:
        print(rows,end=' ')
        col+=1
    rows+=1
    print()
    


# In[55]:


n=int(input("Enter the Number for Rows and COloumns :"))
nums=1
for  rows in range(1,n+1):
    for col in range(rows):
        print(nums,end=' ')
        nums+=1
    print()


# In[58]:


n=int(input("Enter the Number for rows and coloumns :"))
nums=1
rows=1
while rows < n+1:
    col=1
    rows+=1
    while col < rows:
        print(nums,end=' ')
        col+=1
        nums+=1
    print()


# In[82]:


n=int(input("Enter the Number of Rows and Coloumns :"))
for rows in range(1,n+1):
    values=rows
    for col in range(1,rows+1):
        print(values,end=' ')
        values+=1
    print()


# In[83]:


n=int(input("Enter the INput for the Rows and COLOumns :"))
rows=1
while rows <= n:
    col=1
    values=rows
    while col <= rows:
        print(values,end=' ')
        values+=1
        col+=1
    print()
    rows+=1


# In[89]:


n=int(input("Enter the Number for Rows and COloumns :"))
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(rows+col-1,end=' ')
    print()
'''
#Second approach for this out 
1 
2 3 
3 4 5 
4 5 6 7 '''


# In[102]:


n=int(input("Enter the Number for Rows and Coloumns :"))
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(rows-col+1,end=' ')
    print()


# In[111]:


n=int(input("Enter the NUmber for Rows and COloumns :"))
rows=1
while rows <= n:
    values=1
    col=1
    while col <= rows:
        print(values,end=' ')
        col+=1
        values+=1
    print()
    rows+=1


# In[30]:


n = int(input("Enter the matrix size: "))
row = 1
while row <= n:
    col = 1
    nums='A'
    while col <= n:
        print(chr(ord(nums) + row - 1), end=' ')
        col += 1
    print()
    row += 1


# In[35]:


n=int(input("Enter the Matrix Size :"))
for i in range(1,n+1):
    nums='A'
    for j in range(1,n+1):
        print(chr(ord(nums) + j - 1),end=' ')
    print()


# In[77]:


n=int(input("Enter the Matrix Number :"))
rows = 1
nums='A'
while rows <= n:
    col = 1
    while col <= n:
        print(chr(ord(nums)+col-1),end=' ')
        col += 1
    print()
    rows+=1


# ### 

# In[93]:


n=int(input("Enter the Number for the Matrix :"))
rows=1
nums='A'
while rows <= n:
    col = 1
    while col <= n:
        print(chr(ord(nums)+ rows+col-2),end=' ')
        col+= 1
    print()
    rows+=1
    


# In[87]:


n=int(input("Enter the Number for the Matrix :"))
rows=1
nums=1
while rows <= n:
    col=1
    while col <= n:
        print(nums+col -1,end=' ')
        col+=1
    print()
    nums+=col-1
    rows += 1


# In[102]:


n=int(input("Enter the Number for the Matrix :"))
rows=1
nums=ord('A')
while rows <= n:
    col=1
    while col <= n:
        print(chr(nums+col-1),end=' ')
        col+=1
    print()
    nums += col-1
    rows += 1


# In[109]:


n=int(input("Enter the Matrix :"))
rows=1
nums=ord('A')
while rows <= n:
    col =1
    while col <= n:
        print(chr(nums + rows + col -2),end=' ')
        col+=1
    print()
    rows += 1


# In[115]:


n=int(input("Enter the matrix :"))
nums=ord('A')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(nums),end=' ')
    print()
    nums+=1


# In[114]:


n=int(input("Enter the Number for the matrix :"))
nums=ord('A')
rows=1
while rows <= n:
    col=1
    while col <= rows:
        print(chr(nums),end=' ')
        col+=1
        nums+=1
    print()
    rows+=1


# In[131]:


n=int(input("Enter the Number for Rows and Coloumns :"))
nums=ord('A')
rows=1
while rows <= n:
    col=1
    while col <= rows:
        print(chr(nums+col-1),end=' ')
        col+=1
    print()
    nums+=1
    rows+=1
        


# In[152]:


n=int(input("Enter the Number for Rows and Coloumns :"))
nums=ord('D')
rows=1
while rows <= n:
    col=1
    while col <= rows:
        print(chr(nums+col-1),end=' ')
        col+=1
    print()
    nums-=1
    rows+=1
        


# In[41]:


n=int(input("Enter the Matrix :"))
rows=1
while rows <= n:
    space=n-rows
    while space:
        print(' ',end=' ')
        space-=1
    col=1
    while col <= rows:
        print('*',end=' ')
        col+=1
    print()
    rows+=1


# In[45]:


n=int(input("Enter the matrix :"))
for rows in range(1,n+1):
    for space in range(n-rows):
        print(' ',end=' ')
    for col in range(1,rows+1):
        print('*',end=' ')
    print()


# In[52]:


n=int(input("Enter the Matrix :"))
rows=1
while rows <= n:
    col=1
    while col <= n-rows+1:
        print('*',end=' ')
        col+=1
    print()
    rows+=1


# In[54]:


n=int(input("Enter the Matrix :"))
for rows in range(1,n+1):
    for col in range(0,n-rows+1):
        print('*',end=' ')
    print()
    


# In[61]:


n=int(input("enter the matrix :"))
rows=1
while rows <= n:
    spaces=rows-1
    while spaces:
        print(' ',end=' ')
        spaces-=1
    col=1
    while col <= n-rows+1:
        print('*',end=' ')
        col+=1
    print()
    rows+=1


# In[67]:


n = int(input("Enter the Matrix size: "))

for rows in range(n, 0, -1):
    for spaces in range(n - rows):
        print('  ', end='')  # Print spaces
    for col in range(rows):
        print('* ', end='')  # Print asterisks
    print()  # Move to the next line


# In[74]:


n=int(input("Enter the Matrix :"))
rows=1
nums=1
while rows <= n:
    spaces=rows-1
    while spaces:
        print(' ',end=' ')
        spaces-=1
    col=1
    while col <= n-rows+1:
        print(nums+rows-1,end=' ')
        col+=1
    print()
    rows+=1


# In[83]:


n=int(input("Enter the Matrix :"))
rows=1
nums=1
while rows <= n:
    spaces=n-rows
    while spaces:
        print(' ',end=' ')
        spaces-=1
    col=1
    while col <= rows:
        print(nums,end=' ')
        col+=1
    nums+=1
    print()
    rows+=1


# In[88]:


n=int(input("Enter the Matrix :"))
nums=1
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(' ',end=' ')
        spaces-=1
    for col in range(1,rows+1):
        print(nums,end=' ')
        nums+=1
    print()
        


# In[27]:


n=int(input("Enter the Matrix :"))
rows=1
nums=1
while rows <= n:
    spaces=n-rows
    while spaces:
        print(' ',end=' ')
        spaces-=1
    col=1
    while col <= rows:
        print(col,end=' ')
        col+=1
    start=rows-1
    while start:
        print('*',end=' ')
        start-=1
    print()
    rows+=1


# In[61]:


n=int(input("enter the matrix :"))
rows=1
nums=5
while rows <= n:
    col=1
    while col <= n-rows+1:
        print(col,end=' ')
        col+=1
    spaces=rows-1
    while spaces:
        print('*',end=' ')
        spaces-=1
    start=rows-1
    while start:
        print('*',end=' ')
        start-=1
    chalhat=n-rows+1
    while chalhat:
        print(chalhat,end=' ')
        chalhat-=1
    print()
    rows+=1


# In[ ]:





# In[ ]:




