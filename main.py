from customer import Customer
from services import BikeService, TaxiService, ScooterService
from transport import Transport, Taxi

Mery = Customer("Mery")
Patrycja = Customer("Patrycja")

bike = BikeService()
taxi = TaxiService()
scooter = ScooterService()

order1 = Mery.order_transport(bike)
order2 = Patrycja.order_transport(bike)
order3 = Mery.order_transport(taxi)
order4 = Patrycja.order_transport(scooter)
order5 = Mery.order_transport(scooter)


