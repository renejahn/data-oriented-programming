import json
from library_data import deep_get, library_data

def search_book_by_title(lirary_data, query):
  all_books = deep_get(library_data, 'catalog', 'booksByIsbn')
  matching_books = [b for _, b in all_books.items() if query.lower() in b['title'].lower()]
    
  def author_names(library_data, book):
    author_ids = deep_get(library_data, 'catalog', 'booksByIsbn', book['isbn'], 'authorIds')
    return [deep_get(library_data, 'catalog', 'authorsById', author_id, 'name') for author_id in author_ids]

  return [{'title': b['title'], 'isbn': b['isbn'], 'authorNames': author_names(library_data, b)} for b in matching_books]


print(json.dumps(search_book_by_title(library_data, 'watCH')))
