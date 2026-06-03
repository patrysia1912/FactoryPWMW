from abc import ABC, abstractmethod
from transport import Transport, Bike

class TransportServices(ABC):
    def __init__(self):
        self.available = True

    @abstractmethod
    def create_transport(self):
        pass

    def order_transport(self):
        transport = self.create_transport()

    @abstractmethod
    def transport_name(self):
        pass

class BikeService(TransportServices):
    def create_transport(self):
        return Bike()
    def transport_name(self):
        return "Bike"
