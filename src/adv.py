import os
import textwrap
from player import Player
from room import Room
import re

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("player", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
wrapper = textwrap.TextWrapper(width=40)
reg_exp = re.compile('(get|take|drop)\s(.{,25}(\s.{,25})?)')


def clear(): return os.system('cls')  # on Windows System


global current_room
current_room = player.current_room


def get_cardinal_direction(fromRoom):
    cardinal_direction = {"n": fromRoom.n_to, "s": fromRoom.s_to,
                          "w": fromRoom.w_to, "e": fromRoom.e_to}
    return cardinal_direction


def get_next_room(fromRoom, toDirection):
    return get_cardinal_direction(fromRoom)[toDirection]


def pause():
    input("Press any key to proceed")
    clear()


while True:
    print(f"At the {current_room.name}, ", end="")

    word_list = wrapper.wrap(current_room.description)
    for i, element in enumerate(word_list):
        if i == 0:
            print(element.lower())
        else:
            print(element)

    room_inventory = current_room.get_inventory()
    player_inventory = player.get_inventory()
    print(f"Total items found {len(room_inventory)}")
    for item in room_inventory:
        print(item.name)

    command = input("Enter command\n")
    clear()

    if command == "q":
        break
    elif command == "i" or command == "inventory":
        print(f"Total items in your inventory: {len(player_inventory)}")
        for item in player_inventory:
            print(item.name)
            print(item.description)
        pause()
    elif reg_exp.match(command):
        v, o = command.split(" ", 1)
        if(v == "take" or v == "get"):
            for e in room_inventory:
                if e.name == o:
                    current_room.drop_item(e, current_room.name)
                    player.take_item(e)

        elif(v == "drop"):
            for e in player_inventory:
                if e.name == o:
                    player.drop_item(e)
                    current_room.take_item(e, current_room.name)
        pause()
    else:
        try:
            next_room = get_next_room(current_room, command)
            if next_room:
                current_room = next_room
            else:
                raise
        except:
            print("There are no rooms")
            pause()
