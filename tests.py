from abc import ABC
import pytest
from transport import Transport, Bike, Scooter, Taxi
from customer import Customer

#TODO: tworzenie transportu
#TODO: dzialanie metod
#TODO: mechanizm dostepnosci transportu

@pytest.mark.basic
def test_basic():
    assert 2 + 2 == 4

@pytest.mark.basic
def test_create_transport():
    transport1 = Bike()
    transport2 = Taxi()
    transport3 = Scooter()

@pytest.mark.basic
def test_create_customer():
    customer1 = Customer("Mery")

#@pytest.mark.extended
#@pytest.mark.exceptions

