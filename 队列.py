# --*-- coding: utf-8 --*--
# @Time     : 2020/7/30 19:42
# @Author   : mrqinglang
# @software : PyCharm
class Queue(object):
    '''用顺序表list实现队列'''
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        '''往队列添加一个元素'''
        self.__list.append(item)

    def dequeue(self):
        '''从队列头部删除一个元素'''
        try:
            return self.__list.pop(0)
        except:
            return

    def is_empty(self):
        '''判断是否为空'''
        return self.__list == []

    def size(self):
        '''返回栈元素的大小（站在巨人的肩膀上不重复造轮子了）'''
        return len(self.__list)

def main():
    Q = Queue()
    print(Q.is_empty())
    Q.enqueue(100)
    Q.enqueue(10)
    Q.enqueue(1)
    print('长度为'+str(Q.size()))
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())

if __name__ == '__main__':
    main()
