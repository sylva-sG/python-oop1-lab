#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        """Initializes the coffee object with a validated size and price."""
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def tip(self):
        """Prints a appreciation message and increases the coffee price by 1."""
        print("This coffee is great, here’s a tip!")
        self.price += 1
