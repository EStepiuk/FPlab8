__author__ = 'Stepiuk'
import re

phone_book = {'Zheka': '063-975-55-53',
              'Tolik': '097-378-21-21',
              'Topol`': '073-537-37-37',
              'Alexey': '+38050-330-33-00'}


def add_new_item(key, value, data=phone_book):
    if key not in data:
        data[key] = value


def delete_item(key, data=phone_book):
    if key in data:
        del data[key]


def find_item_by_key(key, data=phone_book):
    return data[key] if key in data else None


def find_item_by_value(value, data=phone_book):
    for k, v in data.items():
        if v == value:
            return k
    return None


def list_by_key_mask(mask, data=phone_book):
    exp = re.compile(mask)
    res = {}
    for k, v in data.items():
        if exp.match(k):
            res[k] = v
    return res
