#For this challenge you will be comparing two numbers....
#...and determining which one is greater.
#Completed for a coderbyte coding challenge

def CheckNums(num1, num2):
    if num2 > num1:
        return(True)
    elif num2 == num1:
        return(-1)
    else:
        return(False)

CheckNums(3,122)
