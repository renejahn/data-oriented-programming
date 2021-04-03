from copy import deepcopy
from functools import reduce


def deep_get(dictionary, *keys):
    return reduce(lambda d, key: d.get(key) if d else None, keys, dictionary)

def deep_set(d, information_path, value):
    cd = deepcopy(d)
    reduce(lambda d, key: d.get(key) if d else None, information_path[:-1], cd)[information_path[-1]] = value
    return cd

library_data = {
    'name': 'The smallest library on earth',
    'address': 'Here and now',
    'catalog': {
        'booksByIsbn': {
            '978-1779501127': {
                'isbn': '978-1779501127',
                'title': 'Watchmen',
                'publicationYear': 1987,
                'authorIds': ['alan-moore',
                              'dave-gibbons'],
                'bookItems': [
                    {
                        'id': 'book-item-1',
                        'rackId': 'rack-17',
                    },
                    {
                        'id': 'book-item-2',
                        'rackId': 'rack-17',
                    }
                ]
            }
        },
        'authorsById': {
            'alan-moore': {
                'name': 'Alan Moore',
                'bookIsbns': ['978-1779501127']
            },
            'dave-gibbons': {
                'name': 'Dave Gibbons',
                'bookIsbns': ['978-1779501127']
            }
        }
    },
  'userManagement': {
    'librarians': {
      'franck@gmail.com' : {
        'email': 'franck@gmail.com',
        'encryptedPassword': 'bXlwYXNzd29yZA=='
      }
    },
    'members': {
      'samantha@gmail.com': {
        'email': 'samantha@gmail.com',
        'encryptedPassword': 'c2VjcmV0',
        'isBlocked': False,
      }
    }
  }
}
