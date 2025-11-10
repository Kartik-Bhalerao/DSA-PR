# Hash Table using Division Method and Linear Probing
SIZE = 10
hash_table = [None] * SIZE

def hash_func(key):
    return key % SIZE

def insert(key):
    index = hash_func(key)
    start = index
    while hash_table[index] not in (None, "DELETED"):
        index = (index + 1) % SIZE
        if index == start:
            print("Hash table is full!")
            return
    hash_table[index] = key
    print(f"Inserted {key} at index {index}")

def search(key):
    index = hash_func(key)
    start = index
    while hash_table[index] is not None:
        if hash_table[index] == key:
            print(f"Key {key} found at index {index}")
            return index
        index = (index + 1) % SIZE
        if index == start:
            break
    print(f"Key {key} not found")
    return None

def delete(key):
    index = search(key)
    if index is not None:
        hash_table[index] = "DELETED"
        print(f"Key {key} deleted")

def display():
    print("\nCurrent Hash Table:")
    for i in range(SIZE):
        print(f"Index {i}: {hash_table[i]}")

# Example operations
insert(12)
insert(22)
insert(32)
insert(42)
display()
search(32)
delete(22)
display()
