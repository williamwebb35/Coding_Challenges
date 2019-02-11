# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.
# Input format: The first line contains n. The second line contains an
# array A[] of n integers each separated by a space
# Constraints: 2 <= n <= 10, -100 <= A[i] <= 100
# Output format: print the runner-up score

# converts the first input into an integer and assigns it to n
n = int(input())
# splits the input and converts the input into integers by applying the
# function int across all elements of the input iterable (using map)
nums = map(int, input().split())
# creates unique values (set), converts into a list, and sorts
# in ascending order (sorted)
print(sorted(list(set(nums)))[-2])


# takes the second input, converts into an integer, removes spaces
# and assigns the array as arr
#arr = map(int, input().split())
#arr = input()
#arr2 = list(arr)
#arr2.remove(' ')
#print("arr2 = ", arr2)
# uses numpy to retain only uniqe values in the array
#x = np.unique(arr)
#print("x = ", x)
# converts the array arr into a list and assigns it as ranks
#ranks = list(x)
#print("ranks =", ranks)
# sorts the items in the list 
#ranks.sort()

# remove duplicates / retain unique values only

# print second to last element in the list ranks
#print(ranks[-2])
#print(ranks)




#x = np.array(nums)
#remove spaces
#for i in ranks:
#    if i == ' ':
#        ranks.remove(' ')
#sort ranks
#ranks.sort()
#print second to last list element
#print(ranks)
#print(ranks[-2])

