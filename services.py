from abc import ABC, abstractmethod

class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self, vehicle_type):