from tests.seeds.customerSeeder import *
from tests.seeds.productSeeder import *
from tests.seeds.offerSeeder import *
from tests.seeds.sourceSeeder import *
from db_upgrader.migration import *


def prepare_data():
    CustomerSeeder.seed(20)
    ProductSeeder.seed(3000)
    SourceSeeder.seed(20)
    OfferSeeder.seed(10000)
    return


if __name__ == "__main__":
    # prepare_data()
    start = datetime.now()
    migration = Migration()
    migration.migrate()
    end = datetime.now() - start
    print(end)
