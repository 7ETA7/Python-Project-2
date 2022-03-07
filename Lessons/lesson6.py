# Lesson 6 - control flow Statements

# Boolean
# Those values are either true of false
def boolean_sample():
    print(bool('sample'))
    print(bool(0.0))


# boolean_sample()


# if statement
# Used to find out if a conditions is true
def basic_if(arg1, arg2):
    if arg1 > arg2:
        print('are value is greater than our other one')

    if arg1 == arg2:
        print('both values are the same')


# basic_if(10, 5)


# elif example
# Used when the first condition is false and you want to try another
def basic_if_elif(arg):
    if arg > 10:
        print('sum is greater than 10')
    elif sum == 10:
        print('sum is the 10')
    elif arg < 10:
        print('sum is less than 10')


# basic_if_elif(9)


# else statement
# this keyword can be used to execute a block of code when the if statement
# results are false
def else_example(arg):
    if arg > 15:
        print('our argument is greater than 15')
    else:
        print('Our argument is less than 15')


# else_example(12)


# else with elif
def check_grade(arg):
    if arg == 'A':
        print('Excellent')
    elif arg == 'B':
        print('Good')
    elif arg == 'C':
        print('Average')
    elif arg == 'D':
        print('Below average')
    elif arg == 'F':
        print('failed')
    else:
        print('not a valid grade')



# check_grade('12')
# Nested If Statement
# This allows an if statement to be inside another if statement.
# the innter if statment only if used outer if is true.
# happy = 14


def nested_example(arg):
    if happy > arg:
        print('happy is greater than the argument')
        if arg > 5:
            print('argument is greater than 5')
        else:
            print('argument is less than 5')


# nested_example(4)

# terminary Statemnt
# due conditon can be performed on one line
# Basically a shortened if statement
golf = 22
hotel = 24

# if shorthand
result = golf if golf > hotel else hotel
print(result)

print('both are equal' if golf == hotel else 'golf is greater' if golf
        > hotel else 'hotel is greater')


# This function will break down the above shorthand to normal if
def if_short_decoded():
    if golf == hotel:
        print('both are equal')
    elif golf > hotel:
        print('goolf is greaqter')
    else:
        print('hotel is greater')


if_short_decoded()


# and & or keyword
def combined(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 >= arg3:
        print('argument 1 is the greatest')

    if arg2 > arg3 or arg2 <= arg3:
        print('Argument 2 is greater than 3 but not 1')


combined(10, 20, 30)
