import mysql.connector
from config.db import db_config as config


class StoreException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors


class Store():
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**config)
        except Exception as e:
            raise StoreException(*e.args, **e.kwargs)
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.close()

    def complete(self):
        self._complete = True

    def random(self):
        c = self.conn.cursor(dictionary=True)
        c.execute('SELECT * FROM {} ORDER BY RAND() LIMIT 1;'.format(self.table))
        return c.fetchone()

    def find(self, ID):
        try:
            c = self.conn.cursor(dictionary=True)
            statement = 'SELECT * FROM {} where ID = %s ;'.format(self.table)
            c.execute(statement, (ID,))
            return c.fetchone()
        except Exception as e:
            raise StoreException('error storing customer: {}'.format(e))

    def iter_row(cursor, size=1000):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def close(self):
        if self.conn:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                raise StoreException(*e.args)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    raise StoreException(*e.args)
