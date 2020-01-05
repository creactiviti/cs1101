
# counts down from n toward negative
# infinity and prints 'blastoff' when 
# n is 0 or smaller.
def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)

# counts up from n toward 
# positive infinity and 
# prints 'blastoff' when 
# n is 0 or larger.
def countup(n):
  if n >= 0:
    print('blastoff!')
  else:
    print(n)
    countup(n+1)


n = int(input("type a number: "))

if(n < 0):
  countup(n)
else:
  countdown(n)
