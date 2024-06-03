#!/usr/bin/env python3

class Book:
    pass
    def __init__(self, title = "And Then There Were None", page_count = 272):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """The page count property"""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        "page_count must be an integer"
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


bible = Book(title = "King James Version", page_count = 1360)
print(bible.title)
print(bible. page_count)
bible.turn_page()

geeks_for_geeks = Book()
print(geeks_for_geeks.title)
print(geeks_for_geeks.page_count)
geeks_for_geeks.turn_page()

geeks_for_geeks.title = "Python for Beginners"
print(geeks_for_geeks.title)

geeks_for_geeks.page_count = "12"
print(geeks_for_geeks.page_count)

setattr(geeks_for_geeks, "title", "JavaScript for Dummies")
print(getattr(geeks_for_geeks, "title"))


    



    

    



    


    
        