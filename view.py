__author__ = 'Stepiuk'


def print_item(key, value):
    if key and value:
        print('{:10} - {:>17}'.format(key, value))


def list_items(data):
    if not isinstance(data, dict):
        print('Wrong data')
    for i in sorted(data):
        print_item(i, data[i])


def print_menu():
    print('\na - add'
          '\nd - delete contact'
          '\ns - find by contact name'
          '\nn - find by number'
          '\ne - to exit')
