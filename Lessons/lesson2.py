# My Application Overview Lesson.

# This function should be lowercase and if more than on word it
# should have an underscore to separate each word. you should have
# a parenthesis after the name followed by a colon. Statements that are
# part of the function should be 4 spaces indented.
def my_function():
    print('Hello')
    print('world')

# To run the function, you must call it by name.

my_function()


# when defining a function with arguments go in between.
# the parenthesis and separated by commas.
def my_other(arg1, arg2):
    print(arg1)
    print(arg2)


my_other('Red', 'Green')

# Variable Names
# - must start with a latter or and underscore
# - can not begin with a number
# - can only contain alpha-numeric characters and underscores
# - are case sensitive

# The variables are on the left while the literal value is on the right
# value & value 2 are variables
# blue and 10 are variables
# combined they are a filed
value = 'Blue'
value2 = 10


# Variables can even change types, although you may want to avoid this
value3 = "Happy"
print(value3)
value3 = 20
print(value3)



# Multi-Line statements use backslash to contentue a statement on a second line.
alpha = 1 + 2 + 3 \
    + 4 + 5
print(alpha)

# more than one variable on the same line
beta = 10; charlie = "python"; delta = 5

up, down, left = "town", "stairs", "right"
print(up)
print(down)
print(left)