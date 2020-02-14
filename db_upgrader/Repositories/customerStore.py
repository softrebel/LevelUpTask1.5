from db_upgrader.Repositories.store import Store, StoreException
from db_upgrader.Models.customer import *


class CustomerStore(Store):
    table = 'customer'

    def add_customer(self, customer):
        try:
            c = self.conn.cursor()

            c.execute(
                'INSERT INTO customer (`name`,is_enable,created_by, created_at,update_by,updated_at) VALUES(%s,%s,0,Now(),0,Now())',
                (customer.name, customer.is_enable))
            return c.lastrowid
        except Exception as e:
            raise StoreException('error storing customer: {}'.format(e))
