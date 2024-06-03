#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self, brand = "Adidas", size = 9):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        """The size property"""
        return self._size

    @size.setter
    def size(self, size):
        """size must be an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self, condition = "New"):
        self.condition = condition
        print("Your shoe is as good as new!")


dwayne_wayde = Shoe()
print(dwayne_wayde.brand)
print(dwayne_wayde.size)

jordan = Shoe("Nike", 16)
print(jordan.brand)
print(jordan.size)

maupay = Shoe("Umbro", "ten")
print(maupay.brand)

setattr(maupay, "size", 10)
print(maupay.size)

print(getattr(maupay, "brand"))

print(hasattr(maupay, "brand"))

delattr(maupay, "brand")
print(hasattr(maupay, "brand"))



    

    


        


