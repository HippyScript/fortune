#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import variables
import actions
import events
import ui
import sys
from random import seed

if __name__ == "__main__":

    days = 0  # number of days
    choice = 0  # user's menu choice

    seed()

    ui.welcome_message()
    ui.show_stats()

    while True:
        time.sleep(1.0)
        days += 1

        if variables.stash["Food"] >= 0:
            sys.exit("Your food has run out. Starvation is a slow and painful death.")

        variables.stash["Food"] -= 1

        # Every 4 days player and all indentured servants accumulate gold
        if days % 4 == 0:
            variables.stash["Gold"] = variables.stash["Gold"] + 1 + variables.indentured_count

        # Advertising is good for 14 days and adds 20% to sale prices
        # Subtract 1 from the counter every day it's above 0
        if variables.advertising_duration > 0:
            variables.advertising_duration -= 1
            variables.advertising_boost = 1.2
        else:
            variables.advertising_boost = 1

        # Every 30 days one indentured servant retires
        if days % 30 == 0 and variables.indentured_count > 0:
            variables.indentured_count -= 1
            print("An indentured servant has paid off his debt and retired.")

        # Every subsequent day has a random event
        if days > 1:
            ui.update_display(events.random_event())

        # You win if you collect 1000 gold
        if variables.stash["Gold"] >= 1000:
            ui.victory(days)

        print(actions.action_menu(ui.get_action()))

