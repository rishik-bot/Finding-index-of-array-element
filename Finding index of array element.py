#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Find the index of asked element (in our case 100th) in the array, given the shape of the array (in our case 11*12).

#np.unravel_index(99, (11,12)) --> Shortcut

arr_1=np.arange(1,133,dtype=int).reshape(11,12)
print(arr_1)
n=int(input("Enter the element number: "))
a=arr_1.shape[0]
b=arr_1.shape[1]
row=(int(n/a))-1
column=(n-((row)*b)-1)
print(row,",",column)

