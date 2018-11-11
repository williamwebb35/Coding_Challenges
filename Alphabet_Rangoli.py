# You are given an integer, . Your task is to print an
#alphabet rangoli of size n. (Rangoli is a form of Indian
#folk art based on creation of patterns.) The center of
#the rangoli has the first alphabet letter a, and the
#boundary has the nth alphabet letter (in alphabetical order).

#Input Format
# Only one line of input containing , the size of the rangoli.


def print_rangoli(size):
    if size == 1:
        print("a")
        exit()
    alpha = "abcdefghijklmnopqrstuvwxyz"

    rang = alpha[0:size]

    ranglist = list(rang)

# calculates the number of characters for the width of the rangoli
    width = ((2*size-1) + ((2*size-1)-1))
#print("width=",width)

#calculates the number of dashes on either side of the characters
    sidedashes = int((width -1)/2)

#prints last item in the list of letters for the first row
    print(sidedashes*"-"+(ranglist[-1])+sidedashes*"-")

#this block prints the top of the rangoli 
    reduce = 2
    count = -2
    item_count = (len(ranglist)-2)
    start = size-1
    for item in range(len(ranglist)-1):
        print(((sidedashes-reduce)*"-")+("-".join(ranglist[-1:count:-1]))+"-"+(ranglist[item_count])+"-"+("-".join(ranglist[start::1]))+((sidedashes-reduce)*"-"))
        item_count -= 1
        count = count -1
        start = start -1    
        reduce = reduce + 2

#this block prints the bottom of the rangoli except the middle line and last line
    increase = 2
    count = 0
    start = 2
    for item in range(len(ranglist)-2):
        print(((increase)*"-")+("-".join(ranglist[-1:count:-1]))+"-"+("-".join(ranglist[start::1]))+((increase)*"-"))
        count = count +1
        start = start +1    
        increase = increase + 2

#prints last item in the list of letters for the last row
    print(sidedashes*"-"+(ranglist[-1])+sidedashes*"-")



print_rangoli(1)
    


