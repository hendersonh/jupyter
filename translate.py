#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import string

def WordData(sen):
    col_names =  ['word', 'length']
    data = pd.DataFrame(columns = col_names)
    words = sen.split()
    table = str.maketrans({key: None for key in string.punctuation})
    words = [ word.translate(table) for word in words]
       
    print(words)
"""
    d = data["word"].str.replace(r'[()]', '' )
    data["length"] = d['word'].apply(len)
    return data  
"""

def largestWords(sentence):
    data = WordData(sentence)
    max_len = data["length"].max()
    max_len_bool = data["length"] == max_len
    return data.loc[max_len_bool, "word"]

largest = WordData("To kill or not to (kill) is the big question question question") 
#print("largest words are:\n", largest)

