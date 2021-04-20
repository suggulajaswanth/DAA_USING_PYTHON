class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            print(current.data, end="->")
            current = current.next

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after_node(self, key, data):
        new_node = Node(data)
        current = self.head
        while current and current.data != key:
            current = current.next
        temp = current.next
        current.next = new_node
        new_node.next = temp

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def delete_position(self, pos):
        current = self.head
        if pos == 0:
            self.head = current.next
            current = None
            return
        prev = None
        count = 0
        while current and count != pos:
            prev = current
            current = current.next
            count += 1
        if current is None:
            return
        prev.next = current.next
        current = None

    def length(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        print(count)

    def reverse_string(self, data):
        stack = Stack()
        for i in range(len(data)):
            stack.push(data[i])
        reverse = ""
        while not stack.is_empty():
            reverse += stack.pop()
        print(reverse)

    def swap(self, key1, key2):
        prev1 = None
        current1 = self.head
        while current1.next and current1.data != key1:
            prev1 = current1
            current1 = current1.next
        prev2 = None
        current2 = self.head
        while current2.next and current2.data != key2:
            prev2 = current2
            current2 = current2.next
        if not current1 and not current2:
            return
        if prev1:
            prev1.next = current2
        else:
            self.head = current2
        if prev2:
            prev2.next = current1
        else:
            self.head = current1
        current1.next, current2.next = current2.next, current1.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def ispalindrome(self):
        p = self.head
        reverse = ''
        while p:
            reverse += p.data
            p = p.next
        return reverse == reverse[::-1]

    def removeduplicates(self):
        prev = None
        p = self.head
        list1 = []
        while p:
            if p.data not in list1:
                list1.append(p.data)
                prev = p
            else:
                prev.next = p.next
                p = None
            p = prev.next

    def countoccurences(self, data):
        p = self.head
        count = 0
        while p:
            if p.data == data:
                count += 1
            p = p.next
        return count

    def mergesortedlist(self, llist2):
        p = self.head
        q = llist2.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            newhead = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return newhead

    def len_iterative(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def ntolast(self, key):
        length = self.len_iterative()
        cur = self.head
        datavalue = 0
        while cur:
            if length == key:
                datavalue = cur.data
                break
            cur = cur.next
            length -= 1
        if cur is None:
            return None
        else:
            return datavalue

    def movetailtohead(self):
        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        curr.next = self.head
        prev.next = None
        self.head = curr

    def rotate(self, key):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count < key:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    def sum2lists(self, llist):
        p = self.head
        q = llist.head
        sum_llist = Linkedlist()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        if carry == 1:
            sum_llist.append(1)
            sum_llist.reverse()
            sum_llist.printlist()
        else:
            sum_llist.reverse()
            sum_llist.printlist()


llist = Linkedlist()
llist2 = Linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

# llist.prepend("Birthday date:")
# llist.insert_after_node(3,4)
# llist.delete(1)
# llist.delete_position(5)
# llist.length()
# llist.reverse_string("jasu")
# llist.swap(2,3)
# llist.reverse()
# print(llist.ispalindrome())
# llist.removeduplicates()
# print(llist.countoccurences(3))
# llist.mergesortedlist(llist2)
# print("NTOLASTNODE IS:")
# print(llist.ntolast(2))
# llist.movetailtohead()
# llist.reverse()
# llist2.reverse()
# llist.sum2lists(llist2)
# llist.rotate(4)

llist.printlist()