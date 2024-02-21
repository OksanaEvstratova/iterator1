import pprint
from builtins import print
import types

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count = 0
        self.count2 = 0
        return self

    def __next__(self):

        if self.count2 < len(self.list_of_list[self.count]) :
            result = self.list_of_list[self.count][self.count2]
            self.count2 += 1
        else:
            self.count2 = 0
            self.count += 1
            if self.count == len(self.list_of_list):
                raise StopIteration
            result = self.list_of_list[self.count][self.count2]
            self.count2 += 1

        return result


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def flat_generator(list_of_lists):
    for list1 in list_of_lists:
        for elem in list1:
            yield elem


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):


        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

def get_end_list(list_of_list, end_list):

    for current_element in list_of_list:
        if isinstance(current_element, list) == True:
            get_end_list(current_element, end_list)
        else:
            end_list.append(current_element)

    return end_list

def flat_generator4(list_of_list):
    end_list = []
    get_end_list(list_of_list, end_list)
    for elem in end_list:
        yield elem

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator4(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator4(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator4(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
    test_4()