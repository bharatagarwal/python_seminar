# Bharat Agarwal, 30th April 2021
# This program demonstrates how stripping works

# Note that none of these strip whitespace 
# between characters

name = "  \tJohn Appleseed\t\n\n\t    "

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Bharat Agarwal, 30th April 2021
# This program shows how fstrings work

name = 'Johannes'
message = f"Hello {name}, wold you like to learn some Python today?"

print(message)	
