# Library Borrowing Records Management

from statistics import mode  # Importing mode function
# Input borrow count for each member
borrow_counts = [12, 0, 5, 9, 5, 0, 3, 12, 7]
# 1. Compute average number of books borrowed
average = sum(borrow_counts) / len(borrow_counts)
# 2. Find highest and lowest borrowed books
highest = max(borrow_counts)
lowest = min(borrow_counts)
# 3. Count number of members with 0 borrowings
no_borrow_members = borrow_counts.count(0)
# 4. Find the most frequently borrowed book (mode)
most_frequent = mode(borrow_counts)
# Display all results
print("Borrow Records:", borrow_counts)
print("Average books borrowed:", round(average, 2))
print("Highest borrowed count:", highest)
print("Lowest borrowed count:", lowest)
print("Members who borrowed 0 books:", no_borrow_members)
print("Most frequently borrowed book count (mode):", most_frequent)
