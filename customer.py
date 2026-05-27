from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name):
        self.name = name
    def order_transport(self, service):
        self.ordered = False

