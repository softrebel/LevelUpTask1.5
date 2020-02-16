from db_upgrader.Repositories.offerStore import *
from db_upgrader.Repositories.productStore import *
from db_upgrader.Repositories.sourceStore import *
from db_upgrader.Models.offer import *
from datetime import datetime
from seeds.seeder import *
from helpers.date import random_date





class OfferSeeder(seeder):
    @staticmethod
    def seed(number: int = 10):
        start = datetime.strptime('2/14/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
        end = datetime.strptime('2/14/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
        for i in range(number):
            with ProductStore() as product_store:
                product = Product(**product_store.random())
            with SourceStore() as source_store:
                source_store = Source(**source_store.random())
            with OfferStore() as offer_store:
                id = offer_store.add_offer(Offer(None, product.ID, source_store.ID, random_date(start, end)))
                print(id)
                offer_store.complete()
