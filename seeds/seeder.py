from faker import Faker


class seeder():

    def faker(faker=None):
        return faker or Faker()
