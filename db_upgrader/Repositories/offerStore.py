from db_upgrader.Repositories.store import Store, StoreException
from db_upgrader.Models.offer import *


class OfferStore(Store):
    table = 'offer'

    def add_offer(self, offer):
        try:
            c = self.conn.cursor()
            created_at = str(offer.created_at)
            c.execute(
                "INSERT INTO offer (userId,productId ,sourceId,created_at) VALUES (%s,%s,%s,%s)",
                (offer.userId, offer.productId, offer.sourceId,created_at))
            return c.lastrowid
        except Exception as e:
            raise StoreException('error storing offer: {}'.format(e))

    def update_offer_order(self,offer):
        try:
            c = self.conn.cursor()
            c.execute(
                "UPDATE offer SET `order` = %s WHERE ID = %s",
                (offer.order,offer.ID))
            return c.lastrowid
        except Exception as e:
            raise StoreException('error storing offer: {}'.format(e))

    def get_offers(self):
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM offer o ORDER BY o.userId,o.productId")
            for row in self.iter_row(c, 1000):
                print(row)
        except Exception as e:
            raise StoreException('error storing offer: {}'.format(e))
