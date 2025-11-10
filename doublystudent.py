class Node: 

    def __init__(self, r, n, m): 

       self.r, self.n, self.m = r, n, m 

        self.next = self.prev = None 

class Student: 

    def __init__(self): self.h = None 

 

    def add(self, r, n, m): 

        if self.search(r): return 

        node = Node(r, n, m) 

        if not self.h or self.h.r > r: 

            node.next, self.h = self.h, node 

            if node.next: node.next.prev = node 

        else: 

            cur = self.h 

            while cur.next and cur.next.r < r: cur = cur.next 

            node.next, cur.next = cur.next, node 

            node.prev = cur 

            if node.next: node.next.prev = node 

 

    def delete(self, r): 

        node = self.search(r) 

        if not node: return 

        if node == self.h: self.h = node.next 

        if node.prev: node.prev.next = node.next 

        if node.next: node.next.prev = node.prev 

 

    def update(self, r, n=None, m=None): 

        node = self.search(r) 

        if node: 

            if n: node.n = n 

            if m: node.m = m 

 

    def search(self, r): 

        cur = self.h 

        while cur: 

            if cur.r == r: return cur 

            cur = cur.next 

        return None 

 

    def show(self, by='r', asc=True): 

        nodes = [] 

        cur = self.h 

        while cur: nodes.append(cur); cur = cur.next 

        key = lambda x: x.r if by == 'r' else x.m 

        nodes.sort(key=key, reverse=not asc) 

        print("R Name    M") 

        for n in nodes: print(f"{n.r:<1} {n.n:<7} {n.m}") 

 

# Test 

s = Student() 

s.add(3, "Bob", 88) 

s.add(1, "Alice", 95) 

s.add(2, "Charlie", 85) 

s.show() 

s.show('m', False) 

s.update(1, m=99) 

s.delete(3) 

s.show() 

 
