from collections import deque 

 

class CallCenterQueue: 

    def __init__(self):  # Fixed: __init__ (double underscores) 

        self.queue = deque()  # (customerID, callTime) 

 

    def addCall(self, customerID: str, callTime: int): 

        self.queue.append((customerID, callTime)) 

        print(f"Added: {customerID} ({callTime} min)") 

 

    def answerCall(self): 

        if self.isQueueEmpty(): 

            print("No calls to answer.") 

            return None 

        cust, time = self.queue.popleft() 

        print(f"Answering: {cust} ({time} min)") 

        return (cust, time) 

 

    def viewQueue(self): 

        if self.isQueueEmpty(): 

            print("Queue is empty.") 

            return [] 

        print("Current Queue:") 

        for i, (cust, time) in enumerate(self.queue, 1): 

            print(f"  {i}. {cust} - {time} min") 

        return list(self.queue) 

 

    def isQueueEmpty(self): 

        return len(self.queue) == 0 

 

# Test 

if __name__ == "__main__":  # Fixed: __name__ and __main__ 

    q = CallCenterQueue() 

    q.addCall("Abhishek", 5) 

    q.addCall("Pratik", 3) 

    q.viewQueue() 

    q.answerCall() 

    q.addCall("Soham", 2) 

    q.viewQueue() 

    print("Empty?", q.isQueueEmpty()) 

 
