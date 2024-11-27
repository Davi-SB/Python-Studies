#!/usr/bin/env python
# coding: utf-8

# In[7]:


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


# In[8]:


client = openai.Client()

