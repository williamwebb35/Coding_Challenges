# takes a positive integer n as input and ...
# returns the sum of all that number's digits.
# Written while completing Codecademy Learn Python 2


def digit_sum(x):
  x = str(x)
  nums=[]
  for i in x:
    number = int(i)
    nums.append(number)
  total = 0
  for num in nums:
    total = total + num
  return(total)

digit_sum(1234)
