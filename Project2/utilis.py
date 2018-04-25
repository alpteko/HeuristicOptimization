
# coding: utf-8

# In[92]:


import numpy as np


# In[93]:


def load_data():
    data = np.loadtxt('data.txt')
    data = data[:,0:2]
    return data


# In[134]:


def init_facilities(k):
    data= load_data()
    solution =  []
    T = len(data)
    mask = np.random.randint(k,size=T)
    for i in range(k):
        ind = list(np.where(mask==i)[0])
        solution.append(list(data[ind,:]))
    return solution

