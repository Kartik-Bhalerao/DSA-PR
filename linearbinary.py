# Linear and Binary Search Program
# E-commerce System Example

# List of customer account IDs
ids = [105, 203, 150, 189, 120, 300]
print("Customer Account IDs:", ids)
# Input from user
key = int(input("Enter customer account ID to search: "))
# ----- Linear Search -----
found = False
for i in ids:
    if i == key:
        found = True
        break
if found:
    print("\n Found using Linear Search")
else:
    print("\n Not Found using Linear Search")
# ----- Binary Search -----
ids.sort()  # Sort before binary search
low = 0
high = len(ids) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if ids[mid] == key:
        found = True
        break
    elif ids[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if found:
    print(" Found using Binary Search")
else:
    print("Not Found using Binary Search")
