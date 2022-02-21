from iterators import FlatIterator
from generators import flat_generator
from iterators import CompoundIterator
from generators import generator

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]]

nested_list_new = [
    ['a', [['b'], 'c']],
    ['d', 'e', [[['f']], 'h'], False],
    [1, 2, None]]

if __name__ == '__main__':

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)

    for item in CompoundIterator(nested_list_new):
        print(item)

    horizontal_list = list(generator(nested_list_new))
    print(horizontal_list)
