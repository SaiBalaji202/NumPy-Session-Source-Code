#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# ## Creating Arrays

# In[6]:


arr = np.array([1, 2, 3])
arr.ndim


# In[5]:


arr = np.array([
    [1, 2, 3], 
    [3, 5, 7]
])
arr.ndim


# In[7]:


arr = np.array( [
    [
        [1, 2, 3], 
        [4, 5, 6]
    ], 
    [
        [1, 2, 3], 
        [4, 5, 6]
    ]
]
)
arr.ndim


# In[11]:


np.zeros((4, 2, 3), dtype=int)


# In[12]:


np.ones((2, 4))


# In[13]:


np.full((5, 5), 100)


# In[16]:


np.arange(5, 10, 2)


# In[18]:


np.linspace(1, 10, 50)


# In[19]:


np.eye(4)


# ## Pseudo-Random Numbers 

# In[29]:


np.random.seed(44)
np.random.rand(5, 2)


# In[21]:


np.random.randn(5)


# In[22]:


np.random.randint(1, 10, (3, 3))


# In[27]:


np.random.seed(14)
np.random.randint(1, 10, (3, 3))


# In[40]:


np.random.seed(0)
print(np.random.randn(5))
np.random.seed(0)
print(np.random.randn(5))
print(np.random.randn(5))
print(np.random.randn(5))


# In[33]:


np.random.randn(5)


# In[41]:


arr = np.random.randn(5)


# ## Attributes and Methods

# In[42]:


arr.dtype


# In[43]:


np.random.randint(1, 10, (3, 3)).dtype


# In[44]:


np.random.randint(1, 10, (3, 3)).ndim


# In[45]:


arr = np.random.randint(1, 10, (5, 3))


# In[46]:


arr


# In[47]:


arr.shape


# In[50]:


np.random.randint(1, 100, 8).reshape(4, 3)


# In[53]:


np.random.randint(1, 100, 8).reshape(4, 2).T


# In[54]:


arr


# In[56]:


arr.max(axis=1)


# In[58]:


arr.argmin(axis=1)


# In[59]:


arr.argmax(axis=1)


# In[62]:


arr.min(axis=0)


# In[63]:


arr.shape


# In[64]:


arr.itemsize


# ## Fetching Data

# In[65]:


arr = np.arange(1, 10)


# In[66]:


arr


# In[67]:


arr[3]


# In[72]:


np.random.seed(0)
arr2d = np.random.randint(1, 100, (6, 4))
arr2d


# In[74]:


arr2d[2][1]


# In[75]:


arr2d[2, 1]


# In[76]:


arr2d[2:4, 1:3]


# In[77]:


arr2d[-2:, :]


# In[83]:


arr2d[[3, 1, 5]]


# In[81]:


arr2d[(1, 3, 4)]


# In[84]:


arr  = np.arange(1, 11)


# In[85]:


arr


# In[86]:


arr[arr >= 5]


# In[87]:


arr >= 5


# In[88]:


arr[arr > 10]


# ## Arithmetic Operations

# In[91]:


arr1 = np.random.randint(1, 4, 5)
arr1


# In[92]:


arr2 = np.random.randint(1, 10, 5)
arr2


# In[93]:


arr1 + arr2


# In[94]:


arr1 - arr2


# In[95]:


arr1 * arr2


# In[97]:


arr1 = np.arange(1, 7).reshape(3, 2)
arr2 = np.arange(1, 7).reshape(3, 2)


# In[98]:


arr1, arr2


# In[99]:


arr1 + arr2


# In[101]:


arr2 = np.arange(1, 5).reshape(2, 2)
arr2


# In[102]:


arr1 + arr2


# In[103]:


arr2 = np.array([1, 2])


# In[104]:


arr1.shape, arr2.shape


# In[105]:


arr1 + arr2


# In[108]:


arr1 = np.array([1, 2, 3]).reshape(3, 1)
arr2 = np.array([1, 2, 3])


# In[109]:


arr1


# In[110]:


arr2


# In[111]:


arr1+ arr2


# In[112]:


# (3, 1) (1, 3)

# arr1 => (3, 3)
# arr2 => (3, 3)

# arr1 =>
# [
#     [1, 1, 1], 
#     [2, 2, 2], 
#     [3, 3, 3]
# ]

# arr2 =>
# [
#     [1, 2, 3], 
#     [1, 2, 3], 
#     [1, 2, 3]
# ]


# In[113]:


arr1 = np.zeros((4, 2))
arr2 = np.ones((4, 3))
arr1 + arr2


# In[114]:


arr1 = np.arange(1, 5)


# In[115]:


arr1


# In[116]:


arr1 + 2


# In[117]:


arr1 = np.arange(5)
arr2 = np.arange(5)
arr1 / arr2


# In[118]:


1/ 0


# ## Copy Data

# In[130]:


arr1 = np.arange(5)
arr2 = arr1.copy()
arr1, arr2


# In[131]:


arr2[0] = 10


# In[132]:


arr2


# In[133]:


arr1


# In[124]:


l1 = [1, 2, 3]
l2 = l1[:]
l2[1] = 5
l1, l2


# In[137]:


arr1 = np.arange(5)
arr2 = arr1[0:2].copy()
arr1, arr2


# In[138]:


arr2[0] = 5
arr1, arr2


# ## Mathematical Functions

# In[139]:


arr1


# In[140]:


arr1.sqrt()


# In[141]:


np.sqrt(arr1)


# In[142]:


np.exp(arr1)


# In[143]:


np.sin(arr1)


# In[11]:


# For More Mathematical Functions - https://numpy.org/doc/stable/reference/routines.math.html


# ## Dot Product and Transpose

# In[144]:


arr1 = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])


# In[146]:


arr1 * arr1


# In[148]:


arr1.dot(arr1.T)


# ## Sorting

# In[5]:


arr1 = np.array([5, 4, 9, 1, 2])


# In[150]:


np.sort(arr1)


# In[6]:


np.sort(arr1)[::-1] # Sorting in Reverse Order


# In[9]:


arr1 = np.array([
    [11, 8, 3], 
    [1, 0, 16]
])
np.sort(arr1)


# In[10]:


np.sort(arr1)[:,::-1] # Sorting in Reverse Order


# ## Convert Image to NumPy Array

# In[158]:


from matplotlib.image import imread


# In[159]:


kitten = imread('images/a.jpg')


# In[161]:


type(kitten)


# In[162]:


kitten


# In[166]:


kitten.ndim, kitten.size


# In[164]:


arr1 = np.arange(0, 10)


# In[165]:


arr1.size


# In[ ]:




