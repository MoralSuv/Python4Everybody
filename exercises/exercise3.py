"""
Cover exercise 3 which includes conditional structures
"""

#Rewrite exercise 2 pay calculation to give the employee 1.5 payrate for hours over 40

rate = float(input("Enter Rate: "))
hours = float(input("Enter Hours: "))

if hours >= 40:
    extrahrs = (hours - 40)*1.5+hours
else:
    extrahrs = hours

payrate = rate*extrahrs
print = (Pay, payrate)