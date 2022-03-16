# This is a comment and you should have a space after the number sign.
# Click the enter key after to get rid of the squiggly yellow line.
# Yellow line.
# The statement below is a top level statement.
# It is defined outside a function class. This specific statement.
# This is a function called print that takes information and displays.
# That information to the terminal.

print("Hello world")

# A basic string can be defined by single or double quotes.

print("Hello world")

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    response[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
           polling_active = False

    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in response.items():
        print(name + " would like to climb " + response + ".")




