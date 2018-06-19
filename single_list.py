class Node(object):
    def __init__(self, element, next_=None):
        self.element = element
        self.next = next_


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def append(self, elem):
        self._head = Node(elem, self._head)

    def append_last(self, elem):
        if self._head is None:
            self._head = Node(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Node(elem)

    def print_all(self):
        p = self._head
        while p is not None:
            print(p.element, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print('')

    def rev_(self):
        q = None
        while self._head is not None:
            p = self._head
            self._head = self._head.next
            p.next = q
            q = p
        self._head = q


if __name__ == '__main__':
    llist = SingleLinkList()
    for i in range(11, 25):
        llist.append(i)
    llist.print_all()
    llist.rev_()
    llist.print_all()

