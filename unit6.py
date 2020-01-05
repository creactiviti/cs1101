# Part 1:

# Create a string that is a long series of words separated by spaces. The string is your own creative choice. 
# It can be names, favorite foods, animals, anything. Just make it up yourself. Do not copy the string from another source. 
s = 'once upon a time in a land far far away'
# Turn the string into a list of words using split.
words = s.split(' ')
# Delete three words from the list, but delete each one using a different kind of Python operation. 
del words[0]
words.pop(0)
words = words[1:]
# Sort the list. 
words.sort()
# Add new words to the list (three or more) using three different kinds of Python operation. 
words.append('over')
words.extend(['the'])
words += ['rainbow']
# Turn the list of words back into a single string using join. 
s = ' '.join(words)
# print the modified words list
print(s)


# Part 2:

# Provide your own examples of the following using Python lists. Create your own examples. Do not copy them from another source. 

# Nested lists 
print ( [ [0,1,2], ["a","b","c"], [0.1,0.2,0.3] ] )

# The “*” operator 
print ( ''.join(["h"]+["e"]*10+["lo"]) )

# List slices 
print  ( [0,1,2,3,4,5,6,7,8,9][1:] )
print  ( [0,1,2,3,4,5,6,7,8,9][:-1] )

# The “+=” operator 
a = ['once','upon']
a += ['a','time']
print(a)

# A list filter

def extractNumbers(t):
    res = []
    for c in t:
        if c >= '0' and c<='9':
            res.append(c)
    return res

print (extractNumbers(list('a12bc3de456fg78hijk90')))

# A list operation that is legal but does the "wrong" thing, not what the programmer expects 
myList = [1,2,3,4,5,6,7]
modifiedList = myList.append(8)  # wrong -- return None


# Part 3

# How do you feel about the aspect assessments and feedback you have received from your peers?

# I feel good about the aspect assesment. It helps me really focus on what I need to look for in the assignment.
# I also trust that my peers will asses my fairly by using the aspect assesment as opposed to calling out things 
# that might not be required at the current level I'm at.

# How do you think your peers feel about the aspect assessments and feedback you provided them?

# I want to say that they think it's fair. I really try and just stick to the aspects required and not go off onto some 
# arbitrary requirements. Also, I had a concern last week about a certain missing aspect and I brought it up to the instructor
# and got an answer I was happy it and made me feel like I'm on the right track with how I'm assessing my peers.
