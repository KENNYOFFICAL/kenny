#!/usr/bin/env python
# coding: utf-8

# In[1]:


#3
import streamlit as st
st.header("'temperature conversion'")
st.write ("'**Change Celcius to Fahrenheit**'")
number = st.number_input("enter the value of temperature in Celcius")
C = ((number * (9/5))+32)
st.write (C,"°F")


# In[ ]:




