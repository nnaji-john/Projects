#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Ignore warnings

import warnings
warnings.filterwarnings("ignore") # This is to ignore any warnings that might pop up during execution


# In[3]:


import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import plotly.express as px
import seaborn as sns
from scipy import stats

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

np.random.seed(42)


# In[5]:


# Loading CSV Data
california_tax_data = pd.read_csv('C:/Users/johnp/Python Hult/Retiree/california_tax.csv')
federal_tax_data = pd.read_csv('C:/Users/johnp/Python Hult/Retiree/federal_tax.csv')
massachusetts_tax_data = pd.read_csv('C:/Users/johnp/Python Hult/Retiree/massachussetts.csv')
inflation_rate_data = pd.read_csv('C:/Users/johnp/Python Hult/Retiree/inflation_rate.csv')
rmd_data = pd.read_csv('C:/Users/johnp/Python Hult/Retiree/rmd.csv')


# In[6]:


import os
print(os.getcwd())

