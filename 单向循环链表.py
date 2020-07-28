# --*-- coding: utf-8 --*--
# @Time     : 2020/7/28 9:21
# @Author   : mrqinglang
# @software : PyCharm
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleCycleLinkList(object):
    '''单向循环链表'''
    def __init__(self, node=None):
        self.__head = node
        if node:
            self.next = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        cur = self.__head
        # count记录数据
        count = 1
        if self.is_empty():
            # 判断为空时
            return 0
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''链表遍历'''
        if self.is_empty():
            '''返回空值'''
            print('该链表为空链表')
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem, end=' ')
                cur = cur.next
            print(cur.elem)

    def add(self, item):
        '''链表头部添加元素 头插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            self.__head.next = self.__head
            return
        else:
            cur = self.__head
            # 如果是空链表的话cur指向的时None，None没有next
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head


    def append(self, item):
        '''链表尾部添加元素 尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def insert(self, pos, item):
        '''插入元素
        :param pos: 下标从0开始
        :param item: 插入数据
        :return:
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count <= (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            # 链表为空时
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    # 当为头节点时
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            # 当链表只有一个节点的时候
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleCycleLinkList()
    # ll.append(100)
    # ll.append(10)
    # ll.add(888)
    # ll.append(100)
    # ll.append(1)
    # ll.append(0)
    # ll.insert(2, 11)
    # ll.travel()
    # ll.remove(100)
    ll.travel()
    print(ll.search(100))
