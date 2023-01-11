"""
Cover exercise 3 which includes conditional structures
"""

#Rewrite exercise 2 pay calculation to give the employee 1.5 payrate for hours over 40
problem = input("select an problem: [1,2]:")

if int(problem) == 1:
    rate = float(input("Enter Rate: "))
    hours = float(input("Enter Hours: "))

    if hours >= 40:
        extrahrs = (hours - 40)*1.5 + 40
    else:
        extrahrs = hours

    payrate = rate*extrahrs
    print("Pay: ", payrate)
#Rewrite the program with try and except to output an error when either rate or hours is a string
elif int(problem) == 2:
    rate = input("Enter Rate: ")
    hours = input("Enter Hours: ")
    try:
        hours = int(hours)
        rate = int(rate)
        if hours >= 40:
            extrahrs = (hours - 40)*1.5 + 40
        else:
            extrahrs = hours
        payrate = rate*extrahrs
        print("Pay: ", payrate)
    except:
        print("Error, please enter numeric input.")
    
else:
    print("Please choose 1 or 2.")

