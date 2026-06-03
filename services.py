from abc import ABC, abstractmethod
from transport import Transport, Bike
import transport

class TransportServices(ABC):
    def __init__(self):
        self.available = True

    @abstractmethod
    def create_transport(self):
        pass

    def order_transport(self):
        if self.available == True:
            transport = self.create_transport()
            print(f"{transport.vehicle_type()} is available")
            print(f"{transport.vehicle_type()} is being ordered.")
            print(f"{transport.vehicle_type()} will arrive in {transport.arrival_time()}")
            print(f"You will drive a {transport.vehicle_type()} for {transport.travel_time()}")
            self.available = False
        else:
            print("transport is not available")


    @abstractmethod
    def transport_name(self):
        pass


class BikeService(TransportServices):
    def create_transport(self):
        return Bike()
    def transport_name(self):
        return "Bike"
