# Hash Table Implementation using Division Method and Chaining

# Size of hash table
TABLE_SIZE = 10
# Initialize hash table (list of lists)
hash_table = [[] for _ in range(TABLE_SIZE)]
# Hash function (division method)
def hash_function(key):
    return key % TABLE_SIZE
# Insert operation
def insert(key, value):
    index = hash_function(key)
    # Check if key already exists -> update
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print(f"Updated key {key} with new value {value}")
            return
    # Otherwise insert new pair
    hash_table[index].append([key, value])
    print(f"Inserted key {key} with value {value}")
# Search operation
def search(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            print(f"Key {key} found with value {pair[1]}")
            return pair[1]
    print(f"Key {key} not found")
    return None
# Delete operation
def delete(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print(f"Key {key} deleted")
            return
    print(f"Key {key} not found, cannot delete")
# Display hash table
def display():
    print("\nCurrent Hash Table:")
    for i in range(TABLE_SIZE):
        print(f"Index {i}: {hash_table[i]}")
# Example operations
insert(12, "Apple")
insert(22, "Banana")
insert(32, "Mango")
display()

search(22)
delete(12)
display()
