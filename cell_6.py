#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def LetterChanges(str):
  new_str = list(str)
  for i in range(0,len(new_str),1):
    char = ord(new_str[i])
    if char >= 65 and char <90:
      new_str[i] = chr(char+1)
    elif char == 90:
      new_str[i] = chr(65)
    elif char >= 97 and char < 122:
      new_str[i] = chr(char+1)
    elif char == 122:
      new_str[i] = chr(97)
  for i in range(0,len(new_str),1):
    char = ord(new_str[i])
    if char == 97 or char == 101 or char == 105 or char == 111 or char == 117:
      new_str[i] = chr(char-32)
  str = ''.join(new_str)
  return str

# keep this function call here
str = input("Please enter string: ")
print (LetterChanges(str))

