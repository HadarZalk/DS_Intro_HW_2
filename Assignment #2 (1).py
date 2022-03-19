#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# A.	write a function named reverse(sentence, reverse_word) that takes two strings as an input and returns a new string where the first occurrence of reverse_word in the sentence has been reverted (I.e. spelled backwards). 
# Return type: str. 


# In[140]:


def reverse (sentence, reverse_word):
    try:
        reverse_word = int(reverse_word)
        print("Invalid Value")
    except ValueError:
        temp = reverse_word
        if temp in sentence:
            temp = temp [::-1]
            sentence = sentence.replace(reverse_word,temp,1)
            print (sentence)   
        else: 
            print ("no match word found")
   


# In[141]:


#main 
sentence = input('enter a sentce: ')
reverse_word = input('enter a word you would like to reverse: ')

reverse (sentence, reverse_word)


# In[ ]:


#B.	 Optional Exercise (no grading): Write a function named compute_equation(equation) to compute the equation represented by a string. Return type: int, float, str (errors must be str).


# In[201]:


get_ipython().system('pip install regex')
import re


# In[249]:



def compute_equation (equation):
   regex = re.compile('[*()<>/]')
   if (regex.search(equation) == None):
       print ("invalid input detected")
   elif "^" in equation:
       print ("invalid input detected")
   else:
       print (int(x))


       
       

    
   


# In[250]:


compute_equation ("5*2+1-6^5+0.5") 

