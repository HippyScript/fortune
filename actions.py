import variables
import sys
from random import seed
from random import randint


def buy_items():
    item = ""
    print("╔════════════════════════════════════════╗")
    print("║ ░░░░░░░░░░ WHOLESALE PRICES ░░░░░░░░░░ ║")
    for (k, v) in variables.wholesale.items():
        print("║\t\t" + k + ": $" + str(v) + "\t\t ║")
    print("╚════════════════════════════════════════╝\n")
    while item.upper() != "LEAVE":
        item = input("What item would you like to buy? Type 'leave' to cancel: ")
        if item.upper() == "LEAVE":
            return ""
        quantity = input("How many would you like to buy? ")
        try:
            quantity = int(quantity)
        except ValueError:
            print("Please enter a number.")
        if quantity > 0 and item in variables.wholesale.keys():
            if quantity * variables.wholesale[item] <= variables.stash["Gold"]:
                variables.stash["Gold"] -= quantity * variables.wholesale[item]
                variables.stash[item] += quantity
                print("You bought " + str(quantity) + " and have " + str(
                    int(variables.stash["Gold"])) + " gold remaining.")
            else:
                print("You don't have enough gold to make that purchase. Too bad you can't sell plasma.")


def rob():
    seed()
    success = bool(randint(0, 1))

    if success:
        variables.stash["Gold"] = variables.stash["Gold"] * 1.3
        return "Success! You've robbed your competitor and gained gold!"
    else:
        variables.stash["Gold"] = variables.stash["Gold"] * .75
        if variables.stash["Medicine"] > 0:
            variables.stash["Medicine"] -= 1
            return """Caught red-handed! You manage to flee, dropping some gold in the process.
You use one of your medicines to heal the wounds his knife inflicted."""
        else:
            sys.exit("""Your competitor caught you! Your blade was quick, but his was quicker.
As you lay dying on the dusty floor, you have time to ponder such a tragic end.""")


def advertise():
    # TODO
    return "NO CODE HERE YET"


def scavenge():
    # TODO
    return "NO CODE HERE YET"


def sell_items():
    # TODO
    return


def action_menu(user_choice):
    if user_choice == 1:
        return buy_items()
    elif user_choice == 2:
        return rob()
    elif user_choice == 3:
        return advertise()
    elif user_choice == 4:
        return scavenge()
    elif user_choice == 5:
        return sell_items()
    elif user_choice == 6:
        return
