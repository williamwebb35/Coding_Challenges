#Task 
#Read two integers from STDIN and print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
#Input Format

#The first line contains the first integer, . The second line contains the second integer, .

#Constraints

#Output Format

#Print the three lines as explained above.

num1 = abs(int(input()))
num2 = abs(int(input()))
out1 = (num1 + num2)
out2 = (num1 - num2)
out3 = num1*num2
print(out1)
print(out2)
print(out3)
