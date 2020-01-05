# provided code from assignment
alphabet = "abcdefghijklmnopqrstuvwxyz"   
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
def histogram(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d 

# Implement has_duplicates by creating a histogram using the histogram function above. 
# Do not use any of the implementations of has_duplicates that are given in your textbook. 
# Instead, your implementation should use the counts in the histogram to decide if there are any duplicates. 
def has_duplicates(s): 
    h = histogram(s)
    for v in h.values():
      if(v > 1):
        return True
    return False

# Implement has_duplicates by creating a histogram using the histogram function above. 
# Do not use any of the implementations of has_duplicates that are given in your textbook. 
# Instead, your implementation should use the counts in the histogram to decide if there are any duplicates. 
#
# Write a loop over the strings in the provided test_dups list. Print each string in the list and whether 
# or not it has any duplicates based on the return value of has_duplicates for that string. 
for test_value in test_dups:
    result = has_duplicates(test_value)
    if result:
        print(test_value,"has duplicates")
    else:
        print(test_value,"has no duplicates")

# seperator
print("------------------------------------------")

# Write a function called missing_letters that takes a string parameter and returns 
# a new string with all the letters of the alphabet that are not in the argument string. 
# The letters in the returned string should be in alphabetical order. 
# 
# Your implementation should use a histogram from the histogram function. 
# It should also use the global variable alphabet. It should use this global variable directly, 
# not through an argument or a local copy. It should loop over the letters in alphabet 
# to determine which are missing from the input parameter. 
#
# The function missing_letters should combine the list of missing letters into a string and return that string. 
def missing_letters(s):
    result = []
    h = histogram(s)
    for letter in alphabet:
        if letter not in h:
            result.append(letter)
    return ''.join(result)

# Write a loop over the strings in list test_miss and call missing_letters with each string. 
# Print a line for each string listing the missing letters.
for test_value in test_miss:
    result = missing_letters(test_value)
    if len(result) == 0:
        print(test_value,"uses all the letters ")
    else:
        print(test_value, "is missing letters",result)