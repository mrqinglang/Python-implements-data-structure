# --*-- coding: utf-8 --*--
# @Time     : 2020/7/20 9:15
# @Author   : mrqinglang
# @software : PyCharm
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None
    def length(self):
        '''链表长度'''
        cur = self.__head
        # count记录数据
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''链表遍历'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next

    def add(self, item):
        '''链表头部添加元素 头插法'''
        node = Node(item)
        node.next = self.__head
        self.__head = node
    def append(self, item):
        '''链表尾部添加元素 尾插法'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self, pos, item):
        '''插入元素
        :param pos: 下标从0开始
        :param item: 插入数据
        :return:
        '''
        if pos <= 0:
            self.add(item)
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
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next



    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleLinkList()
    ll.append(100)
    ll.append(10)
    ll.add(888)
    ll.append(100)
    ll.append(1)
    ll.append(0)
    ll.insert(2, 11)
    print(ll.travel())
    ll.remove(100)
    print(ll.travel())
    print(ll.search(11))


