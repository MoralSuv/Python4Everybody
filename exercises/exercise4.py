"""
Cover creating functions for using in repetitive scenarios
"""

#Write the pay computation with overtime and create function compute pay which takes hours and rate as parameters

def computepay(hours,rate):
    """
    Takes hours,rate variables to compute the payrate which accounts for overtime pay at 1.5 the regular rate
    """
    if hours > 40:
        payrate = ((hours-40)*1.5+40)*rate
    else:
        payrate = hours*rate
    return payrate

hour = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

print('Pay:', computepay(hour,rate))