class LinkedListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

    def print(self, end='\n'):
        print(self.key, end=end)


class LinkedList:
    def __init__(self):
        self.head = None
        self.__tail = None
        self.len = 0

    def traverse(self):
        ptr = self.head

        while ptr is not None:
            ptr.print(end=' ')
            ptr = ptr.next
        print('')

    def add(self, key: int):
        node = LinkedListNode(key)

        if self.head is None:
            self.head = node
        else:
            self.__tail.next = node
        self.__tail = node

        self.__increment_len()

    def remove(self, key: int):
        ptr, ptr_prev = self.__locate(key)

        if ptr == self.head and ptr.next is None:
            self.head = None
        elif ptr == self.head and ptr.next is not None:
            self.head = self.head.next

        elif ptr_prev is not None:
            ptr_prev.next = ptr.next

        if ptr == self.__tail:
            self.__tail = ptr_prev

        del ptr

    def __locate(self, key: int):
        ptr, ptr_prev = self.head, None

        while ptr is not None and ptr.key != key:
            ptr_prev = ptr
            ptr = ptr.next

        if ptr is None:
            raise KeyError

        return ptr, ptr_prev

    def __increment_len(self):
        self.len += 1

    def __decrement_len(self):
        self.len -= 1


if __name__ == "__main__":
    ll = LinkedList()

    for num in range(10):
        ll.add(num)
    ll.traverse()

    ll.remove(4)
    ll.traverse()

    ll.remove(5)
    ll.traverse()

    ll.remove(9)
    ll.traverse()

    ll.remove(0)
    ll.traverse()
