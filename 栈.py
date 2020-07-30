# --*-- coding: utf-8 --*--
# @Time     : 2020/7/30 17:20
# @Author   : mrqinglang
# @software : PyCharm
class Stack(object):
    '''用顺序表list实现栈'''
    def __init__(self):
        self.__list = []
    def push(self, item):
        '''添加新元素到栈顶'''
        self.__list.append(item)
    def pop(self):
        '''弹出栈顶元素'''
        return self.__list.pop()
    def peek(self):
        '''返回栈顶元素'''
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        '''判断是否为空'''
        return self.__list == []
    def size(self):
        '''返回栈的元素个数'''
        return len(self.__list)

def main():
    s = Stack()
    s.push(1)
    s.push(10)
    s.push(100)
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())

if __name__ == '__main__':
    main()
