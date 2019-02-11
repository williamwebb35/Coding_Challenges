# Code below was written for a Hackerrank coding challenge
# The code prompts the user to enter numbers
# The code uses the set method to remove duplicates and then calculates ....
# .. the average of the unique numbers

#Now, let's use our knowledge of sets and help Mickey.
#Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
#Formula used: Average = Sum of Distinct Heights/ Total Number of Distinct Heights
#Input Format
#The first line contains the integer, , the total number of plants.
#The second line contains the  space separated heights of the plants.
#Constraints
#0<=N<+100
#Output Format
#Output the average height value on a single line.
#Sample Input
#10
#161 182 161 154 176 170 167 171 170 174
#Sample Output
#169.375

#values = input("Enter some numbers
# need to break up the input of the array
# not sure if the input will be in list form or not
# if not in list form, then insert commas between numbers

array = [10, 161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
num_items = array[0]
print("number of items: ", num_items)
values = array[1:]
print("all the items: ", values)
               
nums = set(values)
print("all the unique items: ", nums)
total = sum(nums)
print("sum of the uniques items: ",total)
average = total/len(nums)
print("average",average)

# code below is for interactive version posted on Trinket.io and Github


values = list(input("Enter the values, each separated by a space: "))
num_items = len(values)
print("The number of values is: ", num_items)
for i in values:
    if i == " ":
        values.remove(" ")
values = [ int(i) for i in values ]

print("The values are: ", values)
               
nums = set(values)
print("The unique values are: ", nums)
total = sum(nums)
print("The sum of the uniques values is: ",total)
average = total/len(nums)
print("The average of the unique values is: ",average)











