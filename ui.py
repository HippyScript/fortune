import variables


# Explanation of the game
def welcome_message():
    print("******* FORTUNE *******\n")
    print("You've set up a shop in your village to supply the villagers with everything they need. Buy supplies at wholesale cost, sell them at a profit, scavenge for more stuff or try your hand at robbery or marketing to amass your fortune. You require 1 food per day to survive.\n")

# Daily inventory and retail prices
def show_stats():
    print("╔═══════════════════════════════════════════════════════╗")
    print("║ ░░░░░░░░░░░░░░░░░░░░░░░ STATS ░░░░░░░░░░░░░░░░░░░░░░░ ║")
    print("║{:>14}{:>25}{:>17}".format("Items", "Prices", "║"))

    for (k, v), (k2, v2) in zip(variables.stash.items(), variables.prices.items()):
        print("║{:>12}: {:^12}|{:>8}{:^2}{:^38}".format(k, int(v), "$", int(v2), "║"))
    print("║-------------------------------------------------------║")
    print("║ Indentured servants: " + str(variables.indentured_count) + "  " \
          + "Days of advertising left: " + str(variables.advertising_duration).ljust(4) + "║")

    print("╚═══════════════════════════════════════════════════════╝\n")


# Display player's stash, current retail prices for all goods,
# and any events that have happened overnight
def update_display(event_str):
    show_stats()
    print(event_str)


# Wholesale prices are fixed for the game and located in
# variables.wholesale
def show_wholesale_prices():
    print("╔════════════════════════════════╗")
    print("║ ░░░░░░ WHOLESALE PRICES ░░░░░░ ║")
    for (k, v) in variables.wholesale.items():
        print("║{:>14}{:^10}{:^17}".format(k, ":  $" + str(v), "║"))
    print("╚════════════════════════════════╝\n")


# Display actions menu and get input
def get_action():
    choice: int = 0

    print("Buy Supplies [1] | Rob Competitor [2] | Advertise [3]")
    print("Scavenge [4] | Sell Supplies [5] | Sleep on It [6]")
    print("Quit [7]")
    try:
        choice = int(input("What would you like to do? "))
    except ValueError:
        print("Please enter a number for one of the choices.")

    if choice > 7 or choice < 1:
        print("Please enter your choice, from 1 to 7.")
        get_action()

    return choice


# Print victory message and stats
def victory(days):
    net_worth: int = 0
    for item in variables.stash:
            net_worth += variables.stash[item] * variables.prices[item]

    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░")
    print("▓░▓░▓░▓░▓░▓░▓ VICTORY!! ▓░▓░▓░▓░▓░▓░▓░▓")
    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░")
    print("You've earned enough to retire.")
    print("It took you {} days to amass your fortune.".format(days))
    print("Your net worth is now ${}".format(net_worth))



    print("")
