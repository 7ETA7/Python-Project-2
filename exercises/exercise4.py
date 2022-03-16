print(4 + 4)

print(12 - 4)

print(2 * 4)

print(16 / 2)


def favorite_number():
    print('my favorite number is 7')


favorite_number()


def number_sets():
    print(456234)
    print(68423791)
    print(13794628)
    print(96374)


number_sets()


def my_other(arg1, arg2):
    print(arg1)
    print(arg2)


my_other(float(20), int(20.50))

# input allows for users to provide information for us to use
movie = input('What is your favorite movie?')
seen = input('How many times have you seen it?')

message = 'My favorite movie is {0} and I seen it {1}'
print(message.format(movie, seen))
