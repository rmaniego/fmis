# -*- coding: utf-8 -*-
"""
    sample.py
    ~~~~~~~~~
    Demonstration for functions, objects, and modules.
    
    :copyright: 2023 Rodney Maniego Jr.
    :license: MIT License
"""

class FMIS:
    def __init__(self, business_name):
        self.business_name = business_name
        self.inventory = {}
    
    def welcome(self):
        print("")
        print("#"*50)
        print(f" {self.business_name} FMIS")
        print("#"*50)

def hello(name):
    print(f" Hello, {name}")