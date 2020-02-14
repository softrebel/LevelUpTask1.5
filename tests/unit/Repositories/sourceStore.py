from db_upgrader.Repositories.sourceStore import *

with SourceStore() as source_store:
    source = Source(source_store.random())
    print(source)
