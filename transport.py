from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def vehicle_type(self):
        pass
    @abstractmethod
    def arrival_time(self):
        pass
    @abstractmethod
    def travel_time(self):
        pass

class Bike(Transport):
    def vehicle_type(self):
        return "Bike"

    def arrival_time(self):
        return "5 minutes"

    def travel_time(self):
        return "10 minutes"

class Scooter(Transport):
    def vehicle_type(self):
        return "Scooter"

    def arrival_time(self):
        return "3 minutes"

    def travel_time(self):
        return "8 minutes"

class Taxi(Transport):
    def vehicle_type(self):
        return "Taxi"

    def arrival_time(self):
        return "2 minutes"

    def travel_time(self):
        return "10 minutes"