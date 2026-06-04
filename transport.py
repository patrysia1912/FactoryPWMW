"""Moduł definiujący typy środków transportu."""

from abc import ABC, abstractmethod


class Transport(ABC):
    """Abstrakcyjna klasa bazowa dla wszystkich pojazdów."""

    @abstractmethod
    def vehicle_type(self):
        """
        Pobiera nazwę typu pojazdu.

        Args:
            Brak.

        Returns:
            str: Typ pojazdu.
        """
        pass

    @abstractmethod
    def arrival_time(self):
        """
        Pobiera przewidywany czas przyjazdu.

        Args:
            Brak.

        Returns:
            str: Czas dojazdu.
        """
        pass

    @abstractmethod
    def travel_time(self):
        """
        Pobiera przewidywany czas trwania podróży.

        Args:
            Brak.

        Returns:
            str: Czas podróży.
        """
        pass


class Bike(Transport):
    """Klasa reprezentująca rower."""

    def vehicle_type(self):
        """
        Zwraca typ pojazdu.

        Args:
            Brak.

        Returns:
            str: Zwraca "Bike".
        """
        return "Bike"

    def arrival_time(self):
        """
        Zwraca czas przyjazdu.

        Args:
            Brak.

        Returns:
            str: Zwraca "5 minutes".
        """
        return "5 minutes"

    def travel_time(self):
        """
        Zwraca czas podróży.

        Args:
            Brak.

        Returns:
            str: Zwraca "10 minutes".
        """
        return "10 minutes"


class Scooter(Transport):
    """Klasa reprezentująca skuter."""

    def vehicle_type(self):
        """
        Zwraca typ pojazdu.

        Args:
            Brak.

        Returns:
            str: Zwraca "Scooter".
        """
        return "Scooter"

    def arrival_time(self):
        """
        Zwraca czas przyjazdu.

        Args:
            Brak.

        Returns:
            str: Zwraca "3 minutes".
        """
        return "3 minutes"

    def travel_time(self):
        """
        Zwraca czas podróży.

        Args:
            Brak.

        Returns:
            str: Zwraca "8 minutes".
        """
        return "8 minutes"


class Taxi(Transport):
    """Klasa reprezentująca taksówkę."""

    def vehicle_type(self):
        """
        Zwraca typ pojazdu.

        Args:
            Brak.

        Returns:
            str: Zwraca "Taxi".
        """
        return "Taxi"

    def arrival_time(self):
        """
        Zwraca czas przyjazdu.

        Args:
            Brak.

        Returns:
            str: Zwraca "2 minutes".
        """
        return "2 minutes"

    def travel_time(self):
        """
        Zwraca czas podróży.

        Args:
            Brak.

        Returns:
            str: Zwraca "10 minutes".
        """
        return "10 minutes"