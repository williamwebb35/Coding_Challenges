# calculates the median of a list of numbers
# written for the Codecadmy Python 2 tutorial

def median(numbers):
  numbers = sorted(numbers)
  amount = len(numbers)
  if amount % 2 == 0:
    even_mid = int(amount/2)
    even_mid_upper = numbers[even_mid]
    even_mid_lower = numbers[even_mid -1]
    even_med = (even_mid_upper + even_mid_lower)/2
    return(even_med)
  else:
    odd_med = int(amount/2)
    return(numbers[odd_med])

median([4, 5, 5, 4])

# Below is the version allow for user input, a single number at a time


num_list =[]
length = int(input("Please enter the number of numbers to consider:  "))
for i in range(length):
    number = input("Enter a number: ")
    #While number:
     #   number = input("Enter a number or 'N' to stop entering numbers: ")
      #  number = int(new_num)
    num_list.append(number)
  
numbers = sorted(num_list)
amount = len(num_list)
if amount % 2 == 0:
    even_mid = int(amount/2)
    even_mid_upper = int(num_list[even_mid])
    even_mid_lower = int(num_list[even_mid -1])
    even_med = ((even_mid_upper + even_mid_lower)/2)
    print("The median is: ",even_med)
else:
    odd_med = int(amount/2)
    print("The median is: ",(num_list[odd_med]))

