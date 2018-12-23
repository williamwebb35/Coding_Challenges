# This script checks a string for a specific word and ...
# .. replaces that word with asterisks
# Written as part of a Codecademy tutorial challenge

phrase = input("Enter some text to censor for a certain word: ")
word = input("Which word should be censored?: ")
def censor(text,word):
    text_l = text.split()
    stars = "*"*len(word)
    
    for item in text_l:
        if item == word:
        
            text_l.insert(text_l.index(word),stars)
            text_l.remove(item)
        
            new_text = " ".join(text_l)
    print("Here is the censored version of the text you entered: ",new_text)
censor(phrase,word)
