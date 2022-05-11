# start of loop
show_instructions = "valid"
while show_instructions != "0":
    # ask user for input
    show_instructions = input("Have you played the Lucky Unicorn Game before?").lower()

    # if input = "yes" or "y" program continues
    if show_instructions == "y" or show_instructions == "yes":
        print("program continues")

    # if input = "no" or "n" display instructions
    elif show_instructions == "n" or show_instructions == "no":
        print("display instructions")

    # if input = invalid re-ask question
    else:
        print("Please enter yes or no!")

