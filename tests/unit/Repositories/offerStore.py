from db_upgrader.Repositories.offerStore import *

with OfferStore() as offer_store:
    offer = offer_store.get_random_offer()
    print(offer)
