class Node: 

    def __init__(self, roll, name, marks): 

        self.roll, self.name, self.marks = roll, name, marks 

        self.next = None 

 

class StudentDB: 

    def __init__(self): self.head = None 

 

    def add(self, roll, name, marks): 

        if self.search(roll): return print("Exists") 

        node = Node(roll, name, marks) 

        if not self.head or self.head.roll > roll: 

            node.next, self.head = self.head, node 

        else: 

            cur = self.head 

            while cur.next and cur.next.roll < roll: cur = cur.next 

            node.next, cur.next = cur.next, node 

 

    def delete(self, roll): 

        if not self.head: return 

        if self.head.roll == roll: self.head = self.head.next; return 

        cur = self.head 

        while cur.next and cur.next.roll != roll: cur = cur.next 

        if cur.next: cur.next = cur.next.next 

 

    def update(self, roll, name=None, marks=None): 

        node = self.search(roll) 

        if node: 

            if name: node.name = name 

            if marks: node.marks = marks 

 

    def search(self, roll): 

        cur = self.head 

        while cur: 

            if cur.roll == roll: return cur 

            cur = cur.next 

        return None 

 

    def display(self, by="roll", asc=True): 

        nodes = [] 

        cur = self.head 

        while cur: nodes.append(cur); cur = cur.next 

        key = lambda x: x.roll if by == "roll" else x.marks 

        nodes.sort(key=key, reverse=not asc) 

        print("Roll  Name         Marks") 

        for n in nodes: print(f"{n.roll:<5} {n.name:<12} {n.marks}") 

 

# Test 

s = StudentDB() 

s.add(103, "Bob", 88) 

s.add(101, "Alice", 95) 

s.add(102, "Charlie", 85) 

s.display() 

s.display(by="marks", asc=False) 

s.update(101, marks=99) 

s.delete(103) 

s.display() 

 
