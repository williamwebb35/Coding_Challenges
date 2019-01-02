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
