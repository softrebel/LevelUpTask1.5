from db_upgrader.Repositories.sourceStore import *
from db_upgrader.Models.source import *
from seeds.seeder import *
import random


class SourceSeeder(seeder):
    def seed(number=10):
        for i in range(number):
            with SourceStore() as source_store:
                id = source_store.add_source(Source(SourceSeeder.faker().name(), random.randint(0, 1), 1))
                source_store.complete()
