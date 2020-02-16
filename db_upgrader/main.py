from db_upgrader.migration import *
from datetime import datetime, timedelta

if __name__ == "__main__":
    start: datetime = datetime.now()
    migration: Migration = Migration()
    migration.migrate()
    end: timedelta = datetime.now() - start
    print(end)
