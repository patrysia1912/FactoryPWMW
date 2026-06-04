from customer import Customer
from services import BikeService
from transport import Transport

Mery = Customer("Mery")
Patrycja = Customer("Patrycja")
bike = BikeService()
order1 = Mery.order_transport(bike)
order2 = Patrycja.order_transport(bike)


