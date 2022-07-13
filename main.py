import random

print("Random Password Generator")
weak_pass = input("Enter a weak password:")

new_pass = ""
for char in weak_pass:
  if char == "i":
    options = ['1', 'L', '|']
    n = random.choice(options)
  elif char == "o":
    options = ["0", "O"]
    n = random.choice(options)
  elif char == "e":
    options = ["3", "E", "#"]
    n = random.choice(options)
  elif char == "s":
    options = ["$", "S", "&"]
    n = random.choice(options)
  elif char == "a":
    options = ["@", "A"]
    n = random.choice(options)
  else:
    n = char
  new_pass = new_pass + n

print("New password: " + new_pass)
