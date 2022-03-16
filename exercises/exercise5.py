education = 'College'
print("Is your education == 'college'? I predict True.")
print(education == 'College')
print("\nIs your education == 'high_school'? I predict False.")
print(education == 'high_school')

home = 'A_house'
print("Is your home == 'A_house'? I predict True.")
print(home == 'A_house')
print("\nIs home == 'apartment'? I predict False.")
print(home == 'apartment')

plane = 'Jet'
print("Is your plane == 'Jet'? I predict True.")
print(plane == 'Jet')
print("\nIs plane == 'passenger'? I predict False.")
print(plane == 'passenger')

money = 'Dollar_bills'
print("Is your money == 'Dollar_bills'? I predict True.")
print(money == 'Dollar_bills')
print("\nIs your money == 'Change'? I predict False.")
print(money == 'Change')

Clothes = 'clean'
print("Are your Clothes == 'clean'? I predict True.")
print(Clothes == 'clean')
print("\nAre your clothes == 'Dirty'? I predict False.")
print(plane == 'Dirty')

# More Conditional Test
plane = 'Jet'
print("Is your plane == 'Jet'? I predict True.")
print(plane >= 'Jet')
print("\nIs plane == 'passenger'? I predict False.")
print(plane >= 'passenger')

time = 'early'
print("Is your time == 'early'? I predict True.")
print(time == 'early')
print("\nIs your time == 'late'? I predict False.")
print(time == 'late')


def arithmetics_operators(arg1=5, arg2=10,):
    result1 = arg1 - arg2 * arg1
    result2 = arg1 + arg2 / arg1
    print(result1, result2)


arithmetics_operators()


def one_argument(arg1):
    result1_mobulus = arg1 is arg1
    print(result1_mobulus)


one_argument('correct?')
