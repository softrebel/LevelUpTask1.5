from db_upgrader.Repositories.customerStore import *

with CustomerStore() as customer_store:
    customer=customer_store.get_random_customer()
    print(customer)