class Node(object):
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class SLList(object):
    '''单链表'''
    def __init__(self):
        self._head = None

    def append_last(self, val):
        if self._head is None:
            self._head = Node(val)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def print_all(self):
        p = self._head
        while p is not None:
            print(p.val, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print('')

    def get_reversed_val(self):
        # 取出链表反转后的序列整数
        n, value = 0, 0
        p = self._head
        while p is not None:
            value += p.val * 10**n
            p = p.next
            n += 1
        # print(value)
        return value


class Solution(object):
    def addTwoNum(self, list1, list2):
        num = list1.get_reversed_val() + list2.get_reversed_val()
        newlist = SLList()
        # 结果反序形成链表
        while num > 0:
            i = num % 10
            num = num // 10
            newlist.append_last(i)
        newlist.print_all()
        return newlist


if __name__ == '__main__':
    list1 = SLList()
    for i in range(3, 6):
        list1.append_last(i)
    list1.print_all()
    list2 = SLList()
    for i in range(4, 7):
        list2.append_last(i)
    list2.print_all()
    Solution().addTwoNum(list1, list2)


