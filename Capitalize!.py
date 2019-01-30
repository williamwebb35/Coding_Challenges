# You are asked to ensure that the first and
# last names of people begin with a capital letter
# in their passports.


def solve(s):
    names = s.split()
    first = names[0].capitalize()
    last = names[1].capitalize()
    print(first,last)
    
solve('hello world')






















