from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name):
        self.name = name

    def order_transport(self, service):
        print(f"{self.name} order transport {service}")
        service.order_transport()


