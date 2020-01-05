
# Determines if a is a power of b
# Definition: a, is a power of b if it is divisible by b 
#             and a/b is a power of b
def is_power(a,b):
  if b == 1:
      # the only positive integer that is a power of "1" is "1" itself
      return a == 1
  elif a == b:
      return True
  elif is_divisible(a,b) and is_power(a/b,b):
      return True
  return False

# Determines if x is divisble by y
# without a remainder
def is_divisible(x, y):
  if x % y == 0:
    return True
  else:
    return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

