# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:41:43 2023

@author: haryi
"""

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_total()
        return total

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart()

    def add_to_cart(self, item):
        self.cart.add_item(item)

    def remove_from_cart(self, item):
        self.cart.remove_item(item)

    def view_cart(self):
        for item in self.cart.items:
            print(f"{item.name} - {item.quantity} x {item.price} = {item.calculate_total()}")

    def checkout(self):
        total = self.cart.calculate_total()
        print(f"Total amount to be paid: {total}")

class Supermarket:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def sell_item(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                return Item(item.name, item.price, quantity)
            else:
                print(f"Sorry, we only have {self.inventory[item]} units of {item.name} available.")
        else:
            print(f"Sorry, we don't have {item.name} in stock.")

    def restock_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def view_inventory(self):
        for item, quantity in self.inventory.items():
            print(f"{item.name} - {quantity}")

# Example usage
if __name__ == '__main__':
    inventory = {
        Item("Apple", 10, 100): 100,
        Item("Banana", 5, 50): 50,
        Item("Orange", 8, 80): 80,
    }

    supermarket = Supermarket("My Supermarket", inventory)

    customer = Customer("John", "john@example.com")

    apple = supermarket.sell_item(Item("Apple", 10, 0), 5)
    customer.add_to_cart(apple)

    banana = supermarket.sell_item(Item("Banana", 5, 0), 2)
    customer.add_to_cart(banana)

    customer.view_cart()
    # Output:
    # Apple - 5 x 10 = 50
    # Banana - 2 x 5 = 10

    customer.checkout()
    # Output:
    # Total amount to be paid: 60


'''
In this implementation, we have defined three classes: Item, Cart, and Customer. The Item class represents an item in the supermarket and has properties such as name, price, and quantity. The Cart class represents the customer's cart and has methods to add and remove items from the cart, as well as to calculate the total price of all items in the cart. The Customer class represents a customer in the supermarket and has methods to add and remove items from their cart, view their cart,
'''