"""
    Parse through the mailbox txt file to extract the days of the week each email was sent
"""

#Open the file from the exercises folder
txtfile = open("./exercise_files/mbox-short.txt")
#Extract the day of the week from each email
for line in txtfile :
    clean_line = line.rstrip()
    words = clean_line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    print(words[2])