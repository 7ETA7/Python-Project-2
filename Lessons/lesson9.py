# lesson 9 Classes & Functions

# basic class definition
class Cat:
    # class variable
    kind = "feline"

    # constructor
    def __init__(self, name, color):
        # instance variables
        self.name = name
        self.color = color

    # basic method
    def cat_color(self):
        return self.color

    def cat_name(self):
        return self.name


# object creation
my_cat = Cat('Felix', 'white')
my_other = Cat('Garfield', 'orange')

# Method is share by all created objects
print(my_cat.cat_name())
print(my_cat.cat_color)
print(my_other.cat_color())

# name is unique to create objects
print(my_cat.name)
print(my_cat.name)

# kind is shared by all created objects
print(my_other.kind)


# function review
# keyword argument allows you to change the order of the function parameters
# when calling that method.
def my_fancy_function(arg, arg2):
    print(arg + ' = ' + arg2)

# normal function call
# my_fancy_function('freday', 'fun')


# keywords = function call
# my_fancy_function(arg2='weekend', arg='Saturday')

# arbitrary arguments allow for many arguments that are unknown.
# usinf +args and **kwargs will define these arguments


# *args will allow a tuple of argumwnts
def favorite_color(*colors):
    print('My favorite color is ' + colors[1])


# favorite_color('red', 'blue', 'green')

# tuple of colors
# 8args takes a tuple in values, but not as a avariable. you will generate
# an error if you push a tuple variable directly
# favs = ('red', 'green', 'blue', ' yellow', 'orange')
# favorite_color(favs)

# The arguments we pass into the function as a tuple, when executed create
# the tuple inside the function. this is why we can't pass a tuple directly


# using **kwargs will allow a dictionary of arguments
def vehicles(**truck):
    print('My trask is a' + truck['model'])


# vehicles(make='chevy1', model='silverado')


# using the default argument allow you to have more than one, with one
# given a default value. these default come after other arguments
def my_hello(arg, arg2='hi'):
    print(arg2 + ' ' + arg)


# my_hello('Tom')
# my_hello('Tim', 'Hello')


# using a return keyword will return the value back out of the functions to
# a variable you define to the left of the function
def simple_add(value1, value2):
    return value1 + value2


# total = simple_add(12, 23)
# print(total)
# print(simple_add(5, 10))


# main function is what is callwd when a python file is ran throught the
# compiler it will perform all action in the file exept functions unless
# they are called directly


if __name__ == '__main__':
    total = simple_add(12, 23)
    print(total)
