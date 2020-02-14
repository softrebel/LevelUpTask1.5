from db_upgrader.Repositories.productStore import *

with ProductStore() as product_store:
    product=product_store.random()
    print(product)