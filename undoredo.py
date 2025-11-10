# Simple Undo/Redo Text Editor using Stack
undo_stack = []
redo_stack = []
document = ""  # Current text
while True:
    print("\n1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':  # Make a Change
        new_text = input("Enter new document text: ")
        undo_stack.append(document)   # Save current state
        document = new_text           # Update text
        redo_stack.clear()            # Clear redo history
        print("Change made!")
    elif choice == '2':  # Undo
        if not undo_stack:
            print("Nothing to undo!")
        else:
            redo_stack.append(document)
            document = undo_stack.pop()
            print("Undo done!")
    elif choice == '3':  # Redo
        if not redo_stack:
            print("Nothing to redo!")
        else:
            undo_stack.append(document)
            document = redo_stack.pop()
            print("Redo done!")
    elif choice == '4':  # Display current state
        print(f"\nCurrent Document: '{document}'")
    elif choice == '5':  # Exit
        print("Exiting editor...")
        break
    else:
        print("Invalid choice! Try again.")
