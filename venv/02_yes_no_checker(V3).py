# yes/no function
def yes_no(question):
    valid = False
    while not valid:

        # ask user for input
        response = input(question).lower()

        # if input = "yes" or "y" program continues
        if response == "yes" or response == "y":
            response = "yes"
            print("You chose yes")

        # if input = "no" or "n" display instructions
        elif response == "no" or response == "n":
            response = "no"
            print("You chose no")

        # if input = invalid, re-ask question
        else:
            print("Please enter yes or no!")

# main routine goes here
show_instructions = yes_no("Have you played the Lucky Unicorn Game before? (y/n)")
print(f"You chose {show_instructions}")
