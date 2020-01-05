# prints 9 lines
def nine_lines():
  three_lines ()
  three_lines ()
  three_lines ()

# print 25 lines
def clear_screen():
  nine_lines()
  nine_lines()
  three_lines()
  three_lines()
  new_line()

# prints a single line
def new_line():
  print('.')

# prints 3 lines
def three_lines():
  new_line()
  new_line()
  new_line()


nine_lines()

print("calling clear_screen()")

clear_screen()


