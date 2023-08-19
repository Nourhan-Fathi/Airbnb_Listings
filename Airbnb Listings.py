#!/usr/bin/env python
# coding: utf-8

# Exploratory Data Analysis of Airbnb Listings

# In[4]:


pip install folium


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium


# In[7]:


# Load the dataset
data = pd.read_csv('listings.csv')

# Get the column names
column_names = data.columns

print(column_names)


# In[8]:


data.info()


# In[9]:


# Data Preprocessing
# Handle missing values
data.dropna(subset=['price', 'availability_365', 'latitude', 'longitude', 'room_type'], inplace=True)

# Data Exploration and Visualization
summary_stats = data.describe()
correlation_matrix = data.corr()

# Price Analysis
plt.figure(figsize=(10, 6))
sns.histplot(data['price'], bins=30, kde=True)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='room_type', y='price', data=data)
plt.title('Price Variation by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()

# Availability Analysis
# You can use time series analysis techniques here

# Location Analysis
plt.figure(figsize=(12, 8))
m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=12)
for index, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)
m.save('map.html')

# Room Type Analysis
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='room_type')
plt.title('Distribution of Room Types')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Statistical Analysis
# You can perform hypothesis testing or regression analysis here

# Print Insights and Conclusions
print("Summary Statistics:\n", summary_stats)
print("Correlation Matrix:\n", correlation_matrix)

# Save the visualizations and results in the notebook

# Remember to adapt and modify the code according to your dataset and specific analysis requirements.


# In[ ]:




