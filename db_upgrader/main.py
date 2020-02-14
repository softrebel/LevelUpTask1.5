from tests.seeds.customerSeeder import *
from tests.seeds.productSeeder import *
from tests.seeds.offerSeeder import *
from tests.seeds.sourceSeeder import *


def prepare_data():
    # CustomerSeeder.seed(20)
    # ProductSeeder.seed(25)
    # SourceSeeder.seed(20)
    OfferSeeder.seed(5000)


prepare_data()