# display program title
print("--LuckyUnicornGame--")


# yes/no function
def yes_no(question):
    valid = False
    while not valid:

        # ask user for input
        response = input(question).lower().strip()

        # if input = "yes" or "y" program continues
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # if input = "no" or "n" display instructions
        elif response == "no" or response == "n":
            response = "no"
            return response

        # if input = invalid, re-ask question
        else:
            print("Please enter yes or no!")


# instructions function
def instructions():
    # display instructions
    print("--Instructions--\n"
          "display instructions")


# main routine
played_before = yes_no("Have you played the Lucky Unicorn Game before? (y/n)\n"
                       ">>>>")

# played before checker
if played_before == "no":
    instructions()


# money wager function
def num_check(question, low, high):
    # error message
    error = "Please enter a whole number from $1 - $10"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            # if input = above 10 or below 0 re-ask question
            if low < response <= high:
                return response
            # output an error
            else:
                print(error)

        except ValueError:

            print(error)

# display function title
print("--DepositMoney--")

# main routine
money_wager = num_check("How much money would you like to wager? ($1-$10)\n"
                        ">>>>", 0, 10)
# how much has been deposited
print(f"Money wagered: ${money_wager}")
