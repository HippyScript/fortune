# Random events in the game
from typing import Any, Union, Callable

import variables
from random import choice
from random import randint

def competitor():
    for (k, v) in variables.prices.items():
        if k != "Gold" and v > 1:
            variables.prices[k] = int(v * .9)

    return "A competitor has set up shop! Prices have taken a hit."


def competitor_gone():
    for (k, v) in variables.prices.items():
        if k != "Gold":
            variables.prices[k] = v + 1

    return "A competitor has closed! Prices for your goods rise."


def robbed():
    for (k, v) in variables.stash.items():
        if bool(randint(0, 1)):
            variables.stash[k] = int(v * .6)

    return "You've been robbed! Some supplies are missing."


def find():
    stash_str = ""
    for (k, v) in variables.stash.items():
        if bool(randint(0, 1)):
            variables.stash[k] = int(v * 1.2)
            stash_str += k + " "

    return "You've found a stash of supplies! In this stash: " + stash_str


def indentured():
    variables.identured_count += 1
    return "You have an indentured servant! The servant will earn you extra money for 30 days."


def fire():
    for (k, v) in variables.stash.items():
        if bool(randint(0, 1)):
            variables.stash[k] = int(v * .7)
    return "A fire has destroyed some of your supplies!"


def blizzard():
    variables.prices["Furs"] = int(variables.prices["Furs"] * 1.3)
    return "A blizzard has raised the price of furs!"


def heatwave():
    variables.prices["Furs"] = int(variables.prices["Furs"] * .75)
    variables.prices["Whiskey"] = int(variables.prices["Whiskey"] * 1.3)
    return "A heatwave hits. Fur prices fall, but the price of whiskey rises."


def noevent():
    return "A quiet night passes."


def random_event():
    return choice(variables.events_list)
