"""
Deal with string transformations and for loops while opening external files
"""
#Open the file from the directory exercise folder where the program is located
txtfile = open("./exercise_files/mbox-short.txt")

#Write program to print lines in the file line by line in all caps
for line in txtfile :
    clean_line = line.rstrip()
    print(clean_line.upper())
