from db_upgrader.migration import *
from seeds.sourceSeeder import *
from seeds.customerSeeder import *
from seeds.productSeeder import *
from seeds.offerSeeder import *

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
