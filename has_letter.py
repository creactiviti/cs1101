# determines if the given string
# has a given letter in it. The functions
# will return True if the letter is found
# anywhere in the string, False otherwise.
def has_letter (string, letter): 
    if len(string) == 0:
      return False
    elif string[0] == letter:
      return True
    else:
      return has_letter(string[1:],letter)

print("has_letter('hello','l') == ", has_letter('hello','l'))
print("has_letter('','l') == ", has_letter('','l'))
print("has_letter('lifo','l') == ", has_letter('lifo','l'))
print("has_letter('goodbye','l') == ", has_letter('goodbye','l'))