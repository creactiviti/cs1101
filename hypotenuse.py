import math

# calculates the length of the hypotenuse 
# of a right triangle given the lengths
# of two other legs a and b as arguments
def hypotenuse(a,b):
  # Use the Pythagorean theorem to calculate 
  # the hypotenuse from right triangle sides.
  squared = a**2 + b**2
  return math.sqrt(squared) 

print("hypotenuse(5,3) == ", hypotenuse(5,3))
print("hypotenuse(10,2) == ", hypotenuse(10,2))
print("hypotenuse(7,5) == ", hypotenuse(7,5))

