nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None],
]

class FlatIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.gen = (i for l in self.lst for i in l)
        self.cursor = -1
        return self.gen

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.lst):
            raise StopIteration
        return self.cursor


for item in FlatIterator(nested_list):
    print(item)