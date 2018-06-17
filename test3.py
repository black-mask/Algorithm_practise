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


if __name__ == '__main__':
    llist = SingleLinkList()
    for i in range(11, 25):
        llist.append(i)
    llist.print_all()

