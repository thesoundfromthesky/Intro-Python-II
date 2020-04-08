# Write a class to hold player information, e.g. what room they are in
# currently.

from inventory import Inventory


class Player(Inventory):
    def __init__(self, name, current_room):
        super().__init__()
        self.name = name
        self.current_room = current_room


