"""
Cover the use of loops for simple problems
"""

#Repeatedly read numbers until user enters done, add all numbers entered print total, count, and the average at the end. Detect mistakes if not a number

tot = 0 
count = 0
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = float(number)   
        tot = tot + number
        count += 1
    except:
        print('Invalid input')
if count != 0:
    print(tot,count,tot/count)
else: 
    print('No result')
