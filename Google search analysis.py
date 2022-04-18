#!/usr/bin/env python
# coding: utf-8

# # Installing PYTRENDS

# In[1]:


get_ipython().system('pip install pytrends   ')


# # importing necessary libraries

# In[2]:


import pandas as pd                    #for analysing data
from pytrends.request import TrendReq  #get the dataframe from google api
import matplotlib.pyplot as plt        #to visulize the data
trends=TrendReq()


# # getting keyword from the user and displaying its trend-country wise

# In[4]:


key=input("ENTER THE KEYWORD TO GET THE DATA: ")
trends.build_payload(kw_list=[key])                # Preparing Keywords to get the data for
data = trends.interest_by_region()                 # Returns data for where the keyword is most searched
data = data.sort_values(by=key, ascending=False)   #displays the dataframe in a table
data = data.head(10)                               #displays the first 10 data with their corresponding values
print(data)                                        


# # plotting it in a bar graph

# In[5]:


data.reset_index().plot(x="geoName", y=key, figsize=(25,15), kind="bar")  #assigning values to x and y axis
plt.style.use('fivethirtyeight')                                          #choosing the graph sheet style
plt.show()                                                                # visualizing the data


# # plotting the line graph based on the trend for the last 5 years

# In[6]:


data = TrendReq(hl='en-US', tz=360)                 #importing dataframe from google api
data.build_payload(kw_list=[key])                   
data = data.interest_over_time()                    #Returns historical, indexed data
fig, ax = plt.subplots(figsize=(25, 15))
data[key].plot()                                    #plotting the graph for the keywords
plt.style.use('fivethirtyeight')
plt.title(f'Total Google Searches for {key}', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()                                         # visualizing the data


# In[ ]:




