from db_upgrader.Repositories.customerStore import *
from db_upgrader.Models.customer import *
from seeds.seeder import *

class CustomerSeeder(seeder):
    def seed(number=10):
        for i in range(number):
            with CustomerStore() as customer_store:
                id = customer_store.add_customer(Customer(CustomerSeeder.faker().name(), 1))
                customer_store.complete()
