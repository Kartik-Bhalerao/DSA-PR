# Real-Time Event Processing System using Queue
from collections import deque   # for queue operations
# Initialize empty queue
queue = deque()
while True:
    print("\n--- Real-Time Event Processing System ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        event = input("Enter event name: ")
        queue.append(event)
        print(f"Event '{event}' added to queue.")
    elif choice == '2':
        if queue:
            event = queue.popleft()
            print(f"Processed Event: {event}")
        else:
            print("No events to process.")
    elif choice == '3':
        if queue:
            print("Pending Events:")
            for e in queue:
                print("-", e)
        else:
            print("No pending events.")
    elif choice == '4':
        if queue:
            event = input("Enter event name to cancel: ")
            if event in queue:
                queue.remove(event)
                print(f"Event '{event}' canceled.")
            else:
                print("Event not found.")
        else:
            print("No events to cancel.")
    elif choice == '5':
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter between 1–5.")


