a="  hello  world  "
nm="harry"
b = "i am learning python"
c = "i am learning python and i love reading books."
d = "i am learning python and i love reading, i almost read 2 books in a week."
# str slicing
print(" string slicing ".center(50, "*"))
print("Orignal string: ", nm)
print(nm[-4:-2])  
# The variable `nm` is assigned the string "harry". The expression `nm[-4:-2]`
#  uses negative indexing to slice the string.'''
# string stripping
print(" string stripping ".center(50, "*"))
print("Orignal string: ", a)
print(a.strip())  # Output: "hello  world"
print (a.lstrip()) # Output: "hello  world  "
print (a.rstrip()) # Output: "  hello  world"
# string replacing
print(" string replacing ".center(50, "*"))
print("Orignal string: ", a)
print(a.replace("world", "guys")) # replace "world" with "guys"
# string splitting
print(" string splitting ".center(50, "*"))
print("Orignal string: ", a)
 # It convert a string into list based on the separator provided.
 # If no separator is provided, it splits on whitespace by default.
print(a.split()) # Output: ['hello', 'world']
# string capitalization
print(" string capitalization ".center(50, "*"))
print("Orignal string: ", a)
print(a.upper()) # Output: "  HELLO  WORLD  "
print(a.lower()) # Output: "  hello  world  "
print(b.title()) # Output: "I Am Learning Python"
print(b.capitalize()) # Output: "I am learning python"
print("i love reading".title()) # Output: "I Love Reading"
# strings allignments
print(" string allignments ".center(50, "*"))
print("Orignal string: ", a)
print(a.center(20, "*"), len(a.center(20, "*"))) # Output: "**  hello  world  **"
print(a.ljust(20, "*"), len(a.ljust(20, "*"))) # Output: "  hello  world  ****"
print(a.rjust(20, "*"), len(a.rjust(20, "*"))) # Output: "****  hello  world  "
print(a, len(a)) # original string is not changed because strings are immutable in Python
# string searching
print(" string searching ".center(50, "*"))
print("Orignal string: ", a)
print("Index of 'world': {0}".format(a.find("world"))) # Output: 8, find() gives index of first occurrence of substring, returns -1 if not found
print("Index of 'python': {0}".format(a.find("python"))) # Output: 13
print("Index of 'xyz': {0}".format(a.find("xyz"))) # Output: -1 (not found)
print("Index of 'world': {0}".format(a.index("world"))) # Output: 8, index() gives index of first occurrence of substring, raises ValueError if not found
print("Orignal string: ", c)
print("Does '{0}' end with '.': {1}".format(c, c.endswith("."))) # Output: True, checks if the string ends with the specified suffix
print("Does '{0}' start with 'i am': {1}".format(c, c.startswith("i am"))) # Output: True, checks if the string starts with the specified prefix
# string counting
print(" string counting  ".center(50, "*"))
print("Orignal string: ", c)
print("Number of 'i' in '{0}': {1}".format(c, c.count("i"))) # Output: 4, counts the number of occurrences of substring
# string formatting
print(" string formatting ".center(50, "*"))
name = "Alice"
age = 30
# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.") # Output: "My name is Alice and I am 30 years old."
# Using str.format()
print("My name is {} and I am {} years old.".format(name, age)) # Output: "My name is Alice and I am 30 years old."
# different ways to format strings
# Using % operator
# The `%` operator is an older method of string formatting in Python. It allows you to embed variables into a string using format specifiers.
#  In this case, `%s` is used for strings and `%d` is used for integers. The variables `name` and `age` are passed as a tuple to the string, and they are inserted into the placeholders in the order they appear.
print("My name is %s and I am %d years old." % (name, age)) # Output: "My name is Alice and I am 30 years old."
# Using str.format() with positional and keyword arguments
# it allows you to specify the order of the arguments using numbers in curly braces `{}`.
# You can also use keyword arguments to make the code more readable.
print("My name is {0} and I am {1} years old.".format(name, age)) # Output: "My name is Alice and I am 30 years old."
# Using str.format() with keyword arguments
# You can also use keyword arguments to make the code more readable. In this case, `name` and `age` are passed as keyword arguments to the `format()` method, and they are inserted into the placeholders in the string using their respective names.
print("My name is {name} and I am {age} years old.".format(name=name, age=age)) # Output: "My name is Alice and I am 30 years old."
# Using f-strings with expressions
# it allows you to include expressions inside the curly braces `{}`. 
# In this case, `name.upper()` converts the name to uppercase, and `age + 5` adds 5 to the age. The resulting values are then inserted into the string.
print("My name is {name.upper()} and I am {age + 5} years old.") # Output: "My name is ALICE and I am 35 years old."
# is functions
print(" string is_functions ".center(50, "*"))
print("Is '{0}' an alphabetic string: {1}".format(a, a.isalpha())) # Output: False, checks if all characters in the string are alphabetic
print("Is '{0}' a digit string: {1}".format(b, b.isdigit())) # Output: False, checks if all characters in the string are digits
print("Is '{0}' an alphanumeric string: {1}".format(c, c.isalnum())) # Output: False, checks if all characters in the string are alphanumeric (letters and numbers)
print("Is '{0}' a whitespace string: {1}".format(nm, nm.isspace())) # Output: False, checks if all characters in the string are whitespace
print("Is '{0}' a lowercase string: {1}".format(a, a.islower())) # Output: True, checks if all characters in the string are lowercase
print("Is '{0}' an uppercase string: {1}".format(b, b.isupper())) # Output: False, checks if all characters in the string are uppercase
print("Is '{0}' a title string: {1}".format(c, c.istitle())) # Output: False, checks if the string is in title case (first letter of each word is uppercase)
print("Is '{0}' a printable string: {1}".format(nm, nm.isprintable())) # Output: True, checks if all characters in the string are printable (not control characters)
# swapping case
print(" string swapping_case ".center(50, "*"))
print("Swapping case of '{0}': {1}".format(a, a.swapcase())) # Output: "  HELLO  WORLD  ", swaps the case of each character in the string
