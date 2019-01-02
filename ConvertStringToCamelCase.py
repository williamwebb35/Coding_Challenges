# Complete the method/function so that it converts dash/underscore delimited words...
#... into camel casing. The first word within the output should be capitalized ...
#...only if the original word was capitalized.

# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    pairs_list = []
    pairs_dict = {}
    for i, letter in enumerate(text):
        pairs_list.append((i,letter))
   
   
    pairs_dict = dict(pairs_list)
    for k, v in pairs_dict.items():
        if not isinstance(v, dict):
            if '-' in v:
                pairs_dict[k+1] = pairs_dict[k+1].upper()
            if '_' in v:
                pairs_dict[k+1] = pairs_dict[k+1].upper()    
    #print(pairs_dict)
    new = list(pairs_dict.values())
    new = [char.replace('-', '') for char in new]
    new = [char.replace('_', '') for char in new]
    phrase = ''.join(new)
    #print(phrase)
    return(phrase)
to_camel_case("the-stealth_warrior")
