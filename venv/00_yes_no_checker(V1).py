# ask user for input
show_instructions = input("Have you played the Lucky Unicorn Game before? (y/n)").lower()

# if input = "yes" program continues
if show_instructions == "yes":
    print("program continues")

# if input = "y" program continues
elif show_instructions == "y":
    print("program continues")

# if input = "no" display instructions
elif show_instructions == "no":
    print("display instructions")

# if input = "n" display instructions
elif show_instructions == "n":
    print("display instructions")

# if input = invalid re-ask question
else:
    print("Please enter yes or no!")
