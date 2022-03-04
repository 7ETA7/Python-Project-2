# Lesson5 - Operators

# Arithmetics Operators
# these operators handle basix math

# addition
def add_example():
    result = 10 + 5
    print(result)


# subtraction
def subtract_example():
    result2 = 23 - 4
    print(result2)


# add_example()
# subtract_example()

# multiplication & Division
def multi_devide(sum1, sum2):
    result_multi = sum1 + sum2
    result_divide = sum1 / sum2
    print(result_multi)
    print(result_divide)


# multi_devide(10, 5)

# modulus
def modulus_example(value):
    result_modulus = value % 24
    print(result_modulus)


# Exponentiatio
def exponent_example(value):
    result_exponent = value ** 3
    print(result_exponent)



# modulus_example(189)
# exponent_example(21)
able = 10
beta = 765


# floor divistion
def floor_example():
    result_floor = beta // able
    print(result_floor)


# floor_example()

# assigment Operators
# These operators assign values to either a new variable or updates an
# exiting variables

def basic_assign(value1, value2):
    value1 += value2
    print(value1)
    value1 -= value2
    print(value1)
    value2 += value1
    print(value2)
    value2 /= value1
    print(value2)


# basic_assign(5, 3)


def basic_assign2(value):
    value %= 32
    print(value)
    value **= 5
    print(value)
    value //= 8
    print(value)


# basic_assign2(543)

# comparison operators
# These opraters are used to compare two values with a result of either
# True or fales


# sequal & not equal
def compare_two(value1, value2):
    result_equal = value1 == value2
    result_not = value1 != value2
    print(result_equal)
    print(result_not)


# compare_two(5, 8)

delta = 10
echo = 34

# greater than and less than
def great_less():
    result1 = delta < echo
    result2 = delta > echo
    print(result1)
    print(result2)



# great_less()

# greaqter than less than or equal to
def great_less_equal(num1):
    result_great = delta >= num1
    result_less = echo <= num1
    print(result_great)
    print(result_less)



# great_less_equal(10)

# Logical Operators
# operators that allow you to combine comparison oprators

# and
def logical_and():
    result = echo > 25 and delta > 9
    print(result)


# logical_and()

# or
def logical_or(num):
    result = echo > num or num < delta
    print(result)

# logical_or(30)





# not
def logical_not(num1, num2):
    result1 = not(num1 > num2)
    result2 = not(num1 < echo or num2 > delta)
    print(result1)
    print(result2)


# logical_not(23, 15)

# indentity Operators
# These operators check to see if the object is the sanem in memory
def Identity_is_not(arg1, arg2, arg3):
# is
    result1 = arg1 is arg2
    print(result1)
    result2 = arg1 is arg3
    print(result2)

# is not
    result3 = arg2 is not arg3
    print(result3)


# Identity_is_not('Hello', 'Python', 'Hello')

# member Operators
# These Operators test to sii if a sequence is in an object
kilo = "some kind of words to search through"


# in & not in
def member_in(arg):
    result = arg in kilo
    print(result)
    result = arg not in kilo
    print(result)


member_in('To'.lower())


