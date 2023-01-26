"""
    Parse through the mailbox txt file to extract the days of the week each email was sent
"""

#Open the file from the exercises folder
txtfile = open("./exercise_files/mbox-short.txt")

for line in txtfile :
    clean_line = line.rstrip()
    words = clean_line.split()
    if words[0] != "From":
        continue
    print(words[2])