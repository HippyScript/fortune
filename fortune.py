#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import variables
import actions
import sys


def update_display(event_str):
    # Display player's stash, current retail prices for all goods,
    # and any events that have happened overnight

    variables.show_stats()
    print(event_str)


if __name__ == "__main__":

    days = 0  # number of days
    choice = 0  # user's menu choice
    print("******* FORTUNE *******\n")
    print("""You've set up a shop in your village to supply the villagers with everything they need.
buy supplies at wholesale cost, sell them at a profit, scavange for more stuff or try your hand
at robbery or marketing to amass your fortune. You require 1 food per day to survive.\n""")

    while True:
        time.sleep(1.0)
        days += 1

        if variables.stash["Food"] == 0:
            sys.exit("Your food has run out. Starvation is a slow and painful death.")

        variables.stash["Food"] -=


        # Every 4 days player and all indentured servants accumulate gold
        if days % 4 == 0:
            variables.stash["Gold"] = variables.stash["Gold"] + 1 + variables.indenturedCount

        # Advertising is good for 14 days and adds 20% to sale prices
        # Subtract 1 from the counter every day it's above 0
        if variables.advertisingDuration > 0:
            variables.advertisingDuration -= 1
            variables.advertisingBoost = 1.2
        else:
            variables.advertisingBoost = 1

        # Every 30 days one indentured servant retires
        if days % 30 == 0 and variables.indenturedCount > 0:
            variables.indenturedCount -= 1
            print("An indentured servant has paid off his debt and retired.")

        if days > 0:
            update_display(variables.random_event())

        print("Buy Supplies [1]\t |\tRob Competitor [2]\t |\tAdvertise [3]")
        print("Scavenge [4]\t\t |\tSell Supplies [5]\t |\tSleep on It [6]")
        print("Quit [7]")
        try:
            choice = int(input("What would you like to do? "))
        except ValueError:
            print("Please enter a number for one of the choices.")

        if 0 < choice <= 7:
            print(actions.action_menu(choice))
            choice = 0
        else:
            print(str(choice) + " isn't an option.")
            choice = 0
