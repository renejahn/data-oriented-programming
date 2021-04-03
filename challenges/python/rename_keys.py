

def rename_keys(map, key_map):
    return {key_map.get(k, k):v for k, v in map.items()}


alan_moore = {
  'name': 'Alan Moore',
  'bookIsbns': ['978-1779501127']
}

print(rename_keys(alan_moore, {'bookIsbns': 'books'}))

bookItem = {
  'id': 'book-item-1',
  'rackId': 'rack-17',
  'isLent': True
}

print(rename_keys(bookItem, {'rackId': 'id', 'id': 'bookItemId'}))
