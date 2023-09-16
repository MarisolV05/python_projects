#A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
  print("hello, User!")
#A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(apple,banana,cheese):
  return [apple,banana,cheese]
#A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(lunchbox):
  if len(lunchbox) == 0:
    print("My lunchbox is empty")
  else:
    for i in range(len(lunchbox)):
      if i == 0:
        print(f"First I eat {lunchbox[0]}")
      else:
        print(f"Next I eat {lunchbox[i]}")
#call functions
hello()
print(pack("apple","banana","cheese"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["Sandwich"])
eat_lunch(["Sandwich", "Juice", "cookie", "fruit"])