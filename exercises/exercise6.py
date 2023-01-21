"""
Cover additional string functions and transformations through an exercise
"""

#take the string and extract the number at the end then use float to convert it.

string = 'X-DSPAM-Confidence: 0.8475'
str_start = string.find(' ')
print(str_start)