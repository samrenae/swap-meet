from swap_meet.item import Item
class Vendor:
    
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category = ""):
        self.item_in_category_list = []
        for item in self.inventory:
            if item.category == category:
                self.item_in_category_list.append(item)
        return self.item_in_category_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            friend.remove(their_item)
            friend.add(my_item)
            self.remove(my_item)
            return True
        return False

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        if self.inventory[0] and friend.inventory[0]:
            Vendor.swap_items(self, friend, my_item = self.inventory[0], their_item = friend.inventory[0])
            return True
        return False
    
    def get_best_by_category(self, category):
        self.current_condition = None
        self.best_item = None
        for item in self.inventory:
            if item.category == category:
                if self.current_condition == None:
                    self.current_condition = item.condition
                    self.best_item = item
                else:
                    if self.current_condition < item.condition:
                        self.current_condition = item.condition
                        self.best_item = item
        return self.best_item
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        self.my_item = Vendor.get_best_by_category(self, category = their_priority)
        other.their_item = Vendor.get_best_by_category(other, category = my_priority)
        if self.my_item and other.their_item:
            Vendor.swap_items(self, other, my_item = self.my_item, their_item = other.their_item)
            return True
        return False

    def get_newest_item(self):
        newest_item = None
        for item in range(len(self.inventory)):
            if newest_item == None:
                newest_item = self.inventory[item]
            elif newest_item.age > self.inventory[item].age:
                newest_item = self.inventory[item]
        return newest_item

    def swap_by_newest(self, other):
        my_newest_item = Vendor.get_newest_item(self)
        other_newest_item = Vendor.get_newest_item(other)
        if my_newest_item and other_newest_item:
            Vendor.swap_items(self, other, my_item = my_newest_item, their_item= other_newest_item)
            return True
        return False

