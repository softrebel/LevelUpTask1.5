from db_upgrader.Repositories.productStore import *
from db_upgrader.Repositories.customerStore import *
from db_upgrader.Models.product import *
from seeds.seeder import *

class ProductSeeder(seeder):
    @staticmethod
    def seed(number:int=10):
        for i in range(number):
            with ProductStore() as product_store, CustomerStore() as customer_store:
                customer = Customer(**customer_store.random())
                id = product_store.add_product(Product(ProductSeeder.faker().name(), customer.ID, 1))
                print(id)
                product_store.complete()
