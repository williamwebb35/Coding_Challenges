# I wrote this from scratch as part of the Codecademy Python tutorial


x = int(input("Enter a number: "))
nums =[]
if x < 2:
    print("Not prime")
    sys.exit()
elif x == 2:
    print("Prime")
    sys.exit()
elif x > 2:
      
    for n in range(2,x):
        rem = x%n
        nums.append(rem)
      
if 0 in nums:
    print("Not prime")
else:
    print("Prime")
