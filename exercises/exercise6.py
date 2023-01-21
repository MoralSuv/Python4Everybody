"""
Cover additional string functions and transformations through an exercise
"""

#take the string and extract the number at the end then use float to convert it.

string = 'X-DSPAM-Confidence: 0.8475 '
str_start = int(string.find(' '))
str_num = float(string[str_start+1:])
print(str_num)
