class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        data = Node(data)
        if self.head is None:
            self.head = data
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = data

    def printlist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circularlinkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def append(self, data):
        data = Node(data)
        if not self.head:
            self.head = data
            self.head.next = self.head
        else:
            currentnode = self.head
            while currentnode.next != self.head:
                currentnode = currentnode.next
            currentnode.next = data
            data.next = self.head

    def islinkedlist(self, lllist):
        curr = lllist.head
        while curr.next:
            curr = curr.next
            if curr.next == lllist.head:
                return True
        return False

    def prepend(self, data):
        newnode = Node(data)
        cur = self.head
        if not self.head:
            newnode.next = self.head
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = newnode
            newnode.next = self.head
            self.head = newnode

    def reverse(self):
        if self.head is None:
            return None
        prev = None
        cur = self.head
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        while (cur != self.head):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        print(prev.data, cur.data)
        self.head.next = prev
        self.head = prev

    def delete(self, data):
        if self.head.data == data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == data:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        cur = self.head
        count = 1
        while cur.next != self.head:
            cur = cur.next
            count += 1
        return count

    def splitlist(self):
        size = len(self)
        if size == 0:
            return
        if size == 1:
            return self.head
        mid = size // 2
        count = 0
        prev = None
        curr = self.head
        while curr and count < mid:
            count += 1
            prev = curr
            curr = curr.next
        # print(curr.data,prev.data)
        prev.next = self.head
        splitllist = Circularlinkedlist()
        while curr.next != self.head:
            splitllist.append(curr.data)
            curr = curr.next
        splitllist.append(curr.data)

        self.printlist()
        print("gap")
        splitllist.printlist()


cllist = Circularlinkedlist()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.append(5)
# cllist.prepend(0)
# cllist.reverse()
# cllist.delete(1)
# cllist.splitlist()
# cllist.printlist()
# llist=Linkedlist()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# print(cllist.islinkedlist(llist))
# print(cllist.islinkedlist(cllist))
cllist.printlist()