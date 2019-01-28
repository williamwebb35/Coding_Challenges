#For this challenge you will be manipulating characters...
#...in a string based off their positions in the alphabet

#Using the Python language, have the function LetterChanges(str)...
#...take the str parameter being passed and modify it using the...
#...following algorithm. Replace every letter in the string with the...
#..letter following it in the alphabet (ie. c becomes d, z becomes a).
#Then capitalize every vowel in this new string (a, e, i, o, u) and
#...finally return this modified string. 

def LetterChanges(x):
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    vowels = ["a", "e", "i", "o", "u"]
    
    new_str = ""
    
    for item in x:
        if item not in alphabet:
            new_str = new_str + item
        if item in alphabet:
            next = (int((alphabet.index(item)))+1)
            new_letter = (alphabet[next])
            new_str = new_str + new_letter

    for new_letter in new_str:
        if new_letter in vowels:
            new_upcase = (new_letter.swapcase())
            new_str = new_str.replace(new_letter, new_upcase)
# the block above changes case but does not change the original string            
    print(new_str)
   
LetterChanges("hello world")
#LEFT OFF:
 #   CURRENT  PROBLEM - LOOKS LIKE I NEED TO CONSIDER SPACES
    
#mine = UIjt mpOh dblf@&
#correct = "UIjt mpOh dblf@&"
