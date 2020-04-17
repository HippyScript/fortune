#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, time
import variables
import actions


def update_display(event_str):
    print("╔═══════════════════════════════════════════════════════╗")
    print("║ ░░░░░░░░░░░░░░░░░░░░░░░ STATS ░░░░░░░░░░░░░░░░░░░░░░░ ║")
    print("║\tStores\t\t\tPrices".ljust(10) + "\t\t\t║")

    for (k, v), (k2, v2) in zip(variables.stash.items(), variables.prices.items()):
        print("║\t" + k + ": " + str(int(v)).ljust(5) + "\t|\t" + "$" + str(v2) + "\t\t\t║")

    print("╚═══════════════════════════════════════════════════════╝\n")
    print(event_str)


if __name__ == "__main__":

    ti = 0
    choice = 0
    while True:
        time.sleep(2.0)
        ti += 1
        if ti % 4 == 0:
            variables.stash["Gold"] = variables.stash["Gold"] + 1 + variables.indenturedCount

        if ti % 30 == 0 and variables.indenturedCount > 0:
            variables.indenturedCount -= 1
            print("An indentured servant has paid off his debt and retired.")

        if ti > 0:
            update_display(variables.random_event())

        choice = input("""Buy Supplies [1]\t|\tRob Competitor [2]\t|\tAdvertise [3]\n
        Scavenge [4]\t|\tSell Supplies [5]\t|\tSleep on It [6]\nWhat would you like to do? """)
        if 0 < int(choice) <= 6:
            print(actions.action_menu(int(choice)))
        else:
            print(str(choice) + " isn't an option.")
