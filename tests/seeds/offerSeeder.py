from tests.seeds.seeder import *
from db_upgrader.Repositories.offerStore import *
from db_upgrader.Repositories.productStore import *
from db_upgrader.Repositories.sourceStore import *
from db_upgrader.Models.offer import *
from random import randrange
from datetime import datetime, timedelta


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


class OfferSeeder(seeder):
    def seed(number=10):
        start = datetime.strptime('2/14/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
        end = datetime.strptime('2/14/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
        for i in range(number):
            with ProductStore() as product_store:
                product = Product(**product_store.random())
            with  SourceStore() as source_store:
                source_store = Source(**source_store.random())
            with OfferStore() as offer_store:
                id = offer_store.add_offer(Offer(None, product.ID, source_store.ID, random_date(start, end)))
                print(id)
                offer_store.complete()
