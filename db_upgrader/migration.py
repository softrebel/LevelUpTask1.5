from seeds.offerSeeder import *
from db_upgrader.Repositories.store import *


class Migration(Store):

    def __init__(self):
        super().__init__()
        self.offer_orders = []
        '''
        [
            {'productId': None, 'offers': [
                {
                    "ID":None,
                    "created_at":None
                }
            ]
             }
        ]
        '''
        self.products = set()

    def fetch_data(self):
        c = self.conn.cursor(dictionary=True)
        statement = '''
                SELECT o.ID,
                   o.userId,
                   o.productId,
                   o.sourceId,
                   o.order,
                   o.created_at,
                   s.name AS `source_name`,
                   s.is_premium `source_is_premium`,
                   p.name,
                   p.customerId AS `customer_ID`,
                   c.name AS `customer_name`
                 FROM levelup.offer o
                  INNER JOIN source s ON o.sourceId=s.ID
                  INNER JOIN product p ON o.productId=p.ID
                  INNER JOIN customer c ON c.ID=p.customerId
                  WHERE p.is_enable=1 AND c.is_enable=1 AND s.is_enable=1 AND s.is_premium=0 
                  ORDER BY p.customerId,o.productId,o.created_at
        '''
        c.execute(statement)
        return Store.iter_row(c)

    def update_offer(self, offer):
        with OfferStore() as offer_store:
            id = offer_store.update_offer_order(offer)
            print(id)
            offer_store.complete()

    def update_data(self):
        for product in self.offer_orders:
            sorted_offers = sorted(product['offers'], key=lambda x: x['created_at'])
            for key, item in enumerate(sorted_offers):
                offer = Offer(order=key + 1, ID=item['ID'])
                self.update_offer(offer)

    def migrate(self):
        for row in self.fetch_data():
            if row['productId'] in self.products:
                for offer in self.offer_orders:
                    if offer['productId'] == row['productId']:
                        offer['offers'].append({
                            "ID": row['ID'],
                            "created_at": row['created_at']
                        })
            else:
                self.offer_orders.append({
                    'productId': row['productId'],
                    'offers': [
                        {
                            "ID": row['ID'],
                            "created_at": row['created_at']
                        }
                    ]
                })
                self.products.add(row['productId'])
        self.update_data()
