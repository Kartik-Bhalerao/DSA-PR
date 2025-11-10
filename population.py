class Node: 

    def __init__(self, c, p): self.c, self.p = c, p; self.l = self.r = None 

 

class CityBST: 

    def __init__(self): self.root = None 

 

    def add(self, c, p): 

        def ins(n):  

            if not n: return Node(c, p) 

            if c < n.c: n.l = ins(n.l) 

            elif c > n.c: n.r = ins(n.r) 

            else: n.p = p 

            return n 

        self.root = ins(self.root) 

 

    def delete(self, c): 

        def del_n(n): 

            if not n: return n 

            if c < n.c: n.l = del_n(n.l) 

            elif c > n.c: n.r = del_n(n.r) 

            else: 

                if not n.l: return n.r 

                if not n.r: return n.l 

                t = n.r 

                while t.l: t = t.l 

                n.c, n.p = t.c, t.p 

                n.r = del_n(n.r) 

            return n 

        self.root = del_n(self.root) 

 

    def update(self, c, p): 

        n = self.search(c) 

        if n: n.p = p 

 

    def search(self, c): 

        n = self.root 

        while n: 

            if c == n.c: return n 

            n = n.l if c < n.c else n.r 

        return None 

 

    def inorder(self, rev=False): 

        res = [] 

        def trav(n): 

            if n: 

                trav(n.l) 

                res.append((n.c, n.p)) 

                trav(n.r) 

        trav(self.root) 

        if rev: res.reverse() 

        print("City       Pop") 

        for c, p in res: print(f"{c:<10} {p}") 

 

    def max_comp(self): 

        def h(n): return 1 + max(h(n.l), h(n.r)) if n else 0 

        return h(self.root) 

 

# Test 

c = CityBST() 

c.add("Delhi", 20000000) 

c.add("Mumbai", 21000000) 

c.add("Kolkata", 15000000) 

c.inorder() 

c.inorder(True) 

c.update("Delhi", 22000000) 

c.delete("Kolkata") 

c.inorder() 

print("Max comp:", c.max_comp()) 
