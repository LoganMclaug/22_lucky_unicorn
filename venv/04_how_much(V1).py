# money wager function
error = "--You can only enter $1 - $10--"

valid = False
while not valid:
    try:
        money_wager = int(input("--How much would you like to deposit?--"))
        # output an error
        if 0 >= money_wager or money_wager > 11:
            print(error)
        # if input = above 10 or below 0 re-ask question
        else:
            # how much has been deposited
            print(f"Money wagered: ${money_wager}")
    except ValueError:
        print(error)
