from db_upgrader.Repositories.store import Store, StoreException
from db_upgrader.Models.source import *


class SourceStore(Store):
    table = 'source'

    def add_source(self, source):
        try:
            c = self.conn.cursor()
            c.execute(
                'INSERT INTO source (`name`,is_premium,is_enable) VALUES(%s,%s,%s)',
                (source.name, source.is_premium, source.is_enable))
            return c.lastrowid
        except Exception as e:
            raise StoreException('error storing source: {}'.format(e))
