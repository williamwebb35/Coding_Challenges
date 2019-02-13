# Example: You are given two integers x and y .
# You need to find out the ordered pairs ( i , j ) ,
# such that ( i + j ) is not equal to n and print them
# in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y)
# sample code without using list comprehension:
#x = int(input())
#y = int(input())
#n = int(input())
#ar = []
#p = 0
#for i in range ( x + 1 ):
#    for j in range( y + 1):
#    if i+j != n:
#        ar.append([])
#ar[p] = [i , j]
#p+=1
#print(ar)

# sample code using list comprehension
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n )])



