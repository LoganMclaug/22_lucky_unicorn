# money wager function
def num_check(question, low, high):
    error = "(You can only wager $1 - $10)"

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

# main routine
money_wager = num_check("--How much would you like to deposit?--", 0, 10)
# how much has been deposited
print(f"Money wagered: ${money_wager}")
