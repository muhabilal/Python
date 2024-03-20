"""""
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:


"""

userName=str(input("Enter Your Name:"))
userAge=int(input("Enter your age:"))
Result="Your Name is: {} and Your Age is: {}"
print(Result.format(userName,userAge))