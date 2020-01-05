import math

# prints the length of the hypotenuse
# of a right-angle triangle by providing
# the length of the two other sides
def print_hypotenuse_length (a,b):
  c = math.sqrt(a**2 + b**2)
  print("a: ", a, " b: ", b, " c: ", c);

print_hypotenuse_length (3,4)

print_hypotenuse_length (2,8)

print_hypotenuse_length (5,10)



