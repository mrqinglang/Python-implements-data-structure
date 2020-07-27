# --*-- coding: utf-8 --*--
# @Time     : 2020/7/27 15:16
# @Author   : mrqinglang
# @software : PyCharm
# 双向链表具有前驱结点和后继结点
class Node(object):
    '''节点定义'''
    def __init__(self, item):
        self.elem = item
        self.next = None  # 后继节点地址
        self.prev = None  # 前驱节点地址

class DoubulelinkList(object):
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
        node.next.prev = node



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
            node.prev = cur
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
            node.prev = pre
            node.next = pre.next
            pre.next = node
            pre.next.next.prev = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    # 考虑只有一个节点
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    pre.next = cur.next
                    if cur.next:
                        cur.next.prev = pre
                break
            else:
                pre = cur
                cur = cur.next
        print('\n没找到你要删的东西')



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
    dll = DoubulelinkList()
    dll.append(100)
    dll.append(10)
    dll.append(1)
    dll.append(0)
    dll.append(777)
    dll.travel()
    dll.insert(2, 666)
    print(dll.search(777))
    dll.travel()
    dll.remove(666)
    dll.travel()
