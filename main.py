"""Główny skrypt uruchamiający przykładowe działanie aplikacji."""

from customer import Customer
from services import BikeService
from transport import Transport

customer = Customer("Mery")

service = BikeService()

order = customer.order_transport(service)

