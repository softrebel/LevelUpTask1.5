import unittest, sys, os

# region for
project_folder = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_folder)
# endregion
from db_upgrader.migration import *
# from seeds.offerSeeder import *
# from seeds.productSeeder import *
# from seeds.customerSeeder import *
# from seeds.sourceSeeder import *
from db_upgrader.Repositories.sourceStore import *
from db_upgrader.Repositories.offerStore import *
from db_upgrader.Repositories.productStore import *
from db_upgrader.Repositories.customerStore import *
from helpers.date import random_date
from config.test import db_config as config
from datetime import datetime
from helpers.sql import parse_sql


class MigrationTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_migration(self):
        with CustomerStore(config) as customer_store:
            user_id = customer_store.add_customer(Customer("Ali Kalan", 1))
            customer_store.complete()
        with ProductStore(config) as product_store:
            product_id = product_store.add_product(Product("sample product", user_id, 1))
            product_store.complete()
        with SourceStore(config) as source_store:
            source_id = source_store.add_source(Source("sample product", 0, 1))
            source_store.complete()
        offers = []
        with OfferStore(config) as offer_store:
            start = datetime.strptime('2/14/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
            end = datetime.strptime('2/14/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
            for index in range(15):
                offers.append(offer_store.add_offer(Offer(None, product_id, source_id, random_date(start, end))))
            offer_store.complete()

        with  Migration(config) as migration:
            migration.migrate()
            migration.conn.commit()
            c = migration.conn.cursor(dictionary=True)
            c.execute('''
                    SELECT COUNT(*)AS "count" FROM offer o
                    WHERE o.sourceId IN (SELECT ID FROM source WHERE is_premium=0)
                    AND o.order=0
            ''')
            self.assertEqual(int(c.fetchone()['count']), 0)



if __name__ == "__main__":
    unittest.main()
