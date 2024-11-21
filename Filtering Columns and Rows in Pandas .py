#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Filtering Columns and Rows in Pandas 


# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv (r"C:\Users\lucas\Desktop\Programacion 2019\Phyton\C:\Users\lucas\Desktop\Programacion 2019\Phyton\Filtering Columns and Rows.Group By and Aggregate Functions in Pandas\world_population.csv")


# In[5]:


df


# In[11]:


df[df["Rank"]< 10]


# In[13]:


# For filtering we can create a variable, and use it to contain the data we are looking
specific_countries = ["Russia", "Nigeria"]


# In[19]:


# we use ISIN for filtering the exact data
df[df["Country"].isin (specific_countries)]


# In[21]:


# STR.CONTAINS we use it for searchin data in STRING FORMAT that contains certain values between ()
df[df["Country"].str.contains ("United")]


# In[27]:


# we change the index to Country in a new variable
df2 = df.set_index("Country")
df2


# In[31]:


# we use the FILTER() for a search of an specific value
df2.filter(items = ["Continent", "Country"])


# In[35]:


df2.filter(like = "Arg", axis = 0)


# In[37]:


# we use LOC for a specific and literall value
df2.loc["United States"]


# In[47]:


# we SORT the values we want to using the function sort_values
df[df["Rank"]< 10].sort_values(by="Rank", ascending = True)


# In[ ]:


# INDEXING


# In[ ]:


# here we set the INDEX in the Country col. 
df.set_index("Country")


# In[63]:


df


# In[65]:


# We use LOC for an exact mach
df.loc["Albania"]


# In[67]:


# we use ILOC for and INTEGER LOCATION of the index or position
df.iloc[4]


# In[69]:


# now we RESET THE INDEX
df.reset_index(inplace = True)


# In[71]:





# In[77]:


# we can set 2 diferent INDEX, but its important the gerarchy in wich they are called
df.set_index(["Continent", "Country"], inplace=True)


# In[79]:


df


# In[81]:


# we can SORT the data
df.sort_index()


# In[ ]:


# Group By and Aggregate Functions in Pandas 


# In[ ]:


# we create a variable and insert the values of the group by


# In[23]:


group_by_frame = df.groupby("1970 Population")


# In[25]:


group_by_frame.min()


# In[ ]:


# group_by_frame.mean() for Average integer value


# In[ ]:


# group_by_frame.max() for the max integer value


# In[ ]:


# group_by_frame.min() for the min integer value


# In[ ]:


# group_by_frame.sum() for summary integers


# In[ ]:


# AGGREGATE FUNCTIONS
# group_by_frame.sum().agg({"1970 Population": ["mean","max","min","sum","count"]})


# In[ ]:


# DESCRIBE FUNCTION
# group_by_frame.describe()


# In[ ]:





# In[ ]:




