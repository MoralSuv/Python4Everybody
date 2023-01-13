"""
Cover the use of loops for simple problems
"""

#Repeatedly read numbers until user enters done, add all numbers entered print total, count, and the average at the end. Detect mistakes if not a number

tot = 0 
while True:
    number = input('Enter a number: ')
    if number = 'done':
        break
    else:
        try:
            float(number)
            tot = tot + number
        except:
            print('bad data')
