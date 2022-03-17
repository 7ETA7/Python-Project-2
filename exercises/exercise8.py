def greet_user(username):
    if username is 'admin':
        print("Hello Admin! You're now operating with special rights")
    else:
        print("Hello " + username.title() + "! How are you doing today ?")


def greeting(usernames):
    if usernames:
        for username in usernames:
            greet_user(username)


usernames = ['admin', 'Roger', 'dark knight']
greeting(usernames)


users = ['John', 'Saskia', 'Georg', 'Melinda',' Kent']
other_users = ['JOHN', 'Evelyn', 'oscar', 'melinda', 'Dustin']


def check_name(new_user, users_lower):
    if new_user.lower() not in users_lower:
        print("Welcome to our website!")
        users.append(new_user)
    else:
        print("Sorry " + new_user + " is already taken.")


def check_names():
    users_lower = [user.lower() for user in users]
    list(map(lambda x: check_name(x, users_lower), other_users))


check_names()


# Exercise 5-11. Ordinal Numbers

numbers = list(range(1,10))

for number in numbers:
    if (number == 1 ):
        print("\n" + str(number) + "st")
    elif (number == 2):
        print("\n" + str(number) + "nd")
    elif (number == 3):
        print("\n" + str(number) + "rd")
    else:
        print("\n" + str(number) + "th")

person_0 = {'first_name': 'Daevon', 'last_name': 'Hil', 'age': 24, 'city': 'Wichita'}
print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])
print(person_0)

person_1 = {'first_name': 'DeAundre', 'last_name': 'Hill', 'age': 24, 'city': 'Wichita'}

person_2 = {'first_name': 'Daevon', 'last_name': 'Hill', 'age': 22, 'city': 'Mesa'}

persons = [person_0, person_1, person_2]

for person in persons:
    print(person)

