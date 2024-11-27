#!/usr/bin/env python
# coding: utf-8

# In[5]:


import openai


# Essa forma funciona, mas deixa a key exposta no código

# In[8]:


myKey = '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'

client = openai.Client(api_key=myKey)

