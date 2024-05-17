#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.set_page_count(page_count)
        
        
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    page_count = property(get_page_count, set_page_count)
    

    
        