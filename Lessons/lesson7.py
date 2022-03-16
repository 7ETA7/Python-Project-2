# Lesson 7 looping statements


# while loop
# Executes a set of statements until its condition is false
def basic_while(arg):
    alpha = arg
    while alpha < 4:
        print(alpha)
        # increment by 1
        alpha += 1


# basic_while(0)


# for loop
# executes a set of atatement as it iterates a collextion or sequence
def basic_for(arg):
    for alpha in arg:
        print(alpha)


# basic_for('I like coding')

# nested for loop
# you can have  loop, both must have different declared variable
# of the outer loop. both must have different declared variables
def basic_nested():
    for hop in range(1, 11):
        for bop in range(hop):
            print(hop, end=' ')
        print()
    print()


# basic_nested()


# range
# This is used to return a sequence of numbers. this includew a start
# number, end number increment
# single argument
def basic_single():
    for able in range(5):
        print(able)


# two argument
def basic_double():
    for beta in range(5):
        print(beta)


# basic_single()
# basic_double()
# three arguments
def basic_three():
    for charlie in range(0, 15, 2):
        print(charlie)


# basic_three()

# pass statement
# this allows for a loop to be created without a body
for num in 'Hello':
    pass


# break statment
# this is used in conjuction with an if statment to break from a loop
def basic_break(num1):
    while num1 < 10:
        print(num1)
        if num == 5:
            break
        num1 += 1


# basic_break(0)


# using a for loop
def basic_break_for():
    for value in 'Python':
        if value == 'h':
            break
        print(value)


basic_break_for()


# continue statement
# This statement will stop an active iteration and begin the next one.
def basic_continue():
    for value in 'python':
        if value == 'h':
            continue
        print(value)


basic_continue()

# else statement
# also used in loops, this stamtement can be used after the loop ends


def basic_else():
    thing1 = 0
    while thing1 < 4:
        print(thing1)
        thing1 += 1
    else:
        print('loop ends')


basic_else()
