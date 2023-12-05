#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np    #I want to get the m and b values that make the line is best fit line
''' *          *                m = m_current - learning_rate * md     => md->the Calculus of cost equation by m
     *        *                 b = b_current - learning_rate * bd    => bd->the Calculus of cost equation by b
      *      *
       *    *
        *  *
          * '''
import matplotlib.pyplot as plt
def gradient_desent(x,y):
    m_current = 0
    b_current = 0 
    iteration = 100000
    n = len(x)
    learning_rate = 0.0001
    for i in range(iteration):
        #y_pred = mx+b  this equation to find the best fit line
        y_pred = m_current*x+b_current
        #cost =1/n sum i--->n (y-ypred)^2how to calculate the error
        cost = (1/n)*sum(val**2 for val in(y-y_pred)) #y-y_pred = y-(mx+b)
        md = (-2/n)*sum(x*(y-y_pred)) #y-y_pred = d/dm[y-(mx+b)]
        bd = (-2/n)*sum(y-y_pred) #y-y_pred = d/db[y-(mx+b)]
        m_current = m_current - learning_rate * md 
        b_current = b_current - learning_rate * bd
#         print("m{}    ,b{}      ,cost{}    ,iteration {}    ".format(m_current,b_current,cost,i))

#     print("m{}    ,b{}".format(m_current,b_current))
    plt.figure(figsize=(12,6) , dpi = 90)
    plt.plot(x,y_pred , c ='r' , linewidth = 2)
    plt.scatter(x,y)
    plt.ylim(ymin = 0 , ymax = 15)
    plt.xlim(xmin = 0 , xmax = 15)
    plt.title('linear regression')
    plt.show()
    print("m{}      ,b{}      ,cost{}  ".format(m_current,b_current,cost))
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,4,2,4,6,4,3,2,5,11])
gradient_desent(x,y)              


# In[ ]:





# In[ ]:




