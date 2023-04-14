# Task-04 Part-02

# Define the hash function
def hash_function(key):
    return key % 5

# Define the initial hash table
hash_table = [[] for _ in range(5)]

# Define the value list
value_list = [3, 2, 9, 11,7,7]

# Populate the hash table with the values from the value list
for value in value_list:
    key = hash_function(value)
    hash_table[key].append(value)

# Define a function to add a new element to the hash table
def add_element():
    new_element = int(input("Enter a new element: "))
    key = hash_function(new_element)
    hash_table[key].append(new_element)

# Define a function to update a value of a certain key
def update_value():
    key = int(input("Enter the key of the element you want to update: "))
    if len(hash_table[key]) == 0:
        print("No elements found for this key.")
        return
    index = int(input("Enter the index of the element you want to update (starting from 0): "))
    if index >= len(hash_table[key]):
        print("Invalid index.")
        return
    new_value = int(input("Enter the new value: "))
    hash_table[key][index] = new_value

# Define a function to delete an element from the hash table
def delete_element():
    key = int(input("Enter the key of the element you want to delete: "))
    if len(hash_table[key]) == 0:
        print("No elements found for this key.")
        return
    index = int(input("Enter the index of the element you want to delete (starting from 0): "))
    if index >= len(hash_table[key]):
        print("Invalid index.")
        return
    del hash_table[key][index]

# Define a function to search for an element in the hash table
def search_element():
    search_value = int(input("Enter an element to search for: "))
    key = hash_function(search_value)
    if search_value in hash_table[key]:
        print(f"{search_value} is found at key {key}.")
    else:
        print(f"{search_value} is not found.")

# Define a function to print all elements with their keys of the hash table.
def print_elements():
    for i in range(len(hash_table)):
        print(f"Key {i}: {hash_table[i]}")

while True:
    # Display menu options and get user input.
    choice = input("""
Choose one of these options:
1. Construct whole Hash Table.
2. Add a new Element.
3. Update an Element.
4. Delete an Element.
5. Search for an Element.
6. Print all Elements with their Keys.
7. Exit.

Please enter your choice: """)

    # Call appropriate functions based on user input.
    if choice == "1":
        print_elements()
    elif choice == "2":
        add_element()
        print_elements()
    elif choice == "3":
        update_value()
        print_elements()
    elif choice == "4":
        delete_element()
        print_elements()
    elif choice == "5":
        search_element()
    elif choice == "6":
        print_elements()
    elif choice == "7":
        break
    else:
        print("Invalid Input.")