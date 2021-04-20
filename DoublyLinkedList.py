class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class doublylinkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count

    def delete(self, data):
        cur = self.head
        length = self.length()
        if cur.data == data and length == 1:
            self.head = None
        elif cur.data == data:
            cur = cur.next
            self.head = cur
            cur.prev = None
        else:
            while cur and cur.data != data:
                cur = cur.next
            next = cur.next
            cur = cur.prev
            cur.next = next

    def addafternode(self, data, key):
        cur = self.head
        while cur:
            if cur.next == None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                next = cur.next
                cur.next = new_node
                new_node.next = next
                new_node.prev = cur
                next.prev = new_node
            cur = cur.next

    def addbeforenode(self, data, key):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur == node:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 2
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs


dlist = doublylinkedlist()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.append(5)
# dlist.prepend(4)
# dlist.delete(1)
# dlist.addafternode(3,2)
# dlist.addbeforenode(0,1)
# dlist.reverse()
# dlist.remove_duplicates()
print(dlist.pairs_with_sum(0))
# dlist.printlist()