#!/usr/bin/env python
# coding: utf-8

# In[12]:


import csv


# In[13]:


f=open('c:\\sqlite3\\csv\\student.csv','w',newline='')


# In[14]:


w=csv.writer(f)


# In[15]:


header=['ID','NAME','CITY','CONTACT']
w.writerow(header)


# In[16]:


line=[[1,'Heer','Tarsadi',9087658976],[2,'Hanee','Mota',8789765543],[3,'Riya','Sarbhon',9854345654],[4,'Hiyaaa','Surat',9876543234],[5,'Krishna','Navsari',9878987677]]
w.writerows(line)


# In[ ]:




