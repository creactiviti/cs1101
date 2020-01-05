# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          for item in val:
            if item not in inverse:
               inverse[item] = [key]
            else:
               inverse[item].append(key)
     return inverse 

# Create a Python dictionary that returns a list of values for each key. The key can be whatever type you want. 
# Design the dictionary so that it could be useful for something meaningful to you. Create at least three different items in it. 
my_family = {"miriam":["mom",57],"michael":["dad",60],"nirit":["sister",31],"nofit":["sister",31],"liv":["daughter",2]}

# Print the original dictionary 
print(my_family)

# Print the inverted dictionary 
print(invert_dict(my_family))