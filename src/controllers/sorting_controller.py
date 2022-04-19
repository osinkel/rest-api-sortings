import math
from concurrent.futures import ProcessPoolExecutor
from pymongo.errors import ServerSelectionTimeoutError
from src.db.connection.base import collection
from src.logic.sort_logic import do_sort

executor = ProcessPoolExecutor(max_workers=10)


def add_sort_to_db(name: str, numbers: list) -> dict:
    future_obj = executor.submit(add_sort_to_db_single, name, numbers)
    return future_obj.result()


def add_sort_to_db_single(name: str, sequence: list) -> dict:
    query = collection.find_one({'sort': name, 'sequence': sequence})
    if not query:
        res = do_sort(name, sequence)
        if not math.isnan(res['time']):
            try:
                collection.insert_one(res)
            except ServerSelectionTimeoutError:
                res = ''
    else:
        del query['_id']
        res = query
    return res


def get_all() -> dict:
    data = {}
    i = 0
    for document in collection.find({}):
        del document['_id']
        data[str(i)] = document
        i += 1
    return {'count': i, 'elements': data}
