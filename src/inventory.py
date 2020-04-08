# from abc import ABC, abstractmethod
# class Inventory(ABC):

import random
from item import Item


class Inventory():
    def __init__(self, inventory=None):
        self.inventory = inventory if type(inventory).__name__=="list" else []

    def get_inventory(self):
        return self.inventory

    def take_item(self, item, name="You"):
        item.on_take(name)
        self.inventory.append(item)

    def drop_item(self, item, name="You"):
        item.on_drop(name)
        self.inventory.remove(item)         

    def fill_inventory(self):
        item_tuple = (["Banishing Shield", "A fairly short, broad, slightly curved blade made of obsidian is held by a grip wrapped in regular, light brown wolf leather"],
                      ["Shadow Statue", "A fine, sharp point makes this weapon ideal to pierce your enemies and turn them into a sieve."],
                      ["Destruction Statuette", "The blade has a small, warped cross-guard, just large enough to give the blade the perfect weight balance. The cross-guard has a plain twist on each side, a sign of mass production."],
                      ["Thaumaturgy Pillar", "A massive pommel is engraved with the sword maker's symbol, an unimpressive symbol at the best of times."],
                      ["Truth Staff", "The blade itself is bare. No markings can be found, engravings, marks and decorations are only for special or expensive weapons."],
                      ["Cloak of Transformation", "This weapon is used the lower ranked guards. Whatever the purpose of its owner, this weapon will be sufficient."],
                      ["Monolith of Fortuity", "A large, broad, slightly curved blade made of iron is held by a grip wrapped in expensive, black wolf leather."],
                      ["Cube of Pain", "The razor-sharp point makes this weapon the best choice if you want to pierce, prick, puncture and perforate your enemies."],
                      ["Urn of Restoration", "The blade has a jagged, curled cross-guard, adding weight to the blade for a better weight balance, as well as offering hand protection during battle. The cross-guard has a basic cross on each side, a sign of mass production."],
                      ["Fleece of Evils", "A thick pommel is decorated with common gems, anything better would be a waste."])
        item_list = [Item(e[0], e[1]) for e in item_tuple]
        random.shuffle(item_list)
        self.inventory = item_list[0:random.randrange(1, len(item_list))]
