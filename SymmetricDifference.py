#Given  sets of integers,M and N,
#print their symmetric difference in ascending order.
#The term symmetric difference indicates those values
#that exist in either  or  but do not exist in both.


# Python code to get difference of two lists 
# Using set()
n1 = int(input())
line1 = input().split()
numbers1 = [ int(x) for x in line1]
n2 = int(input())
line2 = input().split()
numbers2 = [ int(x) for x in line2]
Mset = set(numbers1)
Nset = set(numbers2)
Muniques = Mset.difference(Nset)
Nuniques = Nset.difference(Mset)
AllUniques = Muniques.union(Nuniques)
All = list(AllUniques)
All.sort()
for num in All:
    print(num)

# Sample Input:
#4
#2 4 5 9
#4
#2 4 11 12
