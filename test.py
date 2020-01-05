def do_twice(f,value):
  f(value)
  f(value)

def say(words):
  print(words)

do_twice(say,"hello")

define greet(name):
  print("Hello " + name)

greet("Arik")
