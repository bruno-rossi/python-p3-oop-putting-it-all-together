#!/usr/bin/env python3

class Shoe:
    # Constructor method:
    def __init__(self, brand, size): 
        self.brand = brand
        self.size = size

    @property
    def size(self):
        """The size property"""
        return self._size
    
    @size.setter
    def size(self, size):
        """size setter"""
        if isinstance(size, int) == True:
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")