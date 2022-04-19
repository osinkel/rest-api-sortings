import copy
import time
from src.logic.sorting import selection_sort, insertion_sort, quick_sort, shaker_sort

allowed_sorting = {
    'selection': selection_sort,
    'insertion': insertion_sort,
    'quick': quick_sort,
    'shaker': shaker_sort
}


def do_sort(name_sort: str, seq: list) -> dict | str:
    res = ''
    sort_time = float('nan')
    if name_sort in allowed_sorting and seq and isinstance(seq, list):
        sort_time = time.perf_counter()
        try:
            res = allowed_sorting[name_sort](copy.copy(seq))
        except TypeError:
            sort_time = float('nan')
        else:
            sort_time = time.perf_counter() - sort_time
    return {'sort': name_sort, 'sequence': seq, 'result': res, 'time': sort_time}


if __name__ == '__main__':
    do_sort('quick', ['cow', 'milk', 'dog', 'man', 'article'])