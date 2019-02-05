#Mr. Vincent works in a door mat manufacturing company.
#One day, he designed a new door mat with the following specifications:

#Mat size must be N X M. ( is an odd natural number, and M is three times M.)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.

#Input Format

#A single line containing the space separated values of N and M.

#Constraints
#    5 < N < 101
#    15 < M < 303
    
#Output Format

#Output the design pattern.


# N = # rows
# M = # horizontal characters

def doormat(N, M):
    # calculates # dashes on right or left of first line
    dashes = int(((M-3)/2))
    # defines the middle symbol
    middle = ".|."
    # defines the # of lines on the top and bottom halves
    top_bottom_lines = int((N-1)/2)
    #counter for the number of lines
    middle_count = 1
    # prints the first line
    print(dashes* "-" + middle + dashes * "-")
    # prints the # of top and bottom lines
    for i in range(1, top_bottom_lines):  
        # make a counter that counts up or down the number of middle symbols to print
        # .. using addition assignment
        middle_count = middle_count + 2 #
        side_dashes = int(((M - (middle_count*3))/2))
        # LEFT OFF HERE 10/3: the number of dashes printed on both halves are correct for...
        #the firts two line (9, 6) but not the thrid line (4) which should be 3 instead. This ..
        #.. is because for the third line line_count = 5 and dashes is 9 (starting with M = 21, dashes = 9)
        print(side_dashes*"-"+ middle*middle_count + side_dashes*"-") #middle line
    print(int((M-7)/2)*"-"+"WELCOME"+int((M-7)/2)*"-")
    middle_count = N 
    for i in range(1, top_bottom_lines):
        # make a counter that counts up or down the number of middle symbols to print
        # .. using addition assignment
        middle_count = middle_count - 2 #
        side_dashes = int(((M - (middle_count*3))/2))
        # LEFT OFF HERE 10/3: the number of dashes printed on both halves are correct for...
        #the firts two line (9, 6) but not the thrid line (4) which should be 3 instead. This ..
        #.. is because for the third line line_count = 5 and dashes is 9 (starting with M = 21, dashes = 9)
        print(side_dashes*"-"+ middle*middle_count + side_dashes*"-")    
    # prints the last line
    print(dashes* "-" + middle + dashes * "-")



    # NEXT TO DO: Since the width is constant (M) but the number of middle sumbols increases, perhaps use...
    # substraction of width - # middle symbols to calculate the # of dashes to print on either side...
    # ((M - (middle_count*3))/2) = # dashes on each side

    #1) center the design; remove dashes when extra middle symbols are printed so the entire line ...
    #... stays the same length - perhaps in the for loop, reduce the dashes variables see above
    # 2) make sure the first line has a single middle symbol
    #... starting with the top line ending before the middle line
    # 2) print the middle lines
    # 3) Do step #1 but in reverse printing for the # of middle symbols

doormat(7, 21)
