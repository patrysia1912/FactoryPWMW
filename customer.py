"""Moduł klienta obsługujący proces zamawiania transportu."""

class Customer:
    """
     Klasa reprezentująca klienta w systemie.
    """
    def __init__(self, name):
        """
        Inicjalizuje nowego klienta.

        Args:
        name (str): Imię klienta.

        Returns:
        None
        """
        self.name = name

    def order_transport(self, service):
        """
        Inicjuje  zamawianie w podanej usłudze transportowej.

        Args:
        service (TransportServices): Wybrana usługa transportowa.

        Returns:
        Wynik działania metody order_transport podanej usługi.

        Raises:
        AttributeError: Kiedy podana usługa nie posiada metody order_transport.
        """
        print(f"\n{self.name} order transport {service.transport_name()}")
        return service.order_transport()


