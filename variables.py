# Game Variables and functions

from random import seed
from random import randint


def competitor():
    for (k, v) in prices.items():
        if k != "Gold" and v > 1:
            prices[k] = int(v * .9)

    return "A competitor has set up shop! Prices have taken a hit."


def competitor_gone():
    for (k, v) in prices.items():
        if k != "Gold":
            prices[k] = v + 1

    return "A competitor has closed! Prices for your goods rise."


def robbed():
    seed()
    for (k, v) in stash.items():
        if bool(randint(0, 1)):
            stash[k] = int(v * .6)

    return "You've been robbed! Some supplies are missing."


def find():
    stash_str = ""
    seed()
    for (k, v) in stash.items():
        if bool(randint(0, 1)):
            stash[k] = int(v * 1.2)
            stash_str += k + " "

    return "You've found a stash of supplies! In this stash: " + stash_str


def indentured():
    global indenturedCount
    indenturedCount = indenturedCount + 1

    return "You have an indentured servant! The servant will earn you extra money for 30 days."


def fire():
    seed()
    for (k, v) in stash.items():
        if bool(randint(0, 1)):
            stash[k] = int(v * .7)
    return "A fire has destroyed some of your supplies!"


def blizzard():
    prices["Furs"] = int(prices["Furs"] * 1.3)
    return "A blizzard has raised the price of furs!"


def heatwave():
    prices["Furs"] = int(prices["Furs"] * .75)
    prices["Whiskey"] = int(prices["Whiskey"] * 1.3)
    return "A heatwave hits. Fur prices fall, but the price of whiskey rises."


def noevent():
    return "A quiet night passes."


def random_event():
    seed()
    ev = randint(1, 13)
    func = events.get(ev, lambda: "")
    if func != None:
        return func()
    else:
        return "A quiet night passes."


def show_stats():
    print("╔═══════════════════════════════════════════════════════╗")
    print("║ ░░░░░░░░░░░░░░░░░░░░░░░ STATS ░░░░░░░░░░░░░░░░░░░░░░░ ║")
    print("║\tStores\t\t\tPrices".ljust(10) + "\t\t\t║")

    for (k, v), (k2, v2) in zip(stash.items(), prices.items()):
        print("║\t" + k + ": " + str(int(v)).ljust(5) + "\t|\t" + "$" + str(v2) + "\t\t\t║")
    print("║-------------------------------------------------------║")
    print("║ Indentured servants: " + str(indenturedCount) + "  " \
          + "Days of advertising left: " + str(advertisingDuration).ljust(4) + "║")

    print("╚═══════════════════════════════════════════════════════╝\n")


indenturedCount: int = 0  # number of indentured servants
advertisingDuration: int = 0  # number of days left on current advertising
advertisingBoost: int = 1  # when advertising days are > 0, this is set to 1.2 to boost prices

stash = {
    "Gold": 20,
    "Furs": 0,
    "Bullets": 10,
    "Whiskey": 1,
    "Medicine": 1,
    "Food": 10
}
prices = {
    "Gold": 1,
    "Furs": 4,
    "Bullets": 2,
    "Whiskey": 6,
    "Medicine": 10,
    "Food": 2
}
wholesale = {
    "Furs": 2,
    "Bullets": 1,
    "Whiskey": 3,
    "Medicine": 5,
    "Food": 1
}
events = {
    1: competitor,
    2: noevent,
    3: robbed,
    4: noevent,
    5: find,
    6: noevent,
    7: indentured,
    8: noevent,
    9: fire,
    10: noevent,
    11: blizzard,
    12: noevent,
    13: competitor_gone
}
