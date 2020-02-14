from db_upgrader.Repositories.store import Store, StoreException
from db_upgrader.Models.product import *

class ProductStore(Store):
    table = 'product'
    def add_product(self, product):
        try:
            c = self.conn.cursor()
            c.execute(
                'INSERT INTO product (`name`,customerId,is_enable) VALUES(%s,%s,%s)',
                (product.name,product.customerId, product.is_enable))
            return c.lastrowid
        except Exception as e:
            raise StoreException('error storing product: {}'.format(e))
