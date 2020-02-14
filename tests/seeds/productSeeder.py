# from db_upgrader.Repositories.customerStore import *
# from db_upgrader.Repositories.offerStore import *
# from db_upgrader.Repositories.productStore import *
# from db_upgrader.Repositories.sourceStore import *
#
# from db_upgrader.Models.offer import *
# from db_upgrader.Models.source import *

#
# with ProductStore() as customer_store:
#     id = customer_store.add_product(Product('John', 1))
#     print(id)
#     customer_store.complete()
# with SourceStore() as customer_store:
#     id = customer_store.add_source(Source('John', 1))
#     print(id)
#     customer_store.complete()
# with OfferStore() as offer_store:
#     id = offer_store.add_offer(Offer(1, 1, 1))
#     print(id)
#     offer_store.complete()

from tests.seeds.seeder import *
from db_upgrader.Repositories.productStore import *
from db_upgrader.Repositories.customerStore import *
from db_upgrader.Models.product import *


class ProductSeeder(seeder):
    def seed(number=10):
        for i in range(number):
            with ProductStore() as product_store, CustomerStore() as customer_store:
                customer = Customer(**customer_store.random())
                id = product_store.add_product(Product(ProductSeeder.faker().name(), customer.ID, 1))
                print(id)
                product_store.complete()
