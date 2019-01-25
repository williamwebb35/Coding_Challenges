# A pangram is a sentence that contains every single letter of ...
#...the alphabet at least once
# Given a string, detect whether or not it is a pangram. Return...
#...True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(s):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = s.lower()
    unique = set(s)
    chars = list(unique)
    #chars = sorted(chars)
    letters = list(set(alpha) & set(chars))
    letters = sorted(letters)
    #print(letters)
    if len(letters) == 26:
        return(True)
    else:
        return(False)

is_pangram("The quick, brown fox jumps over the lazy dog!")












