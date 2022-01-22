nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

def list_of_lists(my_list):
    for el in my_list:
        for el2 in el:
            yield el2


for item in list_of_lists(nested_list):
    print(item)