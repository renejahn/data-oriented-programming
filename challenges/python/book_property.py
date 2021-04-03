import json
from library_data import deep_get, library_data

def get_book_property(library_data, isbn, field_name):
  information_path = ['catalog', 'booksByIsbn', isbn, field_name]
  return deep_get(library_data, *information_path)


print(json.dumps(get_book_property(library_data, '978-1779501127', 'title')))
