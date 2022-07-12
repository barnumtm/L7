#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing all libraries that we may need 

import pandas as pd
import datetime
import numpy as np 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


initial_data = yf.download("MRNA", start="2020-12-01", end="2021-12-31") 
# here we are downloading the MRNA info and naming it intiaitla data to work later 

