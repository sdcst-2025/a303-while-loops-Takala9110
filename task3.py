#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
num = input("Enter number")
num = float(num)
roundnum = round(num)

if num - roundnum != 0 or num %2 != 0:
    print("Not an even integer") 
    while num - roundnum != 0 or num %2 != 0:
        num = input("Enter Number")
        num = float(num)
        roundnum = round(num)
        if num - roundnum == 0 and num %2 == 0:
            print ("this is an even integer")
        else:
            print("Not an even integer")
else:
    print("This is an even integer")




