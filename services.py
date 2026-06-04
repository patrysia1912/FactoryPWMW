"""Moduł zawierający usługi transportowe i logikę wzorca Factory Method."""

from abc import ABC, abstractmethod
from transport import Transport, Bike, Scooter, Taxi
import transport


class TransportServices(ABC):
    """
    Abstrakcyjna klasa bazowa zarządzająca usługami transportowymi.
    """
    def __init__(self):
        """
        Inicjalizuje usługę transportową z domyślną dostępnością.

        Args:
            Brak.

        Returns:
            None
        """
        self.available = True

    @abstractmethod
    def create_transport(self):
        """
        Tworzy obiekt transportu. Metoda abstrakcyjna klasy TransportServices.

        Args:
            Brak.

        Returns:
            Transport: Nowy obiekt pojazdu.

        """
        pass

    def order_transport(self):
        """
        Obsługuje proces zamówienia pojazdu i zmienia jego dostępność.
        Wyświetla komunikaty o tym informujące.

        Args:
            Brak.

        Returns:
            None
        """
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
        """
        Zwraca nazwę usługi.

        Args:
            Brak.

        Returns:
            str: Nazwa usługi.
        """
        pass


class BikeService(TransportServices):
    """Usługa obsługująca zamówienia rowerów."""
    def create_transport(self):
        """
        Tworzy instancję roweru.

        Ags:
            Brak.

        Returns:
            Bike: Obiekt roweru.
        """
        return Bike()
    def transport_name(self):
        """
        Zwraca nazwę usługi rowerowej.

        Args:
            Brak.

        Returns:
            Napis "Bike".
        """
        return "Bike"

class ScooterService(TransportServices):
    """Usługa obsługująca zamówienia skuterów."""
    def create_transport(self):
        """
        Tworzy instancję skuteru.

        Args:
            Brak.

        Returns:
            Scooter: Obiekt skuteru.
        """
        return Scooter()

    def transport_name(self):
        """
        Zwraca nazwę usługi dla skuterów.

        Args:
            Brak.

        Returns:
            Napis "Scooter".
        """
        return "Scooter"

class TaxiService(TransportServices):
    """Usługa obsługująca zamówienia taksówek."""
    def create_transport(self):
        """
        Tworzy instancję taksówki.

        Args:
            Brak.

        Returns:
            Taxi: Obiekt taksówki.
        """
        return Taxi()

    def transport_name(self):
        """
        Zwraca nazwę usługi taksówkarskiej.

        Args:
            Brak.

        Returns:
            Napis "Taxi".
        """
        return "Taxi"