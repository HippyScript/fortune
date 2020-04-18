import variables
import ui
import sys
import random

def buy_items():

    item = ""

    while item.upper() != "LEAVE":
        item = input("What item would you like to buy? Type 'leave' to cancel: ").capitalize()
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
        ui.show_stats()

# Robbery allows user to gain gold but runs the risk of
# being caught. When caught, player uses up 1 medicine
# to heal from being stabbed and drops some of their own
# gold. If the player has no medicine, they die
def rob():
    random.seed()
    success = bool(random.randint(0, 1))

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

# Advertising costs 10 pieces of gold but increases retail prices for 14 days
def advertise():

    if variables.stash["Gold"] >= 10:
        print("Advertising costs 10 pieces of gold, lasts for 14 days and allows you to sell your goods at a premium.")
    else:
        return("Advertising costs 10 pieces of gold. You don't have enough gold yet.")

    if input("Buy advertising [y/n]? ").lower() == "y":
        variables.advertising_duration = 14
        return("There's no such thing as bad publicity. Advertising is in place for 14 days.")
    elif input("Buy advertising [y/n]? ").lower() == "n":
        return("You've decided not to advertise.")
    else:
        print("Please enter a 'y' or 'n'.")
        advertise()

# Scavenging uses 1 food and 3 bullets
# If the user runs out of food, they die of starvation
def scavenge():
    random.seed()
    success = bool(random.randint(0, 1))

    if success:
        for (k, v) in variables.stash.items():
            success = bool(random.randint(0, 1))
            if success:
                variables.stash[k] = variables.stash[k] * random.uniform(1.2, 1.6)
                print("Scavenging yields some " + k + ".")
    else:
        if variables.stash["Food"] > 0:
            variables.stash["Food"] -= 1
            variables.stash["Bullets"] -=3
            return "You return empty-handed, having used some of your precious bullets and food."
        else:
            sys.exit("You ventured out to scavenge without bringing enough food. Starvation is a slow death.")


def sell_items():
    item = ""

    while item.upper() != "LEAVE":
        item = input("What item would you like to sell? Type 'leave' to cancel: ").capitalize()
        if item.upper() == "LEAVE":
            return ""
        quantity = input("How many would you like to sell? ")
        try:
            quantity = int(quantity)
        except ValueError:
            print("Please enter a number.")

        item = item.capitalize()

        if variables.stash[item] >= quantity > 0 and item in variables.prices.keys():
            if variables.advertising_boost == 1.2:
                print("\nAdvertising boosts your prices.")
            print("\nYou've sold " + str(quantity) + " " \
                  + item + " for $" + str(int(variables.prices[item] * quantity * variables.advertising_boost)))
            variables.stash["Gold"] += variables.prices[item] * quantity * variables.advertising_boost
            variables.stash[item] -= quantity
        elif variables.stash[item] < quantity < 0:
            print("You don't have enough " + item + " to make this sale.")
        elif item not in variables.prices.keys():
            print("This item doesn't exist.")
        else:
            print(item + " " + str(quantity))

        ui.show_stats()

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
        return ""
    elif user_choice == 7:
        sys.exit("You've closed up shop and sought an early retirement. Good bye!")
