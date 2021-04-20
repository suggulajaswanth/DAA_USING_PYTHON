class InvalidoperationException(Exception):
    pass


class studentRecord:
    def __init__(self, i, Name):
        self.studentId = i
        self.studentName = Name

    def get_student_id(self):
        return self.studentId

    def set_student_id(self, i):
        self.studentId = i

    def __str__(self):
        return str(self.studentId) + "->" + self.studentName


class HashTable:
    def __init__(self, tablesize=11):
        self.m = tablesize
        self.array = [None] * self.m
        self.n = 0

    def hash1(self, key):
        return key % self.m

    # commented functions for rehashing
    # def rehash(self, new_size):
    #     temp = HashTable(new_size)
    #     for i in range(self.m):
    #         if self.array[i] is not None and self.array[i].get_student_id() != -1:
    #             temp.insert(self.array[i])
    #     self.array = temp.array
    #     self.m = new_size
    #
    # def insert1(self, newRecord):
    #     if self.n >= self.m // 2:
    #         self.rehash(self.next_prime(2 * self.m))
    #         print("New Table size is:", self.m)
    #     self.insert(newRecord)

    def insert(self, newRecord):
        key = newRecord.get_student_id()
        h = self.hash1(key)
        location = h
        for i in range(1, self.m):
            if self.array[location] is None or self.array[location].get_student_id() == -1:
                self.array[location] = newRecord
                self.n += 1
                return
            if self.array[location].get_student_id() == key:
                raise InvalidoperationException("Duplicate key")
            location = (h + i) % self.m
        print("Table is full Record can't be inserted ")

    # def next_prime(self,x):
    #     while self.is_prime(x) is not True:
    #         x+=1
    #     return x
    #
    # def is_prime(self,x):
    #     for i in range(2,x):
    #         if x%i==0:
    #             return False
    #     return True

    def search(self, key):
        h = self.hash1(key)
        location = h
        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_student_id() == key:
                return self.array[location]
            location = (h + i) % self.m
        return None

    def display_table(self):
        for i in range(self.m):
            print("[", end='');
            print(i, end='');
            print("]", end='');
            if self.array[i] is not None and self.array[i].get_student_id() != -1:
                print(self.array[i])
            else:
                print("___")

    def delete(self, key):
        h = self.hash1(key)
        location = h
        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_student_id() == key:
                temp = self.array[location]
                self.array[location].set_student_id(-1)
                self.n -= 1
                return temp
                # if self.n>0 and self.n<=self.m//8:
                #     self.rehash(self.next_prime(self.m//2))
                #     print("New Table size is",self.m)
            location = (h + i) % self.m
        return None


size = int(input("Enter initial size of table: "))
table = HashTable(size)

while True:
    print("1. Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display table")
    print("5.Exit")
    option = int(input("Enter your option :"))
    if option == 1:
        id = int(input("Enter student id: "))
        name = input("Enter student name: ")
        aRecord = studentRecord(id, name)
        table.insert(aRecord)
        # table.insert1(aRecord) ->for rehashing table size
    elif option == 2:
        id = int(input("Enter a key to be searched: "))
        aRecord = table.search(id)
        if aRecord is None:
            print("Key not found")
        else:
            print(aRecord)
    elif option == 3:
        id = int(input("Enter a key to be deleted :"))
        table.delete(id)
    elif option == 4:
        table.display_table()
    elif option == 5:
        break
    else:
        print("Wrong option")
    print()



