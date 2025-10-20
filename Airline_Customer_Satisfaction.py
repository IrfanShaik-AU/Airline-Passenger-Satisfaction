#!/usr/bin/env python
# coding: utf-8

# In[10]:


# importing packages


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


# Loading Data

Data_Set = pd.read_csv("D:\Assignments\sem\Airline Passenger Satisfaction.csv")


# In[12]:


# Printing first 5 rows

Data_Set.head()


# In[13]:


# Descriptive statistics

Summary = Data_Set.describe()


# In[14]:


Summary


# In[15]:


# Data types

Data_Set.info()


# In[16]:


# seaborn style

sns.set(style="whitegrid")


# In[19]:


# 1. Class vs. Satisfaction

plt.figure(figsize=(8, 5))
sns.countplot(data = Data_Set, x='Class', hue='satisfaction')
plt.title('Class vs. satisfaction')
plt.xlabel('Class')
plt.ylabel('Count')
plt.legend(title='satisfaction')
plt.tight_layout()
plt.show()


# In[21]:


# 2. Inflight Wifi Service vs. Satisfaction

plt.figure(figsize=(8, 5))
sns.boxplot(data = Data_Set, x='satisfaction', y='Inflight wifi service')
plt.title('Inflight wifi service vs. satisfaction')
plt.xlabel('satisfaction')
plt.ylabel('Inflight Wifi Service Rating')
plt.tight_layout()
plt.show()


# In[36]:


# 3.  Online Boarding vs. Satisfaction
plt.figure(figsize=(8, 5))
sns.boxplot(data = Data_Set, x='satisfaction', y='Online boarding')
plt.title('Online Boarding vs. Satisfaction')
plt.xlabel('Satisfaction')
plt.ylabel('Online Boarding Rating')
plt.tight_layout()
plt.show()


# In[25]:


# 4. Flight Distance vs. Satisfaction

plt.figure(figsize=(8, 5))
sns.boxplot(data = Data_Set, x='satisfaction', y='Food and drink')
plt.title('Food and drink vs. Satisfaction')
plt.xlabel('satisfaction')
plt.ylabel('Food and drink')
plt.tight_layout()
plt.show()


# In[37]:


# 5. Arrival Delay in Minutes vs. Satisfaction
plt.figure(figsize=(8, 5))
sns.boxplot(data = Data_Set, x='satisfaction', y='Arrival Delay in Minutes')
plt.title('Arrival Delay vs. Satisfaction')
plt.xlabel('Satisfaction')
plt.ylabel('Arrival Delay  in Minutes')
plt.tight_layout()
plt.show()


# In[ ]:




