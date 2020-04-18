# Game variables

import events

identured_count: int = 0  # number of indentured servants
advertising_duration: int = 0  # number of days left on current advertising
advertising_boost: int = 1  # when advertising days are > 0, this is set to 1.2 to boost prices

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
events_list = {
    1: events.competitor(),
    2: events.noevent(),
    3: events.robbed(),
    4: events.noevent(),
    5: events.find(),
    6: events.noevent(),
    7: events.indentured(),
    8: events.noevent(),
    9: events.fire(),
    10: events.noevent(),
    11: events.blizzard(),
    12: events.noevent(),
    13: events.competitor_gone()
}
