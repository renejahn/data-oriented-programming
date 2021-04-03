from library_data import deep_get, deep_set, library_data

def block_member(library_data, email):
  information_path = ['userManagement', 'members', email, 'isBlocked'] 
  return deep_set(library_data, information_path, True)


updated_library_data = block_member(library_data, 'samantha@gmail.com')
information_path = ['userManagement', 'members', 'samantha@gmail.com', 'isBlocked']

print([deep_get(updated_library_data, *information_path), deep_get(library_data, *information_path)])