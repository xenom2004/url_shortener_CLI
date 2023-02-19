long_url=input("Enter your string")

# def url_shortener(url):

import pickle

# Create a Python object to be pickled
my_list = [1, 2, 3, 4, 5]

# Open a file for binary writing
with open('my_file.pickle', 'wb') as f:
    # Pickle the object and write it to the file
    pickle.dump(my_list, f)

# Open the file for binary reading
with open('my_file.pickle', 'rb') as f:
    # Load the pickled object from the file
    loaded_list = pickle.load(f)

# Print the original list and the loaded list to verify that they are the same
print("Original list:", my_list)
print("Loaded list:", loaded_list)