from abc import ABC
import pytest
from transport import Transport, Bike, Scooter, Taxi
from customer import Customer
from services import BikeService, TaxiService, ScooterService

@pytest.mark.basic
def test_basic():
    assert 2 + 2 == 4

@pytest.mark.basic
def test_create_transport():
    transport1 = Bike()
    transport2 = Taxi()
    transport3 = Scooter()

    assert isinstance(transport1, Transport)
    assert isinstance(transport2, Transport)
    assert isinstance(transport3, Transport)

@pytest.mark.basic
def test_create_customer():
    customer1 = Customer("Mery")
    customer2 = Customer("Pati")

    assert customer1.name == "Mery"
    assert customer2.name == "Pati"

@pytest.mark.basic
def test_bike_methods():
    transport = Bike()

    assert transport.vehicle_type() == "Bike"
    assert transport.arrival_time() == "5 minutes"
    assert transport.travel_time() == "10 minutes"

@pytest.mark.basic
def test_scooter_methods():
    transport = Scooter()

    assert transport.vehicle_type() == "Scooter"
    assert transport.arrival_time() == "3 minutes"
    assert transport.travel_time() == "8 minutes"

@pytest.mark.basic
def test_taxi_methods():
    transport = Taxi()

    assert transport.vehicle_type() == "Taxi"
    assert transport.arrival_time() == "2 minutes"
    assert transport.travel_time() == "10 minutes"

@pytest.mark.basic
def test_bike_service():
    service = BikeService()
    transport = service.create_transport()

    assert isinstance(transport, Bike)

@pytest.mark.basic
def test_scooter_service():
    service = ScooterService()
    transport = service.create_transport()

    assert isinstance(transport, Scooter)

@pytest.mark.basic
def test_taxi_service():
    service = TaxiService()
    transport = service.create_transport()

    assert isinstance(transport, Taxi)

@pytest.mark.basic
def test_customer_orders_transport():
    customer = Customer("Mery")
    service = TaxiService()

    customer.order_transport(service)

@pytest.mark.basic
def test_service_availability():
    service = BikeService()

    assert service.available is True

    service.available = False
    assert service.available is False

#@pytest.mark.extended
#@pytest.mark.exceptions

