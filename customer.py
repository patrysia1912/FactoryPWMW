from abc import ABC, abstractmethod


class Customer:
    def __init__(self, name):
        self.name = name

    def order_transport(self, service):
        print(f"{self.name} order transport {service.transport_name()}")
        return service.order_transport()


