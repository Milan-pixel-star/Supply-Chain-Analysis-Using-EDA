#!/usr/bin/env python
# coding: utf-8

# ## Supply chain project

# In[10]:


import numpy as np
import pandas as pd


# In[11]:


df=pd.read_csv("F:\\New folder\\ML\\CSV files\\supply_chain.csv")
df


# In[12]:


df.head()


# In[13]:


import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"


# In[14]:


df.describe()


# ## Analyzing the Supply Chain by looking at the relationship between the price of a products and the revenu generated by them

# In[15]:


fig = px.scatter(df, x='Price',
                y='Revenue generated',
                color='Product type',
                hover_data=['Number of products sold'],
                trendline='ols')
fig.show()


# ## Thus, the company drives more revenue from skincare products, and the higher the price of skincare products, the more revenue the generate. Now let's have a look at the sales by product type:

# In[16]:


sales_data=df.groupby('Product type')['Number of products sold'].sum().reset_index()  # to make terminal data in a dataframe

pie_chart=px.pie(sales_data, values='Number of products sold',
                names='Product type',
                title='Sales of product type',
                hover_data=['Number of products sold'],
                hole=0.5,
                color_discrete_sequence=px.colors.qualitative.Pastel)
pie_chart.update_traces(textposition='inside',textinfo='percent+label')
pie_chart.show()


# ## So 45% of the business comes from skincare products, 29.5% from haircare, and 25.5% from cosmetics. Now let's have a look at the total revenue generated by the shipping carriers:

# In[17]:


total_revenue=df.groupby('Shipping carriers')['Revenue generated'].sum().reset_index()
fig = go.Figure()
fig.add_trace(go.Bar(x=total_revenue['Shipping carriers'],   # add trace for plotting the columns
                    y=total_revenue['Revenue generated']))
fig.update_layout(title='Total Revenue by shipping carrier',   # update_layout is done for formating the bar graph
                 xaxis_title='Shipping Carrier',
                 yaxis_title='Revenue generated')
fig.show()


# ## So the company is using three carriers for trasportation, and carrier B helps the company in generating more revenue. Now let'sl have a look at the Average lead time and average manufacturing cost for all the products of the company

# In[19]:


avg_lead_time = df.groupby('Product type')['Lead time'].mean().reset_index()
# avg_lead_time
avg_manufacturing_costs = df.groupby('Product type')['Manufacturing costs'].mean().reset_index()
result = pd.merge(avg_lead_time, avg_manufacturing_costs, on='Product type')
result.rename(columns={'Lead time': 'Average Lead Time', 
                       'Manufacturing costs': 'Average Manufacturing Costs'}, inplace=True)
print(result)


# ## Analyzing SKUs

# There's a column in the dataset as SKUs. You must have heard it for very first time. So, SKUs stands for stock keeping unit. THere are like special codes that help companies keep track of all the different things for sale. Imagine you have a large toy store with lots of toys. Each toy is different and has its name and price, but when you hae to know how many have left, you need a way to identify them. So, you give each toy a unique code, like a secrete number only a store knows. This secrete number is called SKUs.
# 

# In[20]:


revenue_chart=px.line(df,x='SKU',
                     y='Revenue generated',
                     title='Revenue generated by SKUs')
revenue_chart.show()


# ## There's another column in the dataset as stock levels. stock levels refer to the number of products a store or bunsiness has in its inventory. Now let's have a look at the stock level of each SKUs

# In[21]:


stock_chart=px.line(df,x='SKU',
                     y='Stock levels',
                     title='Stock levels by SKUs')
stock_chart.show()


# ## Now let's have a look at the order quantity of each SKU:

# In[22]:


order_quantity_chart=px.bar(df,x='SKU',
                     y='Order quantities',
                     title='Order Quantity by SKUs')
order_quantity_chart.show()


# ## Cost Analysis

# Now lets's analyze the shipping cost of carriers:

# In[23]:


shipping_cost_chart=px.bar(df,x='Shipping carriers',
                     y='Shipping costs',
                     title='Shipping cost by carriers')
shipping_cost_chart.show()


# ## In one of the above visualizaions, we discovered that carrier B helps the company in morre revenue. It is also the most costly carrier among the three. Now let'e have a look at the cost distribution by the transpotation mode:

# In[24]:


transportation_chart=px.pie(df,values='Costs',
                     names='Transportation modes',
                     title='Cost distributoion of transportation mode',
                           hole=0.5,
                           color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# ## So the company spends more on Rosd and Rail modes of transportation for the transportation of goods.

# ## Analyzing Defect Rate

# The defect rate in the supply chain refers to the percentage of products that have somthing wrong or are found brocken after shipping. Let's have a look at the average defect rate of all product types

# In[26]:


defect_rates_by_product = df.groupby('Product type')['Defect rates'].mean().reset_index()

fig = px.bar(defect_rates_by_product, x='Product type', y='Defect rates',
             title='Average Defect Rates by Product Type')
fig.show()


# # So the defect rate of haircare products is higher. Now let’s have a look at the defect rates by mode of transportation:

# In[27]:


pivot_table = pd.pivot_table(df, values='Defect rates', 
                             index=['Transportation modes'], 
                             aggfunc='mean')

transportation_chart = px.pie(values=pivot_table["Defect rates"], 
                              names=pivot_table.index, 
                              title='Defect Rates by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# # Road transportation results in a higher defect rate, and Air transportation has the lowest defect rate.
# 
# So this is how you can analyze a company’s supply chain using the Python programming language.

# In[ ]:




