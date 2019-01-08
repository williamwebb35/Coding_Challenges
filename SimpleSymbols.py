# Have the function SimpleSymbols(str) take the str parameter being...
#...passed and determine if it is an acceptable sequence by either ...
#...returning the string true or false. The str parameter will be ...
#...composed of + and = symbols with several letters between them ...
#...(ie. ++d+===+c++==a) and for the string to be true each letter ...
#...must be surrounded by a + symbol.

## Completed for Coderbyte coding challenge 1/8/19

def SimpleSymbols(str):
    alpha = ["a","b","c","d","e","f","g","h","i","k",
           "l","m","n","o","p","q","r","s","t","u",
           "v","w","x","y","z"]
    before =[]
    after=[]
    indexes = [i for i, item in enumerate(str) if item in alpha]
    #print(indexes)
    for number in indexes:
        prior = number-1
        following = number+1
        before.append(str[prior])
        after.append(str[following])
    for item in before:
        if item != '+':
            return(False)
    for item in after:
        if item != '+':
            return(False)
        else:
            return(True)

SimpleSymbols("+d+=3=+s+")
        

    
# keep this function call here  
print SimpleSymbols(raw_input())  


