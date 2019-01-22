
# Code below was written for a Hackerrank coding challenge
# The code prompts the user to enter numbers
# The code uses the set method to remove duplicates and then calculates ....
# .. the average of the unique numbers


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

